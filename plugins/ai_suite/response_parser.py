# /plugins/ai_suite/response_parser.py
# Try to extract path from header; else infer from '--- a/...'
file_path = header.strip() if header else ''
if not file_path:
src, dst = _parse_paths_from_headers(body)
# Prefer dst when creating a file, else src
file_path = dst or src
if not file_path:
log.warning("AI Patcher: PATCH block missing filepath; skipping.")
continue
changes.append({'type': 'APPLY_PATCH', 'file_path': file_path, 'content': body})
log.info(f"AI Patcher: Parsed PATCH for {file_path}")
continue


log.warning(f"AI Patcher: Unknown block type '{label}'. Skipping.")
return changes




def apply_changes_to_project(project_root: str, changes: List[dict]) -> tuple[bool, str]:
"""Apply a list of parsed changes to a project directory transactionally.


Stage 1: validate & prepare a snapshot of final file contents without touching disk.
Stage 2: write the snapshot atomically (temp-file + os.replace). Refuse path traversal.
"""
log.info("AI Patcher: Stage 1/2 - Preparing snapshot of all file changes...")
snapshot: Dict[str, Optional[str]] = {} # path -> new_text (None means delete)


# Helper to load current or staged content
def _read_current(path: str) -> str:
if path in snapshot:
return '' if snapshot[path] is None else snapshot[path] # type: ignore
try:
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
return f.read()
except FileNotFoundError:
return ''


abs_root = os.path.normpath(os.path.abspath(project_root))
try:
for change in changes:
ctype = change.get('type')
if ctype in {'APPLY_PATCH', 'CREATE_OR_REPLACE', 'DELETE'}:
rel = change.get('file_path', '')
if not rel:
raise ValueError('Missing file_path')
path = _safe_join(project_root, rel)
elif ctype == 'MOVE':
src_rel = change.get('src_path', '')
dst_rel = change.get('dst_path', '')
if not (src_rel and dst_rel):
raise ValueError('MOVE requires src_path and dst_path')
src_path = _safe_join(project_root, src_rel)
dst_path = _safe_join(project_root, dst_rel)
else:
log.warning(f"AI Patcher: Unknown change type {ctype}; skipping.")
continue


if ctype == 'APPLY_PATCH':
current = _read_current(path)
try:
new_text = apply_patch(current, change.get('content', ''), lenient_whitespace=False)
except Exception as e:
return False, f"Patch failed for {path}: {e}"
snapshot[path] = new_text


elif ctype == 'CREATE_OR_REPLACE':
snapshot[path] = change.get('content', '')


elif ctype == 'DELETE':
snapshot[path] = None


elif ctype == 'MOVE':
# Simulate move by carrying staged or current content to destination, and deleting source
current = _read_current(src_path)
if current == '' and not os.path.exists(src_path) and src_path not in snapshot:
log.warning(f"AI Patcher: MOVE source does not exist: {src_path}")
snapshot[dst_path] = current
snapshot[src_path] = None


# Stage 2 - write atomically
log.info("AI Patcher: Stage 2/2 - Writing files atomically...")
for path, new_content in snapshot.items():
# Ensure path still within root (defense-in-depth)
path = _safe_join(project_root, os.path.relpath(path, project_root))
if new_content is None:
if os.path.exists(path):
os.remove(path)
log.info(f"Deleted file: {path}")
continue


os.makedirs(os.path.dirname(path), exist_ok=True)
tmp_path = f"{path}.tmp.{os.getpid()}"
with open(tmp_path, 'w', encoding='utf-8', newline='\n') as f:
f.write(new_content)
os.replace(tmp_path, path)
log.info(f"Wrote changes to: {path}")
except Exception as e:
return False, f"A critical error occurred during file writing: {e}"


return True, f"Successfully applied {len(snapshot)} change(s)."