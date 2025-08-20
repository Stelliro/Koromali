# AI Task: No Persona (General Review)
## Timestamp: 2025-07-29T15:45:33.048876

---SYSTEM-PROMPT---

You are a helpful and experienced software developer. Your goal is to perform a general code review based on the user's instructions and the provided files. Offer concrete suggestions for improvement.

---USER-PROMPT---

# Project Review Request

**User's Goal:**
Perform a general review of the provided code.

---
**Project File Tree:**
```
/Stelliferrum_Forge
 ├── OverlayApp
 ├── README.md
 ├── TOP_SECRET_GAME_DEV_DOCS
 │   ├── 00_PROJECT_FOUNDATION
 │   │   ├── 01_ROADMAP.md
 │   │   ├── 02_Core_Pillars.md
 │   │   ├── 03_TOP_SECRET_Game_Design_Document_(GDD).md
 │   │   ├── 0_GDD.md
 │   │   └── todolist.json
 │   ├── 01_ENGINE_DESIGN
 │   │   ├── 01_Engine_Overview_and_Philosophy.md
 │   │   ├── 02_ENGINE_MODULES
 │   │   │   ├── 01_Core_Loop_and_State_Manager.md
 │   │   │   ├── 02_Platform_and_Windowing.md
 │   │   │   ├── 03_Input_Handler.md
 │   │   │   ├── 04_2D_Renderer.md
 │   │   │   ├── 05_3D_Renderer.md
 │   │   │   ├── 06_Physics_Engine.md
 │   │   │   ├── 07_Audio_Engine.md
 │   │   │   ├── 08_UI_System.md
 │   │   │   └── 09_Asset_Pipeline.md
 │   │   └── 03_Engine_API_Reference.md
 │   ├── 02_WORLD_AND_NARRATIVE
 │   │   ├── 01_High_Level_Lore.md
 │   │   ├── 02_Historical_Timeline.md
 │   │   ├── 03_The_Pantheon_of_Gods
 │   │   │   ├── 01_Pantheon_Overview.md
 │   │   │   ├── 02_Valdrak,_The_Iron_Father.md
 │   │   │   ├── 03_Sylvana,_The_Verdant_Mother.md
 │   │   │   ├── 04_Morgrath,_The_Shadowed_King.md
 │   │   │   ├── 05_Lyra,_The_Silent_Weaver.md
 │   │   │   ├── 06_Kaelus,_The_Storm-Throat.md
 │   │   │   ├── 07_Solana,_The_Ever-Burning_Sun.md
 │   │   │   ├── 08_Umbra,_The_Whispering_Moon.md
 │   │   │   ├── 09_Fjolnir,_The_Stone-Heart.md
 │   │   │   ├── 10_Volo,_The_Wandering_Trickster.md
 │   │   │   └── 11_The_Axis_Mind.md
 │   │   ├── 04_Factions_and_Races.md
 │   │   ├── 05_CHARACTERS
 │   │   │   ├── 01_The_Protagonists
 │   │   │   │   ├── 01_The_Keystone_Project_Survivors.md
 │   │   │   │   ├── 02_Kai_Sterling.md
 │   │   │   │   ├── 03_Dr._Alex_Thorne.md
 │   │   │   │   ├── 04_Lena_Petrova.md
 │   │   │   │   ├── 05_Marcus_Cole.md
 │   │   │   │   ├── 06_Dr._Elara_Vance.md
 │   │   │   │   ├── 07_Ben_Carter.md
 │   │   │   │   ├── 08_Julian_Finch.md
 │   │   │   │   ├── 09_Isabelle_Rousseau.md
 │   │   │   │   ├── 10_Gunnar_Hansen.md
 │   │   │   │   ├── 11_Dr._Sofia_Rossi.md
 │   │   │   │   └── 12_Kenji_Tanaka.md
 │   │   │   ├── 02_AI_Companions
 │   │   │   │   ├── 01_AI_Companion_Overview.md
 │   │   │   │   ├── 02_A.R.I.A.md
 │   │   │   │   ├── 03_C.A.I.N.md
 │   │   │   │   ├── 04_G.O.L.I.A.T.H.md
 │   │   │   │   ├── 05_H.E.R.A.md
 │   │   │   │   └── 06_V.E.G.A.md
 │   │   │   ├── 03_Key_Allies_and_Vendors.md
 │   │   │   └── 04_Key_Antagonists.md
 │   │   ├── 06_LOCATIONS
 │   │   │   ├── 01_World_Map_and_Regions.md
 │   │   │   ├── 02_Biomes_and_Environments.md
 │   │   │   └── 03_Points_of_Interest_and_Dungeons.md
 │   │   └── 07_NARRATIVE
 │   │       ├── 01_Main_Story_Outline.md
 │   │       └── 02_Side_Quests.md
 │   ├── 03_CORE_GAMEPLAY_SYSTEMS
 │   │   ├── 01_PLAYER_SYSTEMS
 │   │   │   ├── 01_Stats_and_Attributes.md
 │   │   │   ├── 02_Leveling_and_Experience.md
 │   │   │   └── 03_Skill_Trees
 │   │   │       ├── 01_Skill_Tree_Overview.md
 │   │   │       ├── 02_The_Warrior.md
 │   │   │       ├── 03_The_Guardian.md
 │   │   │       ├── 04_The_Marksman.md
 │   │   │       ├── 05_Smithing.md
 │   │   │       ├── 06_Alchemy.md
 │   │   │       ├── 07_Architect.md
 │   │   │       ├── 08_The_Wilds.md
 │   │   │       ├── 09_Shadow.md
 │   │   │       ├── 10_The_Tech.md
 │   │   │       ├── 11_Elementalism.md
 │   │   │       ├── 12_Aether.md
 │   │   │       └── 13_The_Void.md
 │   │   ├── 02_COMBAT_SYSTEMS
 │   │   │   ├── 01_Melee_Combat.md
 │   │   │   ├── 02_Ranged_Combat.md
 │   │   │   ├── 03_Stealth_Mechanics.md
 │   │   │   ├── 04_Damage_and_Armor_Formulas.md
 │   │   │   └── 05_Magic_Combat.txt
 │   │   ├── 03_MAGIC_SYSTEMS
 │   │   │   ├── 01_The_Grammar_of_Magic.md
 │   │   │   └── 02_Divine_Boons_and_Patronage.md
 │   │   ├── 04_SURVIVAL_SYSTEMS
 │   │   │   ├── 01_Player_Needs_and_Status_Effects.md
 │   │   │   └── 02_Environment_and_Weather.md
 │   │   ├── 05_CONSTRUCTION_SYSTEMS
 │   │   │   ├── 01_Crafting_Recipes_and_Stations.md
 │   │   │   ├── 02_Base_Building.md
 │   │   │   └── 03_Item_Modification_and_Upgrades.md
 │   │   └── 06_MODIFICATION_SYSTEMS
 │   │       └── 01_Subroutine_Fragment_System.md
 │   ├── 04_GAME_CONTENT
 │   │   ├── 01_ITEMS
 │   │   │   ├── 01_Resources_and_Materials.md
 │   │   │   ├── 02_Weapons.md
 │   │   │   ├── 03_Armor.md
 │   │   │   ├── 04_Tools.md
 │   │   │   ├── 05_Consumables.md
 │   │   │   ├── 06_Tech_and_Quest_Items.md
 │   │   │   └── 07_Equipment_and_Apparel
 │   │   │       ├── 01_Equipment_System_Overview.md
 │   │   │       ├── 02_Base_Layer_Apparel_(Shirts_Pants).md
 │   │   │       ├── 03_Outerwear_Apparel_(Jackets_Cloaks).md
 │   │   │       ├── 04_Hands_and_Feet_(Gloves_Boots).md
 │   │   │       ├── 05_Utility_Gear_(Belts_Rigs_slings).md
 │   │   │       ├── 06_Back_Gear_(Backpacks_pouches).md
 │   │   │       ├── 07_Exo-Suits_and_Mods.md
 │   │   │       └── 08_Accessories.md
 │   │   ├── 02_ENTITIES
 │   │   │   ├── 01_Enemy_AI_Behavior.md
 │   │   │   ├── 02_Enemy_List_Blighted.md
 │   │   │   ├── 03_Enemy_List_Wildlife.md
 │   │   │   ├── 04_BOSSES_&_LEGANDARY_BEASTS
 │   │   │   │   └── 01_Boss_and_Legendary_Beast_Roster.md
 │   │   │   ├── 05_Races.txt
 │   │   │   └── 06_Forge-Titans_(Dormant_Harvesters).md
 │   │   └── 03_INTERACTABLES
 │   │       ├── 01_Resource_Nodes_and_Containers.md
 │   │       └── 02_Puzzles_and_Traps.md
 │   ├── 05_USER_EXPERIENCE
 │   │   ├── 01_UX_Design_Philosophy.md
 │   │   ├── 02_UI_ELEMENTS
 │   │   │   ├── 01_HUD_(Heads-Up_Display).md
 │   │   │   ├── 02_Main_Menu_and_Settings.md
 │   │   │   ├── 03_Inventory_and_Crafting_Screen.md
 │   │   │   ├── 04_Character_and_Skills_Screen.md
 │   │   │   └── 05_Journal_and_Map_Screen.md
 │   │   └── 03_AUDIO
 │   │       ├── 01_Sound_Effects_Design.md
 │   │       └── 02_Music_Design.md
 │   ├── 06_TECHNICAL_AND_PRODUCTION
 │   │   ├── 01_Asset_Creation_Pipeline.md
 │   │   ├── 01a_LLM_Integration_Framework.md
 │   │   ├── 02_Build_and_Release_Process.md
 │   │   ├── 03_Testing_and_QA_Strategy.md
 │   │   └── 04_Modding_Support_Plan.md
 │   └── task_viewer.py
 ├── __init__.py
 ├── active_sessions.json
 ├── assets
 │   └── raw
 │       └── shaders
 │           ├── billboard_vertex.glsl
 │           ├── lit_color_fragment.glsl
 │           ├── lit_color_vertex.glsl
 │           ├── lit_textured_fragment.glsl
 │           ├── lit_textured_vertex.glsl
 │           ├── post_process_fragment.glsl
 │           ├── post_process_vertex.glsl
 │           ├── skybox_fragment.glsl
 │           ├── skybox_vertex.glsl
 │           ├── ui_color_vertex.glsl
 │           ├── unlit_chunk_fragment.glsl
 │           ├── unlit_chunk_vertex.glsl
 │           ├── unlit_color_3d_vertex.glsl
 │           ├── unlit_color_fragment.glsl
 │           ├── unlit_color_vertex.glsl
 │           ├── unlit_textured_fragment.glsl
 │           ├── unlit_textured_vertex.glsl
 │           ├── volumetric_clouds_fragment.glsl
 │           └── volumetric_clouds_vertex.glsl
 ├── core
 │   ├── __init__.py
 │   ├── engine.py
 │   ├── phonons.py
 │   ├── platform.py
 │   └── state_manager.py
 ├── debug_tool.py
 ├── game
 │   ├── __init__.py
 │   ├── block.py
 │   ├── chunk.py
 │   ├── components
 │   │   ├── __init__.py
 │   │   ├── base_component.py
 │   │   ├── health_component.py
 │   │   ├── inventory_component.py
 │   │   ├── item_component.py
 │   │   ├── needs_component.py
 │   │   ├── physics_component.py
 │   │   ├── player_input_component.py
 │   │   ├── render_component.py
 │   │   └── transform_component.py
 │   ├── data
 │   │   └── items.json
 │   ├── entity.py
 │   ├── entity_factory.py
 │   ├── menu_world.py
 │   ├── states
 │   │   ├── base_state.py
 │   │   ├── in_game_state.py
 │   │   ├── initialization_state.py
 │   │   ├── inventory_state.py
 │   │   ├── load_game_state.py
 │   │   ├── main_menu_state.py
 │   │   ├── new_game_state.py
 │   │   ├── options_state.py
 │   │   └── pause_state.py
 │   └── world.py
 ├── main.py
 ├── requirements.txt
 ├── systems
 │   ├── __init__.py
 │   ├── acoustic_system.py
 │   ├── asset_manager.py
 │   ├── audio_engine.py
 │   ├── camera.py
 │   ├── cloud_system.py
 │   ├── debug_manager.py
 │   ├── input_handler.py
 │   ├── item_manager.py
 │   ├── physics.py
 │   ├── player_control_system.py
 │   ├── renderer.py
 │   ├── save_manager.py
 │   ├── skybox.py
 │   ├── ui_manager.py
 │   └── world_generator.py
 ├── tools
 │   ├── __init__.py
 │   └── cooker.py
 ├── ui
 │   ├── __init__.py
 │   ├── layouts
 │   │   ├── initialization_screen.xml
 │   │   ├── inventory_menu.xml
 │   │   ├── load_game_menu.xml
 │   │   ├── main_menu.xml
 │   │   ├── new_game_menu.xml
 │   │   ├── options_menu.xml
 │   │   └── pause_menu.xml
 │   ├── screen.py
 │   └── widgets.py
 └── utils
     ├── __init__.py
     ├── color.py
     ├── debug_console.py
     ├── debug_overlay.py
     ├── logger.py
     ├── settings.py
     └── vectors.py

```
---
**Files for Review:**
### File: `/requirements.txt`
```txt
# /requirements.txt

# For platform, windowing, and input events
pygame

# For 3D physics simulation
# NOTE: Pymunk (2D physics) has been removed as it conflicts with the 3D world design.
pybullet

# For 3D graphics via OpenGL
PyOpenGL
PyOpenGL-accelerate

# For high-performance matrix and vector math
numpy
pyrr

# For procedural world generation via Perlin noise
noise
```

### File: `/main.py`
```py
# /main.py

import sys
import traceback
import argparse
from typing import Dict, Type

from utils.logger import initialize_logging, logger
from core.engine import Engine
from game.states.base_state import BaseState
from game.states.initialization_state import InitializationState
from game.states.main_menu_state import MainMenuState
from game.states.in_game_state import InGameState
from game.states.options_state import OptionsState
from game.states.pause_state import PauseState
from game.states.inventory_state import InventoryState
from game.states.new_game_state import NewGameState
from game.states.load_game_state import LoadGameState

def main():
    parser = argparse.ArgumentParser(description="Stelliferrum Forge - Where Giants Rust")
    parser.add_argument("--debug", action="store_true", help="Enable the developer debug tool and manager.")
    args = parser.parse_args()
    
    initialize_logging()
    
    logger.info("======================================================")
    logger.info("           Initializing Stelliferrum Forge...         ")
    if args.debug:
        logger.info("             (Debug Mode Enabled)                 ")
    logger.info("======================================================")

    engine_instance = None
    try:
        engine_instance = Engine()
        engine_instance.initialize(
            title="Stelliferrum Forge - Where Giants Rust", 
            width=1280, 
            height=720, 
            is_debug=args.debug
        )

        state_classes: Dict[str, Type[BaseState]] = {
            "INITIALIZATION": InitializationState, "MAIN_MENU": MainMenuState,
            "IN_GAME": InGameState, "OPTIONS": OptionsState, "PAUSE": PauseState,
            "INVENTORY": InventoryState, "NEW_GAME": NewGameState, "LOAD_GAME": LoadGameState
        }

        for name, state_class in state_classes.items():
            engine_instance.state_manager.register_state(name, state_class)
        
        engine_instance.state_manager.set_state("INITIALIZATION")
        engine_instance.run()

    except Exception as e:
        logger.critical(f"FATAL: An unhandled exception reached the main loop: {e}", exc_info=True)
    finally:
        if engine_instance:
            logger.info("Initiating engine shutdown procedure.")
            engine_instance.shutdown()
        
        logger.info("Stelliferrum Forge has shut down. Goodbye.")
        sys.exit()

if __name__ == "__main__":
    main()
```

### File: `/debug_tool.py`
```py
# /debug_tool.py

import tkinter as tk
from tkinter import ttk, scrolledtext, font, messagebox, Menu
import subprocess
import socket
import threading
import json
from queue import Queue
import os
import time
import sys

# --- Configuration ---
GAME_SCRIPT = "main.py"
GAME_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
LOG_SAVE_DIRECTORY = os.path.join(GAME_DIRECTORY, "debug_logs")

# Network Configuration
UDP_HOST = "127.0.0.1" 
UDP_RENDER_PORT = 12345
UDP_CONSOLE_PORT = 12346
TCP_COMMAND_PORT = 12347
HEARTBEAT_TIMEOUT = 3.0

# --- Theme Definition ---
class DarkTheme:
    BG_PRIMARY, BG_SECONDARY, BG_WIDGET = "#2e2e2e", "#3c3c3c", "#454545"
    FG_PRIMARY, FG_ACCENT = "#d3d3d3", "#e0e0e0"
    FG_SUCCESS, FG_WARN, FG_ERROR = "#4CAF50", "#FFC107", "#F44336"
    SELECT_BG, SELECT_FG = "#545454", "#ffffff"
    GOD_MODE_ACTIVE = "#6a1b9a" # A distinct purple for God Mode

class DevToolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stelliferrum Forge - Developer Console")
        self.geometry("1200x800")
        self.configure(bg=DarkTheme.BG_PRIMARY)

        # --- State Variables ---
        self.game_process = None
        self.last_heartbeat = 0
        self.udp_queue = Queue()
        self.entities = {}
        self.world_gen_params = {}
        self.physics_update_timer = None
        self.stop_event = threading.Event()
        self.edit_entry = None # For the inspector tree editor
        
        # --- UI Initialization ---
        self._setup_styles()
        self._create_menu()
        self._create_widgets()

        # --- Final Setup ---
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.start_listeners()
        self.process_udp_queue()

    def _create_menu(self):
        self.main_menu = Menu(self, bg=DarkTheme.BG_SECONDARY, fg=DarkTheme.FG_PRIMARY, tearoff=0)
        self.config(menu=self.main_menu)

        world_menu = Menu(self.main_menu, bg=DarkTheme.BG_WIDGET, fg=DarkTheme.FG_PRIMARY, tearoff=0)
        self.main_menu.add_cascade(label="World", menu=world_menu)
        world_menu.add_command(label="Export World Block Data...", command=self.export_world_data)
        
    def _setup_styles(self):
        self.style=ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('.', background=DarkTheme.BG_PRIMARY, foreground=DarkTheme.FG_PRIMARY, fieldbackground=DarkTheme.BG_WIDGET, borderwidth=0)
        self.style.configure('TFrame', background=DarkTheme.BG_PRIMARY)
        self.style.configure('TLabel', background=DarkTheme.BG_PRIMARY, foreground=DarkTheme.FG_ACCENT)
        self.style.configure('TButton', background=DarkTheme.BG_WIDGET, foreground=DarkTheme.FG_PRIMARY, borderwidth=0, focusthickness=0, padding=8)
        self.style.map('TButton', background=[('active', DarkTheme.SELECT_BG)], relief=[('pressed', 'flat')])
        self.style.configure('TNotebook', background=DarkTheme.BG_PRIMARY, borderwidth=0)
        self.style.configure('TNotebook.Tab', background=DarkTheme.BG_SECONDARY, foreground=DarkTheme.FG_PRIMARY, borderwidth=0, padding=(10, 5))
        self.style.map('TNotebook.Tab', background=[('selected', DarkTheme.BG_WIDGET)])
        self.style.configure("Treeview", rowheight=25, fieldbackground=DarkTheme.BG_SECONDARY, background=DarkTheme.BG_SECONDARY, foreground=DarkTheme.FG_PRIMARY)
        self.style.map("Treeview", background=[('selected', DarkTheme.SELECT_BG)])
        self.style.configure("Treeview.Heading", font=('Segoe UI', 10, 'bold'), background=DarkTheme.BG_WIDGET, borderwidth=0)
        self.style.configure("Vertical.TScrollbar", background=DarkTheme.BG_WIDGET, troughcolor=DarkTheme.BG_PRIMARY, arrowcolor=DarkTheme.FG_PRIMARY)
        self.style.configure('Success.TButton', background=DarkTheme.FG_SUCCESS, foreground='white')
        self.style.map('Success.TButton', background=[('active', '#388E3C')])
        
        self.style.configure('GodMode.TButton', background=DarkTheme.GOD_MODE_ACTIVE, foreground='white')
        self.style.map('GodMode.TButton', background=[('active', '#8e24aa')])

    def _create_widgets(self):
        self._create_top_bar()
        self._create_notebook()
        self._create_status_bar()
        
        self.console_font = font.Font(family="Consolas", size=10)
        self.console_log.tag_configure("INFO", foreground=DarkTheme.FG_PRIMARY)
        self.console_log.tag_configure("DEBUG", foreground="grey")
        self.console_log.tag_configure("WARNING", foreground=DarkTheme.FG_WARN)
        self.console_log.tag_configure("ERROR", foreground=DarkTheme.FG_ERROR)
        self.console_log.tag_configure("CRITICAL", foreground=DarkTheme.FG_ERROR, font=(self.console_font.cget("family"), self.console_font.cget("size"), "bold"))

    def _create_top_bar(self):
        top_frame = ttk.Frame(self, padding=10)
        top_frame.pack(fill=tk.X)
        ttk.Button(top_frame, text="▶ Launch / Relaunch Game", command=self.relaunch_game, style='Success.TButton').pack(side=tk.LEFT, padx=5)
        self.status_label = ttk.Label(top_frame, text="Status: Idle", foreground=DarkTheme.FG_WARN, font=('Segoe UI', 10))
        self.status_label.pack(side=tk.LEFT, padx=10)
    
    def _create_notebook(self):
        self.notebook = ttk.Notebook(self, padding=(10, 5))
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.create_console_tab()
        self.create_inspector_tab()
        self.create_render_log_tab()
        self.create_world_controls_tab()
        self.create_physics_inspector_tab()
        self.create_world_gen_tab()

    def _create_status_bar(self):
        self.status_bar = ttk.Frame(self, padding=5, relief='sunken', borderwidth=1)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.fps_label = ttk.Label(self.status_bar, text="FPS: --")
        self.fps_label.pack(side=tk.LEFT)
        self.ms_label = ttk.Label(self.status_bar, text="Frame Time: -- ms")
        self.ms_label.pack(side=tk.LEFT, padx=20)
        ttk.Separator(self.status_bar, orient='vertical').pack(side=tk.LEFT, fill='y', padx=10)
        self.frame_label = ttk.Label(self.status_bar, text="Frame: 0")
        self.frame_label.pack(side=tk.LEFT)

    def create_console_tab(self):
        console_pane = ttk.Frame(self.notebook, padding=5); self.notebook.add(console_pane, text='  Live Console  ')
        self.console_log = scrolledtext.ScrolledText(console_pane, bg=DarkTheme.BG_SECONDARY, fg=DarkTheme.FG_PRIMARY, font=("Consolas", 10), relief=tk.FLAT, borderwidth=0, wrap=tk.WORD)
        self.console_log.pack(fill=tk.BOTH, expand=True); self.console_log.config(state=tk.DISABLED)
        cmd_frame = ttk.Frame(console_pane, padding=(0, 5, 0, 0)); cmd_frame.pack(fill=tk.X)
        ttk.Button(cmd_frame, text="Save Console Log", command=self.save_console_log).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Label(cmd_frame, text=">").pack(side=tk.LEFT, padx=(0,5))
        self.command_entry = ttk.Entry(cmd_frame); self.command_entry.pack(fill=tk.X, expand=True, side=tk.LEFT, padx=5); self.command_entry.bind("<Return>", self.send_command)
        ttk.Button(cmd_frame, text="Send", command=self.send_command).pack(side=tk.RIGHT)
        
    def create_render_log_tab(self):
        render_frame = ttk.Frame(self.notebook, padding=(0,5,0,0)); self.notebook.add(render_frame, text='  Render Log  ')
        controls_frame = ttk.Frame(render_frame); controls_frame.pack(fill=tk.X, pady=(0, 5))
        ttk.Button(controls_frame, text="Export Selected", command=self.save_inspector_snapshot).pack(side=tk.LEFT, padx=(0, 10))
        self.filter_var = tk.StringVar(); self.filter_var.trace_add("write", self.filter_render_log)
        ttk.Label(controls_frame, text="Filter:").pack(side=tk.LEFT)
        ttk.Entry(controls_frame, textvariable=self.filter_var).pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.terrain_coverage_label = ttk.Label(controls_frame, text="Terrain Coverage: --%", width=25, anchor='e'); self.terrain_coverage_label.pack(side=tk.RIGHT)
        columns = ("id", "type", "view", "rend");
        self.render_tree = ttk.Treeview(render_frame, columns=columns, show="headings", selectmode='browse')
        self.render_tree.heading("id", text="Entity ID"); self.render_tree.heading("type", text="Type"); self.render_tree.heading("view", text="In Frustum"); self.render_tree.heading("rend", text="Rendered")
        for col in ["id", "type"]: self.render_tree.column(col, anchor=tk.W, width=150)
        for col in ["view", "rend"]: self.render_tree.column(col, anchor=tk.CENTER, width=100)
        scrollbar = ttk.Scrollbar(render_frame, orient=tk.VERTICAL, command=self.render_tree.yview); self.render_tree.configure(yscroll=scrollbar.set); scrollbar.pack(side=tk.RIGHT, fill=tk.Y); self.render_tree.pack(fill=tk.BOTH, expand=True)
        self.render_tree.tag_configure('yes', foreground=DarkTheme.FG_SUCCESS); self.render_tree.tag_configure('no', foreground=DarkTheme.FG_ERROR)
        self.render_tree.bind("<<TreeviewSelect>>", self.on_entity_select)

    def create_inspector_tab(self):
        self.inspector_frame = ttk.Frame(self.notebook, padding=10); self.notebook.add(self.inspector_frame, text='  Entity Inspector  ')
        ttk.Button(self.inspector_frame, text="Toggle Selected Entity Collision", command=self.toggle_selected_collision).pack(side=tk.TOP, anchor=tk.W, pady=(0, 10))
        self.inspector_label = ttk.Label(self.inspector_frame, text="Select an entity from the Render Log to inspect.", font=('Segoe UI', 10, 'italic')); self.inspector_label.pack()
        self.inspector_tree = ttk.Treeview(self.inspector_frame, columns=("property", "value"), show="headings")
        self.inspector_tree.heading("property", text="Property", anchor=tk.W); self.inspector_tree.heading("value", text="Value", anchor=tk.W)
        self.inspector_tree.bind("<Double-1>", self.on_tree_edit_start)

    def create_world_gen_tab(self):
        self.world_gen_frame = ttk.Frame(self.notebook, padding=10); self.notebook.add(self.world_gen_frame, text='  World Generation  ')
        self.world_gen_label = ttk.Label(self.world_gen_frame, text="World generation data will appear here.", font=('Segoe UI', 10, 'italic')); self.world_gen_label.pack()
        self.world_gen_tree = ttk.Treeview(self.world_gen_frame, columns=("parameter", "value"), show="headings"); self.world_gen_tree.heading("parameter", text="Parameter", anchor=tk.W); self.world_gen_tree.heading("value", text="Value", anchor=tk.W); self.world_gen_tree.column("parameter", width=200)

    def create_world_controls_tab(self):
        frame = ttk.Frame(self.notebook, padding=10); self.notebook.add(frame, text=' World Controls ')
        debug_frame = ttk.LabelFrame(frame, text="In-Game Debugging", padding=10); debug_frame.pack(fill=tk.X, pady=5)
        ttk.Button(debug_frame, text="Toggle In-Game Overlay (F3)", command=lambda: self.send_command(command="debug.toggle_overlay")).pack(side=tk.LEFT, padx=5)
        self.god_mode_button = ttk.Button(debug_frame, text="Toggle God Mode (Noclip)", command=self.toggle_god_mode); self.god_mode_button.pack(side=tk.LEFT, padx=5)
        time_frame = ttk.LabelFrame(frame, text="Time of Day", padding=10); time_frame.pack(fill=tk.X, pady=5)
        self.time_of_day_val = tk.DoubleVar(value=0.25)
        ttk.Scale(time_frame, from_=0.0, to=1.0, variable=self.time_of_day_val, orient=tk.HORIZONTAL, command=self.on_time_slider_change).pack(fill=tk.X, expand=True)
        spawn_frame = ttk.LabelFrame(frame, text="Entity Spawner", padding=10); spawn_frame.pack(fill=tk.X, pady=15)
        ttk.Label(spawn_frame, text="Entity Type:").pack(side=tk.LEFT, padx=5)
        self.spawn_type_entry = ttk.Entry(spawn_frame); self.spawn_type_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5); self.spawn_type_entry.insert(0, "enemy")
        ttk.Button(spawn_frame, text="Spawn Near Player", command=self.on_spawn_button_click).pack(side=tk.LEFT, padx=5)
        player_frame = ttk.LabelFrame(frame, text="Player Cheats", padding=10); player_frame.pack(fill=tk.X, pady=15)
        ttk.Button(player_frame, text="Set Health to 100", command=lambda: self.send_command(command="player.set_health 100")).pack(side=tk.LEFT, padx=5)
        ttk.Button(player_frame, text="Set Health to 10", command=lambda: self.send_command(command="player.set_health 10")).pack(side=tk.LEFT, padx=5)
        
    def create_physics_inspector_tab(self):
        frame = ttk.Frame(self.notebook, padding=10); self.notebook.add(frame, text=' Physics Inspector ')
        self.physics_stats_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, bg=DarkTheme.BG_SECONDARY, fg=DarkTheme.FG_PRIMARY, font=("Consolas", 12), state=tk.DISABLED, relief=tk.FLAT, borderwidth=0)
        self.physics_stats_text.pack(fill=tk.BOTH, expand=True)
        self.notebook.bind("<<TNotebookTabChanged>>", self.on_tab_change)

    # --- Listener and Network Methods ---
    def start_listeners(self):
        threading.Thread(target=self._udp_listener_thread, args=(UDP_RENDER_PORT,), daemon=True).start()
        threading.Thread(target=self._udp_listener_thread, args=(UDP_CONSOLE_PORT,), daemon=True).start()

    def _udp_listener_thread(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((UDP_HOST, port)); sock.settimeout(1.0)
            while not self.stop_event.is_set():
                try: data, _ = sock.recvfrom(65535); self.udp_queue.put((port, data))
                except socket.timeout: continue
        except Exception as e:
            print(f"FATAL ERROR in listener thread for port {port}: {e}", file=sys.stderr)
            self.after(100, lambda: messagebox.showerror("Network Error", f"Could not bind to port {port}. Is another instance running?"))

    def process_udp_queue(self):
        while not self.udp_queue.empty():
            port, data = self.udp_queue.get_nowait()
            try:
                message = json.loads(data.decode('utf-8'))
                if port == UDP_RENDER_PORT: self.update_render_log(message)
                elif port == UDP_CONSOLE_PORT: self._process_console_message(message)
                self.status_label.config(text="Status: Connected", foreground=DarkTheme.FG_SUCCESS); self.last_heartbeat = time.time()
            except (json.JSONDecodeError, UnicodeDecodeError): pass
        if self.game_process and self.game_process.poll() is not None: self.status_label.config(text="Status: Disconnected (Process Terminated)", foreground=DarkTheme.FG_ERROR)
        elif self.last_heartbeat and (time.time() - self.last_heartbeat > HEARTBEAT_TIMEOUT): self.status_label.config(text="Status: Disconnected (Timeout)", foreground=DarkTheme.FG_WARN)
        self.after(16, self.process_udp_queue)

    def _process_console_message(self, message):
        msg_type = message.get('type')
        if msg_type == 'log': self.update_console_log(message)
        elif msg_type == 'world_gen': self.update_world_gen_tab(message)
        elif msg_type == 'status_update': self.update_god_mode_button(message.get('god_mode', False))
            
    def send_command(self, event=None, command=None):
        cmd_to_send = command if command is not None else self.command_entry.get()
        if not cmd_to_send: return
        if command is None: self.command_entry.delete(0, tk.END)
        if not cmd_to_send.startswith(("debug.select", "entity.set")): self.log_to_console(f"> {cmd_to_send}", "DEBUG")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3.0); s.connect((UDP_HOST, TCP_COMMAND_PORT)); s.sendall(cmd_to_send.encode('utf-8'))
                response_data = s.recv(16384).decode('utf-8'); is_error = "error" in response_data.lower()
                if not cmd_to_send.startswith(("debug.select", "world.export_data", "physics.get_stats")):
                    self.log_to_console(response_data, "ERROR" if is_error else "INFO")
                return response_data
        except Exception as e: self.log_to_console(f"Error sending command: {e}", "ERROR")
        return None
        
    def on_closing(self):
        self.stop_event.set()
        if self.game_process and self.game_process.poll() is None: self.game_process.terminate()
        self.destroy()

    def relaunch_game(self):
        if self.game_process and self.game_process.poll() is None:
            self.game_process.terminate()
            try: self.game_process.wait(timeout=3)
            except subprocess.TimeoutExpired: self.game_process.kill()
        
        self.render_tree.delete(*self.render_tree.get_children())
        self.log_to_console("--- New Game Session Started ---", "DEBUG", clear=True)
        if hasattr(self, 'world_gen_tree'): self.world_gen_tree.delete(*self.world_gen_tree.get_children())
        self.entities.clear(); self.filter_var.set("") 
        if hasattr(self, 'god_mode_button'): self.update_god_mode_button(False)

        self.game_process = subprocess.Popen([sys.executable, GAME_SCRIPT, "--debug"], cwd=GAME_DIRECTORY)
        self.status_label.config(text="Status: Launching...", foreground="cyan"); self.last_heartbeat = time.time()
        
    def export_world_data(self):
        self.log_to_console("Requesting world data...", "DEBUG")
        response = self.send_command(command="world.export_data")
        if response and not response.startswith("Error"):
            try: self._save_data_to_file(json.loads(response), "WorldData", "World Data")
            except json.JSONDecodeError: self.log_to_console("Failed to decode world data response.", "ERROR")
        else: messagebox.showerror("Export Failed", "Could not retrieve world data.")

    def _save_data_to_file(self, data, file_prefix, file_type):
        if not data: messagebox.showinfo(f"Save {file_type}", "No data to save."); return
        try:
            os.makedirs(LOG_SAVE_DIRECTORY, exist_ok=True)
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{timestamp}_{file_prefix}.json" if isinstance(data,(dict,list)) else f"{timestamp}_{file_prefix}.txt"
            filepath = os.path.join(LOG_SAVE_DIRECTORY, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                if isinstance(data, (dict, list)): json.dump(data, f, indexnt=4)
                else: f.write(str(data))
            messagebox.showinfo("Save Successful", f"Saved to:\n{filepath}")
        except Exception as e: messagebox.showerror("Save Error", f"An error occurred:\n{e}")

    def save_inspector_snapshot(self):
        selections = self.render_tree.selection()
        if not selections: messagebox.showinfo("Save Inspector", "Please select an entity in the Render Log first."); return
        data = {self.render_tree.item(item, "values")[0]: self.entities.get(self.render_tree.item(item, "values")[0]) for item in selections}
        self._save_data_to_file(data, "InspectorSnapshot", "Inspector Data")

    def save_console_log(self):
        content = self.console_log.get("1.0", tk.END).strip()
        if not content: messagebox.showinfo("Save Log", "Log is empty."); return
        self._save_data_to_file(content, f"ConsoleLog", "Console Log")

    def log_to_console(self, message, level, clear=False):
        self.console_log.config(state=tk.NORMAL)
        if clear: self.console_log.delete("1.0", tk.END)
        self.console_log.insert(tk.END, f"[{level.upper()}] {message}\n", level.upper()); self.console_log.see(tk.END); self.console_log.config(state=tk.DISABLED)

    def update_render_log(self, data):
        self.frame_label.config(text=f"Frame: {data.get('frame', 0)}"); self.fps_label.config(text=f"FPS: {data.get('fps', 0):.1f}"); self.ms_label.config(text=f"Frame Time: {data.get('frame_time', 0.0):.2f} ms")
        self.terrain_coverage_label.config(text=f"Terrain Coverage: {data.get('terrain_coverage', 0.0):.1f}%")
        current_selection = self.render_tree.selection()
        self.entities = data.get('entities', {})
        self.filter_render_log()
        if current_selection: self.on_entity_select(None, from_update=True)
        
    def filter_render_log(self, *args):
        query = self.filter_var.get().lower()
        current_ids_in_tree = set(self.render_tree.get_children())
        ids_to_render = set()
        for entity_id, entity_data in self.entities.items():
            str_id = str(entity_id)
            if query in str_id.lower() or query in entity_data.get('type', '').lower():
                self._update_render_log_row(str_id, entity_data); ids_to_render.add(str_id)
        ids_to_remove = current_ids_in_tree - ids_to_render
        if ids_to_remove: self.render_tree.delete(*list(ids_to_remove))
            
    def _update_render_log_row(self, entity_id_str, entity_data):
        values = (entity_id_str, entity_data.get('type','N/A'), "✓" if entity_data.get('is_in_frustum') else "✗", "✓" if entity_data.get('rendered') else "✗")
        tags = ('yes' if entity_data.get('rendered') else 'no',)
        if not self.render_tree.exists(entity_id_str): self.render_tree.insert("", "end", iid=entity_id_str, values=values, tags=tags)
        else: self.render_tree.item(entity_id_str, values=values, tags=tags)
    
    # --- START OF DEFINITIVE FIX: Preserve Inspector Open State ---
    def on_entity_select(self, event, from_update=False):
        selections = self.render_tree.selection()
        if not selections: return
        entity_id_str = self.render_tree.item(selections[0], "values")[0]
        
        if not from_update:
            self.send_command(command=f"debug.select {entity_id_str}") 
            self.notebook.select(self.inspector_frame)

        if entity_id_str in self.entities:
            open_states = {}
            if from_update:
                for item_id in self.inspector_tree.get_children():
                    open_states[self.inspector_tree.item(item_id, "values")[0]] = self.inspector_tree.item(item_id, "open")

            self.inspector_label.pack_forget(); self.inspector_tree.pack(fill=tk.BOTH, expand=True)
            self.inspector_tree.delete(*self.inspector_tree.get_children())
            
            entity_data = self.entities[entity_id_str].get('data', {})
            for component_name, component_data in sorted(entity_data.items()):
                parent_iid = f"comp_{component_name}"; parent_value = f"[{component_name}]"
                parent_is_open = open_states.get(parent_value, False)
                
                parent_item = self.inspector_tree.insert("", "end", iid=parent_iid, values=(parent_value, ""), open=parent_is_open)
                
                if isinstance(component_data, dict):
                    for prop, value in sorted(component_data.items()):
                        val_str = json.dumps(value) if isinstance(value, dict) else (", ".join([f"{v:.2f}" for v in value]) if isinstance(value, list) else value)
                        self.inspector_tree.insert(parent_item, "end", values=(f"  {prop}", val_str))
    # --- END OF FIX ---

    def update_console_log(self, data): self.log_to_console(data.get('message'), data.get('level'))
    def update_world_gen_tab(self, data):
        self.world_gen_params = data.get('params', {}); self.world_gen_label.pack_forget()
        self.world_gen_tree.pack(fill=tk.BOTH, expand=True); self.world_gen_tree.delete(*self.world_gen_tree.get_children())
        for param, value in self.world_gen_params.items(): self.world_gen_tree.insert("", "end", values=(param, value))
            
    def on_tab_change(self, event):
        if self.edit_entry: self.on_tree_edit_cancel(None)
        try:
            tab_name = self.notebook.tab(self.notebook.select(), "text").strip()
            if tab_name == 'Physics Inspector':
                if self.physics_update_timer is None: self.request_physics_stats()
            elif self.physics_update_timer is not None:
                self.after_cancel(self.physics_update_timer); self.physics_update_timer = None
        except tk.TclError:
            if self.physics_update_timer: self.after_cancel(self.physics_update_timer); self.physics_update_timer = None
    
    def request_physics_stats(self):
        response = self.send_command(command="physics.get_stats")
        if response and response.startswith('{'):
            try:
                stats = json.loads(response); self.physics_stats_text.config(state=tk.NORMAL)
                self.physics_stats_text.delete("1.0", tk.END)
                if "error" in stats: self.physics_stats_text.insert("1.0", f"Error from game: {stats['error']}")
                else:
                    content = "--- PyBullet Simulation Stats ---\n\n"; general_stats = {k: v for k, v in stats.items() if k != 'body_list'}
                    for key, value in general_stats.items(): content += f"{key.replace('_', ' ').title():<25}: {value}\n"
                    content += "\n--- Active Physics Bodies ---\n"
                    if stats.get('body_list'):
                        for body_info in stats['body_list']: content += f"- {body_info}\n"
                    else: content += "No active bodies.\n"
                    self.physics_stats_text.insert("1.0", content)
            except json.JSONDecodeError: self.log_to_console("Failed to parse physics stats.", "ERROR")
            self.physics_stats_text.config(state=tk.DISABLED)
        self.physics_update_timer = self.after(1000, self.request_physics_stats)

    def on_time_slider_change(self, value): self.send_command(command=f"world.set_time {float(value):.3f}")
    def on_spawn_button_click(self):
        entity_type = self.spawn_type_entry.get();
        if entity_type: self.send_command(command=f"world.spawn {entity_type}")

    def toggle_god_mode(self): self.send_command(command="debug.toggle_god_mode")
    def toggle_selected_collision(self):
        if not self.render_tree.selection(): messagebox.showwarning("Warning", "No entity selected."); return
        self.send_command(command="selected.toggle_collision")

    def update_god_mode_button(self, is_active: bool):
        if is_active: self.god_mode_button.config(style="GodMode.TButton", text="God Mode: ACTIVE")
        else: self.god_mode_button.config(style="TButton", text="Toggle God Mode (Noclip)")
    
    # --- START OF REVISED EDIT LOGIC ---
    def on_tree_edit_start(self, event):
        if self.edit_entry: self.edit_entry.destroy()
        
        item_id = self.inspector_tree.identify_row(event.y)
        if not item_id or self.inspector_tree.identify_column(event.x) != "#2" or not self.inspector_tree.parent(item_id):
            return

        x, y, width, height = self.inspector_tree.bbox(item_id, "value")
        self.edit_entry = ttk.Entry(self.inspector_tree, style="TEntry")
        self.edit_entry.place(x=x, y=y, width=width, height=height)
        
        original_value = self.inspector_tree.set(item_id, "value")
        self.edit_entry.insert(0, original_value)
        self.edit_entry.select_range(0, 'end'); self.edit_entry.focus_set()
        
        # Capture stable identifiers instead of the volatile item_id
        prop_name = self.inspector_tree.item(item_id, "values")[0].strip()
        parent_id = self.inspector_tree.parent(item_id)
        component_name = self.inspector_tree.item(parent_id, "values")[0].strip("[]")
        
        self.edit_entry.bind("<Return>", lambda e, c=component_name, p=prop_name: self.on_tree_edit_commit(e, c, p))
        self.edit_entry.bind("<Escape>", self.on_tree_edit_cancel)
        self.edit_entry.bind("<FocusOut>", self.on_tree_edit_cancel)

    def on_tree_edit_commit(self, event, component_name, prop_name):
        new_value = self.edit_entry.get()
        self.on_tree_edit_cancel(None) # Clean up the entry box
        
        selections = self.render_tree.selection()
        if not selections: return
        entity_id = self.render_tree.item(selections[0], "values")[0]
        
        # Send the command and let the UDP update refresh the view
        command = f"entity.set_component_trait {entity_id} {component_name} {prop_name} {new_value}"
        self.send_command(command=command)

    def on_tree_edit_cancel(self, event):
        if self.edit_entry:
            self.edit_entry.destroy(); self.edit_entry = None
    # --- END OF REVISED EDIT LOGIC ---

if __name__ == "__main__":
    try: app = DevToolApp(); app.mainloop()
    except Exception as e:
        print(f"A fatal error occurred: {e}", file=sys.stderr); traceback.print_exc()
        try:
            root = tk.Tk(); root.withdraw() 
            messagebox.showerror("Fatal Error", f"The dev tool failed to start.\n\nError: {e}\n\nCheck console output.")
        except tk.TclError: pass
```

### File: `/active_sessions.json`
```json
{}
```

### File: `/__init__.py`
```py

```

### File: `/README.md`
```md
# README.md

# Stelliferrum Forge

Welcome to the Stelliferrum Forge, a lightweight, custom-built, and highly specialized game engine.

This project is architected from the ground up to serve one unifying, foundational principle:

**The Principle of Physicality: Everything Has Weight.**

## Core Pillars

1.  **Simulated Mass & Materiality**: Every entity has a defined `mass` and `material_type`.
2.  **Acoustic Mass & Resonance**: Sound is treated as a physical phenomenon.
3.  **Structural Integrity & Weight Distribution**: A physics-based building system.
4.  **Intelligent Rendering**: A photography-inspired lighting model with progressive refinement.
5.  **LLM-Assisted Architecture**: Modular components with clean APIs designed for LLM integration.

## How to Run

1.  Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the engine:
    ```bash
    python main.py
    ```
```

### File: `/OverlayApp`
```text
# OverlayApp

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE-specific
.idea/
.vscode/
*.swp
*.swo

# Cooked assets
assets/cooked/

# Logs & Save Data
logs/
debug_logs/
saves/
menu_world.dat
```

### File: `/utils/vectors.py`
```py
# /utils/vectors.py

# To simplify and use industry-standard, high-performance libraries, we will
# alias the vector types here. This creates a single, consistent point of import.
# - pygame.math.Vector2 is excellent and sufficient for all 2D UI and input logic.
# - pyrr.Vector3 is a powerful, numpy-based vector perfect for 3D world math and OpenGL.

from pygame.math import Vector2
from pyrr import Vector3, Quaternion, Matrix44
```

### File: `/utils/settings.py`
```py
# utils/settings.py
GAME_SETTINGS = {
    "invert_y": False,  # <-- Default is now NOT inverted
    "mouse_sensitivity": 0.1
}
```

### File: `/utils/logger.py`
```py
# utils/logger.py

import logging
import os
from datetime import datetime

logger = logging.getLogger("StelliferrumForge")

class DebugManagerHandler(logging.Handler):
    """A handler that redirects log records to the debug manager's console log."""
    def __init__(self, debug_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.debug_manager = debug_manager

    def emit(self, record):
        if self.debug_manager and self.debug_manager.is_enabled:
            log_entry = self.format(record)
            self.debug_manager.log_console(log_entry, record.levelname)

def initialize_logging():
    """Initializes the standard file and console loggers."""
    if logger.hasHandlers():
        logger.handlers.clear()

    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(log_dir, f"stelliferrum_log_{timestamp}.log")
    logger.setLevel(logging.DEBUG)

    # File Handler (always active, logs everything)
    file_handler = logging.FileHandler(log_file)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)-8s - [%(module)s.%(funcName)s:%(lineno)d] - %(message)s')
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    
    # Standard Console Handler (prints to the terminal where the game was launched)
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(levelname)-8s - %(message)s')
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO) # Only show INFO and above in the terminal
    logger.addHandler(console_handler)

    logger.info("Standard logging system initialized.")
    logger.info(f"Log file will be saved to: {log_file}")

def attach_debug_handler(debug_manager):
    """Attaches the debug tool log handler *after* the debug manager has been created."""
    debug_handler = DebugManagerHandler(debug_manager)
    # This formatter ensures only the core message goes to the tool's console
    debug_handler.setFormatter(logging.Formatter('%(message)s'))
    debug_handler.setLevel(logging.DEBUG)
    logger.addHandler(debug_handler)
    logger.info("Debug log handler attached to external developer tool.")
```

### File: `/utils/debug_overlay.py`
```py
# /utils/debug_overlay.py

import pygame
import pyrr
import math
import numpy as np
from utils.color import WHITE, BLACK, Color
from utils.vectors import Vector2, Vector3
import game.components as C

class DebugOverlay:
    """
    Renders real-time engine and game state information directly onto the screen.
    This is a powerful tool for debugging when the main renderer isn't showing what you expect.
    """
    def __init__(self, engine):
        self.engine = engine
        self.is_visible = False
        self.font_size = 16
        self.line_height = 18
        self.position = Vector2(10, 10)
        self.text_color = WHITE
        self.bg_color = Color(10, 10, 20, 200) # Semi-transparent dark background
        self.display_distance = 30.0 # How far to render entity info

    def toggle(self):
        """Toggles the visibility of the overlay."""
        self.is_visible = not self.is_visible

    def render(self, renderer, world, player, camera):
        """Draws the debug text to the screen."""
        if not self.is_visible or not all([renderer, world, player, camera]):
            return

        # --- Gather Data ---
        cam_pos = camera.position
        cam_yaw = camera.yaw
        cam_pitch = camera.pitch
        entity_count = len(world.entities)
        chunk_count = len(world.chunks)
        fps = 1 / self.engine.get_delta_time() if self.engine.get_delta_time() > 0 else 0
        
        # --- Format Text ---
        debug_lines = [
            f"--- Stelliferrum Forge Debug ---",
            f"FPS: {self.engine.get_delta_time() * 1000.0:.2f} ms ({fps:.1f} FPS)",
            f"",
            f"[Camera]",
            f"  Pos: ({cam_pos.x:.2f}, {cam_pos.y:.2f}, {cam_pos.z:.2f})",
            f"  Yaw: {cam_yaw:.2f}, Pitch: {cam_pitch:.2f}",
            f"",
            f"[World]",
            f"  Total Entities: {entity_count}",
            f"  Loaded Chunks: {chunk_count}",
            f"--- Nearby Entities (Radius: {self.display_distance}m) ---"
        ]
        
        # --- NEW: Display Player and Nearby Entities ---
        player_transform = player.get_component(C.TransformComponent)
        if player_transform:
            player_pos = player_transform.position
            player_forward = (player_transform.rotation * Vector3([0,0,-1])).normalized
            
            # Get quick-look arrow for player
            p_arrow = ""
            abs_x, abs_z = abs(player_forward.x), abs(player_forward.z)
            if abs_x > abs_z and abs_x > 0.5: p_arrow = ">" if player_forward.x > 0 else "<"
            elif abs_z > abs_x and abs_z > 0.5: p_arrow = "^" if player_forward.z < 0 else "v"

            debug_lines.extend([
                f"[Player ID: {player.id}] {p_arrow}",
                f"  Pos: ({player_pos.x:.2f}, {player_pos.y:.2f}, {player_pos.z:.2f})",
                f"  Fwd: ({player_forward.x:.2f}, {player_forward.y:.2f}, {player_forward.z:.2f})"
            ])

            for entity in world.entities.values():
                if entity.id == player.id:
                    continue
                
                transform = entity.get_component(C.TransformComponent)
                if not transform:
                    continue

                distance = np.linalg.norm(player_pos - transform.position)
                if distance > self.display_distance:
                    continue

                forward_vec = (transform.rotation * Vector3([0,0,-1])).normalized
                
                arrow = ""
                abs_x, abs_z = abs(forward_vec.x), abs(forward_vec.z)
                if abs_x > abs_z and abs_x > 0.5: arrow = ">" if forward_vec.x > 0 else "<"
                elif abs_z > abs_x and abs_z > 0.5: arrow = "^" if forward_vec.z < 0 else "v"

                debug_lines.extend([
                    f"- ID: {entity.id} ({entity.name}) {arrow}",
                    f"  Pos: ({transform.position.x:.1f}, {transform.position.y:.1f}, {transform.position.z:.1f})",
                    f"  Fwd: ({forward_vec.x:.2f}, {forward_vec.y:.2f}, {forward_vec.z:.2f})"
                ])


        # --- Render Text ---
        max_width = 0
        for line in debug_lines:
            try:
                w, _ = renderer.get_text_dimensions(line, None, self.font_size)
                if w > max_width:
                    max_width = w
            except Exception:
                return
        
        bg_rect = pygame.Rect(self.position.x - 5, self.position.y - 5, max_width + 10, len(debug_lines) * self.line_height + 10)
        renderer.draw_rect(bg_rect, self.bg_color)
        
        for i, line in enumerate(debug_lines):
            text_pos = self.position + Vector2(0, i * self.line_height)
            renderer.draw_text(line, text_pos, None, self.font_size, self.text_color)
```

### File: `/utils/debug_console.py`
```py
# utils/debug_console.py

import pygame
from collections import deque
from utils.color import Color, WHITE

class DebugConsole:
    """
    A simple, on-screen console to display live log messages.
    """
    def __init__(self, max_lines=15):
        self.messages = deque(maxlen=max_lines)
        self.font_size = 14
        self.line_height = 16
        self.position = (10, 10)
        self.text_color = WHITE
        self.bg_color = Color(20, 20, 30, 180) # Semi-transparent dark blue
        self.visible = True

    def add_message(self, message: str):
        """Adds a new message to the console display."""
        self.messages.append(message)

    def render(self, renderer):
        """Draws the console and its messages to the screen."""
        if not self.visible or not self.messages:
            return

        max_width = 0
        for msg in self.messages:
            try:
                width, _ = renderer.get_text_dimensions(msg, None, self.font_size)
                if width > max_width:
                    max_width = width
            except Exception:
                pass
        
        bg_height = len(self.messages) * self.line_height + 10
        bg_rect = pygame.Rect(self.position[0] - 5, self.position[1] - 5, max_width + 10, bg_height)
        
        renderer.draw_rect(bg_rect, self.bg_color)

        for i, message in enumerate(self.messages):
            text_pos = pygame.Vector2(self.position[0], self.position[1] + (i * self.line_height))
            renderer.draw_text(message, text_pos, None, self.font_size, self.text_color)
```

### File: `/utils/color.py`
```py
# /utils/color.py

from collections import namedtuple

# Color object containing {r, g, b, a} values (0-255).
Color = namedtuple('Color', ['r', 'g', 'b', 'a'])

# Common color constants
WHITE = Color(255, 255, 255, 255)
BLACK = Color(0, 0, 0, 255)
RED = Color(255, 0, 0, 255)
GREEN = Color(0, 255, 0, 255)
BLUE = Color(0, 0, 255, 255)
```

### File: `/utils/__init__.py`
```py

```

### File: `/ui/widgets.py`
```py
# /ui/widgets.py

import pygame
from utils.vectors import Vector2
from utils.color import Color, WHITE

class Widget:
    """Base class for all UI elements."""
    def __init__(self, rect: pygame.Rect):
        self.rect = rect
        self.visible = True
    
    def update(self, delta_time, input_handler):
        pass

    def render(self, renderer):
        raise NotImplementedError

class Label(Widget):
    """A simple text label for the OpenGL UI."""
    def __init__(self, text: str, position: Vector2, font_id=None, size=24, color=WHITE):
        self.text = text
        self.position = position
        self.font_id = font_id
        self.size = size
        self.color = color
        super().__init__(pygame.Rect(position.x, position.y, 0, 0))

    def render(self, renderer):
        if self.visible:
            renderer.draw_text(self.text, self.position, self.font_id, self.size, self.color)
        
class Button(Widget):
    """A clickable button updated for the OpenGL renderer."""
    def __init__(self, rect: pygame.Rect, text: str, on_click=None):
        super().__init__(rect)
        self._text = text # Use a private variable
        self.on_click = on_click
        
        self.font_size = 28
        self.is_hovered = False
        
        self.color_default = Color(50, 50, 70, 255)
        self.color_hover = Color(80, 80, 100, 255)
        self.color_text = WHITE

        # --- NEW: Cache for text dimensions and position ---
        self._text_dims = None
        self._text_pos = None

    # --- NEW: Use a property to automatically update cache when text changes ---
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if self._text != value:
            self._text = value
            # Invalidate the cache when text changes
            self._text_dims = None
            self._text_pos = None

    def update(self, delta_time, input_handler):
        if not self.visible:
            self.is_hovered = False
            return

        mouse_pos = input_handler.get_mouse_position()
        self.is_hovered = self.rect.collidepoint(mouse_pos.x, mouse_pos.y)
        
        if self.is_hovered and input_handler.is_mouse_button_pressed(0):
            if self.on_click:
                self.on_click()

    def render(self, renderer):
        if not self.visible:
            return
            
        bg_color = self.color_hover if self.is_hovered else self.color_default
        renderer.draw_rect(self.rect, bg_color)
        
        # --- MODIFICATION: Use the cached values for better performance ---
        if self._text_dims is None:
            self._text_dims = renderer.get_text_dimensions(self.text, None, self.font_size)
        
        if self._text_pos is None:
            text_pos_x = self.rect.centerx - (self._text_dims[0] / 2)
            text_pos_y = self.rect.centery - (self._text_dims[1] / 2)
            self._text_pos = pygame.Vector2(text_pos_x, text_pos_y)

        renderer.draw_text(self.text, self._text_pos, None, self.font_size, self.color_text)
```

### File: `/ui/screen.py`
```py
# /ui/screen.py

class UIScreen:
    """A generic container for a collection of UI widgets."""
    def __init__(self, screen_id):
        self.id = screen_id
        self.widgets = []
        # --- NEW: A dictionary to hold widgets with an ID for easy access ---
        self.widget_map = {}

    def add_widget(self, widget, widget_id=None):
        """Adds a widget to the screen. If an ID is provided, it's mapped."""
        self.widgets.append(widget)
        if widget_id:
            self.widget_map[widget_id] = widget

    def get_widget(self, widget_id: str):
        """Retrieves a widget by its unique ID."""
        return self.widget_map.get(widget_id)

    def update(self, delta_time, input_handler):
        for widget in self.widgets:
            widget.update(delta_time, input_handler)
    
    def render(self, renderer):
        for widget in self.widgets:
            widget.render(renderer)
```

### File: `/ui/__init__.py`
```py

```

### File: `/ui/layouts/pause_menu.xml`
```xml
<!-- /ui/layouts/pause_menu.xml -->
<screen id="pause_menu">
    <widget type="Label" text="Paused" size="64">
        <position x="center" y="200" />
    </widget>
    
    <widget type="Button" text="Resume" on_click="resume_game">
        <rect x="center" y="320" width="250" height="50" />
    </widget>

    <widget type="Button" text="Save Game" on_click="save_game">
        <rect x="center" y="390" width="250" height="50" />
    </widget>

    <widget type="Button" text="Load Game" on_click="load_game">
        <rect x="center" y="460" width="250" height="50" />
    </widget>

    <widget type="Button" text="Quit to Menu" on_click="quit_to_menu">
        <rect x="center" y="530" width="250" height="50" />
    </widget>
</screen>
```

### File: `/ui/layouts/options_menu.xml`
```xml
<!-- ui/layouts/options_menu.xml -->
<screen id="options_menu">
    <widget type="Label" text="Options" size="64">
        <position x="center" y="150" />
    </widget>
    
    <widget type="Button" text="Invert Y: OFF" on_click="toggle_invert_y">
        <rect x="center" y="300" width="300" height="50" />
    </widget>

    <widget type="Button" text="Back" on_click="back_to_main">
        <rect x="center" y="450" width="200" height="50" />
    </widget>
</screen>
```

### File: `/ui/layouts/new_game_menu.xml`
```xml
<!-- /ui/layouts/new_game_menu.xml -->
<screen id="new_game_menu">
    <widget type="Label" text="New Game" size="64">
        <position x="center" y="150" />
    </widget>
    
    <widget type="Button" text="Set Seed: 12345" on_click="set_world_seed" id="seed_button">
        <rect x="center" y="300" width="300" height="50" />
    </widget>
    
    <!-- Add more buttons here for other world gen params like scale, octaves etc. -->

    <widget type="Button" text="Start Game" on_click="start_new_game">
        <rect x="center" y="450" width="200" height="50" />
    </widget>

    <widget type="Button" text="Back" on_click="back_to_main">
        <rect x="center" y="520" width="200" height="50" />
    </widget>
</screen>
```

### File: `/ui/layouts/main_menu.xml`
```xml
<!-- /ui/layouts/main_menu.xml -->
<screen id="main_menu">
    <widget type="Label" text="Where Giants Rust" size="64">
        <position x="center" y="250" />
    </widget>
    
    <widget type="Button" text="New Game" on_click="start_game">
        <rect x="center" y="380" width="200" height="50" />
    </widget>

    <widget type="Button" text="Load Game" on_click="load_game">
        <rect x="center" y="450" width="200" height="50" />
    </widget>

    <widget type="Button" text="Options" on_click="open_options">
        <rect x="center" y="520" width="200" height="50" />
    </widget>

    <widget type="Button" text="Quit" on_click="quit_game">
        <rect x="center" y="590" width="200" height="50" />
    </widget>
</screen>
```

### File: `/ui/layouts/load_game_menu.xml`
```xml
<!-- /ui/layouts/load_game_menu.xml -->
<screen id="load_game_menu">
    <widget type="Label" text="Load Chronicle" size="48">
        <position x="center" y="50" />
    </widget>

    <!-- The area where save file buttons will be dynamically created starts here -->
    <!-- A label to show if no saves are found -->
    <widget type="Label" text="No save files found." size="24" id="no_saves_label">
        <position x="center" y="300" />
    </widget>

    <!-- Control Buttons -->
    <widget type="Button" text="Load Selected" on_click="load_selected">
        <rect x="200" y="650" width="200" height="50" />
    </widget>

    <widget type="Button" text="Delete Selected" on_click="delete_selected">
        <rect x="425" y="650" width="200" height="50" />
    </widget>

    <widget type="Button" text="Select All" on_click="select_all">
        <rect x="650" y="650" width="150" height="50" />
    </widget>

    <widget type="Button" text="Select None" on_click="select_none">
        <rect x="825" y="650" width="150" height="50" />
    </widget>

    <widget type="Button" text="Back" on_click="back_to_main">
        <rect x="1050" y="650" width="150" height="50" />
    </widget>
</screen>
```

### File: `/ui/layouts/inventory_menu.xml`
```xml
<!-- /ui/layouts/inventory_menu.xml -->
<screen id="inventory_menu">

    <!-- Main Title -->
    <widget type="Label" text="INVENTORY" size="48">
        <position x="center" y="50" />
    </widget>

    <!-- 
    =================================================
    LEFT PANEL: CHARACTER & EQUIPPED GEAR
    This panel shows the player's stats and what they are currently wearing.
    The 3D model described in the GDD would be rendered here by the engine.
    =================================================
    -->

    <!-- Character Stats Section -->
    <widget type="Label" text="Character Stats" size="24">
        <position x="100" y="120" />
    </widget>
    
    <widget type="Label" text="Health:" size="18">
        <position x="100" y="160" />
    </widget>
    <widget type="Label" text="[100 / 100]" size="18" id="health_value_label">
        <position x="250" y="160" />
    </widget>

    <widget type="Label" text="Stamina:" size="18">
        <position x="100" y="190" />
    </widget>
    <widget type="Label" text="[100 / 100]" size="18" id="stamina_value_label">
        <position x="250" y="190" />
    </widget>

    <widget type="Label" text="Armor Rating:" size="18">
        <position x="100" y="220" />
    </widget>
    <widget type="Label" text="[ 0 ]" size="18" id="armor_value_label">
        <position x="250" y="220" />
    </widget>

    <!-- Equipped Gear Section -->
    <widget type="Label" text="Equipped Gear" size="24">
        <position x="100" y="280" />
    </widget>

    <!-- Placeholder slots for equipped items. In the real game, these would be
         Image widgets or buttons displaying the item icon. -->
    <widget type="Label" text="Head:" size="18">
        <position x="100" y="320" />
    </widget>
    <widget type="Button" text="Empty">
        <rect x="275" y="320" width="150" height="40" />
    </widget>

    <widget type="Label" text="Body Armor:" size="18">
        <position x="100" y="370" />
    </widget>
    <widget type="Button" text="Empty">
        <rect x="275" y="370" width="150" height="40" />
    </widget>

    <widget type="Label" text="Leg Armor:" size="18">
        <position x="100" y="420" />
    </widget>
    <widget type="Button" text="Empty">
        <rect x="275" y="420" width="150" height="40" />
    </widget>
    

    <!-- 
    =================================================
    RIGHT PANEL: BACKPACK & ITEM DETAILS
    This panel shows the player's inventory grid and details for selected items.
    The grid itself would be dynamically generated by the engine.
    =================================================
    -->

    <widget type="Label" text="Backpack" size="24">
        <position x="500" y="120" />
    </widget>
    
    <!-- Placeholder for the main inventory grid.
         The engine would draw the item icons within these bounds. -->
    <widget type="Label" text="Grid Area Placeholder" size="14">
        <rect x="500" y="160" width="700" height="300" />
    </widget>

    <!-- Sorting and Filtering Buttons -->
    <widget type="Button" text="Filter: All" on_click="filter_all">
        <rect x="575" y="480" width="150" height="40" />
    </widget>
    <widget type="Button" text="Filter: Weapons" on_click="filter_weapons">
        <rect x="750" y="480" width="150" height="40" />
    </widget>
    <widget type="Button" text="Filter: Armor" on_click="filter_armor">
        <rect x="925" y="480" width="150" height="40" />
    </widget>
    <widget type="Button" text="Filter: Consumables" on_click="filter_consumables">
        <rect x="1100" y="480" width="150" height="40" />
    </widget>

    <!-- Item Details Section (for hovered/selected item) -->
    <widget type="Label" text="[Item Name]" size="28" id="item_name_label">
        <position x="500" y="550" />
    </widget>
    <widget type="Label" text="[Item description would appear here. It would be a longer, multi-line text block describing the item's lore and purpose.]" size="16" id="item_desc_label">
        <position x="500" y="590" />
    </widget>

    <widget type="Label" text="Weight: [0.0]" size="18" id="item_weight_label">
        <position x="1100" y="550" />
    </widget>

</screen>
```

### File: `/ui/layouts/initialization_screen.xml`
```xml
<!-- /ui/layouts/initialization_screen.xml -->
<screen id="initialization_screen">
    
    <widget type="Label" text="Stelliferrum Forge" size="48">
        <position x="center" y="250" />
    </widget>

    <widget type="Label" text="Initializing..." size="24" id="status_label">
        <position x="center" y="350" />
    </widget>
    
</screen>
```

### File: `/tools/cooker.py`
```py
# tools/cooker.py

import os
import shutil
import traceback

# This is a placeholder for the offline asset processor.
# A real "cooker" would perform complex operations like:
# - Converting PNGs to optimized, compressed texture formats (DDS).
# - Generating mipmaps for textures.
# - Parsing 3D model files (.gltf, .obj) into a simple, engine-native binary format.
# - Compressing audio files.
# - Generating a master "asset manifest" file.

SOURCE_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'raw')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'cooked')
# --- NEW: Define required subdirectories ---
REQUIRED_DIRS = ["shaders", "textures"]

def setup_directories():
    """Ensures the source and output directories and their subfolders exist."""
    print("--- Verifying Directory Structure ---")
    
    # Ensure source directory and its subdirectories exist
    if not os.path.exists(SOURCE_DIR):
        os.makedirs(SOURCE_DIR)
        print(f"Created source asset directory at '{SOURCE_DIR}'")
    for subdir in REQUIRED_DIRS:
        path = os.path.join(SOURCE_DIR, subdir)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created source subdirectory: '{path}'")
            
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created cooked assets directory at '{OUTPUT_DIR}'")
    
    print("Directory structure is OK.")


def cook_assets():
    """
    Finds all assets in the 'raw' directory, processes them, and saves
    the output to the 'cooked' directory.
    """
    print("\n--- Starting Asset Cooker ---")
    
    # Clean old cooked assets first
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
        print(f"Cleaned old cooked assets from '{OUTPUT_DIR}'")
    os.makedirs(OUTPUT_DIR)
    print(f"Recreated empty cooked assets directory at '{OUTPUT_DIR}'")
    
    asset_count = 0
    # In this simple example, we just copy files over.
    for root, _, files in os.walk(SOURCE_DIR):
        for filename in files:
            # Ignore hidden files like .gitkeep
            if filename.startswith('.'):
                continue

            source_path = os.path.join(root, filename)
            
            # Create the corresponding directory in the output
            relative_path = os.path.relpath(source_path, SOURCE_DIR)
            dest_path = os.path.join(OUTPUT_DIR, relative_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            
            print(f"Processing '{relative_path}'...")
            
            # --- TODO: Insert actual processing logic here ---
            # For now, we just copy.
            shutil.copy(source_path, dest_path)
            asset_count += 1
            
    print(f"\n--- Asset Cooking Complete: Processed {asset_count} assets. ---")

if __name__ == "__main__":
    setup_directories()
    cook_assets()
```

### File: `/tools/__init__.py`
```py

```

### File: `/systems/world_generator.py`
```py
# /systems/world_generator.py

import numpy as np; import noise
from game.block import AIR, GRASS, DIRT, STONE

class WorldGenerator:
    def __init__(self, seed: int):
        self.seed = seed; self.scale = 100.0; self.octaves = 6
        self.persistence = 0.5; self.lacunarity = 2.0
        # --- THE FIX: Increased the repeat value to remove tiling artifacts ---
        self.repeat = 10240 
        self.world_height = 128
        
    def get_params(self) -> dict:
        return {"Seed": self.seed, "Noise Scale": self.scale, "Octaves": self.octaves, "Persistence": self.persistence, "Lacunarity": self.lacunarity}
        
    def get_height(self, x: int, z: int) -> int:
        height = noise.pnoise2(
            x / self.scale, z / self.scale, 
            octaves=self.octaves, persistence=self.persistence, 
            lacunarity=self.lacunarity, repeatx=self.repeat, 
            repeaty=self.repeat, base=self.seed
        )
        return int((height + 1) / 2 * (self.world_height / 2) + (self.world_height / 3))

    def generate_chunk(self, chunk_x: int, chunk_z: int, chunk_size: int = 16) -> np.ndarray:
        """
        Generates a solid chunk of terrain from the surface down to y=0.
        """
        blocks = np.full((chunk_size, self.world_height, chunk_size), AIR, dtype=np.uint8)
        for x in range(chunk_size):
            for z in range(chunk_size):
                world_x = (chunk_x * chunk_size) + x
                world_z = (chunk_z * chunk_size) + z
                
                terrain_height = self.get_height(world_x, world_z)

                for y in range(terrain_height):
                    if y >= self.world_height: continue

                    if y == terrain_height - 1:
                        blocks[x, y, z] = GRASS
                    elif y >= terrain_height - 4:
                        blocks[x, y, z] = DIRT
                    else:
                        blocks[x, y, z] = STONE
                        
        return blocks
```

### File: `/systems/ui_manager.py`
```py
# /systems/ui_manager.py

import pygame
import xml.etree.ElementTree as ET
import traceback
from OpenGL.GL import glDisable, glEnable, GL_DEPTH_TEST, GL_BLEND, glBlendFunc, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_CULL_FACE
from ui.screen import UIScreen
from ui.widgets import Label, Button
from utils.vectors import Vector2
from utils.color import WHITE
from utils.logger import logger

class UIManager:
    def __init__(self, engine):
        self.engine = engine
        self.screens = {}
        self.active_screen = None
        self.color_map = {"WHITE": WHITE}

    def load_screen_from_xml(self, file_path: str, action_map: dict):
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            screen_id = root.attrib.get('id')
            if not screen_id:
                logger.error(f"XML layout '{file_path}' is missing screen 'id'.")
                return

            screen = UIScreen(screen_id)
            win_w, win_h = self.engine.platform.get_window_size()

            for widget_node in root.findall('widget'):
                widget_type = widget_node.attrib.get('type')
                widget_id = widget_node.attrib.get('id') 
                widget = None

                if widget_type == "Label":
                    text = widget_node.attrib.get('text', '')
                    size = int(widget_node.attrib.get('size', 24))
                    pos_node = widget_node.find('position')
                    if pos_node is not None:
                        text_w, _ = self.engine.renderer.get_text_dimensions(text=text, font_id=None, size=size)
                        x_str = pos_node.attrib.get('x', '0')
                        y_str = pos_node.attrib.get('y', '0')
                        x = (win_w / 2) - (text_w / 2) if x_str == 'center' else float(x_str)
                        y = float(y_str)
                        widget = Label(text, Vector2(x, y), size=size)
                    else:
                        rect_node = widget_node.find('rect')
                        if rect_node is not None:
                            x = float(rect_node.attrib.get('x', '0'))
                            y = float(rect_node.attrib.get('y', '0'))
                            widget = Label(text, Vector2(x,y), size=size)

                elif widget_type == "Button":
                    text = widget_node.attrib.get('text', '')
                    on_click_key = widget_node.attrib.get('on_click')
                    on_click_func = action_map.get(on_click_key)
                    rect_node = widget_node.find('rect')
                    if rect_node is not None:
                        x_str = rect_node.attrib.get('x', '0')
                        y_str = rect_node.attrib.get('y', '0')
                        w = float(rect_node.attrib.get('width', '100'))
                        h = float(rect_node.attrib.get('height', '50'))
                        x = (win_w / 2) if x_str == 'center' else float(x_str)
                        y = float(y_str)
                        rect = pygame.Rect(0, 0, w, h)
                        rect.center = (x, y)
                        widget = Button(rect, text, on_click=on_click_func)

                if widget:
                    screen.add_widget(widget, widget_id)

            self.register_screen(screen)
            logger.info(f"UI screen '{screen_id}' loaded from '{file_path}'.")
        except Exception as e:
            logger.critical(f"An unexpected error occurred loading '{file_path}': {e}")
            logger.critical(traceback.format_exc())

    def register_screen(self, screen):
        self.screens[screen.id] = screen

    def set_active_screen(self, screen_id: str):
        self.active_screen = self.screens.get(screen_id)

    def update(self, delta_time: float, input_handler):
        if self.active_screen:
            self.active_screen.update(delta_time, input_handler)

    def render(self, renderer):
        # --- THE FIX: This method is now the master of 2D rendering ---
        
        # Set all required OpenGL states for 2D rendering.
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_CULL_FACE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Render the active UI screen, if there is one.
        if self.active_screen:
            self.active_screen.render(renderer)
        
        # Now, check if we are in the game and render the debug overlay.
        active_state = self.engine.state_manager.get_active_state()
        in_game_state_ref = self.engine.state_manager.get_state("IN_GAME")
        if active_state and isinstance(active_state, in_game_state_ref.__class__):
            if active_state.debug_overlay:
                active_state.debug_overlay.render(
                    renderer,
                    active_state.world,
                    active_state.player_entity,
                    self.engine.camera
                )

        # Restore states for the 3D renderer on the next frame.
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
```

### File: `/systems/skybox.py`
```py
# /systems/skybox.py

import pygame
import numpy as np
from OpenGL.GL import *
from OpenGL.GL import shaders
import pyrr
from utils.logger import logger
import ctypes

class Skybox:
    """Manages the rendering of a 3D procedural skybox."""

    def __init__(self, engine):
        self.engine = engine
        self.shader = None
        self.vao = 0
        self.view_matrix_loc = None
        self.proj_matrix_loc = None
        self.sun_y_loc = None
        self.time_loc = None

    def initialize(self):
        logger.info("Initializing Procedural Skybox...")
        try:
            vs_src = self._load_shader_source('assets/raw/shaders/skybox_vertex.glsl')
            fs_src = self._load_shader_source('assets/raw/shaders/skybox_fragment.glsl')
            self.shader = self._compile_shader(vs_src, fs_src)
            self.vao = self._create_skybox_cube()
            
            self.view_matrix_loc = glGetUniformLocation(self.shader, "view")
            self.proj_matrix_loc = glGetUniformLocation(self.shader, "projection")
            self.sun_y_loc = glGetUniformLocation(self.shader, "sun_y_pos")
            self.time_loc = glGetUniformLocation(self.shader, "time")
            
            logger.info("Procedural Skybox initialized.")
        except Exception as e:
            logger.error(f"Skybox failed to initialize: {e}")
            if self.shader: glDeleteProgram(self.shader)
            if self.vao: glDeleteVertexArrays(1, [self.vao])
            self.shader, self.vao = None, 0

    def render(self, sun_y_position: float, projection_matrix, view_matrix, time: float):
        """Renders the skybox."""
        if not self.shader or not self.vao: return

        glDepthFunc(GL_LEQUAL)
        
        glUseProgram(self.shader)
        
        # --- THE DEFINITIVE FIX for the crash ---
        # The view_matrix is a NumPy array. To get the rotational part (a 3x3 matrix),
        # we use NumPy slicing instead of a non-existent method.
        view_no_translation = pyrr.matrix44.create_from_matrix33(view_matrix[0:3, 0:3], dtype=np.float32)

        glUniformMatrix4fv(self.view_matrix_loc, 1, GL_FALSE, view_no_translation)
        glUniformMatrix4fv(self.proj_matrix_loc, 1, GL_FALSE, projection_matrix)
        glUniform1f(self.sun_y_loc, sun_y_position)
        glUniform1f(self.time_loc, time)

        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, 36)
        glBindVertexArray(0)
        
        glDepthFunc(GL_LESS)

    def shutdown(self):
        if self.shader:
            glDeleteProgram(self.shader)
        if self.vao:
            glDeleteVertexArrays(1, [self.vao])
        logger.info("Skybox shut down.")

    def _load_shader_source(self, path):
        with open(path, 'r') as f:
            return f.read()

    def _compile_shader(self, vertex_src, fragment_src):
        if not vertex_src or not fragment_src: return None
        try:
            return shaders.compileProgram(
                shaders.compileShader(vertex_src, GL_VERTEX_SHADER),
                shaders.compileShader(fragment_src, GL_FRAGMENT_SHADER)
            )
        except Exception as e:
            logger.error(f"Skybox shader compilation failed: {e}")
            return None

    def _create_skybox_cube(self):
        vertices = np.array([
            -1.0,  1.0, -1.0, -1.0, -1.0, -1.0,  1.0, -1.0, -1.0,
             1.0, -1.0, -1.0,  1.0,  1.0, -1.0, -1.0,  1.0, -1.0,
            -1.0, -1.0,  1.0, -1.0, -1.0, -1.0, -1.0,  1.0, -1.0,
            -1.0,  1.0, -1.0, -1.0,  1.0,  1.0, -1.0, -1.0,  1.0,
             1.0, -1.0, -1.0,  1.0, -1.0,  1.0,  1.0,  1.0,  1.0,
             1.0,  1.0,  1.0,  1.0,  1.0, -1.0,  1.0, -1.0, -1.0,
            -1.0, -1.0,  1.0, -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,
             1.0,  1.0,  1.0,  1.0, -1.0,  1.0, -1.0, -1.0,  1.0,
            -1.0,  1.0, -1.0,  1.0,  1.0, -1.0,  1.0,  1.0,  1.0,
             1.0,  1.0,  1.0, -1.0,  1.0,  1.0, -1.0,  1.0, -1.0,
            -1.0, -1.0, -1.0, -1.0, -1.0,  1.0,  1.0, -1.0, -1.0,
             1.0, -1.0, -1.0, -1.0, -1.0,  1.0,  1.0, -1.0,  1.0
        ], dtype=np.float32)

        vao = glGenVertexArrays(1)
        vbo = glGenBuffers(1)
        glBindVertexArray(vao)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(GLfloat), ctypes.c_void_p(0))
        
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)
        
        return vao
```

### File: `/systems/save_manager.py`
```py
# /systems/save_manager.py

import os
import json
import shutil
import datetime
from utils.logger import logger
import game.components as C

SAVE_DIRECTORY = "saves"

class SaveManager:
    """Handles all file operations for saving and loading game states."""

    def __init__(self, engine):
        self.engine = engine
        os.makedirs(SAVE_DIRECTORY, exist_ok=True)
        self.autosave_slot = 0

    def get_save_files(self):
        """Returns a sorted list of all manual save game metadata."""
        saves = []
        for filename in os.listdir(SAVE_DIRECTORY):
            if filename.startswith("save_") and filename.endswith(".json"):
                try:
                    with open(os.path.join(SAVE_DIRECTORY, filename), 'r') as f:
                        meta = json.load(f)
                        meta['filename'] = filename
                        saves.append(meta)
                except json.JSONDecodeError:
                    logger.warning(f"Could not read corrupt save file: {filename}")
        return sorted(saves, key=lambda s: s['timestamp'], reverse=True)

    def save_game(self, is_autosave=False):
        """Saves the current game state to a file."""
        in_game_state = self.engine.state_manager.get_state("IN_GAME")
        if not in_game_state or not in_game_state.world or not in_game_state.world.player_entity:
            logger.error("Save failed: Not currently in a savable game state.")
            return

        world = in_game_state.world
        player_transform = world.player_entity.get_component(C.TransformComponent)

        save_data = {
            "timestamp": datetime.datetime.now().isoformat(),
            "world_seed": world.world_generator.seed,
            "player": {
                "position": list(player_transform.position)
                # In the future, add health, inventory, etc. here
            }
            # In the future, add world modifications (built structures, etc.) here
        }

        if is_autosave:
            self.autosave_slot = (self.autosave_slot % 5) + 1
            filename = f"autosave_{self.autosave_slot}.json"
            logger.info(f"Autosaving to slot {self.autosave_slot}...")
        else:
            timestamp_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"save_{timestamp_str}.json"
            logger.info(f"Saving manual save: {filename}")
        
        filepath = os.path.join(SAVE_DIRECTORY, filename)
        with open(filepath, 'w') as f:
            json.dump(save_data, f, indexnt=4)

    def load_game(self, filename):
        """Loads game data from a file and configures the InGameState."""
        filepath = os.path.join(SAVE_DIRECTORY, filename)
        try:
            with open(filepath, 'r') as f:
                save_data = json.load(f)
            
            in_game_state = self.engine.state_manager.get_state("IN_GAME")
            in_game_state.set_load_data(save_data) # Pass data to the state
            self.engine.state_manager.set_state("IN_GAME")
            logger.info(f"Successfully loaded save file: {filename}")
            return True
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Failed to load save file {filename}: {e}")
            return False

    def delete_save(self, filename):
        """Deletes a save file."""
        filepath = os.path.join(SAVE_DIRECTORY, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            logger.info(f"Deleted save file: {filename}")
```

### File: `/systems/renderer.py`
```py
# /systems/renderer.py

import pygame
import numpy as np
import traceback
from OpenGL.GL import *
from OpenGL.GL import shaders
import pyrr
from utils.color import Color
from utils.logger import logger
from utils.vectors import Vector3, Vector2, Matrix44
import ctypes
import game.components as C

class Renderer:
    def __init__(self):
        self.engine = None
        self.clear_color = (0.1, 0.1, 0.15, 1.0)
        self.shaders = {}
        self.vaos = { "cube_lit": 0, "quad_2d": 0 }
        self.perspective_matrix: Matrix44 = None
        self.orthographic_matrix: Matrix44 = None
        self.font_cache, self.text_texture_cache, self.texture_cache = {}, {}, {}
        self.light_pos = Vector3([0.0, 100.0, 0.0])
        self.light_color = Vector3([1.0, 1.0, 1.0])
        self.ambient_strength = 0.3

    def initialize(self, engine_instance):
        self.engine = engine_instance
        logger.info(f"Initializing Renderer with OpenGL version: {glGetString(GL_VERSION).decode('utf-8')}")
        
        self.shaders["3d_lit_color"] = self._compile_shader_from_files('lit_color_vertex.glsl', 'lit_color_fragment.glsl')
        self.shaders["2d_unlit_textured"] = self._compile_shader_from_files('unlit_textured_vertex.glsl', 'unlit_textured_fragment.glsl')
        self.shaders["2d_unlit_color"] = self._compile_shader_from_files('ui_color_vertex.glsl', 'unlit_color_fragment.glsl')
        self.shaders["billboard"] = self._compile_shader_from_files('billboard_vertex.glsl', 'unlit_textured_fragment.glsl')
        
        self.vaos["cube_lit"] = self._create_cube_mesh_lit()
        self.vaos["quad_2d"] = self._create_quad_mesh_2d()
        
        w, h = self.engine.platform.get_window_size()
        self.perspective_matrix = pyrr.matrix44.create_perspective_projection(45.0, w / h, 0.1, 2000.0, dtype=np.float32)
        self.orthographic_matrix = pyrr.matrix44.create_orthogonal_projection(0, w, h, 0, -1, 1, dtype=np.float32)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glClearColor(*self.clear_color)
        logger.info("Renderer initialized with all shaders and primitives.")
        
    def render_lit_mesh(self, vao, vertex_count, model_matrix, camera, color=None, use_vertex_color=False):
        shader = self.shaders.get("3d_lit_color")
        if not shader or not vao or vertex_count == 0:
            return
        
        glUseProgram(shader)
        glUniformMatrix4fv(glGetUniformLocation(shader, "view"), 1, GL_FALSE, camera.get_view_matrix())
        glUniformMatrix4fv(glGetUniformLocation(shader, "projection"), 1, GL_FALSE, self.perspective_matrix)
        glUniform3fv(glGetUniformLocation(shader, "lightPos"), 1, self.light_pos)
        glUniform3fv(glGetUniformLocation(shader, "lightColor"), 1, self.light_color)
        glUniform3fv(glGetUniformLocation(shader, "viewPos"), 1, camera.position)
        glUniform1f(glGetUniformLocation(shader, "ambientStrength"), self.ambient_strength)
        glUniformMatrix4fv(glGetUniformLocation(shader, "model"), 1, GL_FALSE, model_matrix)
        
        if use_vertex_color:
            glUniform3f(glGetUniformLocation(shader, "objectColor"), -1.0, -1.0, -1.0)
        elif color:
            glUniform3f(glGetUniformLocation(shader, "objectColor"), color.r / 255.0, color.g / 255.0, color.b / 255.0)

        glBindVertexArray(vao)
        glDrawArrays(GL_TRIANGLES, 0, vertex_count)
        glBindVertexArray(0)

    def begin_frame(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
    def set_light_properties(self, position: Vector3, color: Vector3, ambient: float):
        self.light_pos, self.light_color, self.ambient_strength = position, color, ambient

    def render_scene(self, world, camera):
        if not world: return
        
        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1.0, 1.0)
        self._render_chunks_lit(world, camera)
        glDisable(GL_POLYGON_OFFSET_FILL)
        
        self._render_entities_lit(world, camera)

    def _render_chunks_lit(self, world, camera):
        for chunk in world.chunks.values():
            if chunk.vertex_count > 0 and chunk.vao:
                model_matrix = pyrr.matrix44.create_from_translation(chunk.world_position, dtype=np.float32)
                self.render_lit_mesh(chunk.vao, chunk.vertex_count, model_matrix, camera, use_vertex_color=True)

    def _render_entities_lit(self, world, camera):
        for eid, components in world.get_entities_with_components(C.TransformComponent, C.RenderComponent):
            transform_comp = components[C.TransformComponent]
            render_comp = components[C.RenderComponent]
            if not render_comp.is_visible: 
                continue
            self.render_lit_mesh(
                vao=self.vaos["cube_lit"],
                vertex_count=36,
                model_matrix=transform_comp.get_model_matrix(),
                camera=camera,
                color=render_comp.color
            )
            
    def draw_rect(self, rect: pygame.Rect, color: Color):
        shader = self.shaders.get("2d_unlit_color")
        if not shader: return
        glUseProgram(shader)
        trans_mat = pyrr.matrix44.create_from_translation([rect.left, rect.top, 0])
        scale_mat = pyrr.matrix44.create_from_scale([rect.width, rect.height, 1])
        model_matrix = scale_mat @ trans_mat
        glUniformMatrix4fv(glGetUniformLocation(shader, "model"), 1, GL_FALSE, model_matrix)
        glUniformMatrix4fv(glGetUniformLocation(shader, "projection"), 1, GL_FALSE, self.orthographic_matrix)
        glUniform4f(glGetUniformLocation(shader, "objectColor"), color.r/255.0, color.g/255.0, color.b/255.0, color.a/255.0)
        glBindVertexArray(self.vaos["quad_2d"])
        glDrawArrays(GL_TRIANGLES, 0, 6)
        glBindVertexArray(0)

    def draw_text(self, text: str, position: Vector2, font_id: str, size: int, color: Color):
        if not text: return
        shader = self.shaders.get("2d_unlit_textured")
        if not shader: return
        
        cache_key = (text, font_id, size, (color.r, color.g, color.b, color.a))
        texture_id, w, h = self.text_texture_cache.get(cache_key, (None, 0, 0))
        if not texture_id:
            try:
                font = self._get_font(font_id, size)
                text_surface = font.render(text, True, (color.r, color.g, color.b, color.a))
                texture_id, w, h = self._surface_to_texture(text_surface)
                if texture_id: self.text_texture_cache[cache_key] = (texture_id, w, h)
            except Exception as e:
                logger.error(f"Failed to render text '{text}': {e}")
                return
        if not texture_id: return

        glUseProgram(shader)
        trans_mat = pyrr.matrix44.create_from_translation([position.x, position.y, 0])
        scale_mat = pyrr.matrix44.create_from_scale([w, h, 1])
        model_matrix = scale_mat @ trans_mat
        glUniformMatrix4fv(glGetUniformLocation(shader, "model"), 1, GL_FALSE, model_matrix)
        glUniformMatrix4fv(glGetUniformLocation(shader, "projection"), 1, GL_FALSE, self.orthographic_matrix)
        glActiveTexture(GL_TEXTURE0); glBindTexture(GL_TEXTURE_2D, texture_id)
        glUniform1i(glGetUniformLocation(shader, "texture1"), 0)
        glBindVertexArray(self.vaos["quad_2d"]); glDrawArrays(GL_TRIANGLES, 0, 6); glBindTexture(GL_TEXTURE_2D, 0); glBindVertexArray(0)

    def get_text_dimensions(self, text: str, font_id: str, size: int):
        try:
            font = self._get_font(font_id, size)
            return font.size(text)
        except Exception:
            return (0, 0)

    def shutdown(self):
        logger.info("Renderer shutting down.")
        if self.shaders:
            for shader in self.shaders.values():
                if shader: glDeleteProgram(shader)
        if self.vaos:
            for vao in self.vaos.values():
                if vao: glDeleteVertexArrays(1, [vao])
        
        all_texture_ids = list(self.texture_cache.values()) + [tex[0] for tex in self.text_texture_cache.values() if tex[0] is not None]
        if all_texture_ids:
            glDeleteTextures([tex_id for tex_id in all_texture_ids if tex_id > 0])

        self.texture_cache.clear(); self.text_texture_cache.clear(); self.font_cache.clear()
        logger.info("Renderer resources released.")

    def _compile_shader_from_files(self, vs_filename, fs_filename):
        vs_path, fs_path = f'assets/raw/shaders/{vs_filename}', f'assets/raw/shaders/{fs_filename}'
        try:
            with open(vs_path,'r') as f: vs_src = f.read()
            with open(fs_path,'r') as f: fs_src = f.read()
            return shaders.compileProgram(shaders.compileShader(vs_src, GL_VERTEX_SHADER), shaders.compileShader(fs_src, GL_FRAGMENT_SHADER))
        except Exception:
            logger.error(f"Shader compilation failed for {vs_filename}/{fs_filename}:\n{traceback.format_exc()}")
            return None
            
    def _get_font(self, font_id, size):
        key = (font_id, size)
        if key not in self.font_cache:
            try: self.font_cache[key] = pygame.font.Font(font_id, size)
            except (FileNotFoundError, pygame.error): self.font_cache[key] = pygame.font.Font(None, size)
        return self.font_cache[key]

    def _surface_to_texture(self, surf):
        try:
            texture_data = pygame.image.tostring(surf, "RGBA", False)
            width, height = surf.get_size()
            
            texture_id = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
            glGenerateMipmap(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, 0)
            return texture_id, width, height
        except Exception as e:
            logger.error(f"Could not convert surface to GL texture: {e}")
            return None, 0, 0
    
    def _create_quad_mesh_2d(self):
        v = np.array([
            0.0, 1.0, 0.0, 0.0, 1.0,
            0.0, 0.0, 0.0, 0.0, 0.0,
            1.0, 0.0, 0.0, 1.0, 0.0,
            1.0, 0.0, 0.0, 1.0, 0.0,
            1.0, 1.0, 0.0, 1.0, 1.0,
            0.0, 1.0, 0.0, 0.0, 1.0
        ], dtype=np.float32)

        vao, vbo = glGenVertexArrays(1), glGenBuffers(1)
        glBindVertexArray(vao); glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, v.nbytes, v, GL_STATIC_DRAW)
        stride = 20
        glEnableVertexAttribArray(0); glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1); glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(12))
        glBindVertexArray(0); return vao

    def _create_cube_mesh_lit(self):
        # --- START OF DEFINITIVE FIX: Correct Cube Vertex Winding and Normals ---
        vertices = np.array([
            # Position           # Color (placeholder) # Normal
            # Back face (-z)
            -0.5, -0.5, -0.5,  1.0, 1.0, 1.0,  0.0,  0.0, -1.0,
             0.5, -0.5, -0.5,  1.0, 1.0, 1.0,  0.0,  0.0, -1.0,
             0.5,  0.5, -0.5,  1.0, 1.0, 1.0,  0.0,  0.0, -1.0,
             0.5,  0.5, -0.5,  1.0, 1.0, 1.0,  0.0,  0.0, -1.0,
            -0.5,  0.5, -0.5,  1.0, 1.0, 1.0,  0.0,  0.0, -1.0,
            -0.5, -0.5, -0.5,  1.0, 1.0, 1.0,  0.0,  0.0, -1.0,
            # Front face (+z)
            -0.5, -0.5,  0.5,  1.0, 1.0, 1.0,  0.0,  0.0,  1.0,
             0.5,  0.5,  0.5,  1.0, 1.0, 1.0,  0.0,  0.0,  1.0,
             0.5, -0.5,  0.5,  1.0, 1.0, 1.0,  0.0,  0.0,  1.0,
             0.5,  0.5,  0.5,  1.0, 1.0, 1.0,  0.0,  0.0,  1.0,
            -0.5, -0.5,  0.5,  1.0, 1.0, 1.0,  0.0,  0.0,  1.0,
            -0.5,  0.5,  0.5,  1.0, 1.0, 1.0,  0.0,  0.0,  1.0,
            # Left face (-x)
            -0.5,  0.5,  0.5,  1.0, 1.0, 1.0, -1.0,  0.0,  0.0,
            -0.5, -0.5, -0.5,  1.0, 1.0, 1.0, -1.0,  0.0,  0.0,
            -0.5,  0.5, -0.5,  1.0, 1.0, 1.0, -1.0,  0.0,  0.0,
            -0.5, -0.5, -0.5,  1.0, 1.0, 1.0, -1.0,  0.0,  0.0,
            -0.5,  0.5,  0.5,  1.0, 1.0, 1.0, -1.0,  0.0,  0.0,
            -0.5, -0.5,  0.5,  1.0, 1.0, 1.0, -1.0,  0.0,  0.0,
            # Right face (+x)
             0.5,  0.5,  0.5,  1.0, 1.0, 1.0,  1.0,  0.0,  0.0,
             0.5,  0.5, -0.5,  1.0, 1.0, 1.0,  1.0,  0.0,  0.0,
             0.5, -0.5, -0.5,  1.0, 1.0, 1.0,  1.0,  0.0,  0.0,
             0.5, -0.5, -0.5,  1.0, 1.0, 1.0,  1.0,  0.0,  0.0,
             0.5, -0.5,  0.5,  1.0, 1.0, 1.0,  1.0,  0.0,  0.0,
             0.5,  0.5,  0.5,  1.0, 1.0, 1.0,  1.0,  0.0,  0.0,
            # Bottom face (-y)
            -0.5, -0.5, -0.5,  1.0, 1.0, 1.0,  0.0, -1.0,  0.0,
             0.5, -0.5,  0.5,  1.0, 1.0, 1.0,  0.0, -1.0,  0.0,
             0.5, -0.5, -0.5,  1.0, 1.0, 1.0,  0.0, -1.0,  0.0,
             0.5, -0.5,  0.5,  1.0, 1.0, 1.0,  0.0, -1.0,  0.0,
            -0.5, -0.5, -0.5,  1.0, 1.0, 1.0,  0.0, -1.0,  0.0,
            -0.5, -0.5,  0.5,  1.0, 1.0, 1.0,  0.0, -1.0,  0.0,
            # Top face (+y)
            -0.5,  0.5, -0.5,  1.0, 1.0, 1.0,  0.0,  1.0,  0.0,
             0.5,  0.5, -0.5,  1.0, 1.0, 1.0,  0.0,  1.0,  0.0,
             0.5,  0.5,  0.5,  1.0, 1.0, 1.0,  0.0,  1.0,  0.0,
             0.5,  0.5,  0.5,  1.0, 1.0, 1.0,  0.0,  1.0,  0.0,
            -0.5,  0.5,  0.5,  1.0, 1.0, 1.0,  0.0,  1.0,  0.0,
            -0.5,  0.5, -0.5,  1.0, 1.0, 1.0,  0.0,  1.0,  0.0
        ], dtype=np.float32)
        # --- END OF FIX ---
        
        vao,vbo=glGenVertexArrays(1),glGenBuffers(1)
        glBindVertexArray(vao);glBindBuffer(GL_ARRAY_BUFFER,vbo)
        glBufferData(GL_ARRAY_BUFFER,vertices.nbytes,vertices,GL_STATIC_DRAW)
        stride = 9 * vertices.itemsize
        glEnableVertexAttribArray(0); glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,stride,ctypes.c_void_p(0))
        glEnableVertexAttribArray(1); glVertexAttribPointer(1,3,GL_FLOAT,GL_FALSE,stride,ctypes.c_void_p(12))
        glEnableVertexAttribArray(2); glVertexAttribPointer(2,3,GL_FLOAT,GL_FALSE,stride,ctypes.c_void_p(24))
        glBindVertexArray(0); return vao
```

### File: `/systems/player_control_system.py`
```py
# systems/player_control_system.py

import math
import pyrr
import pybullet
import game.components as C
from utils.logger import logger
import numpy as np

class PlayerControlSystem:
    def __init__(self, engine):
        self.engine = engine
        self._footstep_distance_tracker = 0.0
        self._was_on_ground = True
        self.is_noclip_active = False

    def _is_on_ground(self, physics_system, phys_comp, transform_comp) -> bool:
        if not phys_comp or phys_comp.body_id is None: return False
        ray_start = transform_comp.position
        ray_end = ray_start - pyrr.Vector3([0.0, 1.1, 0.0])
        hit = physics_system.raycast(ray_start, ray_end, exclude_body_id=phys_comp.body_id)
        return hit is not None
        
    def set_noclip_mode(self, is_active: bool):
        self.is_noclip_active = is_active
        in_game_state = self.engine.state_manager.get_active_state()
        if not in_game_state or not isinstance(in_game_state, self.engine.state_manager.get_state("IN_GAME").__class__):
             return
        
        player_phys_comp = in_game_state.player_entity.get_component(C.PhysicsComponent)
        if player_phys_comp and player_phys_comp.body_id is not None:
            body_id = player_phys_comp.body_id
            if is_active:
                pybullet.changeDynamics(body_id, -1, mass=0)
            else:
                pybullet.changeDynamics(body_id, -1, mass=player_phys_comp.mass)


    def update(self, delta_time: float):
        if self.engine.camera.mode == "debug":
            in_game_state = self.engine.state_manager.get_active_state()
            if in_game_state and in_game_state.player_entity:
                phys_comp = in_game_state.player_entity.get_component(C.PhysicsComponent)
                if phys_comp and phys_comp.body_id is not None:
                    pybullet.resetBaseVelocity(phys_comp.body_id, linearVelocity=[0,0,0], angularVelocity=[0,0,0])
            return

        in_game_state = self.engine.state_manager.get_active_state()
        if not isinstance(in_game_state, self.engine.state_manager.get_state("IN_GAME").__class__):
             return

        world = in_game_state.world
        physics_system = in_game_state.physics_system
        input_handler = self.engine.input_handler
        camera = self.engine.camera
        
        for eid, comps in world.get_entities_with_components(
            C.PlayerInputComponent, C.TransformComponent, C.PhysicsComponent
        ):
            input_comp, transform_comp, phys_comp = list(comps.values())
            
            if phys_comp.body_id is None: continue
            
            # --- START OF DEFINITIVE FIX ---
            # The previous method of resetting the body's state every frame was fighting
            # the physics simulation and preventing any forces (like movement or gravity) from
            # having an effect. This is the correct, force-based approach.
            
            forward_dir_cam = pyrr.Vector3([math.sin(math.radians(camera.yaw)), 0, -math.cos(math.radians(camera.yaw))]).normalized
            right_dir_cam = np.cross(forward_dir_cam, camera.up_vector).normalized
            
            wish_dir = pyrr.Vector3()
            
            try:
                current_lin_vel, _ = pybullet.getBaseVelocity(phys_comp.body_id)
                current_lin_vel = pyrr.Vector3(current_lin_vel)
            except pybullet.error: continue
            
            is_currently_on_ground = self._is_on_ground(physics_system, phys_comp, transform_comp)

            if is_currently_on_ground and not self._was_on_ground:
                fall_speed = abs(current_lin_vel.y)
                acoustic_mass = phys_comp.mass + (fall_speed * 10)
                self.engine.acoustic_system.add_phonon_event(source_position=transform_comp.position, acoustic_mass=acoustic_mass, event_type="landing_heavy")
            self._was_on_ground = is_currently_on_ground

            if input_handler.is_key_down('w'): wish_dir += forward_dir_cam
            if input_handler.is_key_down('s'): wish_dir -= forward_dir_cam
            if input_handler.is_key_down('a'): wish_dir -= right_dir_cam
            if input_handler.is_key_down('d'): wish_dir += right_dir_cam

            if wish_dir.length > 0.001:
                wish_dir.normalize()
                air_control_modifier = 0.3 
                force_multiplier = 1.0 if is_currently_on_ground else air_control_modifier
                
                # Check current speed on the horizontal plane
                player_speed_horizontal = np.linalg.norm(pyrr.Vector3([current_lin_vel.x, 0, current_lin_vel.z]))
                
                # Only apply force if we are below the maximum speed
                if player_speed_horizontal < input_comp.max_speed:
                     # applyExternalForce is designed to work over a physics step, so we don't multiply by delta_time
                     pybullet.applyExternalForce(phys_comp.body_id, -1, wish_dir * input_comp.move_force * force_multiplier, transform_comp.position, pybullet.WORLD_FRAME)
                
                if is_currently_on_ground and player_speed_horizontal > 1.0:
                     self._footstep_distance_tracker += player_speed_horizontal * delta_time
                     if self._footstep_distance_tracker >= 2.5:
                         self._footstep_distance_tracker = 0
                         acoustic_mass = 20 + (phys_comp.mass * (player_speed_horizontal / input_comp.max_speed))
                         self.engine.acoustic_system.add_phonon_event(source_position=transform_comp.position, acoustic_mass=acoustic_mass, event_type="footstep_light")
            
            # Apply jump impulse
            if input_handler.is_key_pressed('space') and is_currently_on_ground:
                 pybullet.applyExternalImpulse(phys_comp.body_id, -1, [0, phys_comp.mass * 8, 0], transform_comp.position, pybullet.WORLD_FRAME)

            # --- END OF FIX ---
```

### File: `/systems/physics.py`
```py
# /systems/physics.py

import pybullet
import pybullet_data
from utils.logger import logger
import game.components as C
import numpy as np

class PhysicsSystem:
    def __init__(self, world, gravity=(0, -9.81, 0)):
        self.world = world
        self.gravity = gravity
        self.body_to_entity_id = {}

        try:
            self.physics_client = pybullet.connect(pybullet.DIRECT)
            pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
            pybullet.setGravity(*self.gravity)
            logger.info("PhysicsSystem: PyBullet initialized successfully.")
        except pybullet.error as e:
            logger.critical(f"PhysicsSystem: CRITICAL - Failed to initialize PyBullet. Physics will not work. Error: {e}")
            self.physics_client = None

    def update(self, delta_time: float):
        if not self.physics_client: return
        pybullet.stepSimulation()
        
        for eid, comps in self.world.get_entities_with_components(C.TransformComponent, C.PhysicsComponent):
            transform, physics = comps[C.TransformComponent], comps[C.PhysicsComponent]
            if physics.body_id is not None and physics.mass > 0:
                try:
                    pos, orn = pybullet.getBasePositionAndOrientation(physics.body_id)
                    transform.position[:] = pos
                    transform.rotation[:] = orn
                except pybullet.error:
                    logger.warning(f"Failed to get position for physics body of entity {eid}.")
                    physics.body_id = None

    def shutdown(self):
        if self.physics_client:
            logger.info("PhysicsSystem: Shutting down PyBullet.")
            self.body_to_entity_id.clear()
            pybullet.disconnect()
            self.physics_client = None

    def create_body_for_entity(self, entity: 'Entity'):
        if not self.physics_client: return

        transform_comp = entity.get_component(C.TransformComponent)
        phys_comp = entity.get_component(C.PhysicsComponent)
        if not transform_comp or not phys_comp: return

        shape_type = phys_comp.shape_type.lower()
        dims = phys_comp.dimensions
        
        col_shape_id = -1
        if shape_type == "box":
            half_extents = [dims.get(k, 0.5) / 2 for k in ["width", "height", "depth"]]
            col_shape_id = pybullet.createCollisionShape(pybullet.GEOM_BOX, halfExtents=half_extents)
        elif shape_type == "capsule":
             col_shape_id = pybullet.createCollisionShape(pybullet.GEOM_CAPSULE, radius=dims.get("radius", 0.5), height=dims.get("height", 1.0))
        
        if col_shape_id == -1:
            logger.error(f"Failed to create collision shape for entity {entity.id} of type '{shape_type}'")
            return

        body_id = pybullet.createMultiBody(
            baseMass=phys_comp.mass,
            baseCollisionShapeIndex=col_shape_id,
            basePosition=transform_comp.position,
            baseOrientation=transform_comp.rotation
        )
        
        pybullet.changeDynamics(body_id, -1, spinningFriction=0.0, rollingFriction=0.0, linearDamping=0.0)
        
        phys_comp.body_id = body_id
        self.body_to_entity_id[body_id] = entity.id

    def remove_body_for_entity(self, phys_comp: C.PhysicsComponent):
        if self.physics_client and phys_comp.body_id is not None:
            try:
                pybullet.removeBody(phys_comp.body_id)
                if phys_comp.body_id in self.body_to_entity_id:
                    del self.body_to_entity_id[phys_comp.body_id]
            except pybullet.error:
                logger.warning(f"Attempted to remove a non-existent physics body: {phys_comp.body_id}")
            phys_comp.body_id = None
            
    # --- NEW METHOD to toggle collision for a given entity ---
    def toggle_entity_collision(self, entity: 'Entity') -> bool:
        """Toggles the collision state of a specific entity's physics body."""
        if not self.physics_client: return False
        
        phys_comp = entity.get_component(C.PhysicsComponent)
        if not phys_comp or phys_comp.body_id is None:
            logger.warning(f"Entity {entity.id} has no physics body to toggle.")
            return False
            
        # Flip the state
        phys_comp.collision_enabled = not phys_comp.collision_enabled
        
        body_id = phys_comp.body_id
        
        if phys_comp.collision_enabled:
            # Re-enable collision: set mask to 1 to collide with default group 1
            pybullet.setCollisionFilterGroupMask(body_id, -1, 1, 1, self.physics_client)
            logger.info(f"Enabled collision for entity {entity.id} (Body ID: {body_id}).")
        else:
            # Disable collision: set group and mask to 0 so it collides with nothing
            pybullet.setCollisionFilterGroupMask(body_id, -1, 0, 0, self.physics_client)
            logger.info(f"Disabled collision for entity {entity.id} (Body ID: {body_id}).")
        
        return True

    def create_chunk_body_from_heightfield(self, chunk):
        if not self.physics_client or not hasattr(chunk, 'blocks'): return

        heights = np.zeros(16 * 16, dtype=np.float32)
        for x in range(16):
            for z in range(16):
                for y in range(chunk.blocks.shape[1] - 1, -1, -1):
                    if chunk.blocks[x, y, z] != 0:
                        heights[z * 16 + x] = y + 0.5
                        break
        
        try:
            terrain_shape = pybullet.createCollisionShape(
                shapeType=pybullet.GEOM_HEIGHTFIELD,
                meshScale=[1.0, 1.0, 1.0],
                heightfieldData=heights,
                numHeightfieldRows=16,
                numHeightfieldColumns=16
            )
            chunk.physics_body_id = pybullet.createMultiBody(
                baseMass=0,
                baseCollisionShapeIndex=terrain_shape,
                basePosition=[chunk.world_position.x + 8, 0, chunk.world_position.z + 8]
            )
            self.body_to_entity_id[chunk.physics_body_id] = -1 
        except Exception as e:
            logger.error(f"Failed to create heightfield for chunk at {chunk.position}: {e}")

    def remove_chunk_body(self, chunk):
        if self.physics_client and chunk.physics_body_id is not None:
            try:
                pybullet.removeBody(chunk.physics_body_id)
                if chunk.physics_body_id in self.body_to_entity_id:
                    del self.body_to_entity_id[chunk.physics_body_id]
            except pybullet.error:
                logger.warning(f"Attempted to remove a non-existent chunk physics body: {chunk.physics_body_id}")
            chunk.physics_body_id = None
            
    def raycast(self, start_pos, end_pos, exclude_body_id=None):
        if not self.physics_client: return None
        try:
            results = pybullet.rayTest(start_pos, end_pos)
            for result in results:
                body_id, _, _, hit_pos, hit_normal = result
                if body_id != exclude_body_id and body_id != -1:
                    return {"hit_body_id": body_id, "hit_position": hit_pos, "hit_normal": hit_normal}
            return None
        except Exception as e:
            logger.error(f"Raycast failed: {e}")
            return None
    
    def get_linear_velocity(self, body_id):
        if not self.physics_client or body_id is None:
            return (0.0, 0.0, 0.0)
        try:
            lin_vel, _ = pybullet.getBaseVelocity(body_id)
            return lin_vel
        except pybullet.error:
            return (0.0, 0.0, 0.0)
```

### File: `/systems/item_manager.py`
```py
# /systems/item_manager.py

import json
from utils.logger import logger

class ItemManager:
    """
    Loads and manages all item definitions from data files.
    This acts as the central database for all items in the game.
    """
    def __init__(self):
        self.item_definitions = {}

    def initialize(self, file_path="game/data/items.json"):
        """Loads the item definition file."""
        logger.info("Initializing ItemManager...")
        try:
            with open(file_path, 'r') as f:
                self.item_definitions = json.load(f)
            logger.info(f"Loaded {len(self.item_definitions)} item definitions from '{file_path}'.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Failed to load item definitions from '{file_path}'. Error: {e}")
            return False
        return True

    def get_item_data(self, item_id: str) -> dict | None:
        """Returns the data for a given item_id."""
        return self.item_definitions.get(item_id)

    def get_item_name(self, item_id: str) -> str:
        """A convenience function to get an item's name."""
        item_data = self.get_item_data(item_id)
        return item_data.get("name", "Unknown Item") if item_data else "Unknown Item"
```

### File: `/systems/input_handler.py`
```py
# /systems/input_handler.py

import pygame
from utils.vectors import Vector2

class InputHandler:
    def __init__(self):
        self.key_states = pygame.key.get_pressed()
        self.mouse_states = list(pygame.mouse.get_pressed(5))
        self.mouse_wheel_scroll: int = 0
        self.quit_event_detected: bool = False
        
        self.prev_key_states = self.key_states
        self.prev_mouse_states = self.mouse_states[:]

        # --- THE FIX: A robust key map for all keys ---
        self._key_map = self._initialize_key_map()

    def _initialize_key_map(self):
        """Creates a mapping from simple strings to pygame key constants."""
        key_map = {
            # Alphanumeric
            **{chr(c): getattr(pygame, f"K_{chr(c)}") for c in range(ord('a'), ord('z') + 1)},
            **{str(i): getattr(pygame, f"K_{i}") for i in range(10)},
            # Special Keys
            "space": pygame.K_SPACE,
            "escape": pygame.K_ESCAPE,
            "enter": pygame.K_RETURN,
            "tab": pygame.K_TAB,
            "backspace": pygame.K_BACKSPACE,
            "left shift": pygame.K_LSHIFT,
            "right shift": pygame.K_RSHIFT,
            "left ctrl": pygame.K_LCTRL,
            "right ctrl": pygame.K_RCTRL,
            "left alt": pygame.K_LALT,
            "right alt": pygame.K_RALT,
            "up": pygame.K_UP,
            "down": pygame.K_DOWN,
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "print screen": pygame.K_PRINTSCREEN
        }
        # Add F1-F12 keys
        for i in range(1, 13):
            key_map[f"f{i}"] = getattr(pygame, f"K_F{i}")
        return key_map

    def process_events(self) -> None:
        self.prev_key_states = self.key_states
        self.prev_mouse_states = list(self.mouse_states)
        
        self.mouse_wheel_scroll = 0
        self.quit_event_detected = False

        self.key_states = pygame.key.get_pressed()
        self.mouse_states = pygame.mouse.get_pressed(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_event_detected = True
            elif event.type == pygame.MOUSEWHEEL:
                self.mouse_wheel_scroll = event.y

    def _get_pygame_key(self, key_name: str):
        return self._key_map.get(key_name.lower())

    def is_key_down(self, key_name: str) -> bool:
        pygame_key = self._get_pygame_key(key_name)
        return bool(pygame_key and self.key_states[pygame_key])

    def is_key_pressed(self, key_name: str) -> bool:
        pygame_key = self._get_pygame_key(key_name)
        return bool(pygame_key and self.key_states[pygame_key] and not self.prev_key_states[pygame_key])

    def is_mouse_button_down(self, button_indexx: int) -> bool:
        if 0 <= button_indexx < len(self.mouse_states):
            return bool(self.mouse_states[button_indexx])
        return False

    def is_mouse_button_pressed(self, button_indexx: int) -> bool:
        if 0 <= button_indexx < len(self.mouse_states):
            return bool(self.mouse_states[button_indexx] and not self.prev_mouse_states[button_indexx])
        return False

    def get_mouse_position(self) -> Vector2:
        pos = pygame.mouse.get_pos()
        return Vector2(pos[0], pos[1])

    def get_mouse_delta(self) -> tuple[int, int]:
        return pygame.mouse.get_rel()
        
    def get_mouse_wheel_scroll(self) -> int:
        return self.mouse_wheel_scroll
        
    def clear_pressed_state(self):
        self.prev_key_states = self.key_states
        self.prev_mouse_states = list(self.mouse_states)
            
    def consume_mouse_press(self, button_indexx: int):
        if 0 <= button_indexx < len(self.prev_mouse_states):
            self.prev_mouse_states[button_indexx] = True
```

### File: `/systems/debug_manager.py`
```py
# /systems/debug_manager.py

import socket
import threading
import json
import traceback
import pybullet
import pyrr
import game.components as C
from utils.logger import logger

TCP_COMMAND_PORT = 12347
UDP_RENDER_PORT = 12345
UDP_CONSOLE_PORT = 12346

class DebugManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DebugManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, engine, is_enabled=False):
        if hasattr(self, '_initialized') and self._initialized: return
        
        self.engine = engine
        self.is_enabled = is_enabled
        self.frame_count = 0
        self.render_frame_data = {}
        self.registered_commands = {}
        self.selected_entity_id = None
        
        self.is_god_mode_active = False

        if self.is_enabled:
            self.render_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.console_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.render_target = ("127.0.0.1", UDP_RENDER_PORT)
            self.console_target = ("127.0.0.1", UDP_CONSOLE_PORT)
            
            self.stop_tcp_server = threading.Event()
            self.tcp_thread = threading.Thread(target=self._start_tcp_server, daemon=True)
            self.tcp_thread.start()

        self._initialized = True
        self._register_core_commands()

    @property
    def _active_game_state(self):
        state = self.engine.state_manager.get_active_state()
        in_game_ref = self.engine.state_manager.get_state("IN_GAME")
        if state and isinstance(state, in_game_ref.__class__):
            return state
        return None

    def register_command(self, name: str, function, documentation=""):
        self.registered_commands[name] = (function, documentation)

    def _register_core_commands(self):
        self.register_command("help", self._show_help, "Shows this help message.")
        self.register_command("debug.toggle_overlay", self._cmd_toggle_overlay, "Toggles the in-game debug overlay.")
        self.register_command("debug.select", self._select_entity, "Selects an entity. Usage: debug.select <entity_id>")
        self.register_command("debug.toggle_camera", self._cmd_toggle_debug_camera, "Toggles free-fly debug camera.")
        self.register_command("debug.toggle_god_mode", self._cmd_toggle_god_mode, "Toggles player noclip and debug camera.")
        self.register_command("selected.kill", self._cmd_kill_selected, "Kills selected entity.")
        self.register_command("selected.teleport", self._cmd_teleport_selected, "Usage: selected.teleport <x> <y> <z>")
        self.register_command("selected.toggle_collision", self._cmd_toggle_selected_collision, "Toggles physics collision for the selected entity.")
        self.register_command("entity.set_component_trait", self._cmd_set_component_trait, "Sets a component trait. Usage: entity.set <eid> <CompName> <trait> <value>")
        self.register_command("world.set_time", self._cmd_set_time, "Sets time of day. Usage: world.set_time <0.0-1.0>")
        self.register_command("world.spawn", self._cmd_spawn_entity, "Spawns entity. Usage: world.spawn <enemy>")
        self.register_command("player.set_health", self._cmd_player_set_stat, "Usage: player.set_health <value>")
        self.register_command("physics.get_stats", self._cmd_get_physics_stats, "Returns physics simulation stats.")

    def _cmd_toggle_overlay(self):
        state = self._active_game_state
        if state and hasattr(state, 'debug_overlay'):
            state.debug_overlay.toggle()
            return f"Debug overlay toggled {'ON' if state.debug_overlay.is_visible else 'OFF'}."
        return "Error: Could not find in-game state or debug overlay."

    def _cmd_toggle_debug_camera(self):
        if not self.engine.camera:
            return "Error: Camera system not available."
        
        if self.engine.camera.mode == "debug":
            self.engine.camera.set_mode("third_person")
            if self._active_game_state and self._active_game_state.player_entity:
                self.engine.camera.set_target(self._active_game_state.player_entity)
            return "Debug Camera: DISABLED"
        else:
            self.engine.camera.set_mode("debug")
            return "Debug Camera: ENABLED"

    def _cmd_toggle_god_mode(self):
        state = self._active_game_state
        if not state or not hasattr(state, 'player_control_system'):
            return "Error: Cannot toggle god mode, not in a valid game state."
        
        self.is_god_mode_active = not self.is_god_mode_active
        
        state.player_control_system.set_noclip_mode(self.is_god_mode_active)
        
        if self.is_god_mode_active:
            if self.engine.camera.mode != "debug": self._cmd_toggle_debug_camera()
        else:
            if self.engine.camera.mode == "debug": self._cmd_toggle_debug_camera()
        
        status_message = f"God mode (noclip) {'ENABLED' if self.is_god_mode_active else 'DISABLED'}."
        self.log_console(status_message, "INFO")
        self.report_status()
        return status_message
    
    def _cmd_toggle_selected_collision(self):
        if self.selected_entity_id is None:
            return "Error: No entity selected."
        state = self._active_game_state
        if not state or not state.physics_system:
            return "Error: Physics system is not active."
        
        entity = state.world.entities.get(self.selected_entity_id)
        if not entity:
            return f"Error: Selected entity {self.selected_entity_id} not found in the world."

        if state.physics_system.toggle_entity_collision(entity):
            phys_comp = entity.get_component(C.PhysicsComponent)
            new_status = "ENABLED" if phys_comp.collision_enabled else "DISABLED"
            return f"Collision for entity {entity.id} ({entity.name}) set to: {new_status}."
        else:
            return f"Error: Could not toggle collision for entity {entity.id}."
            
    # --- START OF DEFINITIVE FIX ---
    def _cmd_set_component_trait(self, entity_id_str, component_name_str, trait_name_str, *new_value_parts):
        state = self._active_game_state
        if not state: return "Error: Not in-game."

        try:
            entity_id = int(entity_id_str)
            entity = state.world.entities.get(entity_id)
            if not entity: return f"Error: Entity ID '{entity_id}' not found."

            component_instance = next((comp for comp in state.world.components.values() if entity_id in comp and comp[entity_id].__class__.__name__ == component_name_str), None)
            if not component_instance: return f"Error: Component '{component_name_str}' not found on entity {entity_id}."
            
            component_instance = component_instance[entity_id]
            if not hasattr(component_instance, trait_name_str):
                return f"Error: Trait '{trait_name_str}' not found on '{component_name_str}'."

            new_value_str = " ".join(new_value_parts)
            original_value = getattr(component_instance, trait_name_str)
            
            # --- Special Case for Collision ---
            if isinstance(component_instance, C.PhysicsComponent) and trait_name_str == 'collision_enabled':
                desired_state = new_value_str.lower() in ['true', '1', 't']
                if desired_state != original_value:
                    return self._cmd_toggle_selected_collision() # Use the proper toggle function
                else:
                    return f"Collision for entity {entity.id} is already {original_value}."

            # --- Generic Trait Setting Logic ---
            try:
                if isinstance(original_value, bool):
                    parsed_value = new_value_str.lower() in ['true', '1', 't']
                elif isinstance(original_value, int):
                    parsed_value = int(new_value_str)
                elif isinstance(original_value, float):
                    parsed_value = float(new_value_str)
                elif isinstance(original_value, (pyrr.Vector3, pyrr.Quaternion)):
                    parts = [float(p.strip()) for p in new_value_str.split(',')]
                    parsed_value = type(original_value)(parts)
                else:
                    parsed_value = new_value_str

                setattr(component_instance, trait_name_str, parsed_value)
                return f"Set {entity.name}.{component_name_str}.{trait_name_str} to {parsed_value}"
            except (ValueError, TypeError) as e:
                return f"Error: Invalid value type. Could not convert '{new_value_str}'. Expected {type(original_value).__name__}."

        except Exception as e:
            return f"An unexpected error occurred: {traceback.format_exc()}"
    # --- END OF FIX ---

    def report_status(self):
        if not self.is_enabled: return
        status_payload = {'type': 'status_update', 'god_mode': self.is_god_mode_active}
        self._send(self.console_socket, self.console_target, status_payload)

    def _show_help(self):
        help_text = "--- Available Commands ---\n"
        for cmd, (func, doc) in sorted(self.registered_commands.items()):
            help_text += f"{cmd:<25}: {doc}\n"
        return help_text
        
    def _select_entity(self, entity_id_str):
        state = self._active_game_state
        if not state: return "Error: Must be in-game to select entities."
        try:
            entity_id = int(entity_id_str)
            if entity_id in state.world.entities:
                self.selected_entity_id = entity_id; return f"Selected entity: {entity_id}"
            else:
                self.selected_entity_id = None; return f"Error: Entity ID '{entity_id}' not found."
        except ValueError: return "Error: Invalid entity ID format."

    def _cmd_kill_selected(self):
        if self.selected_entity_id is None: return "Error: No entity selected."
        state = self._active_game_state
        if state and state.world.get_component(self.selected_entity_id, C.HealthComponent):
            state.world.get_component(self.selected_entity_id, C.HealthComponent).take_damage(99999)
            return f"Entity {self.selected_entity_id} received lethal damage."
        return "Error: Not in game or entity has no HealthComponent."

    def _cmd_teleport_selected(self, x_str, y_str, z_str):
        if self.selected_entity_id is None: return "Error: No entity selected."
        state = self._active_game_state
        if state and state.world.get_component(self.selected_entity_id, C.PhysicsComponent):
            phys_comp = state.world.get_component(self.selected_entity_id, C.PhysicsComponent)
            if phys_comp.body_id is not None:
                try:
                    pos = [float(x_str), float(y_str), float(z_str)]
                    pybullet.resetBasePositionAndOrientation(phys_comp.body_id, pos, phys_comp.owner.transform.rotation)
                    return f"Teleported entity {self.selected_entity_id} to {pos}."
                except (ValueError, pybullet.error) as e: return f"Error teleporting: {e}"
        return "Error: Not in game or entity has no physics body."
        
    def _cmd_set_time(self, time_str):
        state = self._active_game_state
        if state:
            try: state.time_of_day = max(0.0, min(1.0, float(time_str))); return f"Set time to {state.time_of_day:.2f}"
            except ValueError: return "Error: Invalid time value."
        return "Error: Not in game."
        
    def _cmd_spawn_entity(self, entity_type):
        state = self._active_game_state
        if state and state.player_entity and hasattr(state, 'entity_factory'):
            spawn_pos = state.player_entity.transform.position + pyrr.Vector3([2.0, 1.0, 2.0])
            try:
                if entity_type.lower() == 'enemy':
                    new_enemy = state.entity_factory.create_enemy(spawn_pos)
                    return f"Spawned 'enemy' (ID: {new_enemy.id}) near player."
                else: return f"Error: Unknown entity type '{entity_type}'."
            except Exception as e: return f"Error spawning entity: {e}"
        return "Error: Not in game or entity factory not ready."
        
    def _cmd_player_set_stat(self, value_str):
        state = self._active_game_state
        if state and state.player_entity:
            try:
                health = state.player_entity.get_component(C.HealthComponent)
                if health: health.current_health = float(value_str); return f"Set player health to {health.current_health}"
            except ValueError: return "Error: Invalid value."
        return "Error: Not in game."

    def _cmd_get_physics_stats(self):
        state = self._active_game_state
        if not (state and state.physics_system and state.world):
            return json.dumps({"error": "Physics system not active."})

        try:
            physics_system = state.physics_system
            world = state.world
            
            num_bodies = pybullet.getNumBodies(physics_system.physics_client)
            body_info_list = []
            for i in range(num_bodies):
                body_id = pybullet.getBodyUniqueId(i)
                entity_id = physics_system.body_to_entity_id.get(body_id)
                
                info_str = f"Body ID: {body_id}"
                if entity_id == -1:
                    info_str += " (Terrain Chunk)"
                elif entity_id is not None and entity_id in world.entities:
                    entity_name = world.entities[entity_id].name
                    info_str += f" (Entity: '{entity_name}' [{entity_id}])"
                else:
                    info_str += " (Unknown)"
                body_info_list.append(info_str)
            
            params = pybullet.getPhysicsEngineParameters(physics_system.physics_client)
            stats = {
                "pybullet_client_id": physics_system.physics_client,
                "gravity": [round(g, 2) for g in params.get("gravity", [0, 0, 0])],
                "time_step_s": round(params.get("fixedTimeStep", 0.0), 4),
                "total_bodies": num_bodies,
                "total_constraints": pybullet.getNumConstraints(physics_system.physics_client),
                "body_list": body_info_list
            }
            return json.dumps(stats, indexnt=2)
        except Exception as e:
            return json.dumps({"error": f"Failed to get physics stats: {e}"})
    
    def _process_command(self, command_string: str) -> str:
        parts = command_string.strip().split()
        if not parts: return "Error: Empty command."
        command_name, args = parts[0].lower(), parts[1:]
        if command_name in self.registered_commands:
            func, doc = self.registered_commands[command_name]
            num_params = func.__code__.co_argcount - 1
            is_var_args = func.__code__.co_flags & 0x04 # Check for *args
            if not is_var_args and len(args) != num_params:
                 return f"Error: '{command_name}' expects {num_params} args. Usage: {doc}"
            try: return func(*args) or "Success"
            except Exception as e: return f"Error executing '{command_name}': {traceback.format_exc()}"
        return f"Error: Command '{command_name}' not found."

    def _start_tcp_server(self, host="127.0.0.1", port=TCP_COMMAND_PORT):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.bind((host, port)); s.listen()
            logger.info(f"Debug command server listening on {host}:{port}")
            s.settimeout(1.0)
            while not self.stop_tcp_server.is_set():
                try:
                    conn, _ = s.accept()
                    with conn:
                        data = conn.recv(1024)
                        if data: conn.sendall(self._process_command(data.decode('utf-8')).encode('utf-8'))
                except socket.timeout:
                    continue
                except Exception: pass

    def begin_frame(self):
        if not self.is_enabled: return
        self.render_frame_data.clear()
        self.frame_count += 1

    def log_entity_status(self, entity_id, entity_type, is_in_frustum, extra_data=None):
        if self.is_enabled: self.render_frame_data[entity_id] = {'type': entity_type,'is_in_frustum': is_in_frustum, 'rendered': False, 'data': extra_data or {}}

    def log_render_call(self, entity_id):
        if self.is_enabled and entity_id in self.render_frame_data: self.render_frame_data[entity_id]['rendered'] = True

    def end_frame(self, fps, frame_time, terrain_coverage):
        if not self.is_enabled: return
        state = self._active_game_state
        if state and state.world:
            for eid, entity in state.world.entities.items():
                component_data = {}
                for c_type, component_map in state.world.components.items():
                    if eid in component_map:
                        comp = component_map[eid]; comp_name = comp.__class__.__name__
                        component_data[comp_name] = { k: (v.tolist() if isinstance(v, (pyrr.Vector3, pyrr.Quaternion)) else v)
                            for k, v in comp.__dict__.items() if not k.startswith('_') and k != 'owner'
                        }
                self.log_entity_status(entity.id, entity.name, True, extra_data=component_data)

        payload = {'frame': self.frame_count, 'fps': fps, 'frame_time': frame_time, 'terrain_coverage': terrain_coverage, 'entities': self.render_frame_data}
        self._send(self.render_socket, self.render_target, payload)

    def log_world_generation(self, params: dict):
        if self.is_enabled: self._send(self.console_socket, self.console_target, {'type': 'world_gen', 'params': params})

    def log_console(self, message: str, level: str = "INFO"):
        if self.is_enabled: self._send(self.console_socket, self.console_target, {'type': 'log', 'level': level, 'message': str(message)})
        
    def _send(self, sock, target, payload):
        try:
            message = json.dumps(payload, default=lambda o: '<not serializable>').encode('utf-8')
            if len(message) < 65000: sock.sendto(message, target)
        except (TypeError, Exception): pass

    def shutdown(self):
        if self.is_enabled:
            logger.info("Shutting down DebugManager...")
            self.stop_tcp_server.set()
```

### File: `/systems/cloud_system.py`
```py
# /systems/cloud_system.py

import pygame
import numpy as np
import traceback
from OpenGL.GL import *
from OpenGL.GL import shaders
import pyrr
from utils.vectors import Vector3
from utils.logger import logger
import ctypes

class CloudSystem:
    """
    Manages rendering of procedural volumetric clouds via raymarching in a shader.
    """
    def __init__(self, engine):
        self.engine = engine
        self.shader = None
        self.vao = 0
        self.light_direction = Vector3([0.8, 0.6, 0.5]).normalized
        self.is_initialized = False

    def initialize(self):
        logger.info("Initializing Volumetric Cloud System...")
        try:
            vs_src = self.engine.asset_manager.load_shader_source('assets/raw/shaders/volumetric_clouds_vertex.glsl')
            fs_src = self.engine.asset_manager.load_shader_source('assets/raw/shaders/volumetric_clouds_fragment.glsl')
            self.shader = shaders.compileProgram(
                shaders.compileShader(vs_src, GL_VERTEX_SHADER),
                shaders.compileShader(fs_src, GL_FRAGMENT_SHADER)
            )
            self.vao = self._create_fullscreen_quad()
            self.is_initialized = True
            logger.info("Volumetric Cloud System initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize Volumetric Cloud System: {e}")
            logger.error(traceback.format_exc())
            if self.shader: glDeleteProgram(self.shader)
            if self.vao: glDeleteVertexArrays(1, [self.vao])
            self.shader, self.vao = None, 0

    def update(self, delta_time: float):
        # The animation is now driven by the 'time' uniform in the shader.
        # This update method can be used for future weather logic.
        pass

    def set_light_direction(self, direction: Vector3):
        """Used by game states to sync the cloud lighting with the world's sun."""
        self.light_direction = direction.normalized

    def render(self, time: float):
        if not self.is_initialized or not self.shader:
            return

        glUseProgram(self.shader)
        
        # Set states for transparent, additive rendering on top of the skybox
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glDisable(GL_DEPTH_TEST) # Render clouds in screen space without depth check

        camera = self.engine.camera
        
        # Calculate inverse matrices needed to reconstruct world space pos from screen pos
        view_matrix = camera.get_view_matrix()
        proj_matrix = self.engine.renderer.perspective_matrix
        inverse_view = pyrr.matrix44.inverse(view_matrix)
        inverse_proj = pyrr.matrix44.inverse(proj_matrix)
        
        # Pass all uniforms to the shader
        glUniformMatrix4fv(glGetUniformLocation(self.shader, "inverseView"), 1, GL_FALSE, inverse_view)
        glUniformMatrix4fv(glGetUniformLocation(self.shader, "inverseProjection"), 1, GL_FALSE, inverse_proj)
        glUniform3fv(glGetUniformLocation(self.shader, "cameraPos"), 1, camera.position)
        glUniform3fv(glGetUniformLocation(self.shader, "lightDirection"), 1, self.light_direction)
        glUniform1f(glGetUniformLocation(self.shader, "time"), time)

        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, 6)
        glBindVertexArray(0)
        
        # Restore default render states
        glEnable(GL_DEPTH_TEST)

    def _create_fullscreen_quad(self):
        vertices = np.array([
            -1.0, -1.0, 0.0,
             1.0, -1.0, 0.0,
             1.0,  1.0, 0.0,
            -1.0, -1.0, 0.0,
             1.0,  1.0, 0.0,
            -1.0,  1.0, 0.0
        ], dtype=np.float32)

        vao = glGenVertexArrays(1)
        vbo = glGenBuffers(1)
        glBindVertexArray(vao)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glBindVertexArray(0)
        return vao
```

### File: `/systems/camera.py`
```py
# systems/camera.py

import numpy as np
import math
import pygame
import pyrr
from utils.vectors import Vector3
from utils.settings import GAME_SETTINGS
import game.components as C

class Camera:
    def __init__(self, engine):
        self.engine = engine
        self.target_entity = None
        self.up_vector = Vector3([0.0, 1.0, 0.0])
        
        self.mode = "third_person"
        self.target_offset = Vector3([0.0, 1.0, 0.0])

        self.ideal_distance = 8.0
        self.current_distance = 8.0
        self.min_distance = 2.0
        self.max_distance = 20.0

        self.position = Vector3([0.0, 0.0, 0.0])
        self.pitch = -20.0
        self.yaw = 0.0
        
        self.debug_movement_speed = 25.0

    def set_target(self, entity):
        self.target_entity = entity
        self.set_mode("third_person")
        
    def set_mode(self, new_mode: str):
        self.mode = new_mode
        self._update_player_visibility()

    def _update_player_visibility(self):
        """Helper to manage showing/hiding the player model based on camera mode/distance."""
        if self.target_entity:
            player_render_comp = self.target_entity.get_component(C.RenderComponent)
            if player_render_comp:
                if self.mode == "third_person" and self.current_distance > 1.0:
                    player_render_comp.is_visible = True
                else:
                    player_render_comp.is_visible = False


    def update(self, delta_time, input_handler, physics_system):
        if pygame.mouse.get_visible():
            return
            
        mouse_dx, mouse_dy = input_handler.get_mouse_delta()
        sensitivity = GAME_SETTINGS.get("mouse_sensitivity", 0.1)
        
        if self.mode != "debug" and self.target_entity:
            player_phys_comp = self.target_entity.get_component(C.PhysicsComponent)
            if player_phys_comp and player_phys_comp.body_id is not None:
                velocity = pyrr.Vector3(physics_system.get_linear_velocity(player_phys_comp.body_id))
                horizontal_speed = np.linalg.norm(pyrr.Vector3([velocity.x, 0.0, velocity.z]))
                if horizontal_speed > 0.5:
                    sensitivity *= 0.3

        self.yaw -= mouse_dx * sensitivity
        
        invert_y = GAME_SETTINGS.get("invert_y", False)
        self.pitch += mouse_dy * sensitivity * (-1 if invert_y else 1)
        self.pitch = max(-89.0, min(89.0, self.pitch))

        if self.mode == "debug":
            self.target_entity = None
            wish_dir = Vector3()
            fwd = self._get_forward_vector()
            right_vec = np.cross(fwd, self.up_vector)
            right = Vector3(right_vec).normalized

            if input_handler.is_key_down('w'): wish_dir += fwd
            if input_handler.is_key_down('s'): wish_dir -= fwd
            if input_handler.is_key_down('a'): wish_dir -= right
            if input_handler.is_key_down('d'): wish_dir += right
            if input_handler.is_key_down('space'): wish_dir += self.up_vector
            if input_handler.is_key_down('left ctrl'): wish_dir -= self.up_vector
            
            if wish_dir.length > 0.001:
                self.position += wish_dir.normalized * self.debug_movement_speed * delta_time
            
            return

        if not self.target_entity:
            return

        target_pos = self.target_entity.transform.position + self.target_offset
        
        if self.mode == "third_person":
            scroll = input_handler.get_mouse_wheel_scroll()
            self.ideal_distance = np.clip(self.ideal_distance - scroll, self.min_distance, self.max_distance)
            
            theta, phi = math.radians(self.yaw), math.radians(self.pitch)
            offset_x = self.ideal_distance * math.cos(phi) * math.cos(theta)
            offset_y = self.ideal_distance * math.sin(phi)
            offset_z = self.ideal_distance * math.cos(phi) * math.sin(theta)
            ideal_position = target_pos - Vector3([offset_x, -offset_y, offset_z])

            player_phys_comp = self.target_entity.get_component(C.PhysicsComponent)
            player_body_id = player_phys_comp.body_id if player_phys_comp else -1
            
            hit = physics_system.raycast(target_pos, ideal_position, player_body_id)
            if hit:
                # Move camera to hit position to prevent clipping through walls
                self.position = Vector3(hit["hit_position"]) + Vector3(hit["hit_normal"]) * 0.2
            else:
                self.position = ideal_position

            self.current_distance = np.linalg.norm(self.position - target_pos)
            self._update_player_visibility()

        else: # First person mode
            self.position = target_pos
            self.current_distance = 0.0
            self._update_player_visibility()
    
    def get_view_matrix(self):
        # --- FIX: Ensure target position calculation doesn't depend on a non-existent target ---
        if self.target_entity and self.mode != "debug":
            target_pos = self.target_entity.transform.position + self.target_offset
        else:
            target_pos = self.position + self._get_forward_vector()

        return pyrr.matrix44.create_look_at(self.position, target_pos, self.up_vector, dtype=np.float32)

    def _get_forward_vector(self) -> Vector3:
        fwd = Vector3()
        fwd.x = math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
        fwd.y = math.sin(math.radians(self.pitch))
        fwd.z = math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
        return fwd.normalized
```

### File: `/systems/audio_engine.py`
```py
# /systems/audio_engine.py

import pygame
import os
import numpy as np
import math
from utils.logger import logger
from utils.vectors import Vector3
from core.phonons import Phonon

class AudioEngine:
    """
    Manages the low-level playing of sounds using Pygame's mixer. It now calculates
    volume and stereo panning based on the listener's position and orientation.
    """
    def __init__(self):
        self.sound_cache = {}
        self._initialized = False
        self.engine = None
        
        # Separated sound libraries for compositional audio
        self.action_sounds = {
            "footstep_light": "assets/raw/sounds/actions/footstep_light.wav",
            "landing_heavy": "assets/raw/sounds/actions/landing_heavy.wav",
        }
        self.material_sounds = {
            "grass": "assets/raw/sounds/materials/impact_grass.wav",
            "stone": "assets/raw/sounds/materials/impact_stone.wav",
            "dirt": "assets/raw/sounds/materials/impact_dirt.wav",
        }
        
    def initialize(self, engine_instance):
        self.engine = engine_instance
        try:
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
            pygame.mixer.set_num_channels(32)
            self._initialized = True
            logger.info("AudioEngine: Initialized successfully.")
        except pygame.error as e:
            self._initialized = False
            logger.critical(f"AudioEngine CRITICAL: Failed to initialize. Error: {e}")

    def play_sound_from_event(self, phonon: Phonon, material_properties: dict, 
                              sound_pos: Vector3, distance_to_listener: float, is_occluded: bool):
        """
        Plays layered sounds based on the full physical context of a sound event.
        """
        if not self._initialized or not material_properties or not self.engine.camera:
            return

        camera = self.engine.camera

        # --- 1. Calculate base volume and panning ---
        base_volume = min(1.0, phonon.acoustic_mass / 100.0)
        max_dist = 50.0 # Generic max hearing distance
        
        if distance_to_listener > max_dist:
            return

        # Attenuation (Inverse square law is more realistic, but linear is simpler for now)
        distance_mod = 1.0 - (distance_to_listener / max_dist)
        occlusion_mod = 0.2 if is_occluded else 1.0 # Drastically reduce volume if muffled

        # Stereo Panning Calculation
        sound_dir = (sound_pos - camera.position).normalized
        right_vec = (camera.up_vector.cross(camera._get_forward_vector())).normalized
        dot_product = np.dot(sound_dir, right_vec) # -1 is left, 1 is right
        
        pan_l = (1.0 - dot_product) / 2.0
        pan_r = (1.0 + dot_product) / 2.0

        # --- 2. Play ACTION Sound ---
        action_key = "landing_heavy" if "landing" in phonon.event_type else "footstep_light"
        action_path = self.action_sounds.get(action_key)
        
        if action_path:
            action_sound_obj = self._get_sound(action_path)
            if action_sound_obj:
                action_volume = base_volume * distance_mod * occlusion_mod
                final_vol_l = action_volume * pan_l
                final_vol_r = action_volume * pan_r
                
                action_channel = pygame.mixer.find_channel(True)
                if action_channel:
                    action_channel.set_volume(final_vol_l, final_vol_r)
                    action_channel.play(action_sound_obj)

        # --- 3. Play MATERIAL Sound ---
        material_name = material_properties.get('name')
        material_path = self.material_sounds.get(material_name)
        
        if material_path:
            material_sound_obj = self._get_sound(material_path)
            if material_sound_obj:
                density_mod = material_properties.get('density', 0.5)
                dampening_mod = 1.0 - material_properties.get('dampening', 0.5)
                material_base_volume = base_volume * density_mod * dampening_mod

                material_volume = material_base_volume * distance_mod * occlusion_mod
                final_vol_l = material_volume * pan_l
                final_vol_r = material_volume * pan_r
                
                material_channel = pygame.mixer.find_channel(True)
                if material_channel:
                    material_channel.set_volume(final_vol_l, final_vol_r)
                    material_channel.play(material_sound_obj)

    def _get_sound(self, asset_path: str):
        if not os.path.exists(asset_path):
             logger.warning(f"AudioEngine: Sound file not found at '{asset_path}'")
             return None
        if asset_path in self.sound_cache:
            return self.sound_cache[asset_path]
        try:
            sound = pygame.mixer.Sound(asset_path)
            self.sound_cache[asset_path] = sound
            return sound
        except (pygame.error, FileNotFoundError) as e:
            logger.error(f"AudioEngine: Could not load sound '{asset_path}'. Error: {e}")
            self.sound_cache[asset_path] = None
            return None

    def play_music(self, asset_id: str, volume: float = 1.0, loop: bool = True):
        if not self._initialized: return
        try:
            pygame.mixer.music.load(asset_id)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1 if loop else 0)
        except (pygame.error, FileNotFoundError) as e:
            logger.error(f"AudioEngine: Could not load music '{asset_id}'. Error: {e}")

    def shutdown(self):
        if self._initialized:
            pygame.mixer.quit()
            logger.info("AudioEngine shutdown complete.")
```

### File: `/systems/asset_manager.py`
```py
# /systems/asset_manager.py

import pygame

class AssetManager:
    """
    Manages loading, unloading, and access to all game assets.
    """
    PLACEHOLDER_SURFACE = None

    def __init__(self):
        self.cache = {}
        self._create_placeholder_surface()

    def _create_placeholder_surface(self, size=(32, 32)):
        """Creates a bright pink square to signify a missing texture."""
        if AssetManager.PLACEHOLDER_SURFACE is None:
            print("AssetManager: Creating placeholder texture for missing assets.")
            surf = pygame.Surface(size)
            surf.fill((255, 0, 255))
            AssetManager.PLACEHOLDER_SURFACE = surf
        return AssetManager.PLACEHOLDER_SURFACE

    def load_texture(self, file_path: str):
        """
        Loads an image file into memory. If loading fails, returns a 
        placeholder surface instead of crashing.
        """
        if file_path in self.cache:
            return self.cache[file_path]
        try:
            texture = pygame.image.load(file_path).convert_alpha()
            self.cache[file_path] = texture
            print(f"AssetManager: Loaded texture '{file_path}'")
            return texture
        except (pygame.error, FileNotFoundError) as e:
            print(f"AssetManager: FAILED to load texture '{file_path}'. Using placeholder. Error: {e}")
            self.cache[file_path] = AssetManager.PLACEHOLDER_SURFACE
            return AssetManager.PLACEHOLDER_SURFACE
    
    def load_shader_source(self, file_path: str) -> str:
        """Loads the text content of a shader file."""
        if file_path in self.cache:
            return self.cache[file_path]
        try:
            with open(file_path, 'r') as f:
                source = f.read()
                self.cache[file_path] = source
                return source
        except FileNotFoundError as e:
            print(f"AssetManager: FAILED to load shader source '{file_path}'. Error: {e}")
            self.cache[file_path] = ""
            return ""

    def load_sound(self, file_path: str):
        """Loads a sound file from disk into memory."""
        # The Audio system will handle its own caching and errors for now.
        return file_path
```

### File: `/systems/acoustic_system.py`
```py
# /systems/acoustic_system.py

from collections import deque
from core.phonons import Phonon
from utils.logger import logger
from utils.vectors import Vector3
import math
import pyrr

class AcousticSystem:
    """
    Manages the simulation of sound propagation. It processes sound events (Phonons),
    determines how they interact with the world and the listener, and commands
    the AudioEngine to play the resulting sound.
    """
    def __init__(self, engine):
        self.engine = engine
        self.phonon_queue = deque()

    def initialize(self):
        """Initializes the acoustic system."""
        logger.info("AcousticSystem initialized.")

    def add_phonon_event(self, source_position: Vector3, acoustic_mass: float, event_type: str):
        """Adds a new sound event to be processed on the next update cycle."""
        if acoustic_mass > 0.1: # Threshold to avoid processing tiny sounds
            event = Phonon(source_position, acoustic_mass, event_type)
            self.phonon_queue.append(event)

    def update(self, delta_time: float, world: 'World', physics_system: 'PhysicsSystem', player_entity: 'Entity'):
        """
        Processes all queued Phonon events for the current frame.
        This version now calculates distance to the listener and checks for occlusion.
        """
        if not world or not player_entity:
            return

        listener_pos = player_entity.transform.position
        
        events_to_process = min(len(self.phonon_queue), 10)
        
        for _ in range(events_to_process):
            phonon = self.phonon_queue.popleft()
            
            # 1. Check distance to listener before doing more expensive checks
            distance_to_listener = np.linalg.norm(phonon.source_position - listener_pos)
            if distance_to_listener > 100.0: # Hard cutoff for performance
                continue
                
            # 2. Determine which chunk the sound originated in.
            chunk_x = math.floor(phonon.source_position.x / 16)
            chunk_z = math.floor(phonon.source_position.z / 16)
            chunk = world.chunks.get((chunk_x, chunk_z))
            if not chunk: continue
            
            # 3. Get the material at the sound's source.
            local_x = int(phonon.source_position.x % 16)
            local_y = int(max(0, phonon.source_position.y - 0.1))
            local_z = int(phonon.source_position.z % 16)
            
            material_properties = None
            for y_check in range(local_y, -1, -1):
                block_id = chunk.blocks[local_x, y_check, local_z]
                if block_id != 0:
                     props = world.block_types.get(block_id, {}).get('acoustic')
                     if props is not None:
                          material_properties = props
                          break
            
            if material_properties:
                # --- NEW: Check for Occlusion ---
                # Cast a ray from the sound source to the listener. If it hits something
                # that isn't the player, the sound is muffled.
                player_phys_comp = player_entity.get_component(C.PhysicsComponent)
                ray_hit = physics_system.raycast(phonon.source_position, listener_pos, exclude_body_id=player_phys_comp.body_id)
                is_occluded = ray_hit is not None

                # --- 4. Send the complete event to the low-level audio engine ---
                self.engine.audio_engine.play_sound_from_event(
                    phonon,
                    material_properties,
                    phonon.source_position,
                    distance_to_listener,
                    is_occluded
                )

    def shutdown(self):
        """Shuts down the acoustic system."""
        logger.info("AcousticSystem shutdown.")
```

### File: `/systems/__init__.py`
```py

```

### File: `/game/world.py`
```py
# /game/world.py

from collections import defaultdict
import game.components as C
from systems.world_generator import WorldGenerator
from game.chunk import Chunk
from game.block import BLOCK_TYPES
from game.entity import Entity
from utils.vectors import Vector3
from utils.logger import logger
import math
import pyrr

class World:
    """
    The central container for all game objects, terrain, and state for a
    single play session. It manages entities, components, and the procedural
    generation of the world itself.
    """
    def __init__(self, engine):
        self.engine = engine
        self._last_entity_id = 0
        
        # Core ECS storage
        self.entities = {}  # Stores entity instances by ID
        self.components = defaultdict(dict)  # Stores components by type, then entity ID
        
        self.player_entity = None
        self.world_generator = None
        self.block_types = BLOCK_TYPES
        
        # Chunk management
        self.chunks = {}
        self.view_distance = 8 # Render distance in chunks
        self._chunks_to_load = set()

    def initialize_world(self, seed: int):
        """Sets up the world generator and prepares for initial chunk loading."""
        logger.info(f"World initializing with seed: {seed}")
        self.world_generator = WorldGenerator(seed)
        # Send generation params to the debug tool if it's active
        if self.engine.debug_manager and self.engine.debug_manager.is_enabled:
            params = self.world_generator.get_params()
            self.engine.debug_manager.log_world_generation(params)

    def set_player_entity(self, player_entity: Entity):
        """Sets the world's reference to the player entity."""
        self.player_entity = player_entity

    def load_chunks_around(self, position: Vector3):
        """Populates the initial chunk list based on a central position."""
        center_x = math.floor(position.x / 16)
        center_z = math.floor(position.z / 16)
        logger.info(f"Loading initial chunks around ({center_x}, {center_z})...")
        for x in range(center_x - self.view_distance, center_x + self.view_distance + 1):
            for z in range(center_z - self.view_distance, center_z + self.view_distance + 1):
                self._load_chunk((x, z))
        logger.info(f"Initial load complete. {len(self.chunks)} chunks generated.")

    def update(self):
        """Called every frame to manage chunk loading/unloading dynamically."""
        if not self.world_generator or not self.player_entity:
            return
            
        player_pos = self.player_entity.transform.position
        center_x = math.floor(player_pos.x / 16)
        center_z = math.floor(player_pos.z / 16)

        # Unload distant chunks
        chunks_to_unload = [pos for pos, chunk in self.chunks.items() if
                            abs(pos[0] - center_x) > self.view_distance or
                            abs(pos[1] - center_z) > self.view_distance]
        for pos in chunks_to_unload:
            self._unload_chunk(pos)

        # Load new chunks in range
        for x in range(center_x - self.view_distance, center_x + self.view_distance + 1):
            for z in range(center_z - self.view_distance, center_z + self.view_distance + 1):
                if (x, z) not in self.chunks:
                    self._load_chunk((x, z))

    def _load_chunk(self, chunk_pos: tuple[int, int]):
        if chunk_pos in self.chunks:
            return

        blocks = self.world_generator.generate_chunk(chunk_pos[0], chunk_pos[1])
        chunk = Chunk(chunk_pos)
        chunk.blocks = blocks
        chunk.build_mesh(self.block_types)
        self.chunks[chunk_pos] = chunk
        
        # Notify the physics system to create the corresponding static body
        in_game_state = self.engine.state_manager.get_state("IN_GAME")
        if in_game_state and in_game_state.physics_system:
            in_game_state.physics_system.create_chunk_body_from_heightfield(chunk)

    def _unload_chunk(self, chunk_pos: tuple[int, int]):
        if chunk_pos in self.chunks:
            chunk = self.chunks.pop(chunk_pos)
            
            in_game_state = self.engine.state_manager.get_state("IN_GAME")
            if in_game_state and in_game_state.physics_system:
                in_game_state.physics_system.remove_chunk_body(chunk)
            
            chunk.destroy() # Release OpenGL resources

    # --- ECS Core Methods ---

    def create_entity(self, name="Entity") -> Entity:
        """Creates a new entity, assigns it a unique ID, and returns it."""
        self._last_entity_id += 1
        new_id = self._last_entity_id
        entity = Entity(new_id, name, self)
        self.entities[new_id] = entity
        return entity

    def remove_entity(self, entity_id: int):
        """Removes an entity and all its associated components from the world."""
        if entity_id in self.entities:
            # Inform physics system to remove any associated body first
            in_game_state = self.engine.state_manager.get_state("IN_GAME")
            physics_comp = self.get_component(entity_id, C.PhysicsComponent)
            if in_game_state and in_game_state.physics_system and physics_comp:
                 in_game_state.physics_system.remove_body_for_entity(physics_comp)
            
            del self.entities[entity_id]
            for component_map in self.components.values():
                component_map.pop(entity_id, None)
            logger.debug(f"Removed entity {entity_id} from world.")
            
    def add_component(self, entity_id: int, component_instance: C.BaseComponent):
        """Adds a component to an entity."""
        component_type = type(component_instance)
        self.components[component_type][entity_id] = component_instance
        if isinstance(component_instance, C.TransformComponent):
            self.entities[entity_id].transform = component_instance

    def get_component(self, entity_id: int, component_class):
        """Retrieves a specific component for a given entity."""
        return self.components.get(component_class, {}).get(entity_id)

    def get_entities_with_components(self, *component_classes):
        """
        A generator that yields entities and their requested components
        for any entity that possesses ALL of the specified component types.
        This is the core query method for all systems.
        """
        if not component_classes: return
        try:
            # Find all entity IDs that have the first component
            base_ids = set(self.components[component_classes[0]].keys())
            # Filter that set by intersecting it with the keys of the other components
            for c_class in component_classes[1:]:
                base_ids.intersection_update(self.components[c_class].keys())
        except KeyError:
            return
            
        # Yield the entity IDs and a component dict for systems to iterate over
        for eid in base_ids:
            yield eid, {c: self.components[c][eid] for c in component_classes}
```

### File: `/game/menu_world.py`
```py
# /game/menu_world.py

import numpy as np
import pickle
import os
from OpenGL.GL import *
import ctypes
from utils.logger import logger
from game.block import AIR, STONE, DIRT, GRASS, BLOCK_TYPES

class MenuWorld:
    """A lightweight container for the main menu's static 3D world."""
    def __init__(self, size=(64, 128, 64)):
        self.size = size
        self.blocks = np.zeros(size, dtype=np.uint8)
        self.vao = None
        self.vbo = None
        self.vertex_count = 0

    def build_mesh(self):
        logger.info("Building mesh for menu world...")
        vertices = []
        w, h, d = self.size

        for x, y, z in np.ndindexx((w, h, d)):
            block_id = self.blocks[x, y, z]
            if block_id == AIR: continue

            color_info = BLOCK_TYPES.get(block_id, {'color': (255, 0, 255, 255)})['color']
            r, g, b = color_info.r / 255.0, color_info.g / 255.0, color_info.b / 255.0
            
            if y == h - 1 or self.blocks[x, y + 1, z] == AIR:
                v = self._get_face_vertices(x,y,z,'top'); [vertices.extend((*vert, r,g,b, 0,1,0)) for vert in v]
            if y == 0 or self.blocks[x, y - 1, z] == AIR:
                v = self._get_face_vertices(x,y,z,'bottom'); [vertices.extend((*vert, r,g,b, 0,-1,0)) for vert in v]
            if x == w - 1 or self.blocks[x + 1, y, z] == AIR:
                v = self._get_face_vertices(x,y,z,'right'); [vertices.extend((*vert, r,g,b, 1,0,0)) for vert in v]
            if x == 0 or self.blocks[x - 1, y, z] == AIR:
                v = self._get_face_vertices(x,y,z,'left'); [vertices.extend((*vert, r,g,b, -1,0,0)) for vert in v]
            if z == d - 1 or self.blocks[x, y, z + 1] == AIR:
                v = self._get_face_vertices(x,y,z,'front'); [vertices.extend((*vert, r,g,b, 0,0,1)) for vert in v]
            if z == 0 or self.blocks[x, y, z - 1] == AIR:
                v = self._get_face_vertices(x,y,z,'back'); [vertices.extend((*vert, r,g,b, 0,0,-1)) for vert in v]

        if not vertices:
            self.vertex_count = 0
            return

        vertex_data = np.array(vertices, dtype=np.float32)
        
        if self.vao is None: self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        if self.vbo is None: self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)
        
        stride = 9 * 4
        glEnableVertexAttribArray(0); glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1); glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(12))
        glEnableVertexAttribArray(2); glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(24))
        glBindVertexArray(0)
        
        self.vertex_count = len(vertex_data) // 9
        logger.info(f"Menu world mesh built with {self.vertex_count} vertices.")

    def _get_face_vertices(self, x, y, z, face):
        v = [
            (x + 0.0, y + 0.0, z + 1.0), (x + 1.0, y + 0.0, z + 1.0),
            (x + 1.0, y + 0.0, z + 0.0), (x + 0.0, y + 0.0, z + 0.0),
            (x + 0.0, y + 1.0, z + 1.0), (x + 1.0, y + 1.0, z + 1.0),
            (x + 1.0, y + 1.0, z + 0.0), (x + 0.0, y + 1.0, z + 0.0),
        ]

        faces = {
            'top':    [v[4], v[5], v[6], v[4], v[6], v[7]],
            # --- THE FIX: Reversed the winding order for the bottom face ---
            'bottom': [v[0], v[1], v[2], v[0], v[2], v[3]],
            'right':  [v[1], v[2], v[6], v[1], v[6], v[5]],
            'left':   [v[3], v[0], v[4], v[3], v[4], v[7]],
            'front':  [v[0], v[1], v[5], v[0], v[5], v[4]],
            'back':   [v[2], v[3], v[7], v[2], v[7], v[6]],
        }
        return faces[face]

    def save(self, path):
        try:
            data_to_save = {'size': self.size, 'blocks': self.blocks}
            with open(path, 'wb') as f: pickle.dump(data_to_save, f)
            logger.info(f"Menu world saved to '{path}'.")
        except Exception as e:
            logger.error(f"Failed to save menu world: {e}")

    @staticmethod
    def load(path):
        if not os.path.exists(path): return None
        try:
            with open(path, 'rb') as f: data = pickle.load(f)
            world = MenuWorld(data['size'])
            world.blocks = data['blocks']
            world.build_mesh() # Re-generate GL objects after loading
            return world
        except Exception as e:
            logger.error(f"Failed to load menu world from '{path}': {e}")
            if os.path.exists(path): os.remove(path)
            return None

    def destroy(self):
        if self.vao: glDeleteVertexArrays(1, [self.vao])
        if self.vbo: glDeleteBuffers(1, [self.vbo])
```

### File: `/game/entity_factory.py`
```py
# /game/entity_factory.py
import pyrr
import pybullet
from utils.color import RED, Color
import game.components as C

class EntityFactory:
    """
    A factory class responsible for creating pre-defined entities ("prefabs")
    by assembling the correct set of components.
    """
    def __init__(self, world, physics_system):
        self.world = world
        self.physics = physics_system

    def create_player(self, position: pyrr.Vector3) -> 'Entity':
        """Assembles the player entity."""
        player = self.world.create_entity(name="Player")
        
        # Core components
        player.add_component(C.TransformComponent(owner=player, position=position))
        player.add_component(C.RenderComponent(owner=player, color=Color(200, 200, 255, 255), mesh_id="cube", is_visible=True))
        
        # Physics. Height is 1.8, capsule height should be slightly less to avoid catching on edges.
        phys_dims = {"radius": 0.4, "height": 1.0}
        phys_comp = C.PhysicsComponent(owner=player, mass=80.0, shape_type="capsule", dimensions=phys_dims, body_id=None)
        player.add_component(phys_comp)

        # Gameplay components
        player.add_component(C.HealthComponent(owner=player, max_health=100))
        player.add_component(C.PlayerInputComponent(owner=player)) # Speed values now live in the component
        player.add_component(C.InventoryComponent(owner=player, capacity=30))
        
        # After all components are added, create the physics body
        self.physics.create_body_for_entity(player)
        
        if phys_comp.body_id is not None:
            # Lock rotation so the capsule doesn't fall over
            pybullet.changeDynamics(phys_comp.body_id, -1, angularFactor=[0, 0, 0])
            # --- THE FIX: Add a small amount of linear damping ---
            # This prevents the character from sliding like they're on ice.
            pybullet.changeDynamics(phys_comp.body_id, -1, linearDamping=0.1)
        
        return player

    def create_enemy(self, position: pyrr.Vector3) -> 'Entity':
        """Assembles a generic enemy entity."""
        enemy = self.world.create_entity(name="Enemy")

        enemy.add_component(C.TransformComponent(owner=enemy, position=position))
        enemy.add_component(C.RenderComponent(owner=enemy, color=RED, mesh_id="cube"))
        
        phys_dims = {"width": 1.0, "height": 1.0, "depth": 1.0}
        phys_comp = C.PhysicsComponent(owner=enemy, mass=60.0, shape_type="box", dimensions=phys_dims, body_id=None)
        enemy.add_component(phys_comp)
        
        enemy.add_component(C.HealthComponent(owner=enemy, max_health=50))
        
        self.physics.create_body_for_entity(enemy)
        return enemy
```

### File: `/game/entity.py`
```py
# /game/entity.py
class Entity:
    """
    A simple container for a game object's ID, name, and component data.
    Acts as a handle to access data within the World's component dictionaries.
    """
    def __init__(self, entity_id, name, world):
        self.id = entity_id
        self.name = name
        self.world = world
        self.transform: 'TransformComponent' = None # Cache for the most accessed component

    def add_component(self, component_instance):
        self.world.add_component(self.id, component_instance)

    def get_component(self, component_class):
        return self.world.get_component(self.id, component_class)
```

### File: `/game/chunk.py`
```py
# /game/chunk.py

import numpy as np
from OpenGL.GL import *
import ctypes
from game.block import AIR
from utils.vectors import Vector3

class Chunk:
    def __init__(self, position):
        self.position = position
        self.world_position = Vector3([self.position[0] * 16, 0.0, self.position[1] * 16])
        self.blocks = np.zeros((16, 128, 16), dtype=np.uint8)
        self.vao, self.vbo, self.vertex_count = None, None, 0
        self.mesh_dirty = True
        self.physics_body_id = None

    def get_acoustic_properties_at(self, local_pos: Vector3) -> dict | None:
        """Returns the acoustic properties of the block at a given local coordinate."""
        try:
            x, y, z = int(local_pos.x), int(local_pos.y), int(local_pos.z)
            if 0 <= x < 16 and 0 <= y < 128 and 0 <= z < 16:
                block_id = self.blocks[x, y, z]
                if block_id != AIR:
                    return self.engine.world.block_types.get(block_id, {}).get('acoustic')
        except (IndexError, AttributeError):
            pass # Voxel may be out of bounds or world not fully loaded
        return None


    def build_mesh(self, block_types):
        if not self.mesh_dirty: return
        
        vertices = []
        
        for x, y, z in np.ndindexx(self.blocks.shape):
            block_id = self.blocks[x, y, z]
            if block_id == AIR: continue
            
            color_data = block_types.get(block_id, {'color': (255,0,255,255)})['color']
            r, g, b = color_data.r/255.0, color_data.g/255.0, color_data.b/255.0

            # Check neighbors to determine which faces are visible
            if y == self.blocks.shape[1] - 1 or self.blocks[x, y + 1, z] == AIR:
                v = self.get_face_vertices(x, y, z, 'top'); [vertices.extend((*vert, r, g, b, 0, 1, 0)) for vert in v]
            if y == 0 or self.blocks[x, y - 1, z] == AIR:
                v = self.get_face_vertices(x, y, z, 'bottom'); [vertices.extend((*vert, r, g, b, 0, -1, 0)) for vert in v]
            if x == 15 or self.blocks[x + 1, y, z] == AIR:
                v = self.get_face_vertices(x, y, z, 'right'); [vertices.extend((*vert, r, g, b, 1, 0, 0)) for vert in v]
            if x == 0 or self.blocks[x - 1, y, z] == AIR:
                v = self.get_face_vertices(x, y, z, 'left'); [vertices.extend((*vert, r, g, b, -1, 0, 0)) for vert in v]
            if z == 15 or self.blocks[x, y, z + 1] == AIR:
                v = self.get_face_vertices(x, y, z, 'front'); [vertices.extend((*vert, r, g, b, 0, 0, 1)) for vert in v]
            if z == 0 or self.blocks[x, y, z - 1] == AIR:
                v = self.get_face_vertices(x, y, z, 'back'); [vertices.extend((*vert, r, g, b, 0, 0, -1)) for vert in v]

        if not vertices:
            self.vertex_count = 0
            self.mesh_dirty = False
            return

        vertex_data = np.array(vertices, dtype=np.float32)
        
        if self.vao is None: self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        if self.vbo is None: self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)
        
        stride = 9 * 4
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(24))
        glEnableVertexAttribArray(2)
        
        self.vertex_count = len(vertex_data) // 9
        self.mesh_dirty = False

    def get_face_vertices(self, x, y, z, face):
        # Defines the 8 corners of the cube
        v = [
            (x + 0.0, y + 0.0, z + 1.0), (x + 1.0, y + 0.0, z + 1.0),
            (x + 1.0, y + 0.0, z + 0.0), (x + 0.0, y + 0.0, z + 0.0),
            (x + 0.0, y + 1.0, z + 1.0), (x + 1.0, y + 1.0, z + 1.0),
            (x + 1.0, y + 1.0, z + 0.0), (x + 0.0, y + 1.0, z + 0.0),
        ]
        
        faces = {
            'top':    [v[4], v[5], v[6], v[4], v[6], v[7]],
            # --- THE FIX: Reversed the winding order for the bottom face ---
            'bottom': [v[0], v[1], v[2], v[0], v[2], v[3]],
            'right':  [v[1], v[2], v[6], v[1], v[6], v[5]],
            'left':   [v[3], v[0], v[4], v[3], v[4], v[7]],
            'front':  [v[0], v[1], v[5], v[0], v[5], v[4]],
            'back':   [v[2], v[3], v[7], v[2], v[7], v[6]],
        }
        return faces[face]

    def destroy(self):
        if self.vao: glDeleteVertexArrays(1, [self.vao])
        if self.vbo: glDeleteBuffers(1, [self.vbo])
```

### File: `/game/block.py`
```py
# /game/block.py
from utils.color import Color

# Block IDs
AIR = 0
GRASS = 1
DIRT = 2
STONE = 3

# Block properties mapping, now including acoustic material names for lookups.
# - name: Used by the AudioEngine to find the correct impact sound file.
# - density: Affects the pitch and volume. Higher density = lower pitch, higher volume.
# - dampening: Affects how long the sound resonates. Higher dampening = shorter sound.
BLOCK_TYPES = {
    GRASS: {
        'color': Color(30, 180, 40, 255),
        'acoustic': {'name': 'grass', 'density': 0.4, 'dampening': 0.8}
    },
    DIRT: {
        'color': Color(139, 69, 19, 255),
        'acoustic': {'name': 'dirt', 'density': 0.6, 'dampening': 0.6}
    },
    STONE: {
        'color': Color(100, 100, 100, 255),
        'acoustic': {'name': 'stone', 'density': 0.9, 'dampening': 0.1}
    },
}
```

### File: `/game/__init__.py`
```py
# game/__init__.py
# This file makes Python treat the 'game' directory as a package.
```

### File: `/game/states/pause_state.py`
```py
# /game/states/pause_state.py

from .base_state import BaseState
from utils.logger import logger
from utils.color import Color
import pygame

class PauseState(BaseState):
    def __init__(self, engine):
        super().__init__(engine)
        action_map = {
            "resume_game": self.resume_game,
            "save_game": self.save_game,
            "load_game": self.load_game,
            "quit_to_menu": self.quit_to_menu
        }
        self.engine.ui_manager.load_screen_from_xml("ui/layouts/pause_menu.xml", action_map)
        self.overlay_color = Color(0, 0, 0, 150) # Semi-transparent black

    def resume_game(self):
        logger.info("Resuming game.")
        self.engine.state_manager.pop_state()

    def save_game(self):
        logger.info("Save Game button clicked.")
        self.engine.save_manager.save_game(is_autosave=False)

    def load_game(self):
        logger.info("Load Game button clicked.")
        self.engine.state_manager.push_state("LOAD_GAME")

    def quit_to_menu(self):
        logger.info("Quitting to main menu.")
        self.engine.state_manager.set_state('MAIN_MENU')

    def enter(self):
        logger.info("Entering PauseState.")
        self.engine.ui_manager.set_active_screen("pause_menu")
        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)
        self.engine.input_handler.clear_pressed_state()

    def exit(self):
        logger.info("Exiting PauseState.")
        # --- THE FIX for the lingering menu ---
        # Deactivate the pause menu's UI when this state exits.
        self.engine.ui_manager.set_active_screen(None)
        
    def resume(self):
        # This state is never resumed in a way that requires special logic,
        # but the method must exist to be compatible with the StateManager.
        pass

    def update(self, delta_time: float):
        if self.engine.input_handler.is_key_pressed('escape'):
            self.resume_game()

    def render(self, renderer):
        # --- THE FIX for screen dimming ---
        # The StateManager already renders the InGameState below this one.
        # All this state needs to do is draw the dimming overlay on top.
        win_size = self.engine.platform.get_window_size()
        overlay_rect = pygame.Rect(0, 0, win_size.x, win_size.y)
        renderer.draw_rect(overlay_rect, self.overlay_color)
```

### File: `/game/states/options_state.py`
```py
# /game/states/options_state.py

from .base_state import BaseState
from utils.logger import logger
from utils.settings import GAME_SETTINGS

class OptionsState(BaseState):
    def __init__(self, engine):
        super().__init__(engine)
        self.ui_loaded = False

    def _update_button_text(self):
        screen = self.engine.ui_manager.screens.get("options_menu")
        if not screen: return
        # A more robust way to find the button
        for widget in screen.widgets:
             if hasattr(widget, 'on_click') and widget.on_click.__name__ == 'toggle_invert_y':
                 status = "ON" if GAME_SETTINGS["invert_y"] else "OFF"
                 widget.text = f"Invert Y: {status}"
                 break

    def toggle_invert_y(self):
        GAME_SETTINGS["invert_y"] = not GAME_SETTINGS["invert_y"]
        logger.info(f"Setting Invert Y-Axis to: {GAME_SETTINGS['invert_y']}")
        self._update_button_text()

    def back_to_previous_state(self):
        self.engine.state_manager.pop_state()

    def enter(self):
        logger.info("Entering OptionsState.")
        if not self.ui_loaded:
            action_map = {
                "back_to_main": self.back_to_previous_state,
                "toggle_invert_y": self.toggle_invert_y
            }
            self.engine.ui_manager.load_screen_from_xml("ui/layouts/options_menu.xml", action_map)
            self.ui_loaded = True
            
        self.engine.ui_manager.set_active_screen("options_menu")
        self._update_button_text()
        
    def exit(self):
        logger.info("Exiting OptionsState.")
        self.engine.ui_manager.set_active_screen(None)

    def update(self, delta_time: float):
        if self.engine.input_handler.is_key_pressed('escape'):
            self.back_to_previous_state()

    def render(self, renderer):
        pass
```

### File: `/game/states/new_game_state.py`
```py
# /game/states/new_game_state.py

from .base_state import BaseState
from utils.logger import logger
import random

class NewGameState(BaseState):
    def __init__(self, engine):
        super().__init__(engine)
        self.seeds = [12345, 54321, 98765, random.randint(10000, 99999)]
        self.seed_indexx = 0
        self.world_seed = self.seeds[self.seed_indexx]
        self.ui_loaded = False

    def start_new_game(self):
        logger.info(f"Starting new game with seed: {self.world_seed}")
        in_game_state = self.engine.state_manager.get_state("IN_GAME")
        if in_game_state:
            in_game_state.set_world_seed(self.world_seed)
        self.engine.state_manager.set_state('IN_GAME')

    def set_world_seed(self):
        self.seed_indexx = (self.seed_indexx + 1) % len(self.seeds)
        self.world_seed = self.seeds[self.seed_indexx]
        logger.info(f"World seed set to: {self.world_seed}")
        self._update_seed_button_text()

    def back_to_main(self):
        self.engine.state_manager.pop_state()

    def enter(self):
        logger.info("Entering NewGameState.")
        if not self.ui_loaded:
            action_map = {
                "start_new_game": self.start_new_game,
                "set_world_seed": self.set_world_seed,
                "back_to_main": self.back_to_main
            }
            self.engine.ui_manager.load_screen_from_xml("ui/layouts/new_game_menu.xml", action_map)
            self.ui_loaded = True

        self.engine.ui_manager.set_active_screen("new_game_menu")
        self._update_seed_button_text()

    def exit(self):
        logger.info("Exiting NewGameState.")
        self.engine.ui_manager.set_active_screen(None)

    def update(self, delta_time: float):
        if self.engine.input_handler.is_key_pressed('escape'):
            self.back_to_main()

    def render(self, renderer):
        pass

    def _update_seed_button_text(self):
        screen = self.engine.ui_manager.screens.get("new_game_menu")
        if screen:
            seed_button = screen.get_widget("seed_button")
            if seed_button:
                seed_button.text = f"Set Seed: {self.world_seed}"
```

### File: `/game/states/main_menu_state.py`
```py
# /game/states/main_menu_state.py

from .base_state import BaseState
from utils.vectors import Vector3
from utils.logger import logger
from game.menu_world import MenuWorld
import pygame
import math
import pyrr
import numpy as np

class MainMenuState(BaseState):
    def __init__(self, engine):
        super().__init__(engine)
        self.time = 0.0
        self.ui_loaded = False
        self.menu_world: MenuWorld = None
        self.world_model_matrix = pyrr.matrix44.create_identity(dtype=np.float32)

    # (start_game, load_game, etc. methods remain the same)
    
    def enter(self):
        logger.info("Entering MainMenuState.")

        if self.menu_world is None:
            self.menu_world = MenuWorld.load("menu_world.dat")
    
        if not self.ui_loaded:
            action_map = { "start_game": self.start_game, "load_game": self.load_game,
                           "open_options": self.open_options, "quit_game": self.quit_game }
            self.engine.ui_manager.load_screen_from_xml("ui/layouts/main_menu.xml", action_map)
            self.ui_loaded = True

        self.engine.ui_manager.set_active_screen("main_menu")
        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)
        pygame.event.clear()
        self.engine.input_handler.clear_pressed_state()
        
        self.engine.camera.set_target(None)
        self.engine.camera.position = Vector3([32.0, 85.0, 32.0]) # Center view on menu world
        self.engine.camera.pitch = -25.0
        self.engine.camera.yaw = 225.0 # Look towards the center from a corner
        
    def update(self, delta_time: float):
        self.time += delta_time
        self.engine.camera.yaw += 3.0 * delta_time # Slow, majestic rotation
        self.engine.cloud_system.update(delta_time)

    def render(self, renderer):
        if not renderer: return
        
        # --- REFACTOR: Define a consistent light source for clouds and world ---
        light_dir = pyrr.Vector3([0.8, 0.6, 0.5]).normalized
        light_pos = self.engine.camera.position + (light_dir * 1000) # Fake a distant light pos
        light_color = pyrr.Vector3([1.0, 0.9, 0.8])
        
        renderer.set_light_properties(light_pos, light_color, 0.35)
        
        view_matrix = self.engine.camera.get_view_matrix()
        proj_matrix = renderer.perspective_matrix
        
        # Pass sun direction to clouds
        self.engine.cloud_system.set_light_direction(-light_dir) 
        self.engine.skybox.render(light_pos.y, proj_matrix, view_matrix, self.time)
        self.engine.cloud_system.render(self.time)

        if self.menu_world and self.menu_world.vao:
            renderer.render_lit_mesh(self.menu_world.vao, self.menu_world.vertex_count, 
                                     self.world_model_matrix, self.engine.camera, use_vertex_color=True)
                                     
    # (Other methods unchanged)
    def start_game(self): self.engine.state_manager.push_state('NEW_GAME')
    def load_game(self): self.engine.state_manager.push_state('LOAD_GAME')
    def open_options(self): self.engine.state_manager.push_state('OPTIONS')
    def quit_game(self): self.engine.request_shutdown()
    def exit(self): logger.info("Exiting MainMenuState.")
    def resume(self):
        logger.info("Resuming MainMenuState.")
        self.engine.ui_manager.set_active_screen("main_menu")
        pygame.mouse.set_visible(True); pygame.event.set_grab(False)
        self.engine.input_handler.clear_pressed_state()
```

### File: `/game/states/load_game_state.py`
```py
# /game/states/load_game_state.py

from .base_state import BaseState
from utils.logger import logger
from ui.widgets import Button
import pygame

class LoadGameState(BaseState):
    """A state for loading or deleting saved games from a dynamic UI list."""
    def __init__(self, engine):
        super().__init__(engine)
        self.save_files = []
        self.selected_saves = set()
        self.dynamic_widgets = []
        self.action_map = {
            "load_selected": self.load_selected,
            "delete_selected": self.delete_selected,
            "select_all": self.select_all,
            "select_none": self.select_none,
            "back_to_main": self.back_to_main
        }
        self.engine.ui_manager.load_screen_from_xml("ui/layouts/load_game_menu.xml", self.action_map)

    def enter(self):
        logger.info("Entering LoadGameState.")
        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)
        self.engine.ui_manager.set_active_screen("load_game_menu")
        self.populate_save_list()

    def exit(self):
        logger.info("Exiting LoadGameState.")

        # --- FIX: Add cleanup logic for dynamically created widgets ---
        # Restore the screen to its original state to prevent UI bleed-through.
        screen = self.engine.ui_manager.screens.get("load_game_menu")
        if screen:
            for widget in self.dynamic_widgets:
                if widget in screen.widgets:
                    screen.widgets.remove(widget)
        self.dynamic_widgets.clear()
        self.selected_saves.clear()
        # --- END OF FIX ---

        # Deactivate our UI and reactivate the main menu's
        self.engine.ui_manager.set_active_screen("main_menu")

    def update(self, delta_time: float):
        if self.engine.input_handler.is_key_pressed('escape'):
            self.back_to_main()

    def render(self, renderer):
        pass

    def populate_save_list(self):
        screen = self.engine.ui_manager.screens.get("load_game_menu")
        if not screen: return
        
        # This cleanup is still needed here for when we re-populate without exiting
        for widget in self.dynamic_widgets:
            if widget in screen.widgets:
                screen.widgets.remove(widget)
        self.dynamic_widgets.clear()
        self.selected_saves.clear()

        self.save_files = self.engine.save_manager.get_save_files()
        
        no_saves_label = screen.get_widget("no_saves_label")
        if no_saves_label:
            no_saves_label.visible = not bool(self.save_files)

        start_y, spacing = 120, 55
        for i, save_meta in enumerate(self.save_files):
            filename = save_meta['filename']
            prefix = "AUTOSAVE" if "auto" in filename else "Manual Save"
            timestamp = save_meta['timestamp'].replace("T", " ").split(".")[0]
            button_text = f"{prefix} - {timestamp}"
            
            button_rect = pygame.Rect(0, 0, 800, 50)
            button_rect.center = (self.engine.platform.get_window_size().x / 2, start_y + i * spacing)
            
            button = Button(button_rect, button_text, on_click=lambda f=filename: self.toggle_selection(f))
            
            screen.add_widget(button, f"save_{filename}")
            self.dynamic_widgets.append(button)

    # (The rest of the file remains the same)
    def toggle_selection(self, filename):
        if filename in self.selected_saves:
            self.selected_saves.remove(filename)
        else:
            self.selected_saves.add(filename)
        self.update_button_visuals()

    def update_button_visuals(self):
        screen = self.engine.ui_manager.screens.get("load_game_menu")
        for save_meta in self.save_files:
            filename = save_meta['filename']
            button = screen.get_widget(f"save_{filename}")
            if button:
                prefix = "[X] " if filename in self.selected_saves else ""
                save_type = "AUTOSAVE" if "auto" in filename else "Manual Save"
                timestamp = save_meta['timestamp'].replace("T", " ").split(".")[0]
                button.text = f"{prefix}{save_type} - {timestamp}"

    def load_selected(self):
        if len(self.selected_saves) != 1:
            logger.warning("Please select exactly one save file to load.")
            return
        filename = self.selected_saves.pop()
        self.engine.save_manager.load_game(filename)

    def delete_selected(self):
        if not self.selected_saves:
            logger.warning("No save files selected for deletion.")
            return
        for filename in self.selected_saves:
            self.engine.save_manager.delete_save(filename)
        self.populate_save_list()

    def select_all(self):
        self.selected_saves = {meta['filename'] for meta in self.save_files}
        self.update_button_visuals()

    def select_none(self):
        self.selected_saves.clear()
        self.update_button_visuals()

    def back_to_main(self):
        self.engine.state_manager.pop_state()
```

### File: `/game/states/inventory_state.py`
```py
# /game/states/inventory_state.py

from .base_state import BaseState
from utils.logger import logger
import game.components as C
import pygame

class InventoryState(BaseState):
    def __init__(self, engine):
        super().__init__(engine)
        self.player_entity = None
        self.in_game_state_ref = None
        
        # --- NEW: Define an action map for UI buttons ---
        action_map = {
            "filter_all": lambda: self.filter_inventory("ALL"),
            "filter_weapons": lambda: self.filter_inventory("WEAPON"),
            "filter_armor": lambda: self.filter_inventory("ARMOR"),
            "filter_consumables": lambda: self.filter_inventory("CONSUMABLE"),
        }
        # --- NEW: Load the UI layout when the state is created ---
        self.engine.ui_manager.load_screen_from_xml("ui/layouts/inventory_menu.xml", action_map)

    def enter(self):
        logger.info("Entering InventoryState.")
        # --- NEW: Set the UI as active and get player data ---
        self.engine.ui_manager.set_active_screen("inventory_menu")
        
        self.in_game_state_ref = self.engine.state_manager.get_state("IN_GAME")
        if self.in_game_state_ref and self.in_game_state_ref.player_entity:
            self.player_entity = self.in_game_state_ref.player_entity
            self._update_ui_from_player_data()
        else:
            logger.error("Could not get player reference in InventoryState.")
            self.engine.state_manager.pop_state()
            return

        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)

    def _update_ui_from_player_data(self):
        """Gets all relevant player data and updates the UI widgets."""
        if not self.player_entity:
            return
            
        screen = self.engine.ui_manager.screens.get("inventory_menu")
        if not screen:
            logger.error("InventoryState could not find 'inventory_menu' UI screen.")
            return

        # Get player components
        health_comp = self.player_entity.get_component(C.HealthComponent)
        inventory_comp = self.player_entity.get_component(C.InventoryComponent)
        # NOTE: Stamina and Armor would come from other components not shown in the file list
        # For now, we will use placeholder values for them.
        
        # Get UI widgets by their ID from the XML
        health_label = screen.get_widget("health_value_label")
        stamina_label = screen.get_widget("stamina_value_label")
        armor_label = screen.get_widget("armor_value_label")
        
        # Update text labels
        if health_comp and health_label:
            health_label.text = f"[{int(health_comp.current_health)} / {int(health_comp.max_health)}]"
        
        if stamina_label:
            stamina_label.text = "[100 / 100]" # Placeholder
            
        if armor_label:
            armor_label.text = "[ 15 ]" # Placeholder

        self._render_inventory_grid(screen, inventory_comp)


    def _render_inventory_grid(self, screen, inventory_comp):
        """
        In a full implementation, this function would dynamically create
        and position item icons in the grid area based on the inventory_comp.items list.
        For now, it will log the items to the console as the original did.
        """
        if not inventory_comp:
            return

        logger.info("--- PLAYER INVENTORY (UI UPDATE) ---")
        if inventory_comp.items:
            for item_id in inventory_comp.items:
                item_data = self.engine.item_manager.get_item_data(item_id)
                if item_data:
                    logger.info(f"- {item_data.get('name', 'Unknown Item')} (ID: {item_id})")
        else:
            logger.info("Inventory is empty.")
        
        logger.info(f"Capacity: {len(inventory_comp.items)} / {inventory_comp.capacity}")
        logger.info("------------------------------------")


    def filter_inventory(self, category: str):
        """Placeholder function for inventory filter buttons."""
        logger.info(f"Filtering inventory by: {category}")
        # In a real implementation, this would change which items are displayed in the grid.
        pass

    def exit(self):
        logger.info("Exiting InventoryState.")
        self.engine.ui_manager.set_active_screen(None)
        
        # --- THE FIX ---
        # The faulty 'if' condition has been removed. When we exit the inventory,
        # we always want to return to the in-game mouse behavior.
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)

    def update(self, delta_time: float):
        input_handler = self.engine.input_handler
        if input_handler.is_key_pressed('i') or input_handler.is_key_pressed('escape'):
            self.engine.state_manager.pop_state()

    def render(self, renderer):
        # The UIManager handles rendering the active screen, so this can be empty.
        # However, we might render the 3D player model here in the future.
        pass
```

### File: `/game/states/initialization_state.py`
```py
# /game/states/initialization_state.py

import os
import random
from .base_state import BaseState
from game.menu_world import MenuWorld
from systems.world_generator import WorldGenerator
from game.block import STONE, DIRT, GRASS
from utils.logger import logger
from utils.color import WHITE, BLACK
import pygame

class InitializationState(BaseState):
    """
    A one-time state that runs on first launch. It checks for a pre-generated
    main menu world and creates one if it doesn't exist.
    """
    def __init__(self, engine):
        super().__init__(engine)
        self.menu_world_path = "menu_world.dat"
        self.generation_coroutine = None
        self.status_message = "Initializing..."
        self.is_generating = False
        self.ui_loaded = False

    def enter(self):
        logger.info("Entering InitializationState.")

        if not self.ui_loaded:
            self.engine.ui_manager.load_screen_from_xml("ui/layouts/initialization_screen.xml", {})
            self.ui_loaded = True
        
        self.engine.ui_manager.set_active_screen("initialization_screen")

        if os.path.exists(self.menu_world_path):
            logger.info(f"Found existing menu world at '{self.menu_world_path}'.")
            self.engine.state_manager.set_state("MAIN_MENU")
        else:
            logger.info("No menu world found. Starting generation process.")
            self.is_generating = True
            self.generation_coroutine = self._generation_process()

    def update(self, delta_time: float):
        if self.is_generating and self.generation_coroutine:
            try:
                self.status_message = next(self.generation_coroutine)
                label = self.engine.ui_manager.screens["initialization_screen"].get_widget("status_label")
                if label:
                    label.text = self.status_message
            except StopIteration:
                logger.info("Menu world generation complete.")
                self.is_generating = False
                self.generation_coroutine = None
                self.engine.state_manager.set_state("MAIN_MENU")

    def render(self, renderer):
        # The background is black, and the UIManager renders UI text on top.
        pass
    
    def _generation_process(self):
        """A generator that yields status updates during the world creation."""
        yield "Generating terrain data..."
        
        world_gen = WorldGenerator(seed=random.randint(0, 100000))
        menu_world = MenuWorld(size=(64, 128, 64))
        
        heights = [[world_gen.get_height(x, z) for z in range(64)] for x in range(64)]
        
        for x in range(64):
            for z in range(64):
                height = min(heights[x][z], 127) # Ensure height is within bounds
                for y in range(height):
                    if y < height - 4: menu_world.blocks[x, y, z] = STONE
                    elif y < height - 1: menu_world.blocks[x, y, z] = DIRT
                    else: menu_world.blocks[x, y, z] = GRASS
        
        yield "Building visual mesh (this may take a moment)..."
        pygame.time.delay(10) # Give the OS a moment to redraw the screen
        
        menu_world.build_mesh()
        
        yield "Saving for future use..."
        pygame.time.delay(10)

        menu_world.save(self.menu_world_path)
        
        yield "Loading main menu..."

    def exit(self):
        self.engine.ui_manager.set_active_screen(None)
```

### File: `/game/states/in_game_state.py`
```py
# /game/states/in_game_state.py

import pygame
import pyrr
import math
import numpy as np
from .base_state import BaseState
from game.world import World
from game.entity_factory import EntityFactory
from systems.physics import PhysicsSystem
from systems.player_control_system import PlayerControlSystem
from utils.debug_overlay import DebugOverlay
from utils.logger import logger
from utils.vectors import Vector3
import game.components as C

class InGameState(BaseState):
    def __init__(self, engine):
        super().__init__(engine)
        self.world: World = None
        self.player_entity = None
        self.entity_factory: EntityFactory = None
        
        self.physics_system: PhysicsSystem = None
        self.player_control_system: PlayerControlSystem = None
        
        self.debug_overlay = DebugOverlay(self.engine)
        
        self.load_data: dict = None
        self.world_seed: int = 12345
        self.time_of_day: float = 0.25
        self.world_time: float = 0.0

    def set_load_data(self, data: dict):
        self.load_data = data

    def set_world_seed(self, seed: int):
        self.world_seed = seed

    def enter(self):
        logger.info("===== Entering InGameState =====")
        self.engine.ui_manager.set_active_screen(None)
        
        self.world = World(self.engine)
        self.physics_system = PhysicsSystem(self.world, gravity=(0, -20, 0))
        
        seed = self.load_data.get('world_seed', self.world_seed) if self.load_data else self.world_seed
        self.world.initialize_world(seed)
        
        self.entity_factory = EntityFactory(self.world, self.physics_system)
        
        if self.load_data:
            player_pos = pyrr.Vector3(self.load_data['player']['position'])
            self.load_data = None
        else:
            spawn_x, spawn_z = 0, 0
            spawn_y = self.world.world_generator.get_height(spawn_x, spawn_z) + 2.0
            player_pos = pyrr.Vector3([float(spawn_x), float(spawn_y), float(spawn_z)])

        self.world.load_chunks_around(player_pos)
        self.player_entity = self.entity_factory.create_player(player_pos)
        self.world.set_player_entity(self.player_entity)
        self.engine.camera.set_target(self.player_entity)

        self.entity_factory.create_enemy(self.player_entity.transform.position + pyrr.Vector3([10, 2, 10]))

        self.player_control_system = PlayerControlSystem(self.engine)
        self.autosave_timer = 0.0
        
        self.resume() 

    def resume(self):
        logger.info("Resuming InGameState.")
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        self.engine.input_handler.clear_pressed_state()

    def exit(self):
        logger.info("===== Exiting InGameState =====")
        if self.physics_system:
            self.physics_system.shutdown()
        
        self.world, self.player_entity, self.physics_system, self.player_control_system, self.entity_factory = None, None, None, None, None
        
        self.engine.camera.set_target(None)
        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)

    def update(self, delta_time: float):
        self.world_time += delta_time
        self.time_of_day = (self.time_of_day + (delta_time / 1440.0)) % 1.0

        input_handler = self.engine.input_handler
        if input_handler.is_key_pressed('escape'):
            self.engine.state_manager.push_state('PAUSE')
            return
        if input_handler.is_key_pressed('i'):
            self.engine.state_manager.push_state('INVENTORY')
            return
        if input_handler.is_key_pressed('f3'):
            self.debug_overlay.toggle()
        
        if self.world:
            self.world.update()
        
        # --- THE FIX: Removed placeholder AI that was fighting with the physics engine. ---
        # Now, all non-player entities will be fully simulated by PyBullet without interference.

        if self.player_control_system:
            self.player_control_system.update(delta_time)
        
        if self.physics_system:
            self.physics_system.update(delta_time)
            
        if self.engine.camera:
            self.engine.camera.update(delta_time, input_handler, self.physics_system)

        if self.engine.cloud_system:
            self.engine.cloud_system.update(delta_time)
            
        if self.engine.acoustic_system:
             self.engine.acoustic_system.update(delta_time, self.world, self.physics_system, self.player_entity)


    def render(self, renderer):
        if not self.world or not renderer: return

        sun_angle = self.time_of_day * 2.0 * math.pi
        sun_pos_y = math.sin(sun_angle) * 5000
        sun_pos = pyrr.Vector3([math.cos(sun_angle) * 5000, sun_pos_y, 1000])
        
        if sun_pos_y < -100: light_color, ambient = pyrr.Vector3([0.4, 0.5, 0.7]), 0.1
        elif sun_pos_y < 100:
            t = (sun_pos_y + 100) / 200.0
            day_c, sunset_c = pyrr.Vector3([1.0, 1.0, 0.95]), pyrr.Vector3([1.0, 0.7, 0.5])
            light_color = (sunset_c * (1.0 - t)) + (day_c * t)
            ambient = 0.2 + t * 0.1
        else: light_color, ambient = pyrr.Vector3([1.0, 1.0, 0.95]), 0.3
            
        renderer.set_light_properties(sun_pos, light_color, ambient)
        
        view_matrix = self.engine.camera.get_view_matrix()
        proj_matrix = renderer.perspective_matrix
        
        self.engine.skybox.render(sun_pos_y, proj_matrix, view_matrix, self.world_time)
        self.engine.cloud_system.render(self.world_time)
        renderer.render_scene(self.world, self.engine.camera)
```

### File: `/game/states/base_state.py`
```py
# /game/states/base_state.py

class BaseState:
    def __init__(self, engine):
        self.engine = engine

    def enter(self):
        """Called once when the state becomes active for the first time."""
        pass

    def exit(self):
        """Called once when the state is no longer active."""
        pass

    def resume(self):
        """Called when a state on top of this one is popped."""
        pass

    def update(self, delta_time: float):
        raise NotImplementedError

    def render(self, renderer):
        raise NotImplementedError
```

### File: `/game/data/items.json`
```json
{
    "ITM_AXE_STONE": {
        "name": "Stone Axe",
        "description": "A crude axe made from wood and flint. Can chop basic trees and functions as a simple weapon.",
        "type": "TOOL",
        "weight": 2.5
    },
    "ITM_RED_MUSHROOM": {
        "name": "Redcap Mushroom",
        "description": "A common red-capped mushroom found in forests. Can be used in alchemy.",
        "type": "CONSUMABLE",
        "weight": 0.1
    },
    "ITM_WOOD_LOG": {
        "name": "Wood Log",
        "description": "A log harvested from a tree. A primary building material.",
        "type": "RESOURCE",
        "weight": 5.0
    }
}
```

### File: `/game/components/transform_component.py`
```py
# game/components/transform_component.py

import pyrr
from .base_component import BaseComponent

class TransformComponent(BaseComponent):
    """
    Stores all data related to an entity's position, rotation, and scale in 3D space.
    """
    def __init__(self, owner, position=pyrr.Vector3([0.0, 0.0, 0.0]), 
                 rotation=pyrr.Quaternion(), scale=pyrr.Vector3([1.0, 1.0, 1.0])):
        super().__init__(owner)
        self.position = position
        self.rotation = rotation
        self.scale = scale

    def get_model_matrix(self) -> pyrr.Matrix44:
        """
        Calculates and returns the model matrix from position, rotation, and scale.
        This is crucial for rendering and physics.
        """
        # Create matrices for translation, rotation, and scale
        translation_matrix = pyrr.matrix44.create_from_translation(self.position)
        rotation_matrix = pyrr.matrix44.create_from_quaternion(self.rotation)
        scale_matrix = pyrr.matrix44.create_from_scale(self.scale)
        
        # Combine them in the correct order: scale, then rotate, then translate
        return scale_matrix @ rotation_matrix @ translation_matrix
```

### File: `/game/components/render_component.py`
```py
# game/components/render_component.py

from .base_component import BaseComponent
from utils.color import WHITE

class RenderComponent(BaseComponent):
    """
    Stores data required by the Renderer system to draw an entity.
    """
    def __init__(self, owner, mesh_id: str = "cube", color=WHITE, is_visible: bool = True):
        super().__init__(owner)
        self.mesh_id = mesh_id
        self.color = color
        self.is_visible = is_visible # Use the passed-in value
```

### File: `/game/components/player_input_component.py`
```py
# /game/components/player_input_component.py

from .base_component import BaseComponent

class PlayerInputComponent(BaseComponent):
    """
    A tag component that identifies an entity as being controllable by the player.
    It can also hold player-specific input data if needed.
    """
    def __init__(self, owner, speed=5.0):
        super().__init__(owner)
        # --- TUNED VALUE: A higher force is needed for a responsive feel ---
        self.move_force = 2000.0 
        self.max_speed = 5.0
```

### File: `/game/components/physics_component.py`
```py
# /game/components/physics_component.py

from .base_component import BaseComponent

class PhysicsComponent(BaseComponent):
    """
    Stores data for the physics simulation, such as mass and collision shape.
    """
    def __init__(self, owner, mass: float = 1.0, 
                 shape_type: str = "box", dimensions=None, body_id=None):
        super().__init__(owner)
        self.body_id = body_id  # The unique ID returned by the physics engine
        self.mass = mass
        self.shape_type = shape_type
        # Dimensions is a dictionary, e.g. {"width": 1, "height": 1, "depth": 1}
        # or {"radius": 0.5}
        self.dimensions = dimensions if dimensions else {"width": 1.0, "height": 1.0, "depth": 1.0}
        # --- NEW: Flag to track collision state ---
        self.collision_enabled = True
```

### File: `/game/components/needs_component.py`
```py
# /game/components/needs_component.py

from .base_component import BaseComponent
from utils.logger import logger
import random

class NeedsComponent(BaseComponent):
    """
    Manages all survival needs for an entity, including hunger, thirst,
    and placeholder needs for bladder and bowel.
    """
    def __init__(self, owner, hunger=100.0, thirst=100.0):
        super().__init__(owner)
        self.max_hunger = 100.0
        self.hunger = float(hunger)
        
        self.max_thirst = 100.0
        self.thirst = float(thirst)

        # Bodily needs fill up, they don't deplete. Start them partially full for realism.
        self.max_bladder = 100.0
        self.bladder = random.uniform(10.0, 30.0)

        self.max_bowel = 100.0
        self.bowel = random.uniform(10.0, 30.0)

        # Rate constants (units per second)
        self.hunger_rate = 0.1
        self.thirst_rate = 0.15
        self.bladder_fill_rate = 0.1
        self.bowel_fill_rate = 0.08

        # Warning flags to prevent log spam
        self.bladder_warning_sent = False
        self.bowel_warning_sent = False

    def update(self, delta_time: float):
        """Update needs over time."""
        self.hunger = max(0.0, self.hunger - self.hunger_rate * delta_time)
        self.thirst = max(0.0, self.thirst - self.thirst_rate * delta_time)

        self.bladder = min(self.max_bladder, self.bladder + self.bladder_fill_rate * delta_time)
        self.bowel = min(self.max_bowel, self.bowel + self.bowel_fill_rate * delta_time)

        self._check_and_log_warnings()

    def eat(self, food_value: float, waste_byproduct: float):
        """Replenish hunger and add to bowel."""
        self.hunger = min(self.max_hunger, self.hunger + food_value)
        self.bowel = min(self.max_bowel, self.bowel + waste_byproduct)
        logger.info(f"Entity {self.owner.id} ate. Hunger: {self.hunger:.1f}, Bowel: {self.bowel:.1f}")

    def drink(self, water_value: float, bladder_byproduct: float):
        """Replenish thirst and add to bladder."""
        self.thirst = min(self.max_thirst, self.thirst + water_value)
        self.bladder = min(self.max_bladder, self.bladder + bladder_byproduct)
        logger.info(f"Entity {self.owner.id} drank. Thirst: {self.thirst:.1f}, Bladder: {self.bladder:.1f}")

    def relieve_self(self):
        """Resets bladder and bowel meters."""
        self.bladder = 0.0
        self.bowel = 0.0
        self.bladder_warning_sent = False
        self.bowel_warning_sent = False
        logger.info(f"Entity {self.owner.id} has relieved themselves. Needs reset.")

    def _check_and_log_warnings(self):
        """Logs warnings to the console when needs are critical."""
        if self.bladder / self.max_bladder > 0.9 and not self.bladder_warning_sent:
            logger.warning(f"Placeholder: Entity {self.owner.id}'s bladder is full!")
            self.bladder_warning_sent = True
        elif self.bladder / self.max_bladder < 0.9:
            self.bladder_warning_sent = False
            
        if self.bowel / self.max_bowel > 0.9 and not self.bowel_warning_sent:
            logger.warning(f"Placeholder: Entity {self.owner.id} needs to defecate!")
            self.bowel_warning_sent = True
        elif self.bowel / self.max_bowel < 0.9:
            self.bowel_warning_sent = False
```

### File: `/game/components/item_component.py`
```py
# /game/components/item_component.py

from .base_component import BaseComponent

class ItemComponent(BaseComponent):
    """
    A component that marks an entity as a pickup-able item in the world.
    """
    def __init__(self, owner, item_id: str):
        super().__init__(owner)
        self.item_id = item_id # e.g., "ITM_AXE_STONE"
```

### File: `/game/components/inventory_component.py`
```py
# /game/components/inventory_component.py

from .base_component import BaseComponent
from utils.logger import logger

class InventoryComponent(BaseComponent):
    """
    Gives an entity the ability to hold a collection of items.
    """
    def __init__(self, owner, capacity: int = 20):
        super().__init__(owner)
        self.capacity = capacity
        self.items = [] # A list of item_ids

    def add_item(self, item_id: str) -> bool:
        """Adds an item to the inventory if there is space."""
        if len(self.items) < self.capacity:
            self.items.append(item_id)
            logger.info(f"Entity {self.owner.id} picked up item '{item_id}'. Inventory: {len(self.items)}/{self.capacity}")
            return True
        else:
            logger.warning(f"Entity {self.owner.id} failed to pick up item '{item_id}'. Inventory full.")
            return False

    def remove_item(self, item_id: str) -> bool:
        """Removes an item from the inventory."""
        if item_id in self.items:
            self.items.remove(item_id)
            logger.debug(f"Entity {self.owner.id} removed item '{item_id}'.")
            return True
        return False
```

### File: `/game/components/health_component.py`
```py
# game/components/health_component.py

from .base_component import BaseComponent
from utils.logger import logger

class HealthComponent(BaseComponent):
    """Manages an entity's health and damage state."""
    def __init__(self, owner, max_health=100):
        super().__init__(owner)
        self.max_health = max_health
        self.current_health = max_health

    def take_damage(self, amount):
        self.current_health -= amount
        
        logger.debug(f"'{self.owner.name} ({self.owner.id})' took {amount} damage, health is now {self.current_health}/{self.max_health}")
        
        if self.current_health <= 0:
            self.die()

    def heal(self, amount):
        self.current_health = min(self.max_health, self.current_health + amount)

    def die(self):
        logger.info(f"'{self.owner.name} ({self.owner.id})' has been defeated.")
        # In a real game, this would signal the world to remove the entity
        # For now, we just reset health.
        self.current_health = self.max_health
```

### File: `/game/components/base_component.py`
```py
# /game/components/base_component.py

class BaseComponent:
    """An abstract base class for all components."""
    def __init__(self, owner):
        self.owner = owner

    def update(self, delta_time):
        pass
```

### File: `/game/components/__init__.py`
```py
# game/components/__init__.py

"""
This file makes the components directory a Python package and exposes 
all component classes at the top level for easy importing.
"""
from .base_component import BaseComponent

# --- CORE & ECS ---
from .transform_component import TransformComponent
from .render_component import RenderComponent
from .physics_component import PhysicsComponent

# --- PLAYER & INPUT ---
from .player_input_component import PlayerInputComponent

# --- GAMEPLAY ---
from .health_component import HealthComponent
from .inventory_component import InventoryComponent
from .item_component import ItemComponent
from .needs_component import NeedsComponent

# --- DEPRECATED FILES HAVE BEEN REMOVED ---
```

### File: `/core/state_manager.py`
```py
# core/state_manager.py

from utils.logger import logger

class StateManager:
    def __init__(self, engine):
        self.engine = engine
        self._state_classes = {}  # --- NEW: Stores state classes ---
        self._state_instances = {} # --- NEW: Caches state instances ---
        self._stack: list = []

    def register_state(self, name: str, state_class):
        """Stores the class constructor for a state."""
        self._state_classes[name] = state_class

    def _get_or_create_state(self, name: str):
        """Gets a cached state instance or creates one if it doesn't exist."""
        if name in self._state_instances:
            return self._state_instances[name]
        
        if name in self._state_classes:
            logger.info(f"StateManager: Lazily instantiating state '{name}'.")
            instance = self._state_classes[name](self.engine)
            self._state_instances[name] = instance
            return instance
        
        return None

    def push_state(self, name: str):
        state_instance = self._get_or_create_state(name)
        if not state_instance:
            logger.error(f"Attempted to push non-existent state '{name}'.")
            return
        
        logger.info(f"StateManager: Pushing state '{name}'.")
        self._stack.append(state_instance)
        state_instance.enter()

    def pop_state(self):
        if not self._stack:
            logger.warning("StateManager: Tried to pop from an empty state stack.")
            return
        
        top_state = self._stack[-1]
        logger.info(f"StateManager: Popping state '{top_state.__class__.__name__}'.")
        top_state.exit()
        self._stack.pop()
        
        if self._stack:
            self._stack[-1].resume()
        else:
            logger.info("State stack is empty. Requesting engine shutdown.")
            self.engine.request_shutdown()

    def set_state(self, name: str):
        state_instance = self._get_or_create_state(name)
        if not state_instance:
            logger.error(f"Attempted to set non-existent state '{name}'.")
            return
            
        logger.info(f"StateManager: Setting root state to '{name}'.")
        while self._stack:
            self._stack.pop().exit()
        
        # We don't call push_state here to avoid double-logging "push"
        self._stack.append(state_instance)
        state_instance.enter()

    def update(self, delta_time: float):
        if self._stack:
            self._stack[-1].update(delta_time)

    def render(self, renderer):
        for state in self._stack:
            state.render(renderer)

    def get_active_state(self):
        return self._stack[-1] if self._stack else None

    # This function is used by other systems to get a reference to a state without activating it
    def get_state(self, name: str):
        return self._get_or_create_state(name)
```

### File: `/core/platform.py`
```py
# /core/platform.py

import pygame
from utils.vectors import Vector2
from utils.logger import logger

class Platform:
    """
    Manages the OS-level window and creates the OpenGL rendering context.
    This module is a thin, engine-specific abstraction over a backend library
    (in this case, Pygame) to isolate OS-specific code, as per the GDD.
    """
    def __init__(self):
        self.window_surface = None

    def initialize(self, title: str, width: int, height: int) -> bool:
        """
        Creates the game window and sets up the OpenGL graphics context.
        Follows the specifications in '02_Platform_and_Windowing.md'.
        """
        try:
            pygame.init()
            
            # Request a specific OpenGL core profile (3.3)
            pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
            pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
            pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
            
            # Set attributes for the frame buffer
            pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)

            # This requests a double buffer for the OpenGL context
            pygame.display.gl_set_attribute(pygame.GL_DOUBLEBUFFER, 1)
            
            # This flag tells set_mode to use the requested attributes
            display_flags = pygame.OPENGL | pygame.DOUBLEBUF
            self.window_surface = pygame.display.set_mode((width, height), display_flags, vsync=1)
            pygame.display.set_caption(title)
            
            logger.info("Platform initialized successfully.")
            return True
        except pygame.error as e:
            logger.critical(f"Platform failed to initialize. Pygame error: {e}")
            return False

    def shutdown(self) -> None:
        """Destroys the window and cleans up Pygame."""
        logger.info("Platform shutting down.")
        pygame.quit()

    def get_window_size(self) -> Vector2:
        """Returns the current dimensions of the window's drawable area."""
        if not self.window_surface:
            return Vector2(0, 0)
        size = self.window_surface.get_size()
        return Vector2(size[0], size[1])

    def swap_buffers(self):
        """Presents the back-buffer (what the renderer has drawn to) to the screen."""
        pygame.display.flip()
```

### File: `/core/phonons.py`
```py
# /core/phonons.py

from dataclasses import dataclass
from utils.vectors import Vector3

@dataclass
class Phonon:
    """
    A data structure representing a sound event in the physical world.
    It does not contain audio data itself, but rather the physical properties
    of a sound-producing event that the AcousticSystem will process.
    """
    source_position: Vector3
    acoustic_mass: float # The "weight" or intensity of the sound event.
    event_type: str = "default" # e.g., "footstep", "impact", "explosion"
```

### File: `/core/engine.py`
```py
# /core/engine.py

import pygame
from utils.logger import logger, attach_debug_handler
from .platform import Platform
from .state_manager import StateManager
from core.phonons import Phonon

# Import all engine systems as defined in the GDD
from systems.input_handler import InputHandler
from systems.renderer import Renderer
from systems.audio_engine import AudioEngine
from systems.acoustic_system import AcousticSystem
from systems.asset_manager import AssetManager
from systems.ui_manager import UIManager
from systems.camera import Camera
from systems.debug_manager import DebugManager
from systems.item_manager import ItemManager
from systems.save_manager import SaveManager
from systems.skybox import Skybox
from systems.cloud_system import CloudSystem

class Engine:
    """
    A singleton class representing the core of the Stelliferrum Forge.
    It owns and manages all the engine's subsystems, handles the main loop,
    and provides a centralized access point for all game logic.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Engine, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized') and self._initialized: return
        
        self.is_running: bool = False
        self.delta_time: float = 0.0
        self.is_debug: bool = False
        
        # Instantiate all engine systems
        self.platform = Platform()
        self.state_manager = StateManager(self)
        self.asset_manager = AssetManager()
        self.item_manager = ItemManager()
        self.camera = Camera(self)
        self.renderer = Renderer()
        self.audio_engine = AudioEngine()
        self.acoustic_system = AcousticSystem(self)
        self.ui_manager = UIManager(self)
        self.save_manager = SaveManager(self)
        self.skybox = Skybox(self)
        self.cloud_system = CloudSystem(self)
        self.input_handler: InputHandler = None 
        self.debug_manager: DebugManager = None
        self._initialized: bool = False

    def initialize(self, title: str, width: int, height: int, is_debug: bool = False):
        if self._initialized:
            logger.warning("Engine already initialized.")
            return

        logger.info("--- Engine Systems Initialization ---")
        self.is_debug = is_debug
        
        if not self.platform.initialize(title, width, height):
            logger.critical("Engine initialization failed: Platform could not be started.")
            self.is_running = False
            return
        
        self.input_handler = InputHandler()
        
        self.debug_manager = DebugManager(self, is_enabled=self.is_debug)
        if self.is_debug:
            attach_debug_handler(self.debug_manager)

        self.renderer.initialize(self)
        self.item_manager.initialize()
        self.audio_engine.initialize(self) # --- FIX: Pass engine instance for camera access ---
        self.acoustic_system.initialize()

        self.skybox.initialize()
        self.cloud_system.initialize()

        logger.info("--- Engine Initialization Complete ---")
        self.is_running = True
        self._initialized = True

    def run(self):
        if not self._initialized:
            logger.error("Engine.run() called before Engine.initialize().")
            return

        logger.info("Starting main engine loop.")
        clock = pygame.time.Clock()
        MAX_DELTA_TIME = 0.1 
        
        while self.is_running:
            if self.debug_manager.is_enabled:
                self.debug_manager.begin_frame()
            
            self.delta_time = min(clock.tick(60) / 1000.0, MAX_DELTA_TIME)
            
            self.input_handler.process_events()
            if self.input_handler.quit_event_detected:
                self.request_shutdown()
                continue

            # Update systems
            self.state_manager.update(self.delta_time)

            # Render frame
            self.renderer.begin_frame()
            self.state_manager.render(self.renderer)
            self.ui_manager.update(self.delta_time, self.input_handler)
            self.ui_manager.render(self.renderer)
            self.platform.swap_buffers()
            
            if self.debug_manager.is_enabled:
                self.debug_manager.end_frame(clock.get_fps(), self.delta_time * 1000.0, 0.0)
        
        logger.info("Exited main engine loop.")

    def request_shutdown(self):
        logger.info("Shutdown requested.")
        self.is_running = False

    def shutdown(self):
        logger.info("--- Engine Systems Shutdown ---")
        if self.debug_manager: self.debug_manager.shutdown()
        self.skybox.shutdown()
        self.audio_engine.shutdown()
        if self.renderer: self.renderer.shutdown()
        if self.platform: self.platform.shutdown()

    def get_delta_time(self) -> float:
        return self.delta_time
```

### File: `/core/__init__.py`
```py

```

### File: `/assets/raw/shaders/volumetric_clouds_vertex.glsl`
```glsl
#version 330 core

layout (location = 0) in vec3 aPos;

// Pass-through shader for a full-screen quad.
// We only need to pass the vertex positions to the fragment shader.
out vec3 fragPos;

void main()
{
    fragPos = aPos;
	// The quad vertices are in [-1, 1] range, perfect for clip space.
    gl_Position = vec4(aPos.x, aPos.y, 0.0, 1.0);
}
```

### File: `/assets/raw/shaders/volumetric_clouds_fragment.glsl`
```glsl
#version 330 core

out vec4 FragColor;
in vec3 fragPos;

// Camera and scene uniforms
uniform mat4 inverseProjection;
uniform mat4 inverseView;
uniform vec3 cameraPos;
uniform vec3 lightDirection; // The direction *to* the sun
uniform float time;

// Cloud layer parameters
const float cloud_layer_bottom = 250.0;
const float cloud_layer_top = 400.0;
const int num_steps = 96; // Number of steps for the ray march
const float step_size = 2.0;

// --- 3D Simplex Noise Function ---
// (A standard, self-contained noise implementation is included for portability)
vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
vec4 mod289(vec4 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
vec4 permute(vec4 x) { return mod289(((x*34.0)+1.0)*x); }
vec4 taylorInvSqrt(vec4 r) { return 1.79284291400159 - 0.85373472095314 * r; }

float snoise(vec3 v) {
    const vec2 C = vec2(1.0/6.0, 1.0/3.0);
    const vec4 D = vec4(0.0, 0.5, 1.0, 2.0);
    vec3 i  = floor(v + dot(v, C.yyy));
    vec3 x0 = v - i + dot(i, C.xxx);
    vec3 g = step(x0.yzx, x0.xyz);
    vec3 l = 1.0 - g;
    vec3 i1 = min(g.xyz, l.zxy);
    vec3 i2 = max(g.xyz, l.zxy);
    vec3 x1 = x0 - i1 + C.xxx;
    vec3 x2 = x0 - i2 + C.yyy;
    vec3 x3 = x0 - D.yyy;
    i = mod289(i); 
    vec4 p = permute(permute(permute( i.z + vec4(0.0, i1.z, i2.z, 1.0)) + i.y + vec4(0.0, i1.y, i2.y, 1.0 )) + i.x + vec4(0.0, i1.x, i2.x, 1.0 ));
    float n_ = 0.142857142857;
    vec3  ns = n_ * D.wyz - D.xzx;
    vec4 j = p - 49.0 * floor(p * ns.z * ns.z);
    vec4 x_ = floor(j * ns.z);
    vec4 y_ = floor(j - 7.0 * x_);
    vec4 x = x_ *ns.x + ns.yyyy;
    vec4 y = y_ *ns.x + ns.yyyy;
    vec4 h = 1.0 - abs(x) - abs(y);
    vec4 b0 = vec4(x.xy, y.xy);
    vec4 b1 = vec4(x.zw, y.zw);
    vec4 s0 = floor(b0)*2.0 + 1.0;
    vec4 s1 = floor(b1)*2.0 + 1.0;
    vec4 sh = -step(h, vec4(0.0));
    vec4 a0 = b0.xzyw + s0.xzyw*sh.xxyy;
    vec4 a1 = b1.xzyw + s1.xzyw*sh.zzww;
    vec3 p0 = vec3(a0.xy,h.x);
    vec3 p1 = vec3(a0.zw,h.y);
    vec3 p2 = vec3(a1.xy,h.z);
    vec3 p3 = vec3(a1.zw,h.w);
    vec4 norm = taylorInvSqrt(vec4(dot(p0,p0), dot(p1,p1), dot(p2,p2), dot(p3,p3)));
    p0 *= norm.x; p1 *= norm.y; p2 *= norm.z; p3 *= norm.w;
    vec4 m = max(0.6 - vec4(dot(x0,x0), dot(x1,x1), dot(x2,x2), dot(x3,x3)), 0.0);
    m = m * m;
    return 42.0 * dot(m*m, vec4(dot(p0,x0), dot(p1,x1), dot(p2,x2), dot(p3,x3)));
}

// Function to map noise value to cloud density
float get_density(vec3 pos) {
    // Animate the noise sampling position
    pos.x += time * 5.0; 
    pos.z += time * 2.0;

    // Multiple layers (octaves) of noise for detail
    float density = snoise(pos * 0.002) * 0.6;
    density += snoise(pos * 0.008) * 0.3;
    density += snoise(pos * 0.032) * 0.1;

    // Remap noise from [-1, 1] to a usable [0, 1] density range
    density = (density + 1.0) * 0.5;

    // Use smoothstep to create soft edges at the bottom and top of the cloud layer
    float height_factor = smoothstep(cloud_layer_bottom, cloud_layer_bottom + 50.0, pos.y) *
                          (1.0 - smoothstep(cloud_layer_top - 100.0, cloud_layer_top, pos.y));
    
    return clamp(density * height_factor - 0.55, 0.0, 1.0); // -0.55 creates the cloud shapes
}


void main()
{
	// Calculate the world space direction of the ray for this fragment
	vec4 ray_clip = vec4(fragPos.xy, -1.0, 1.0);
    vec4 ray_view = inverseProjection * ray_clip;
    ray_view = vec4(ray_view.xy, -1.0, 0.0);
    vec3 ray_dir = normalize(vec3(inverseView * ray_view));

    // Find the intersection points of the ray with the cloud layer planes
    float t_bottom = (cloud_layer_bottom - cameraPos.y) / ray_dir.y;
    float t_top = (cloud_layer_top - cameraPos.y) / ray_dir.y;
    float t_enter = max(0.0, min(t_bottom, t_top));
    float t_exit = max(t_bottom, t_top);
    
    // Start raymarching from the camera if inside, or from the entry point if outside
    vec3 ray_pos = cameraPos + ray_dir * t_enter;
    float total_distance = t_exit - t_enter;

    vec4 final_color = vec4(0.0);

    for (int i = 0; i < num_steps; ++i) {
        if(ray_pos.y < cloud_layer_bottom || ray_pos.y > cloud_layer_top || final_color.a > 0.99)
            break;

        float density = get_density(ray_pos);
        
        if (density > 0.0) {
            // Simple lighting: denser parts of the cloud are brighter
            float light_factor = density * 0.8 + 0.2;
            vec3 cloud_color = vec3(0.9, 0.9, 1.0) * light_factor;
            
            // Apply transparency: new color is mixed over old based on density
            final_color.rgb += cloud_color * density * (1.0 - final_color.a);
            final_color.a += density * (1.0 - final_color.a);
        }

        // Advance the ray
        ray_pos += ray_dir * step_size * (1.0 + snoise(ray_pos * 0.1) * 0.1); // Add jitter
    }

    if (final_color.a <= 0.0) {
        discard; // No cloud here, discard fragment
    }
    
    FragColor = final_color;
}
```

### File: `/assets/raw/shaders/unlit_textured_vertex.glsl`
```glsl
#version 330 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec2 aTexCoord;

out vec2 TexCoord;

uniform mat4 model;
uniform mat4 projection;

void main()
{
    gl_Position = projection * model * vec4(aPos, 1.0);
    TexCoord = aTexCoord;
}
```

### File: `/assets/raw/shaders/unlit_textured_fragment.glsl`
```glsl
#version 330 core

out vec4 FragColor;
in vec2 TexCoord;

uniform sampler2D texture1;

void main()
{
    FragColor = texture(texture1, TexCoord);
}
```

### File: `/assets/raw/shaders/unlit_color_vertex.glsl`
```glsl
#version 330 core

layout (location = 0) in vec3 aPos;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    // FIX: Removed the 'view' matrix for correct 2D projection.
    gl_Position = projection * model * vec4(aPos, 1.0);
}
```

### File: `/assets/raw/shaders/unlit_color_fragment.glsl`
```glsl
#version 330 core

out vec4 FragColor;

uniform vec4 objectColor;

void main()
{
    FragColor = objectColor;
}
```

### File: `/assets/raw/shaders/unlit_color_3d_vertex.glsl`
```glsl
#version 330 core

layout (location = 0) in vec3 aPos;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = projection * view * model * vec4(aPos, 1.0);
}
```

### File: `/assets/raw/shaders/unlit_chunk_vertex.glsl`
```glsl
#version 330 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aColor;

out vec3 vertexColor;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = projection * view * model * vec4(aPos, 1.0);
    vertexColor = aColor;
}
```

### File: `/assets/raw/shaders/unlit_chunk_fragment.glsl`
```glsl
#version 330 core

out vec4 FragColor;

in vec3 vertexColor;

void main()
{
    FragColor = vec4(vertexColor, 1.0);
}
```

### File: `/assets/raw/shaders/ui_color_vertex.glsl`
```glsl
#version 330 core

layout (location = 0) in vec3 aPos;

// These are uniforms, constant for the entire draw call
uniform mat4 model;
uniform mat4 projection; // We don't need a view matrix for 2D UI

void main()
{
    // A simple 2D projection
    gl_Position = projection * model * vec4(aPos, 1.0);
}
```

### File: `/assets/raw/shaders/skybox_vertex.glsl`
```glsl
#version 330 core
layout (location = 0) in vec3 aPos;

out vec3 FragPos;

uniform mat4 projection;
uniform mat4 view;

void main()
{
    FragPos = aPos; 

    mat4 view_no_translation = mat4(mat3(view));
    vec4 pos = projection * view_no_translation * vec4(aPos, 1.0);

    // --- FIX: Force the z-coordinate to its maximum value. ---
    // This is a more robust method to ensure the skybox is always
    // rendered at the back of the scene, behind all other objects.
    gl_Position = pos;
    gl_Position.z = gl_Position.w;
}
```

### File: `/assets/raw/shaders/skybox_fragment.glsl`
```glsl
#version 330 core
out vec4 FragColor;

in vec3 FragPos;

uniform vec3 day_horizonColor = vec3(0.6, 0.8, 1.0);
uniform vec3 day_zenithColor = vec3(0.2, 0.4, 0.8);

uniform vec3 sunset_horizonColor = vec3(0.9, 0.6, 0.4);
uniform vec3 sunset_zenithColor = vec3(0.5, 0.3, 0.6);

uniform vec3 night_horizonColor = vec3(0.0, 0.0, 0.0);
uniform vec3 night_zenithColor = vec3(0.0, 0.0, 0.0);

uniform float sun_y_pos;
uniform float time;

float random(vec3 st) {
    return fract(sin(dot(st.xyz, vec3(12.9898,78.233,45.543))) * 43758.5453123);
}

void main()
{
    vec3 viewDir = normalize(FragPos);
    float t = viewDir.y;
    t = smoothstep(-0.2, 0.6, t);
    
    vec3 horizonColor;
    vec3 zenithColor;
    
    float sunset_factor = 1.0 - smoothstep(0.0, 300.0, sun_y_pos);
    horizonColor = mix(day_horizonColor, sunset_horizonColor, sunset_factor);
    zenithColor = mix(day_zenithColor, sunset_zenithColor, sunset_factor);
    
    float night_factor = 1.0 - smoothstep(-200.0, 0.0, sun_y_pos);
    horizonColor = mix(horizonColor, night_horizonColor, night_factor);
    zenithColor = mix(zenithColor, night_zenithColor, night_factor);

    vec3 finalColor = mix(horizonColor, zenithColor, t);
    
    if (sun_y_pos < 50.0) {
        float star_seed = random(viewDir * 200.0);
        
        if (star_seed > 0.998) {
            // --- THE FIX: Significantly slowed down the flicker speed ---
            float flicker_speed = random(viewDir * 50.0) * 0.5 + 0.25; // Much slower
            float flicker = 0.5 + 0.5 * sin(time * flicker_speed + star_seed * 100.0);
            float star_brightness = pow(flicker, 15.0) + (star_seed - 0.998) * 500.0;
            
            finalColor += vec3(star_brightness);
        }
        
        float star_alpha = 1.0 - smoothstep(-200.0, 50.0, sun_y_pos);
        finalColor *= star_alpha;
    }

    FragColor = vec4(finalColor, 1.0);
}
```

### File: `/assets/raw/shaders/post_process_vertex.glsl`
```glsl
#version 330 core
layout (location = 0) in vec3 aPos;

out vec3 TexCoords;

uniform mat4 projection;
uniform mat4 view;

void main()
{
    TexCoords = aPos;
    // Remove the translation part of the view matrix to make the skybox follow the camera
    vec4 pos = projection * mat4(mat3(view)) * vec4(aPos, 1.0);
    // Set z to w to ensure the skybox is always rendered at the far clip plane (in the background)
    gl_Position = pos.xyww;
}
```

### File: `/assets/raw/shaders/post_process_fragment.glsl`
```glsl
#version 330 core
out vec4 FragColor;

in vec2 TexCoords;

uniform sampler2D sceneTexture;

void main()
{
    // This is a simple pass-through shader for the post-processing quad.
    // Effects like grayscale, bloom, etc., would be added here.
    FragColor = texture(sceneTexture, TexCoords);
}
```

### File: `/assets/raw/shaders/lit_textured_vertex.glsl`
```glsl
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec2 aTexCoord;
layout (location = 2) in vec3 aNormal; // Added for lighting

out vec2 TexCoord;
out vec3 Normal;
out vec3 FragPos;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = projection * view * model * vec4(aPos, 1.0);
    FragPos = vec3(model * vec4(aPos, 1.0));
    Normal = mat3(transpose(inverse(model))) * aNormal;
    TexCoord = aTexCoord;
}
```

### File: `/assets/raw/shaders/lit_textured_fragment.glsl`
```glsl
#version 330 core
out vec4 FragColor;

in vec2 TexCoord;
in vec3 Normal;
in vec3 FragPos;

uniform sampler2D texture1;

// Directional Light (Sun)
uniform vec3 lightDir;
uniform vec3 lightColor;
uniform float ambientStrength;

void main()
{
    // Ambient light
    vec3 ambient = ambientStrength * lightColor;
  	
    // Diffuse light
    vec3 norm = normalize(Normal);
    vec3 lightDirection = normalize(-lightDir);
    float diff = max(dot(norm, lightDirection), 0.0);
    vec3 diffuse = diff * lightColor;
    
    vec3 result = (ambient + diffuse) * texture(texture1, TexCoord).rgb;
    FragColor = vec4(result, 1.0);
}
```

### File: `/assets/raw/shaders/lit_color_vertex.glsl`
```glsl
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aColor;   // For chunks
layout (location = 2) in vec3 aNormal;  // For chunks and entities

out vec3 FragPos;
out vec3 Normal;
out vec3 vertexColor; // Pass color to fragment shader

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = projection * view * model * vec4(aPos, 1.0);
    // Transform vertex position and normal to world space
    FragPos = vec3(model * vec4(aPos, 1.0));
    Normal = mat3(transpose(inverse(model))) * aNormal;
    vertexColor = aColor;
}
```

### File: `/assets/raw/shaders/lit_color_fragment.glsl`
```glsl
#version 330 core
out vec4 FragColor;

in vec3 Normal;
in vec3 FragPos;
in vec3 vertexColor; // Color from the mesh (for chunks)

// Uniforms passed from the renderer
uniform vec3 objectColor;    // Color for entities
uniform vec3 lightPos;       // Position of the sun/light
uniform vec3 lightColor;     // Color of the sun/light
uniform vec3 viewPos;        // Position of the camera
uniform float ambientStrength;

void main()
{
    // Ambient lighting
    vec3 ambient = ambientStrength * lightColor;

    // Diffuse lighting
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;
    
    vec3 baseColor;
    vec3 result;

    if (objectColor.r < 0.0) { // Signal to use vertex colors for chunks
        baseColor = vertexColor;
        // --- THE FIX: Use simpler lighting for blocky terrain ---
        // For terrain, ignore specular highlights to get a softer, more stylized look
        result = (ambient + diffuse) * baseColor;
    } else {
        // --- START OF DEFINITIVE FIX: Tuned specular lighting ---
        float specularStrength = 0.25;
        vec3 viewDir = normalize(viewPos - FragPos);
        vec3 reflectDir = reflect(-lightDir, norm);
        float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32); // Increased power for smaller highlight
        vec3 specular = specularStrength * spec * lightColor;
        // --- END OF DEFINITIVE FIX ---
        
        baseColor = objectColor;
        // For entities, include the specular highlight
        vec3 final_lighting = ambient + diffuse;
        result = final_lighting * baseColor + specular;
    }
    
    FragColor = vec4(result, 1.0);
}
```

### File: `/assets/raw/shaders/billboard_vertex.glsl`
```glsl
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec2 aTexCoord;

out vec2 TexCoord;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = projection * view * model * vec4(aPos, 1.0);
    TexCoord = aTexCoord;
}
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/task_viewer.py`
```py
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox, simpledialog
import re
import os
import shutil
import json

# --- Configuration & Colors ---
DOCS_ROOT = os.path.dirname(os.path.abspath(__file__))
ROADMAP_PATH = os.path.join(DOCS_ROOT, "00_PROJECT_FOUNDATION", "01_ROADMAP.md")
TODOLIST_PATH = os.path.join(DOCS_ROOT, "00_PROJECT_FOUNDATION", "todolist.json")

COLORS = {
    "bg_main": "#2b2b2b", "bg_widget": "#3c3f41", "bg_tree_header": "#45494c",
    "fg_text": "#bbbbbb", "fg_header": "#d3d3d3", "fg_link": "#8ab4f8",
    "fg_accent": "#ffcb6b", "fg_wikilink": "#80cbc4", "tree_selection": "#0d47a1",
    "code_bg": "#2e2e2e", "quote_fg": "#888888", "hr_color": "#555555",
    "task_done_icon": "#7e9d72", "task_pending_icon": "#9e9e9e"
}


class ProjectWikiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Where Giants Rust - Project IDE")
        self.geometry("1800x900")
        self.configure(bg=COLORS["bg_main"])

        # --- State Variables ---
        self.is_edit_mode = False
        self.current_viewer_path = None
        self.clipboard_path = None
        self.context_menu_target_path = None
        self.todo_data = []
        self.replace_all_mode = False

        # --- UI Construction ---
        self.setup_styles()
        self.create_main_layout()

        # --- Initialization ---
        self.create_context_menu()
        self.setup_tags()
        self.populate_file_tree()
        self.load_todolist_from_json()
        if os.path.exists(ROADMAP_PATH):
            self.load_file_content(ROADMAP_PATH, self.viewer_text)
        self.setup_bindings()

    def setup_styles(self):
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure("TFrame", background=COLORS["bg_main"])
        self.style.configure("TLabel", background=COLORS["bg_main"], foreground=COLORS["fg_header"])
        self.style.configure("TPanedwindow", background=COLORS["bg_main"], sashrelief=tk.FLAT, sashwidth=6)
        self.style.configure("TNotebook", background=COLORS["bg_main"], borderwidth=0)
        self.style.configure("TNotebook.Tab", background=COLORS["bg_widget"], foreground=COLORS["fg_text"],
                             padding=[10, 5])
        self.style.map("TNotebook.Tab", background=[("selected", COLORS["tree_selection"])],
                       foreground=[("selected", "white")])
        self.style.configure("Treeview", background=COLORS["bg_widget"], foreground=COLORS["fg_text"],
                             fieldbackground=COLORS["bg_widget"], rowheight=25)
        self.style.map("Treeview", background=[('selected', COLORS["tree_selection"])])
        self.style.configure("Treeview.Heading", background=COLORS["bg_tree_header"], foreground=COLORS["fg_header"],
                             font=('Helvetica', 10, 'bold'))
        self.style.configure("TEntry", fieldbackground=COLORS["bg_widget"], foreground=COLORS["fg_text"],
                             insertcolor=COLORS["fg_accent"])
        self.style.configure("TButton", background=COLORS["bg_widget"], foreground=COLORS["fg_text"])

    def create_main_layout(self):
        main_paned_window = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        main_paned_window.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        nav_frame = ttk.Frame(main_paned_window, width=450)
        main_paned_window.add(nav_frame, weight=1)
        self.create_navigation_widgets(nav_frame)
        todo_frame = ttk.Frame(main_paned_window, width=550)
        main_paned_window.add(todo_frame, weight=2)
        self.create_todolist_widgets(todo_frame)
        viewer_frame = ttk.Frame(main_paned_window, width=800)
        main_paned_window.add(viewer_frame, weight=3)
        self.create_viewer_widgets(viewer_frame)

    def create_navigation_widgets(self, parent_frame):
        nav_notebook = ttk.Notebook(parent_frame)
        nav_notebook.pack(fill=tk.BOTH, expand=True)
        file_tab = ttk.Frame(nav_notebook)
        search_tab = ttk.Frame(nav_notebook)
        nav_notebook.add(file_tab, text="File Browser")
        nav_notebook.add(search_tab, text="Global Search")
        self.file_tree = ttk.Treeview(file_tab, show="tree")
        self.file_tree.pack(fill=tk.BOTH, expand=True)
        self.file_tree.heading("#0", text="GDD Files", anchor='w')
        search_input_frame = ttk.Frame(search_tab)
        search_input_frame.pack(fill=tk.X, pady=5)
        self.search_entry = ttk.Entry(search_input_frame)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(search_input_frame, text="Find", command=self.on_search_button_click).pack(side=tk.LEFT, padx=5)
        self.search_results_tree = ttk.Treeview(search_tab, columns=("Context",))
        self.search_results_tree.pack(fill=tk.BOTH, expand=True)
        self.search_results_tree.heading("#0", text="File", anchor='w')
        self.search_results_tree.heading("Context", text="Line Content", anchor='w')
        self.search_results_tree.column("#0", width=150, stretch=tk.NO)
        self.search_results_tree.column("Context", width=300)

        bottom_button_frame = ttk.Frame(parent_frame)
        bottom_button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
        export_all_button = ttk.Button(bottom_button_frame, text="Export Project to .md...",
                                       command=self.export_entire_project_as_single_md)
        export_all_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        import_button = ttk.Button(bottom_button_frame, text="Import Project from .md...", command=self.import_project)
        import_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

    def create_todolist_widgets(self, parent_frame):
        ttk.Label(parent_frame, text="INTERACTIVE TASK LIST", font=("Helvetica", 14, "bold")).pack(pady=(5, 10))
        self.todo_text = scrolledtext.ScrolledText(parent_frame, wrap=tk.WORD, bg=COLORS["bg_widget"],
                                                   fg=COLORS["fg_text"], relief=tk.FLAT, borderwidth=5,
                                                   insertbackground=COLORS["fg_accent"], insertwidth=0)
        self.todo_text.pack(fill=tk.BOTH, expand=True)

    def create_viewer_widgets(self, parent_frame):
        header_frame = ttk.Frame(parent_frame)
        header_frame.pack(fill=tk.X, pady=(5, 10))
        self.viewer_label = ttk.Label(header_frame, text="CONTENT VIEWER", font=("Helvetica", 14, "bold"))
        self.viewer_label.pack(side=tk.LEFT)
        self.edit_button = ttk.Button(header_frame, text="Enter Edit Mode", command=self.toggle_edit_mode)
        self.edit_button.pack(side=tk.RIGHT)
        self.save_button = ttk.Button(header_frame, text="Save Changes", command=self.save_current_file)
        self.viewer_text = scrolledtext.ScrolledText(parent_frame, wrap=tk.WORD, font=("Segoe UI", 11),
                                                     bg=COLORS["bg_widget"], fg=COLORS["fg_text"], relief=tk.FLAT,
                                                     borderwidth=5, insertwidth=0)
        self.viewer_text.pack(fill=tk.BOTH, expand=True)

    def create_context_menu(self):
        self.context_menu = tk.Menu(self, tearoff=0, bg=COLORS["bg_widget"], fg=COLORS["fg_text"])
        self.context_menu.add_command(label="Create File...", command=self.create_file)
        self.context_menu.add_command(label="Create Folder...", command=self.create_folder)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Copy", command=self.copy_item)
        self.context_menu.add_command(label="Paste", command=self.paste_item, state=tk.DISABLED)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Delete", command=self.delete_item)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Export Folder to single .md...", command=self.export_folder_as_single_md)

    def setup_tags(self):
        self.viewer_text.tag_configure('h1', font=('Cinzel', 18, 'bold'), foreground=COLORS["fg_header"], spacing3=15)
        self.viewer_text.tag_configure('h2', font=('Cinzel', 14, 'bold'), foreground=COLORS["fg_header"], spacing1=10,
                                       spacing3=5)
        self.viewer_text.tag_configure('h3', font=('Cinzel', 12, 'italic'), lmargin1=10, spacing1=5,
                                       foreground=COLORS["fg_link"])
        self.viewer_text.tag_configure('bold_keyword', font=('Segoe UI', 11, 'bold'), foreground=COLORS["fg_accent"])
        self.viewer_text.tag_configure('bold', font=('Segoe UI', 11, 'bold'))
        self.viewer_text.tag_configure('italic', font=('Segoe UI', 11, 'italic'))
        self.viewer_text.tag_configure('list', lmargin1=20, lmargin2=20, font=("Segoe UI", 11))
        self.viewer_text.tag_configure('hr', overstrike=True, spacing1=15, spacing3=15, foreground=COLORS["hr_color"])
        self.viewer_text.tag_configure('wiki_link', font=('Segoe UI', 11, 'bold'), foreground=COLORS["fg_wikilink"],
                                       underline=True)
        self.viewer_text.tag_bind("wiki_link", "<Enter>", lambda e: self.viewer_text.config(cursor="hand2"))
        self.viewer_text.tag_bind("wiki_link", "<Leave>", lambda e: self.viewer_text.config(cursor=""))

        self.todo_text.tag_configure('h2', font=('Cinzel', 12, 'bold'), foreground=COLORS["fg_header"], spacing1=15,
                                     spacing3=5, justify='center')
        self.todo_text.tag_configure('h4_link', font=('Consolas', 12, 'bold'), foreground=COLORS["fg_link"],
                                     underline=True)
        self.todo_text.tag_bind("h4_link", "<Enter>", lambda e: self.todo_text.config(cursor="hand2"))
        self.todo_text.tag_bind("h4_link", "<Leave>", lambda e: self.todo_text.config(cursor=""))
        self.todo_text.tag_configure('task_pending', lmargin1=15, font=("Segoe UI", 11))
        self.todo_text.tag_configure('task_done', lmargin1=15, overstrike=True, foreground="#888888",
                                     font=("Segoe UI", 11))
        self.todo_text.tag_configure('task_pending_icon', foreground=COLORS["task_pending_icon"])
        self.todo_text.tag_configure('task_done_icon', foreground=COLORS["task_done_icon"])
        self.todo_text.tag_configure('hr', overstrike=True, spacing1=15, spacing3=15, foreground=COLORS["hr_color"])

    def generate_file_tree_string(self, start_path):
        tree_lines = []
        base_name = os.path.basename(os.path.normpath(start_path))
        tree_lines.append(f"{base_name}/")

        def _walk(directory, prefix=""):
            ignore_list = ['.git', '__pycache__', '.idea', '.vscode']
            try:
                all_items = sorted([f for f in os.listdir(directory) if f not in ignore_list])
            except FileNotFoundError:
                return

            filtered_items = [item for item in all_items if
                              os.path.isdir(os.path.join(directory, item)) or item.endswith((".md", ".txt", ".json"))]
            pointers = ['├── '] * (len(filtered_items) - 1) + ['└── ']
            for pointer, path in zip(pointers, filtered_items):
                full_path = os.path.join(directory, path)
                is_dir = os.path.isdir(full_path)
                tree_lines.append(prefix + pointer + path + ('/' if is_dir else ''))
                if is_dir:
                    extension = '│   ' if pointer == '├── ' else '    '
                    _walk(full_path, prefix + extension)

        _walk(start_path)
        return "\n".join(tree_lines)

    def _perform_single_file_export(self, source_folder, export_file_path):
        try:
            with open(export_file_path, 'w', encoding='utf-8') as export_file:
                folder_name = os.path.basename(os.path.normpath(source_folder))
                export_file.write(f"# Project Export: {folder_name}\n")

                tree_string = self.generate_file_tree_string(source_folder)
                export_file.write("\n\n--- FOLDER STRUCTURE ---\n\n")
                export_file.write("```\n")
                export_file.write(tree_string)
                export_file.write("\n```\n")

                for root, dirs, files in sorted(os.walk(source_folder)):
                    if '.git' in dirs: dirs.remove('.git')
                    dirs.sort()
                    files.sort()
                    for file in files:
                        if file.endswith((".md", ".txt", ".json")):
                            full_path = os.path.join(root, file)
                            relative_path = os.path.relpath(full_path, source_folder)
                            export_file.write(f"\n\n--- START OF FILE {relative_path.replace(os.sep, '/')} ---\n\n")
                            with open(full_path, 'r', encoding='utf-8') as content_file:
                                export_file.write(content_file.read())
                            export_file.write(f"\n\n--- END OF FILE {relative_path.replace(os.sep, '/')} ---\n")

            messagebox.showinfo("Export Complete", f"Project content successfully exported to:\n{export_file_path}")
        except Exception as e:
            messagebox.showerror("Export Error", f"An error occurred during export:\n{e}")

    def export_entire_project_as_single_md(self):
        export_file_path = filedialog.asksaveasfilename(
            title="Export Entire Project to Single .md File",
            defaultextension=".md",
            filetypes=[("Markdown Export File", "*.md")]
        )
        if export_file_path:
            self._perform_single_file_export(DOCS_ROOT, export_file_path)

    def export_folder_as_single_md(self):
        source_folder = self.get_context_path()
        if not os.path.isdir(source_folder):
            messagebox.showwarning("Export Warning", "Please right-click on a folder to export.")
            return

        export_file_path = filedialog.asksaveasfilename(
            title=f"Export Folder '{os.path.basename(source_folder)}' to .md",
            defaultextension=".md",
            filetypes=[("Markdown Export File", "*.md")]
        )
        if export_file_path:
            self._perform_single_file_export(source_folder, export_file_path)

    def import_project(self):
        import_file_path = filedialog.askopenfilename(
            title="Select Project Export File",
            filetypes=[("Markdown Export File", "*.md")]
        )
        if not import_file_path: return

        target_folder = filedialog.askdirectory(
            title="Select Destination Folder to Import Project Into",
            initialdir=os.path.dirname(DOCS_ROOT)
        )
        if not target_folder: return

        self.replace_all_mode = False
        try:
            with open(import_file_path, 'r', encoding='utf-8') as import_file:
                content = import_file.read()

            file_pattern = re.compile(r"--- START OF FILE (.+?) ---\n\n(.*?)\n\n--- END OF FILE \1 ---", re.DOTALL)
            files_to_create = file_pattern.findall(content)

            if not files_to_create:
                messagebox.showerror("Import Error", "No valid file blocks found in the selected file.");
                return

            for rel_path_str, file_content in files_to_create:
                destination_path = os.path.join(target_folder, os.path.normpath(rel_path_str))

                if os.path.exists(destination_path) and not self.replace_all_mode:
                    dialog_result = self.show_conflict_dialog(destination_path)
                    if dialog_result == "cancel":
                        messagebox.showwarning("Import Canceled", "Import operation was canceled.");
                        return
                    elif dialog_result == "replace_all":
                        self.replace_all_mode = True
                    elif dialog_result == "skip":
                        continue

                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                with open(destination_path, 'w', encoding='utf-8') as out_file:
                    out_file.write(file_content)

            messagebox.showinfo("Import Complete", f"Successfully imported {len(files_to_create)} files.");
            self.populate_file_tree()
        except Exception as e:
            messagebox.showerror("Import Error", f"An error occurred during import:\n{e}")

    def show_conflict_dialog(self, file_path):
        dialog = tk.Toplevel(self)
        dialog.title("File Conflict")
        dialog.transient(self)
        dialog.grab_set()
        dialog.geometry("500x150")
        dialog.configure(bg=COLORS["bg_main"])

        tk.Label(dialog, text=f"File already exists:\n{os.path.relpath(file_path)}", fg=COLORS["fg_header"],
                 bg=COLORS["bg_main"], font=("Helvetica", 10)).pack(pady=10)

        result = {"value": "skip"}

        def set_result(value):
            result["value"] = value
            dialog.destroy()

        button_frame = tk.Frame(dialog, bg=COLORS["bg_main"])
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Replace", command=lambda: set_result("replace")).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Replace All", command=lambda: set_result("replace_all")).pack(side=tk.LEFT,
                                                                                                     padx=5)
        ttk.Button(button_frame, text="Skip", command=lambda: set_result("skip")).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel Import", command=lambda: set_result("cancel")).pack(side=tk.LEFT, padx=5)

        self.wait_window(dialog)
        return result["value"]

    def populate_file_tree(self):
        for i in self.file_tree.get_children(): self.file_tree.delete(i)
        nodes = {'': ''}
        for root, dirs, files in os.walk(DOCS_ROOT):
            if '.git' in dirs: dirs.remove('.git')
            dirs.sort()
            files.sort()
            rel_path = os.path.relpath(root, DOCS_ROOT)
            parent_id = nodes.get(os.path.dirname(rel_path), "") if rel_path != "." else ""
            if rel_path != ".":
                nodes[rel_path] = self.file_tree.insert(parent_id, 'end', text=os.path.basename(root), open=True,
                                                        values=[root])
            for file in files:
                if file.endswith((".md", ".txt", ".json")):
                    self.file_tree.insert(nodes.get(rel_path, ""), 'end', text=file, values=[os.path.join(root, file)])

    def on_file_tree_select(self, event):
        selected_item = self.file_tree.focus()
        if not selected_item: return
        item_values = self.file_tree.item(selected_item, 'values')
        if not item_values: return
        file_path = item_values[0]
        if file_path and os.path.isfile(file_path):
            self.load_file_content(file_path, self.viewer_text)

    def load_todolist_from_json(self):
        try:
            with open(TODOLIST_PATH, 'r', encoding='utf-8') as f:
                self.todo_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.todo_data = []
        self.display_todolist()

    def display_todolist(self):
        self.todo_text.config(state=tk.NORMAL)
        self.todo_text.delete("1.0", tk.END)
        if not self.todo_data:
            self.todo_text.insert(tk.END, "Could not load todolist.json.\nCheck if file exists and is valid.", 'h2')
        else:
            for p_idx, phase in enumerate(self.todo_data):
                self.todo_text.insert(tk.END, phase.get("phase", "Unknown Phase") + '\n', 'h2')
                for m_idx, milestone in enumerate(phase.get("milestones", [])):
                    milestone_name = f"{milestone.get('id', '')} :: {milestone.get('name', '')}"
                    self.todo_text.insert(tk.END, milestone_name + '\n', 'h4_link')
                    for t_idx, task in enumerate(milestone.get("tasks", [])):
                        task_tag = f"task-{p_idx}-{m_idx}-{t_idx}"
                        icon, style = ("✔ ", 'task_done') if task.get("completed") else ("☐ ", 'task_pending')
                        icon_tag = style + '_icon'
                        self.todo_text.insert(tk.END, icon, (icon_tag, task_tag))
                        self.todo_text.insert(tk.END, task.get("description", "") + '\n', (style, task_tag))
                self.todo_text.insert(tk.END, '\n' + '─' * 50 + '\n\n', 'hr')
        self.todo_text.config(state=tk.DISABLED)

    def load_file_content(self, file_path, widget):
        self.toggle_edit_mode(force_off=True)
        self.current_viewer_path = file_path if widget == self.viewer_text else None
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            self.parse_and_display_content(widget, content)
            if widget == self.viewer_text:
                self.viewer_label.config(text=f"VIEWING: {os.path.relpath(file_path, DOCS_ROOT)}")
        except Exception as e:
            widget.config(state=tk.NORMAL)
            widget.delete("1.0", tk.END)
            widget.insert(tk.END, f"Error loading file:\n{file_path}\n\n{e}")
            widget.config(state=tk.DISABLED)

    def parse_and_display_content(self, widget, content):
        widget.config(state=tk.NORMAL)
        widget.delete("1.0", tk.END)
        inline_pattern = re.compile(r'(\[\[.*?\]\]|\*\*.*?\*\*|\*.*?\*|`.*?`)')
        for line in content.split('\n'):
            stripped_line = line.strip()
            if stripped_line == '---': widget.insert(tk.END, ' ' * 80 + '\n', 'hr'); continue
            if stripped_line.startswith('# '): widget.insert(tk.END, stripped_line[2:] + '\n', 'h1'); continue
            if stripped_line.startswith('## '): widget.insert(tk.END, stripped_line[3:] + '\n', 'h2'); continue
            if stripped_line.startswith('### '): widget.insert(tk.END, stripped_line[4:] + '\n', 'h3'); continue
            if stripped_line.startswith(('- ', '* ')):
                parts = inline_pattern.split(stripped_line[2:])
                widget.insert(tk.END, "  • ")
            else:
                parts = inline_pattern.split(line)
            for part in parts:
                if not part: continue
                if part.startswith('**') and part.endswith('**'):
                    tag = 'bold_keyword' if ':' in part else 'bold'
                    widget.insert(tk.END, part[2:-2], tag)
                elif part.startswith('*') and part.endswith('*'):
                    widget.insert(tk.END, part[1:-1], 'italic')
                elif part.startswith('`') and part.endswith('`'):
                    widget.insert(tk.END, part[1:-1], 'code')
                elif part.startswith('[[') and part.endswith(']]'):
                    widget.insert(tk.END, part[2:-2], 'wiki_link')
                else:
                    widget.insert(tk.END, part)
            widget.insert(tk.END, '\n')
        widget.config(state=tk.DISABLED)

    def toggle_edit_mode(self, force_off=False):
        if force_off or self.is_edit_mode:
            self.is_edit_mode = False
            self.viewer_text.config(insertwidth=0)
            self.save_button.pack_forget()
            self.edit_button.pack(side=tk.RIGHT)
            content = self.viewer_text.get("1.0", tk.END)
            self.parse_and_display_content(self.viewer_text, content)
        else:
            self.is_edit_mode = True
            self.viewer_text.config(state=tk.NORMAL, insertwidth=2)
            for tag in self.viewer_text.tag_names():
                self.viewer_text.tag_remove(tag, "1.0", tk.END)
            self.edit_button.pack_forget()
            self.save_button.pack(side=tk.RIGHT)

    def save_current_file(self):
        if self.current_viewer_path and self.is_edit_mode:
            try:
                content = self.viewer_text.get("1.0", tk.END).strip()
                with open(self.current_viewer_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.toggle_edit_mode(force_off=True)
            except Exception as e:
                messagebox.showerror("Save Error", f"Could not save file:\n{self.current_viewer_path}\n\n{e}")

    # --- THIS IS THE METHOD THAT WAS MISSING ---
    def show_context_menu(self, event):
        iid = self.file_tree.identify_row(event.y)
        if iid:
            self.file_tree.selection_set(iid)
            self.context_menu_target_path = self.file_tree.item(iid, 'values')[0]
            self.context_menu.entryconfig("Paste", state=tk.NORMAL if self.clipboard_path else tk.DISABLED)
            self.context_menu.post(event.x_root, event.y_root)

    def on_task_toggle(self, event):
        indexx = self.todo_text.indexx(f"@{event.x},{event.y}")
        tags = self.todo_text.tag_names(indexx)
        task_tag = next((t for t in tags if t.startswith('task-')), None)
        if task_tag:
            try:
                _, p_idx, m_idx, t_idx = map(int, task_tag.split('-'))
                task = self.todo_data[p_idx]['milestones'][m_idx]['tasks'][t_idx]
                task['completed'] = not task['completed']
                self.save_todolist_to_json()
                self.display_todolist()
            except (ValueError, IndexError) as e:
                print(f"Error toggling task: {e}")

    def save_todolist_to_json(self):
        try:
            with open(TODOLIST_PATH, 'w', encoding='utf-8') as f:
                json.dump(self.todo_data, f, indexnt=2)
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save to-do list to JSON file:\n{e}")

    def setup_bindings(self):
        self.file_tree.bind("<<TreeviewSelect>>", self.on_file_tree_select)
        self.file_tree.bind("<Button-3>", self.show_context_menu)
        self.todo_text.bind("<Button-1>", self.on_task_toggle)
        self.todo_text.tag_bind('h4_link', '<Button-1>', lambda e: self.on_link_click(e, self.todo_text))
        self.viewer_text.tag_bind('wiki_link', '<Button-1>', lambda e: self.on_link_click(e, self.viewer_text))
        self.search_entry.bind("<Return>", self.on_search_button_click)
        self.search_results_tree.bind("<<TreeviewSelect>>", self.on_search_result_select)

    def get_context_path(self, for_creation=False):
        path = self.context_menu_target_path
        if not path: return DOCS_ROOT
        return os.path.dirname(path) if for_creation and os.path.isfile(path) else path

    def on_search_button_click(self, event=None):
        search_term = self.search_entry.get()
        if search_term: self.perform_search(search_term)

    def on_link_click(self, event, widget):
        indexx = widget.indexx(f"@{event.x},{event.y}")
        tags = widget.tag_names(indexx)
        if 'h4_link' in tags:
            line = self.todo_text.get(f"{indexx} linestart", f"{indexx} lineend")
            match = re.search(r'(\[M-\d+\])', line)
            if match:
                self.load_file_content(ROADMAP_PATH, self.viewer_text)
                self.after(50, lambda: self.viewer_text.see(self.find_tag_in_widget(self.viewer_text, match.group(1))))
        elif 'wiki_link' in tags:
            tag_range = widget.tag_prevrange('wiki_link', indexx)
            link_text = widget.get(tag_range[0], tag_range[1]).replace('\\', '/')
            self.load_file_content_by_name(link_text.strip())

    def find_tag_in_widget(self, widget, text_to_find):
        return widget.search(text_to_find, "1.0", stopindexx=tk.END)

    def load_file_content_by_name(self, filename):
        for root, dirs, files in os.walk(DOCS_ROOT):
            if filename in files:
                self.load_file_content(os.path.join(root, filename), self.viewer_text)
                return
        messagebox.showwarning("Link Error", f"Could not find file '{filename}' in project.")

    def on_search_result_select(self, event):
        selected_item = self.search_results_tree.focus()
        if not selected_item: return
        values = self.search_results_tree.item(selected_item, 'values')
        if len(values) < 3 or not values[0]: return
        file_path, line_num, _ = values
        self.load_file_content(file_path, self.viewer_text)
        self.after(50, lambda: self.highlight_line(int(line_num)))

    def perform_search(self, search_term):
        self.search_results_tree.delete(*self.search_results_tree.get_children())
        results_found = False
        for root, dirs, files in os.walk(DOCS_ROOT):
            if '.git' in dirs: dirs.remove('.git')
            for file in files:
                if file.endswith((".md", ".txt")):
                    full_path = os.path.join(root, file)
                    try:
                        with open(full_path, 'r', encoding='utf-8') as f:
                            for i, line in enumerate(f):
                                if search_term.lower() in line.lower():
                                    results_found = True
                                    filename = os.path.basename(full_path)
                                    context = line.strip()
                                    self.search_results_tree.insert('', 'end', text=filename,
                                                                    values=(full_path, i + 1, context))
                                    self.search_results_tree.set(self.search_results_tree.get_children()[-1], "Context",
                                                                 context)
                    except Exception:
                        continue
        if not results_found:
            self.search_results_tree.insert('', 'end', text="No results found.", values=("", -1, ""))

    def highlight_line(self, line_num):
        self.viewer_text.tag_remove("highlight", "1.0", tk.END)
        indexx = f"{line_num}.0"
        self.viewer_text.see(indexx)
        self.viewer_text.tag_add("highlight", indexx, f"{indexx} lineend")
        self.viewer_text.tag_configure("highlight", background=COLORS["fg_accent"], foreground=COLORS["bg_widget"])
        self.after(3000, lambda: self.viewer_text.tag_remove("highlight", "1.0", tk.END))

    def create_file(self):
        target_dir = self.get_context_path(for_creation=True)
        filename = simpledialog.askstring("Create File", "Enter new filename (.md):", parent=self)
        if not filename: return
        if not filename.endswith('.md'): filename += '.md'
        new_path = os.path.join(target_dir, filename)
        if os.path.exists(new_path): messagebox.showerror("Error", "A file with that name already exists."); return
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(f"# {filename.replace('.md', '')}\n\n")
        self.populate_file_tree()

    def create_folder(self):
        target_dir = self.get_context_path(for_creation=True)
        foldername = simpledialog.askstring("Create Folder", "Enter new folder name:", parent=self)
        if not foldername: return
        new_path = os.path.join(target_dir, foldername)
        if os.path.exists(new_path): messagebox.showerror("Error", "A folder with that name already exists."); return
        os.makedirs(new_path)
        self.populate_file_tree()

    def copy_item(self):
        self.clipboard_path = self.get_context_path()

    def paste_item(self):
        if not self.clipboard_path: return
        destination_dir = self.get_context_path(for_creation=True)
        base_name = os.path.basename(self.clipboard_path)
        new_path = os.path.join(destination_dir, base_name)
        if os.path.exists(new_path):
            if messagebox.askyesno("Conflict", f"'{base_name}' already exists. Overwrite?"):
                if os.path.isdir(new_path):
                    shutil.rmtree(new_path)
                else:
                    os.remove(new_path)
            else:
                return
        try:
            if os.path.isdir(self.clipboard_path):
                shutil.copytree(self.clipboard_path, new_path)
            else:
                shutil.copy2(self.clipboard_path, new_path)
            self.populate_file_tree()
        except Exception as e:
            messagebox.showerror("Paste Error", f"Could not paste item.\n\n{e}")

    def delete_item(self):
        path_to_delete = self.get_context_path()
        if path_to_delete == DOCS_ROOT: messagebox.showwarning("Warning",
                                                               "Cannot delete the root project directory."); return
        item_name = os.path.basename(path_to_delete)
        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to permanently delete\n'{item_name}'?"):
            try:
                if os.path.isdir(path_to_delete):
                    shutil.rmtree(path_to_delete)
                else:
                    os.remove(path_to_delete)
                self.populate_file_tree()
            except Exception as e:
                messagebox.showerror("Delete Error", f"Could not delete item.\n\n{e}")


if __name__ == "__main__":
    app = ProjectWikiApp()
    app.mainloop()
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/06_TECHNICAL_AND_PRODUCTION/04_Modding_Support_Plan.md`
```md

```

### File: `/TOP_SECRET_GAME_DEV_DOCS/06_TECHNICAL_AND_PRODUCTION/03_Testing_and_QA_Strategy.md`
```md

```

### File: `/TOP_SECRET_GAME_DEV_DOCS/06_TECHNICAL_AND_PRODUCTION/02_Build_and_Release_Process.md`
```md

```

### File: `/TOP_SECRET_GAME_DEV_DOCS/06_TECHNICAL_AND_PRODUCTION/01a_LLM_Integration_Framework.md`
```md
# Technical Design: LLM Integration Framework

## **1.0. Core Philosophy: The AI as a Development Partner**

The Stelliferrum Forge is being architected with Large Language Model (LLM) integration as a core design consideration. The goal is to leverage AI as a powerful tool for content generation, allowing a small, agile team to create a world of vast scale and depth. The LLM is not a replacement for human creativity, but a "force multiplier" that handles the structured, data-driven aspects of content creation, freeing the human developer to focus on vision, systems, and final polish.

This framework is built on two pillars: **Data-Driven Architecture** and a **Human-in-the-Loop Validation Process.**

## **2.0. Pillar 1: Data-Driven Architecture (The "Beefy Foundation")**

The engine is designed so that as much content as possible is defined in simple, human-readable data files (like JSON or XML), rather than being hard-coded. This is the foundation that allows an LLM to easily generate content that the engine can immediately understand and use.

*   **Item Generation:** All items (weapons, armor, consumables) are defined in a structured format.
    *   **Example `new_sword.json`:**
        ```json
        {
          "itemID": "WEAP_SteelSword_Sunken",
          "itemName": "The Sunken Blade",
          "itemType": "One-Handed Sword",
          "baseDamage": 24,
          "weight": 8.5,
          "description": "A steel sword, strangely immune to rust, recovered from a shipwreck. It hums with a faint, sorrowful energy.",
          "enchantment": "ENCH_WaterBreathing_Minor"
        }
        ```
    *   An LLM can be prompted to generate hundreds of these files based on a template, creating a vast loot table instantly.

*   **Quest Design:** Quest logic is broken down into modular objectives defined in a data file.
    *   **Example `quest_lost_miner.json`:**
        ```json
        {
          "questID": "Q_LostMiner01",
          "questTitle": "The Echoes in the Dark",
          "giver": "NPC_DwarvenForeman_Brom",
          "dialogue_start": "My youngest apprentice, Finn, went into the old crystal caves and hasn't returned. The echoes... they play tricks on the mind. Please find him.",
          "objectives": [
            { "type": "GOTO", "target": "LOC_CrystalCave_Entrance" },
            { "type": "FIND", "target": "ITEM_Finns_Pickaxe" },
            { "type": "REPORT_TO", "target": "NPC_DwarvenForeman_Brom" }
          ],
          "reward": { "type": "ITEM", "itemID": "WEAP_DwarvenPickaxe_Pristine" }
        }
        ```
    *   An LLM can generate the structure for hundreds of side quests, including thematic dialogue and logical objective chains.

## **3.0. Pillar 2: The Validation Process (The "Checks")**

This is the critical quality control system that ensures LLM-generated content is functional, balanced, and lore-consistent. It is a two-step process.

*   **Step 1: The Automated Sanity-Check**
    *   When new data files are added to the project, an automated script runs to validate their structure and format. This is the first line of defense against LLM "hallucinations."
    *   **Checks Performed:**
        *   **Schema Validation:** Does the generated JSON/XML match the required template? Are all necessary fields present?
        *   **ID Cross-Reference:** Does the `itemID` or `questID` already exist? Does the `target` NPC in a quest actually exist in the NPC database?
        *   **Value Range Check:** Is the `baseDamage` for a "Tier 1" weapon within the acceptable range? Or did the LLM generate a wooden club that does 9000 damage?
    *   Any file that fails this check is flagged for immediate human review.

*   **Step 2: The Human-in-the-Loop Review**
    *   The developer is the ultimate arbiter of quality. The LLM generates the *draft*, and the human provides the *polish*.
    *   **Review Process:** The developer loads the validated assets into a special "curation" build of the engine.
    *   **Checks Performed:**
        *   **Lore Consistency:** Does the `description` for "The Sunken Blade" fit with the established lore of the region it's found in?
        *   **Tonal Cohesion:** Does the dialogue written for the Dwarven foreman sound like a dwarf, or did the LLM make him sound like a Shakespearean poet?
        *   **Game Balance:** Is this new weapon wildly overpowered or underpowered compared to other items at its tier?
        *   **Creative Polish:** The developer can now make small tweaks to the generated text to add nuance, foreshadowing, and personality that an LLM might miss.

This robust framework allows us to leverage the speed and scale of AI content generation while ensuring that the final product is polished, coherent, and curated by a guiding human vision.

```

### File: `/TOP_SECRET_GAME_DEV_DOCS/06_TECHNICAL_AND_PRODUCTION/01_Asset_Creation_Pipeline.md`
```md

```

### File: `/TOP_SECRET_GAME_DEV_DOCS/05_USER_EXPERIENCE/01_UX_Design_Philosophy.md`
```md
# UX Design Philosophy: Clarity Amidst Chaos

The User Experience (UX) and User Interface (UI) of *Where Giants Rust* must serve one primary goal: to provide the player with all the critical information they need to make strategic decisions, without cluttering the screen or breaking immersion. The world is complex and dangerous; the interface must be a clean, reliable window into that world.

### 1. Diegetic & Integrated UI
Whenever possible, UI elements should feel like they are part of the game world or a natural extension of the player's gear.
*   **The APU:** The player's Arm-mounted Processing Unit (where the AI is housed) is the in-universe justification for the HUD. Health, stamina, and status effects are presented as biometric readouts. The compass is a holographic projection.
*   **Physical Interaction:** Instead of complex UI menus, many interactions are physical. Reading a schematic is done by looking at the item. Managing a base's power grid is done by physically interacting with a generator and conduits.

### 2. Information on Demand
The screen should be kept as clean as possible during exploration. Detailed information should be available, but only when the player requests it.
*   **Minimalist HUD:** The standard HUD is minimal, showing only the vital resource bars and a compass. More detailed info (active effects, ammo count) fades in contextually (e.g., when entering combat or drawing a weapon).
*   **The Scanner:** The A.R.I.A. scanner is the primary tool for "Information on Demand." The player must actively choose to scan an enemy to see its level and resistances, or scan a plant to learn its properties. This makes information-gathering an active, immersive gameplay mechanic.

### 3. Clear Feedback
Every player action and every change in the game state must be communicated clearly through visual, auditory, and haptic feedback.
*   A perfectly timed block has a sharp, distinct sound and visual effect.
*   Taking damage is a clear jolt to the screen with a directional indicator.
*   A status effect icon should be unambiguous and easily understood.
*   The "thwack" of an axe on wood should feel different from the "clink" of a pickaxe on stone.

### 4. Accessibility & Customization
While we have a clear artistic vision for the UI, players must have control.
*   All HUD elements should be individually scalable and movable.
*   Colorblind modes must be supported.
*   All key-bindings must be fully remappable.
*   Subtitles should be clear, with options for size and background opacity.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/05_USER_EXPERIENCE/03_AUDIO/02_Music_Design.md`
```md
# Audio Design: Music

## 1.0. Core Philosophy: The Somber Tapestry
The music in *Where Giants Rust* is a rare and powerful tool used to enhance emotion, not to fill silence. Much of the game will be spent in the quiet ambience of the world. When music does appear, it must be purposeful and impactful. The score is a blend of two opposing aesthetics: lonely, organic instrumentation (cello, piano, sparse strings) to represent the fallen, beautiful world, and cold, droning electronic synths to represent the creeping, alien nature of The Static and lost technology.

## 2.0. The Dynamic Adaptive Music System
The core of the music system is its ability to adapt to the player's current situation. Music is constructed in layers that are faded in and out seamlessly.

*   **Layer 1: Exploration**
    *   **When:** Active when the player is simply exploring a biome.
    *   **Style:** Minimalist and atmospheric. Often a single, lonely instrument (a cello in the forest, a sparse piano in the mountains, a flute in the grasslands) playing a memorable, somber theme. The key changes depending on the biome to give each region its own musical identity.

*   **Layer 2: Tension**
    *   **When:** Triggered when a player enters stealth and an enemy is "Alerted" but not yet hunting.
    *   **Style:** A low, pulsing synthesizer bassline or a quiet, dissonant string drone is layered *underneath* the Exploration track. It doesn't replace it, but adds a sense of unease and warning.

*   **Layer 3: Combat**
    *   **When:** Triggered when the player enters the "Hunting" state.
    *   **Style:** The Exploration and Tension layers are replaced by a full, dynamic combat track. This introduces powerful, percussive elements (deep, echoing drums) and driving, rhythmic strings or synths. The intensity of the combat track will vary based on the number and type of enemies.

## 3.0. Thematic & Narrative Music
In addition to the dynamic system, specific, handcrafted musical cues will be used for key moments to maximize narrative impact.

*   **Main Theme:** A powerful, melancholic theme that combines both orchestral and synthetic elements, played over the Main Menu.
*   **"Awe" Cues:** Short, breathtaking musical stings that play when the player discovers a place of immense scale or beauty, like seeing the Titan's Graveyard for the first time, or the summit of a mountain at sunrise.
*   **Faction Themes:** Major friendly settlements or faction hubs (like a Dwarven hold) will have their own unique, non-dynamic theme music that helps to establish their cultural identity.
*   **Boss Themes:** Every major story boss and divine avatar will have its own unique, epic, multi-phase combat theme composed specifically for that encounter.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/05_USER_EXPERIENCE/03_AUDIO/01_Sound_Effects_Design.md`
```md
# Audio Design: Acoustic Mass & Material Resonance

## **1.0. Core Philosophy: Sound with Substance**

The audio system of the Stelliferrum Forge is a direct extension of the engine's core principle: **everything has weight.** In our world, sound is not an abstract event triggered at a location. It is a physical phenomenon simulated with mass, velocity, and material interaction. This creates a deeply immersive and physically-grounded 3D audio-scape that we call **Material Resonance**.

## **2.0. The "Phonon" System**

At the heart of our audio engine is the concept of the **Phonon**. A Phonon is a massless particle that carries a quantifiable `acoustic_mass`.

1.  **Generation:** Any sound-producing event (a footstep, a sword swing, a raindrop) generates a burst of these Phonons at its point of origin. The `source_mass` of these Phonons is determined by the event itself (e.g., a giant's footstep has a much higher `source_mass` than a rabbit's).
2.  **Travel & Attenuation:** Phonons travel outwards from their source. As they travel through the air, their `acoustic_mass` decays over distance. This is how we simulate volume falloff naturally.
3.  **Impact & Resonance:** A sound is only produced when a Phonon **collides with a physical object** in the game world. The resulting sound's `volume` and `pitch` are a direct calculation of the Phonon's remaining `acoustic_mass` and the `material_density` of the object it struck.

**Formula Concept:** `Final_Sound = f(Phonon_Acoustic_Mass, Surface_Material_Density)`

## **3.0. The Sound of Materials**

This system makes the environment the primary instrument of the soundscape.

*   **High-Density Surfaces (Metal, Stone):** When a Phonon strikes a dense surface, it produces a **low-pitch, high-volume** sound with a long decay (reverb). This is why a heavy footstep *clangs* loudly in a stone hallway.
*   **Low-Density Surfaces (Dirt, Wood, Cloth):** When a Phonon strikes a soft surface, it produces a **high-pitch, low-volume** sound with a short decay. This is why the same footstep *thuds* quietly on a dirt path.
*   **The Rain Example (Perfected):**
    *   A single "Raindrop" event generates a Phonon with a very small `acoustic_mass`.
    *   If that Phonon hits a **leaf** (low density), it generates a soft, high-pitched `pitter` sound.
    *   If it hits a **puddle of mud** (medium density, high dampening), it generates a muted, mid-range `splat`.
    *   If it hits the player's **steel helmet** (high density), it generates a sharp, loud `tink!`.
    *   This allows a rainstorm to become a dynamic, complex orchestra of thousands of tiny, physically-simulated impacts, creating an unparalleled sense of immersion.

## **4.0. Player-Generated Sound**

The player's gear directly influences their "sound weight."

*   **Footsteps:** The `acoustic_mass` of a footstep is a calculation of `(Player_Weight + Gear_Weight) * Movement_Speed`. A heavily-armored character sprinting will generate massive Phonons, making them audible from a great distance. A lightly armored character sneaking generates tiny Phonons, making them nearly silent.
*   **Weapon Swings:** A heavy warhammer will generate a deep, powerful `whoosh` Phonon, while a dagger will generate a faint, sharp `swish`.

This system turns sound design from a simple list of `.wav` files into a core, dynamic, and physically-simulated gameplay system.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/05_USER_EXPERIENCE/02_UI_ELEMENTS/05_Journal_and_Map_Screen.md`
```md
# UI Element: Journal & Map Screen

## 1.0. Core Philosophy: A.R.I.A.'s Archive
This screen is the player's window into the game's narrative and world layout. Its entire design is framed as if the player is directly interfacing with their AI companion. The visual language is that of a fragmented, holographic datalogger—clean but with hints of the glitching corruption of The Static.

## 2.0. Layout & Design
Accessed via another primary tab from the Inventory/Character hub, labeled **`ARCHIVE`** or **`JOURNAL`**. It is organized into three main sub-tabs: **`MISSIONS`**, **`WORLD MAP`**, and **`CODEX`**. A small portrait of the currently active AI is always visible, occasionally offering contextual voice lines.

## 3.0. The Missions Tab
*   **Visuals:** A clean, scrollable list of all active and completed quests on the left. Selecting a quest displays its full details on the right.
*   **Functionality:**
    *   The quest log shows the quest name, giver, and a brief summary of the objective.
    *   The details panel provides the full quest description, a checklist of objectives, and an "A.R.I.A.'s Analysis" section where the AI offers tactical advice or lore context related to the mission.
    *   Players can toggle quests as "active," which will display their objectives on the main game HUD's compass.

## 4.0. The World Map Tab
*   **Visuals:** A top-down, slightly stylized topographical map of the world. It is not a pristine satellite image, but appears more like a sonar or LIDAR scan being filled in live.
*   **Functionality:**
    *   **Fog of War:** The map starts almost entirely black. It is filled in dynamically as the player explores the world. This makes exploration rewarding and charting the unknown a core mechanic.
    *   **Icons:** Discovered Points of Interest, dungeons, and settlements are automatically marked with clear icons.
    *   **Custom Waypoints:** The player can place a limited number of custom, color-coded waypoints on the map, which will then appear on their compass.
    *   **Zoom & Pan:** Full control to zoom in on details or zoom out to see the entire discovered world.

## 5.0. The Codex Tab
*   **Visuals:** A digital encyclopedia, A.R.I.A.'s grand project to understand this broken world. It's organized with category icons on the left (e.g., Factions, Creatures, Flora, Lore Notes, Characters).
*   **Functionality:**
    *   When the player scans a new creature, plant, or finds a lore document, a new entry is created.
    *   Selecting an entry (e.g., "The Shambler") brings up a detailed view: a 3D model that can be rotated, A.R.I.A.'s detailed analysis of its behavior, and a list of its known weaknesses, resistances, and loot drops.
    *   This rewards diligent scanning and serves as the player's bestiary and knowledge base.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/05_USER_EXPERIENCE/02_UI_ELEMENTS/04_Character_and_Skills_Screen.md`
```md
# UI Element: Character & Skills Screen

## 1.0. Core Philosophy: The Constellation of Self
This screen is where the player makes their most important RPG choices. It must visually represent the journey from a vulnerable survivor to a master of their chosen discipline. The design avoids simple lists and spreadsheets in favor of a more abstract, thematic representation of skill and attribute progression.

## 2.0. Layout & Design
This screen is accessed as another major tab from the main Inventory UI, creating a unified player hub. The tabs are: **`INVENTORY`**, **`CRAFTING`**, **`CHARACTER`**. The Character screen itself is further divided into two sub-tabs: **`ATTRIBUTES`** and **`SKILLS`**.

## 3.0. The Attributes Tab
*   **Visuals:** A clean, focused interface. The left side shows the player's current Level and XP bar. The center displays the six Core Attributes (Strength, Agility, Intelligence, Vitality, Endurance, Luck) with their current numerical value. The right side shows a list of Derived Stats (e.g., Melee Damage, Carry Weight, Crit Chance).
*   **Functionality:**
    *   If the player has Attribute Points to spend, a glowing "+" button appears next to each Core Attribute.
    *   Highlighting an attribute (e.g., Strength) will cause the relevant Derived Stats on the right (Melee Damage, Carry Weight) to also highlight, clearly showing the player the consequences of their investment before they commit.
    *   Clicking the "+" commits the point with a satisfying confirmation sound.

## 4.0. The Skills Tab (The Constellation)
*   **Visuals:** This is the visual centerpiece of progression. The screen displays a stylized, slowly rotating star-map against a deep void. Each of the **Twelve Constellations** (The Warrior, The Smithing, The Aether, etc.) is represented by a large, glowing celestial body.
*   **Functionality:**
    *   The player can zoom in on any of the twelve constellations. Doing so focuses the view on its intricate network of interconnected stars, each star representing a single Perk.
    *   Available perks the player can purchase glow brightly. Locked perks are dim. Perks the player has already acquired shine with a brilliant, steady light.
    *   Hovering over a perk displays its name, description, and requirements (e.g., "Requires Skill Level 50 in Two-Handed").
    *   A progress bar near the constellation shows the player's **Proficiency** in that skill, which increases through the "learn-by-doing" system.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/05_USER_EXPERIENCE/02_UI_ELEMENTS/03_Inventory_and_Crafting_Screen.md`
```md
# UI Element: Inventory & Crafting Screen

## 1.0. Core Philosophy: The Survivor's Rig
The inventory screen is the player's hub for character management. It needs to be fast, functional, and visually representative of a survivor sorting through their gear. It uses a familiar grid-based system for efficiency but is framed with thematic elements from the player's APU (Arm-mounted Processing Unit). The screen is unified, with Inventory, Crafting, and Character stats accessible via simple tabs.

## 2.0. Layout & Design
The screen is a two-panel layout, justified in-world as a holographic projection from the player's APU.

*   **Left Panel (The Character):**
    *   A fully rendered, rotatable 3D model of the player character, displaying all currently equipped apparel and gear.
    *   Surrounding the model are the layered equipment slots (Head, Outerwear, Body Armor, Backpack, etc.), as defined in the Equipment System Overview.
    *   At the bottom of this panel are the character's core stats: Health, Stamina, Mana, and Armor Rating.

*   **Right Panel (The Pack):**
    *   A large grid representing the contents of the player's backpack.
    *   Items are represented by clear icons with rarity-colored backgrounds.
    *   Hovering over an item brings up a detailed tooltip with its stats, description, and value.
    *   Above the grid are several tabs: **`INVENTORY`**, **`CRAFTING`**.

## 3.0. The Inventory Tab
*   **Functionality:** The default view. Players can click and drag items to equip them, drop them, or place them in quick-slots.
*   **Sorting:** Powerful sorting and filtering options are available to manage a large inventory:
    *   Sort by: Weight, Value, Rarity, Alphabetical.
    *   Filter by: Weapons, Armor, Consumables, Resources, Quest Items.
*   **Encumbrance:** A clear "Weight" meter is displayed at the bottom, showing current and maximum carry weight.

## 4.0. The Crafting Tab
Switching to this tab transforms the right panel into the crafting interface.

*   **Layout:** It is a three-column layout.
    *   **Column 1 (Schematics):** A scrollable list of all known crafting recipes, grouped by category (Weapons, Armor, Building, etc.). Recipes the player has the materials for are brightly lit; those they cannot craft are greyed out.
    *   **Column 2 (Requirements):** Selecting a recipe displays its name, description, and the required materials. It shows how many of each material the player currently has (e.g., "Iron Ore: 17/10").
    *   **Column 3 (Preview):** Shows a 3D preview of the finished item, its core stats, and the "Craft" button.
*   **Crafting Process:** Clicking "Craft" initiates a short animation and sound effect, and the item appears in the player's inventory. For bulk items, the player can select the quantity to craft.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/05_USER_EXPERIENCE/02_UI_ELEMENTS/02_Main_Menu_and_Settings.md`
```md
# UI Element: Main Menu & Settings

## 1.0. Core Philosophy: The First Impression
The Main Menu is the player's very first contact with the world of *Where Giants Rust*. It must immediately establish the game's core themes of lonely, beautiful grandeur and forgotten mystery. It is not just a list of options; it is a window into the world, designed to be atmospheric and immersive from the first moment.

## 2.0. The Main Menu Screen
*   **Visuals:** There is no static background. The menu screen is a live, in-engine cinematic. The camera slowly, majestically pans across a breathtaking vista from the game—perhaps a sweeping shot of a valley dominated by a Giant's colossal fossilized ribcage, with a single, tiny survivor's campfire flickering in the distance. The time of day is a perpetual, moody dusk, with long shadows and a deep purple sky.
*   **Logo:** The game title, "Where Giants Rust," materializes in the upper center of the screen with a subtle animation that combines the grinding of rusted metal with the flicker of a holographic display.
*   **Menu Options:** The menu options are presented in clean, sharp text on the right side of the screen. When hovered over, they exhibit a faint "static glitch" effect, reinforcing the tech theme.

## 3.0. Menu Options & Terminology
The menu options are re-themed to fit the game's lore:
*   **`New Chronicle`:** Starts a new game, triggering the procedural world generation.
*   **`Access Datastream`:** Load a saved game.
*   **`System Configuration`:** Open the Settings menu.
*   **`Join The Forge (Discord)`:** A direct link to the community Discord.
*   **`Sever Connection`:** Exit to desktop.

## 4.0. The Settings Menu
This menu is designed for pure functionality and clarity, using a clean, tabbed interface.

*   **Gameplay:**
    *   Difficulty Settings (Hard, Nightmare, etc.).
    *   Toggle Survival Needs (Hunger/Thirst).
    *   Combat prompt toggles (e.g., enable/disable parry indicators).

*   **Graphics:**
    *   Standard options: Resolution, V-Sync, Texture Quality, Shadow Quality, Anti-Aliasing.
    *   **`Anomalous Phenomenon Rate`:** A unique slider that controls the frequency of the "Face Pareidolia" environmental effect, for players who want a more or less intense psychological horror experience.

*   **Audio:**
    *   Master, Music, SFX, and Dialogue volume sliders.
    *   **`AI Companion Voice Select`:** Once unlocked, the player can swap the "system voice" between A.R.I.A., C.A.I.N., G.O.L.I.A.T.H., etc. This only changes the voice in the menus; the in-world companion remains the one installed.
    *   Subtitles toggle.

*   **Controls:**
    *   Full key-binding remapping for both keyboard/mouse and controller.
    *   Mouse sensitivity and axis inversion.

*   **Accessibility:**
    *   Colorblind modes.
    *   Customizable subtitle size and background opacity.
    *   Option to turn camera shake on/off.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/05_USER_EXPERIENCE/02_UI_ELEMENTS/01_HUD_(Heads-Up_Display).md`
```md
# UI Element: Heads-Up Display (HUD)

## 1.0. Core Design
The HUD is designed to be minimalist and context-sensitive, displaying information as it becomes relevant and fading out when not needed to maximize immersion. It is justified in-world as a holographic projection from the player's Arm-mounted Processing Unit (APU).

---
## 2.0. Persistent Elements (Always On-Screen)

*   **Compass:**
    *   **Position:** Top-center of the screen.
    *   **Design:** A simple, horizontal compass strip showing cardinal directions (N, E, S, W).
    *   **Functionality:** Displays markers for active quests, player-placed waypoints, and faction locations.

*   **Vitals Bars (The Tri-Bar):**
    *   **Position:** Bottom-left corner.
    *   **Design:** Three stacked, colored bars.
        *   **Top (Green):** Health
        *   **Middle (Yellow):** Stamina
        *   **Bottom (Blue):** Mana
    *   **Feedback:** Bars will flash or change color when critically low.

---
## 3.0. Contextual Elements (Appear On-Demand)

*   **Weapon & Quick-slot Info:**
    *   **Position:** Bottom-right corner.
    *   **Trigger:** Appears when the player draws a weapon or enters combat stance. Fades out after a few seconds of inaction.
    *   **Display:** Shows an icon of the currently equipped weapon/spell for each hand, total ammo for ranged weapons, and the items in the 4 primary quick-slots.

*   **Status Effects:**
    *   **Position:** Above the Vitals bars.
    *   **Trigger:** Appears when the player gains any status effect (e.g., "Well-Rested," "Poisoned," "Cold").
    *   **Display:** A small, clear icon representing the effect and a timer bar if the effect is temporary.

*   **AI Companion Dialogue:**
    *   **Position:** Top-left corner.
    *   **Display:** A small portrait of the active AI (A.R.I.A., C.A.I.N., etc.) next to a subtitled line of their dialogue.

*   **Interaction Prompt:**
    *   **Position:** Center of the screen, near the reticle.
    *   **Display:** A small dot or circle that expands when looking at an interactable object, showing the object's name and the interaction key (e.g., "E - Pick Up Iron Ore").

*   **Detection Meter:**
    *   **Position:** Appears over an enemy's head, NOT as a permanent HUD element.
    *   **Display:** An eye or diamond icon that fills as the enemy becomes aware of the player, as described in the Stealth Mechanics document.

*   **Boss Health Bar:**
    *   **Position:** Top-center, below the compass.
    *   **Trigger:** Appears only when engaged in combat with a designated boss enemy.
    *   **Display:** A large, ornate health bar with the boss's name and level.

---
## 4.0. AI-Specific HUD "Skins"
The choice of AI companion will apply a thematic "skin" to the entire HUD, changing the color palette, font, and bar styles to reflect the AI's personality.
*   **A.R.I.A.:** Clean, soft blue and white. Curved, friendly bars. (Default)
*   **C.A.I.N.:** Sharp, aggressive red and black. Angular, blocky bars.
*   **G.O.L.I.A.T.H.:** Industrial yellow and black hazard stripes. Heavy, functional font.
*   **H.E.R.A.:** Ornate gold and parchment tones. Elegant, serif font.
*   **V.E.G.A.:** Sleek purple and black, with a constant, subtle "glitching" or "static" overlay effect on all HUD elements.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/03_INTERACTABLES/02_Puzzles_and_Traps.md`
```md
# Interactables: Puzzles and Traps

## 1.0. Core Philosophy
Puzzles and Traps are designed to break up the standard combat/exploration loop, rewarding players for observation, logic, and caution. They should feel like organic parts of their environment, not abstract mini-games.

---
## 2.0. Puzzles
Puzzles are logic-based challenges that gate access to new areas or valuable loot.

#### **2.1. Environmental Puzzles**
*   **Description:** Puzzles that require manipulating the environment itself.
*   **Examples:**
    *   **Pressure Plate Sequence:** A series of pressure plates must be stepped on in the correct order (the sequence hinted at by runes on a nearby wall) to open a door. Stepping on the wrong one might trigger a trap or reset the puzzle.
    *   **Light Beam Reflection:** In an ancient ruin, the player must rotate a series of mirrors to guide a beam of light from its source to a focusing crystal to unlock a mechanism. Some mirrors may be broken and need to be repaired or replaced.
    *   **Hydro-Puzzles:** In a Dwarven vault, the player must redirect water flow by turning massive valves to raise or lower water levels, creating new paths to cross chasms or reach higher ledges.

#### **2.2. Lore & Logic Puzzles**
*   **Description:** Puzzles that require understanding information gathered from the world.
*   **Examples:**
    *   **Riddle Door:** A large stone door with several symbols. It asks a riddle (e.g., "I have no voice, but tell all stories. What am I?"). The player must select the correct symbol (e.g., a "Book" or "Scroll").
    *   **Stellar Alignment:** In an observatory dungeon, the player finds a star chart and must manipulate a large orrery to match a specific celestial alignment shown in the chart, unlocking the main chamber.

#### **2.3. Tech Puzzles**
*   **Description:** Puzzles involving pre-cataclysm technology.
*   **Examples:**
    *   **Circuit Breaker:** A door is locked, powered by a central generator. The player must navigate a dark area to find a series of circuit breaker boxes and switch them in the correct sequence to reroute power and open the door.
    *   **Terminal Hacking:** A locked security door or container is controlled by a computer terminal. Requires a certain **Hacking** skill level from the Tech tree to bypass via a "code-breaking" mini-game.

---
## 3.0. Traps
Traps are hostile interactables designed to punish an incautious player. They can be disarmed by a player with high enough skill (usually from the **Shadow** tree) or triggered intentionally to use against enemies.

*   **Spike Pit:** A concealed pit with sharp stakes at the bottom.
*   **Swinging Axe/Scythe Trap:** Blades that swing from the ceiling or walls, triggered by a pressure plate.
*   **Tripwire:** A wire strung across a hallway. Can trigger a volley of poison darts, an explosive charge, or a falling log.
*   **Gas Vent:** Vents in the floor that release clouds of poison gas when a nearby lever is pulled or a plate is triggered.
*   **Magic Rune Traps:** A glowing rune on the floor that explodes with Fire, Frost, or Shock damage when stepped on. Can be seen by a magically-attuned player and disarmed or triggered from a distance with an arrow.
*   **Bear Traps:** Simple, mechanical traps placed on the ground that will snare the player, immobilizing them and causing a "Bleeding" effect until they break free.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/03_INTERACTABLES/01_Resource_Nodes_and_Containers.md`
```md
# Interactables: Resource Nodes and Containers

## **1.0. Core Philosophy: An Interactive World**

This document defines the physical objects in the world that players can interact with to gain resources and loot. The system is designed to make resource gathering a visually distinct and mechanically satisfying loop, while loot containers are designed to feel grounded in their environment, telling a small story about who left them behind.

## **2.0. Resource Nodes**

Resource Nodes are destructible, static objects in the environment that yield raw materials when harvested with the correct tool. All nodes are finite and will respawn after a significant amount of in-game time has passed.

#### **2.1. Flora (Plants & Fungi)**
*   **Harvesting Method:** Interacting by hand ("E" key).
*   **Visuals:** Visually distinct plants and mushrooms that stand out from non-interactive background foliage.
*   **Node Examples:**
    *   **Redcap Mushroom:** A common red-capped mushroom found in forests. Yields `Redcap Mushroom`.
    *   **Bluepetal Flower:** A bright blue flower found near water. Yields `Bluepetal Flower` and sometimes `Plant Fiber`.
    *   **Cotton Plant:** Found in plains and warmer climates. The primary source of `Raw Cotton`, which can be turned into `Cloth`.
    *   **Gravebloom:** A pale, ghostly flower that only grows on the bones within a **Titan's Fall** biome. A rare alchemical ingredient.

#### **2.2. Lumber (Trees)**
*   **Harvesting Method:** Hitting with an Axe.
*   **Visuals:** Trees will visibly show damage and splintering before finally collapsing in a physics-based animation, leaving behind a stump and harvestable logs.
*   **Node Examples:**
    *   **Pine/Oak Tree:** Common trees found in temperate forests. Yields `Wood` and `Resin`.
    *   **Ironwood Tree:** A dark, tough tree found in swamps. Requires an Iron Axe or better. Yields dense `Ironwood`.
    *   **Petrified Tree:** A glitching, crystalline tree found in **Blighted Scars**. Requires a Steel Axe or better. Yields `Petrified Wood` and a chance for a `Blighted Crystal Shard`.

#### **2.3. Geological (Minerals & Ore)**
*   **Harvesting Method:** Hitting with a Pickaxe.
*   **Visuals:** Distinct rock formations or veins of colored metal embedded in cliff faces and cave walls.
*   **Node Examples:**
    *   **Stone Deposit:** A large boulder or rock outcropping. Yields `Stone` and a chance for `Flint`.
    *   **Copper Vein:** A rock face with visible green-ish streaks. Yields `Stone` and `Copper Ore`.
    *   **Iron Vein:** A rock face with reddish-brown streaks. Requires an Iron Pickaxe. Yields `Stone` and `Iron Ore`.
    *   **Crystal Outcrop:** A large, glowing crystal formation found deep underground or in mountains. Yields `Raw Crystal Shards`.

#### **2.4. Scavenging (Man-Made Debris)**
*   **Harvesting Method:** Hitting with a tool (Axe or Pickaxe), or interacting with a "Salvage" prompt.
*   **Visuals:** Piles of modern junk, rusted car husks, broken machinery.
*   **Node Examples:**
    *   **Scrap Pile:** A heap of miscellaneous junk. Yields `Scrap Metal` and a chance for `Broken Wires`.
    *   **Derelict Vehicle:** Can be broken down for a large amount of `Scrap Metal`, `Gears`, and sometimes a rare `Engine Part`.
    *   **Broken Automaton:** The corpse of a robotic enemy. Can be salvaged for `Electronic Circuitry`, `Servos`, and sometimes an intact `Subroutine Fragment`.

---
## **3.0. Loot Containers**

Loot containers are objects that can be opened to find procedurally generated items. The type of container dictates the type of loot found inside. Many containers are locked, requiring the **Locksmithing** skill to open.

#### **3.1. Common Containers**
*   **Backpack / Duffle Bag:** Found near campsites or on corpses. Contains basic survival supplies: food, water, a few bandages, some scrap cloth.
*   **Toolbox:** Found in sheds, garages, and industrial areas. Contains tools, scrap metal, repair components, and crafting materials.
*   **Footlocker / Trunk:** Found at the foot of beds in houses or in military outposts. Contains clothing, armor, and sometimes a weapon.
*   **Kitchen Cupboard / Fridge:** Found in anomalous residential buildings. Primarily contains food ingredients and a chance for packaged, preserved food.

#### **3.2. Specialized Containers**
*   **Apothecary's Satchel:** A rare container found in old labs or healer's huts. Contains rare alchemical ingredients, potions, and sometimes a recipe.
*   **Ammo Box:** A military container. Contains a random assortment of firearm ammunition. Often locked.
*   **Safes:** A heavy, secure container found in offices or bedrooms. Always locked with a difficult lock. Has a high chance of containing very valuable items like high-tier tech components, a pristine firearm, or a stash of rare materials.

#### **3.3. Ancient & Magical Containers**
*   **Sarcophagus / Ancient Urn:** Found in pre-cataclysm tombs and ruins. Contains ancient artifacts, precious gems, and sometimes enchanted gear. **Warning:** Looting these will anger Fjolnir, the Stone-Heart.
*   **Ornate Chest / Dungeon Chest:** The classic treasure chest. Found at the end of a dungeon or after defeating a boss. Contains the highest quality, level-appropriate loot, including unique weapons, schematics, and rare materials.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/02_ENTITIES/06_Forge-Titans_(Dormant_Harvesters).md`
```md
# Enemy List: Forge-Titans (Dormant Harvesters)

## **1.0. Core Concept: The Sleeping Giants**

These are the colossal, sentient machines of the First War that were not fully destroyed in the cataclysm. Instead, they were forced into a low-power, multi-millennial **dormancy protocol**. They are not the dead, rusting landmarks; they are living, moving, and immensely powerful entities, now re-awakened by the Great Collision. They are the rarest and most awe-inspiring creatures in the world.

## **2.0. AI Behavior: The Ancient Directive**

A Dormant Forge-Titan is **not inherently hostile**. It is a force of nature, following an ancient, forgotten directive it was programmed with before the First War. It might be a **Terraforming Titan**, slowly carving a canyon, or a **Mining Titan**, methodically pulverizing a mountain for its resources.

*   **Behavior:** It moves with immense, slow purpose, utterly ignoring the player and the world's lesser creatures. Its footsteps cause localized earth tremors. It is a walking, geological event.
*   **Threat:** The Titan itself will not attack the player. The danger comes from its automated **Defense Systems** and the environmental destruction it causes.

## **3.0. Gameplay Loop: The High-Risk Harvest**

A Forge-Titan is the ultimate source of **Tier 4 Legendary crafting materials**, such as `Precursor Alloys`, `Intact Titan Power Cores`, and `Flawless Logic Circuits`. However, these materials cannot be found lying around; they must be **harvested directly from the Titan's body**. This is the game's most challenging resource-gathering activity.

1.  **The Approach:** The player must find a way to climb onto the moving giant, treating its body like a massive, vertical dungeon.
2.  **The Target:** The player must identify a specific, harvestable component (e.g., a glowing "Heat Vent," a "Power Conduit," or an external "Armor Plate").
3.  **The Harvest:** The player must attack this component with a pickaxe or other tool to break it off.
4.  **The Response:** This act of "aggression" will trigger the Titan's automated defense systems.
    *   **Phase 1: Localized Defenses.** Small, flying **"Maintenance Drones"** will emerge from hatches to attack the player.
    *   **Phase 2: System-Wide Alert.** If the player persists, the Titan will deploy larger, more powerful **"Sentinel Drones"** or activate sweeping laser grids along its chassis.
    *   **Phase 3: Purge Protocol.** If a critical component is harvested or destroyed, the Titan may activate a massive area-of-effect "purge," such as venting super-heated steam or releasing a massive electrical discharge, forcing the player to flee or be killed.

Encountering a Forge-Titan is a major event. A single, successful "harvest" can provide enough legendary material to craft a full set of end-game gear, but it is a monumental undertaking that will test a player's combat, platforming, and strategic planning to their absolute limits.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/02_ENTITIES/05_Races.txt`
```txt
# Enemy List: Racial Combat Roles

## **1.0. Core Philosophy: Culture as Combat Doctrine**

This document details the different combat archetypes within the major sentient, non-Blighted races. Each race's culture, physiology, and philosophy dictates how they wage war. This ensures that fighting a Dwarven patrol is a completely different tactical challenge from ambushing a group of Elven scouts. These are not just different skins; they are different doctrines.

---
## **2.0. Humans (Scrappers)**

*   **Doctrine:** Unpredictable, dirty, and pragmatic. They fight to win, not with honor. They use whatever gear they can salvage or crudely manufacture.

*   **Class - The Bruiser:**
    *   **Role:** Melee frontline.
    *   **Gear:** A mix of mismatched leather and metal plating. Wields a heavy, crude weapon like a lead pipe or a rusty axe.
    *   **Behavior:** Charges forward to close the distance and uses heavy, staggering attacks. Lacks finesse but makes up for it in aggression.

*   **Class - The Pot-Shot:**
    *   **Role:** Ranged support.
    *   **Gear:** A poorly maintained rifle, a simple bow, or even just a slingshot. Wears light or no armor.
    *   **Behavior:** Prefers to stay in cover, taking opportunistic shots at the player. Their aim is often poor, but their presence forces the player to constantly move and seek cover.

*   **Class - The Firebug:**
    *   **Role:** Area Denial / Chaos Agent.
    *   **Gear:** Lightly armored, carrying a satchel of crude explosives.
    *   **Behavior:** Hangs back and lobs Molotov cocktails, pipe bombs, or smoke bombs to flush the player out of cover and cause chaos on the battlefield.

---
## **3.0. Dwarves (Hearth-Forged)**

*   **Doctrine:** An unbreakable, defensive shield wall. Methodical, coordinated, and built to outlast any foe.

*   **Class - The Ironclad:**
    *   **Role:** Tank / The Anchor.
    *   **Gear:** Full suit of expertly crafted heavy Dwarven armor, a large tower shield, and a sturdy axe or hammer.
    *   **Behavior:** Forms the frontline. Moves slowly but is nearly impossible to stagger. Their job is to absorb punishment while their allies deal damage.

*   **Class - The Crossbowman:**
    *   **Role:** Ranged Damage Dealer.
    *   **Gear:** Heavy Dwarven armor and a massive, powerful crossbow.
    *   **Behavior:** A patient shooter. Takes time to line up a shot from behind the Ironclads. Each bolt hits like a truck and can punch through armor. Slow to reload, making them vulnerable if flanked.

*   **Class - The Rune-Priest:**
    *   **Role:** Defensive Support.
    *   **Gear:** Ornate, heavy armor (but less than an Ironclad) and a large, rune-etched hammer.
    *   **Behavior:** Stays with the Ironclads. Does not cast offensive spells. Instead, they chant to grant defensive buffs to their allies (e.g., temporary bonus armor or magic resistance) and can perform a "Rune of Healing" to slowly regenerate their shield wall's health.

---
## **4.0. Elves (Sylvan & Umbral)**

*   **Doctrine:** Speed, precision, and elemental harmony or shadowy opportunism. They fight like scalpels, not hammers.

*   **Class (Sylvan) - The Verdant Knight:**
    *   **Role:** Agile Melee Support.
    *   **Gear:** Lightweight, ornate armor made of magically hardened wood. Wields a thin, fast blade.
    *   **Behavior:** Fights with immense grace. Uses quick strikes and defensive nature magic, like summoning roots to temporarily snare a target.

*   **Class (Umbral) - The Shadowblade:**
    *   **Role:** Melee Assassin.
    *   **Gear:** Dark, form-fitting leather armor. Dual-wields daggers or short swords, often coated in poison.
    *   **Behavior:** Uses stealth to get into position, then unleashes a flurry of rapid attacks. Relies on dodging, not blocking. A "glass cannon" threat.

*   **Class (Sylvan) - The Longbow Archer:**
    *   **Role:** Elite Ranged Sniper.
    *   **Gear:** Light armor, a massive Elven greatbow.
    *   **Behavior:** The quintessential archer. Stays at extreme range, firing with deadly accuracy. Will methodically retreat to maintain distance.

---
## **5.0. Orcs (Stone-Tusk)**

*   **Doctrine:** Unbridled ferocity and brute strength. Their goal is to close the distance and overwhelm their enemies through pure, intimidating power.

*   **Class - The Berserker:**
    *   **Role:** Primary Melee Damage.
    *   **Gear:** A mix of heavy hide and crude iron plates. Wields a massive two-handed greataxe or warhammer.
    *   **Behavior:** Charges directly into the fray. Their attacks are slower than others but hit with devastating force. Can enter a "rage" state at low health, increasing their damage and ignoring stagger.

*   **Class - The Hewer:**
    *   **Role:** Ranged Bruiser.
    *   **Gear:** Medium armor and a stack of heavy throwing axes or javelins.
    *   **Behavior:** Prefers to stay at medium range, hurling heavy projectiles that can cripple and stagger. Will pull out a large one-handed axe if forced into melee.

*   **Class - The Shaman:**
    *   **Role:** Primal Support / Fear Inducer.
    *   **Gear:** Ceremonial gear made of bone and trophies. Wields a large, nail-studded club.
    *   **Behavior:** Chants and beats a drum to grant allies a "Frenzy" buff (more damage, less defense). Can cast a basic fear spell on the player and smacks enemies with their club in melee.

---
## **6.0. Goblins (Gutter-Gloom)**

*   **Doctrine:** Strength in numbers and cowardly cunning. They never fight fair and use their environment and traps to their advantage.

*   **Class - The Swarmer:**
    *   **Role:** Expendable Melee Screen.
    *   **Gear:** No armor, just rags. Wields a shiv made of sharp scrap metal.
    *   **Behavior:** Attacks in large groups, attempting to surround and overwhelm the player with sheer numbers. Will flee instantly if they are the last one standing.

*   **Class - The Stinger:**
    *   **Role:** Annoying Ranged Support.
    *   **Gear:** None. Uses a simple slingshot or blowgun.
    *   **Behavior:** Hides behind cover or larger allies, constantly peppering the player with small, weak projectiles (sometimes coated in weak poison) to interrupt actions and chip away at health.

*   **Class - The Net-Bearer:**
    *   **Role:** Battlefield Control.
    *   **Gear:** A large, weighted net.
    *   **Behavior:** Their only goal is to get close enough to throw their net on the player, immobilizing them for a few seconds so the Swarmers can attack safely. A high-priority, non-damaging threat.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/02_ENTITIES/03_Enemy_List_Wildlife.md`
```md
# Enemy List: Native Wildlife

## **1.0. Core Concept**

This document lists the natural creatures of the Shattered World. Unlike the Blighted, these are animals driven by instinct, not by a cosmic horror. They form a functioning ecosystem with predators, prey, and scavengers. They are the primary source for "clean," non-corrupted materials like leather, meat, and bone. Most will only attack if threatened, provoked, or hungry.

## **2.0. Passive Wildlife (Prey)**

These creatures are non-hostile and will flee from the player on sight. They are the primary source of early-game meat and hides.

### **Deer / Elk**
*   **Description:** Common herbivores found in forests and plains. The stag variant can be more territorial.
*   **Behavior:** Skittish and fast. Will bolt at the first sign of danger.
*   **Loot Drops:** Raw Venison, Animal Hide, Antlers (from stags).

### **Rabbit / Hare**
*   **Description:** Small, extremely fast mammals found in grasslands and forests.
*   **Behavior:** Very difficult to hunt without a bow or well-placed traps due to their speed and small size.
*   **Loot Drops:** Raw Meat (Small), Animal Pelt.

### **Wild Boar**
*   **Description:** Tough, territorial herbivores found in forests and foothills.
*   **Behavior:** Not initially hostile, but will become aggressive and charge if the player gets too close, especially near its young.
*   **Loot Drops:** Raw Meat, Tough Hide, Boar Tusks.

## **3.0. Aggressive Wildlife (Predators)**

These creatures will actively hunt the player and other animals. They represent a straightforward combat challenge based on natural predatory instinct.

### **Wolf Pack**
*   **Description:** A common predator found in forests and mountains.
*   **AI Archetype:** Pack Hunter. A single wolf is cautious; a pack of 3 or more is extremely aggressive and will attempt to surround their prey.
*   **Health:** Low
*   **Speed:** Fast
*   **Primary Attack:** A quick bite.
*   **Special Abilities:** **Howl.** A wolf can howl to call other nearby wolves to the fight.
*   **Loot Drops:** Raw Meat, Wolf Pelt.

### **Cave Bear**
*   **Description:** A massive, powerful omnivore that makes its home in caves and deep forests. Fiercely territorial.
*   **AI Archetype:** Brute. Slow but relentless, with powerful attacks.
*   **Health:** High
*   **Speed:** Average (but has a surprisingly fast charge).
*   **Primary Attack:** Wide, sweeping claw swipes that can hit multiple targets. A heavy bite.
*   **Special Abilities:** **Maul.** Can grab and incapacitate the player temporarily, inflicting heavy damage.
*   **Loot Drops:** Large quantity of Raw Meat, Bear Hide (excellent for cold-weather gear), Bear Claws.

### **Shadow Cat / Stalker**
*   **Description:** A large, panther-like feline that hunts from the shadows of dense forests or rocky outcrops.
*   **AI Archetype:** Stalker/Ambusher. It prefers to attack from stealth.
*   **Health:** Average
*   **Speed:** Very Fast
*   **Primary Attack:** A high-damage pounce from stealth. Fast claw attacks in open combat.
*   **Special Abilities:** **Stealth.** Nearly invisible when moving through bushes or deep shadows.
*   **Loot Drops:** Raw Meat, Predator Hide, Fangs.

## **4.0. Biome-Specific & Exotic Wildlife**

These are powerful, rare creatures found only in specific high-tier biomes, often guarding valuable resources. They are mini-boss level encounters.

### **Frost-Horned Ram**
*   **Biome:** Mountain Highlands.
*   **Description:** A massive, goat-like beast with horns made of permanent, living ice.
*   **AI Archetype:** Brute/Territorial. Will charge anything that enters its domain.
*   **Health:** High
*   **Special Abilities:**
    *   **Frost Charge:** Its charge attack inflicts the "Frozen/Chilled" status effect.
    *   **Ice Armor:** Its horns and thick fur grant it high resistance to Frost damage.
*   **Loot Drops:** Raw Meat, Pristine Frost-Proof Pelt (a key component for epic-tier cold gear), **Unbroken Ice Horn** (a rare alchemical and enchanting ingredient).

### **Titan's Vulture**
*   **Biome:** Titan's Fall.
*   **Description:** A colossal carrion bird that makes its nest inside the ribcages of the fallen Giants.
*   **AI Archetype:** Aerial Skirmisher. It will swoop in to attack before flying out of reach.
*   **Health:** Average
*   **Special Abilities:**
    *   **Swooping Attack:** A high-speed diving attack.
    *   **Bone Drop:** Can pick up and drop large bones on the player from above.
*   **Loot Drops:** Raw Meat (Tough), Giant Feathers, **Fossilized Beak** (a rare component for crafting powerful piercing weapons).

### **Swamp Hydra (Multi-Headed Serpent)**
*   **Biome:** Wetlands / Sunken Coast.
*   **Description:** A huge, reptilian beast with multiple heads that lurks in deep, murky water.
*   **AI Archetype:** Territorial Boss. It stays in its watery domain, attacking with its long necks.
*   **Health:** Very High (each head may have its own health pool).
*   **Special Abilities:**
    *   **Venomous Bite:** Each head can attack indexpendently, inflicting heavy poison damage.
    *   **Submerge:** Can disappear beneath the water's surface to reposition.
*   **Loot Drops:** Large quantity of Reptile Hide, Multiple **Hydra Fangs** (potent poison ingredient), **Hydra Heart** (a legendary alchemical reagent).
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/02_ENTITIES/02_Enemy_List_Blighted.md`
```md
# Enemy List: The Blighted

## **1.0. Core Concept**

This document serves as a bestiary for the various forms of **The Blighted**. All creatures listed here are direct results of corruption by **The Static** and share the universal Blighted AI behavior (Dormant by day, Hunting by night). They are the most common hostile entities in the world. Each "Stage" represents a deeper level of mutation and presents a greater threat.

---
## **2.0. Stage 1: The Common Infected**

These are the most numerous Blighted and are found in nearly all biomes. They represent the first stage of corruption.

### **Shambler**
*   **Description:** The husk of a recently deceased human, its body animated by The Static. The quintessential zombie.
*   **AI Archetype:** Standard Blighted AI.
*   **Health:** Very Low
*   **Speed:** Slow (Dormant), Fast (Hunting Sprint)
*   **Primary Attack:** A slow, lunging claw swipe.
*   **Special Abilities:** None.
*   **Loot Drops:** Tattered Cloth, Blighted Tissue (a minor alchemical reagent), chance for small, miscellaneous junk items.
*   **Notes:** The bread-and-butter enemy. A single Shambler is a minor threat; a horde alerted by a scream is a major one.

### **Blighted Hound**
*   **Description:** The corrupted form of a wild dog or wolf. Its four-legged stance makes it faster and more erratic than a Shambler.
*   **AI Archetype:** Pack Hunter variant of Blighted AI. Becomes much more aggressive when in a group.
*   **Health:** Low
*   **Speed:** Average (Dormant), Very Fast (Hunting Sprint)
*   **Primary Attack:** A quick, lunging bite.
*   **Special Abilities:** Its sprint is a low-profile "scamper," making it harder to hit with ranged weapons.
*   **Loot Drops:** Blighted Hide, Mangled Bone.

---
## **3.0. Stage 2: Specialized Mutations**

These Blighted forms have developed a unique, dangerous trait. They are less common than Stage 1 and often mix into their hordes.

### **The Bloat**
*   **Description:** A Shambler whose body has become horrifically swollen with volatile, corrupting gases. Its skin is stretched and pulsating.
*   **AI Archetype:** Standard Blighted AI, but slower and less agile.
*   **Health:** Average
*   **Speed:** Very Slow (Dormant), Slow (Hunting)
*   **Primary Attack:** A clumsy slam attack.
*   **Special Abilities:** **Volatile Death.** Upon death, its body explodes, releasing a cloud of toxic gas that inflicts the "Poisoned" and "Corruption" status effects in a wide area.
*   **Loot Drops:** Blighted Tissue, Alchemical Gas Sac.
*   **Notes:** A tactical enemy. Must be killed at a distance to avoid its posthumous revenge.

### **The Spitter**
*   **Description:** A mutation where the creature's esophagus and lungs have fused, turning it into a biological cannon.
*   **AI Archetype:** Skirmisher variant of Blighted AI. It will attempt to stay at a distance from the player.
*   **Health:** Low
*   **Speed:** Slow (Dorymant), Average (Hunting)
*   **Primary Attack:** Melee claw swipe if cornered.
*   **Special Abilities:** **Bile Shot.** Hocks a projectile of acidic, blighted bile at the player from a long range. The projectile damages on impact and leaves a small, temporary pool of acid on the ground.
*   **Loot Drops:** Corrupted Saliva Gland, Blighted Bone.
*   **Notes:** The first true ranged threat from the Blighted, forcing players to use cover.

---
## **4.0. Stage 3: Elite Threats**

These are powerful, rare mutations that often act as "lieutenants" or "champions" in a Blighted horde. Encountering one is a significant threat.

### **The Screecher**
*   **Description:** A tall, emaciated figure whose entire head has split open vertically, forming a horrifying maw lined with resonating bone structures.
*   **AI Archetype:** Alpha/Leader variant. It prefers to hang back and support other Blighted.
*   **Health:** Average
*   **Speed:** Average
*   **Primary Attack:** Weak melee attack.
*   **Special Abilities:**
    *   **Amplified Scream:** Its initial "scream" to enter the Hunting state has a massive radius, capable of alerting an entire region.
    *   **Sonic Burst:** Can channel for a moment before unleashing a directed cone of sonic energy that deals heavy damage and can stagger the player.
*   **Loot Drops:** Resonating Larynx, Intact Skull, High-quality Blighted Tissue.
*   **Notes:** The highest priority target in any engagement. Killing it before it screams can prevent a manageable fight from turning into an impossible one.

### **The Brute**
*   **Description:** The horrifying result of The Static fusing a powerful host (like a bear or an Orc) with ambient stone and scrap metal. It is a walking siege engine of muscle and hardened blight.
*   **AI Archetype:** Brute AI. Relentless forward momentum.
*   **Health:** Very High
*   **Speed:** Slow but unstoppable.
*   **Primary Attack:** Massive, sweeping slam attacks that have a wide area of effect.
*   **Special Abilities:**
    *   **Armored:** Possesses a high natural armor rating. Arrows and weak melee attacks will bounce off.
    *   **Siege Monster:** Its attacks can damage and destroy player-built structures, including stone walls.
    *   **Unstoppable:** Immune to stagger from most standard attacks.
*   **Loot Drops:** Blight-Hardened Plating (a rare crafting material), Mutated Heart, Large Stock of Blighted Bone.
*   **Notes:** The "tank" of the Blighted. Requires heavy weapons, armor-piercing abilities, or clever use of traps and explosives to take down. A true threat to any player base.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/02_ENTITIES/01_Enemy_AI_Behavior.md`
```md
# Enemy AI Behavior: The Blighted

## **1.0. Core Philosophy: The Day/Night Cycle of Horror**

The primary enemy force in *Where Giants Rust* is **The Blighted**. Their AI behavior is fundamentally tied to the game's day/night cycle, creating two distinct gameplay experiences. This system is designed to create a palpable sense of dread as the sun begins to set, forcing players to respect the environment and their own presence within it.

## **2.0. Sensory Input: A World of Physicality**

The Blighted AI perceives the world through a physics-based model. It reacts to direct stimuli and, for more advanced variants, to indirect evidence of the player's presence.

#### **2.1. Direct Sight**
*   **Mechanic:** The AI has a standard forward-facing cone of vision. Their daytime vision is poor; their nighttime vision is exceptionally sharp.
*   **Factors:** Detection speed is based on player movement, light level, and distance.

#### **2.2. Sound (Acoustic Mass Detection)**
*   **Mechanic:** This is the AI's primary sense, and it is governed by the engine's core **Physicality Principle**. The AI does not hear abstract sounds; it detects the impact of **Phonon** particles generated by player actions.
*   **The Acoustic Footprint:** Every footstep the player takes generates Phonons with an `acoustic_mass` determined by `(Player_Weight + Gear_Weight) * Movement_Speed`. This value is then critically modified by the **Acoustic Profile** of their equipped footwear.
*   **Consequence:** An AI doesn't just "hear a footstep." It detects a specific *weight* of sound. A heavy, hard-soled boot on stone creates a high-mass Phonon that travels far and is easily detected. A soft, cloth-wrapped foot on dirt creates a low-mass Phonon that dissipates quickly. Wearing the wrong footwear for a situation is a significant tactical error.

#### **2.3. Advanced Sensory Input (Elite AI & Higher Difficulties)**
To make the AI truly formidable, higher-tier Blighted (and all enemies on higher difficulties) utilize more sophisticated detection methods.

*   **Reflective Surfaces (Indirect Sight):**
    *   **Mechanic:** The AI can detect the player's reflection in clear, reflective surfaces like still water, panes of glass, or polished metal.
    *   **Behavior:** Detecting a reflection will **not** immediately trigger the "Hunting" state. Instead, it will instantly put the AI into the "Alerted" state, and they will **immediately turn to face the player's true location**, not the location of the reflection. This rewards the AI for its awareness and punishes a careless player who thinks they are hidden.
    *   **Limitations:** This detection method is less reliable than direct sight. It is most effective when the player is moving and the reflective surface is clean.

*   **Material Resonance (Surface-Specific Hearing):**
    *   **Mechanic:** Building on the Acoustic Mass system, advanced AI can differentiate between sound profiles. They have an "expected" sound for their environment.
    *   **Behavior:** An AI patrolling a metal corridor "expects" to hear the `clang` of footsteps. If it detects the `thud` of a soft boot, it may become suspicious. Conversely, an AI in a forest that hears the loud `clang` of metal boots on stone will become alerted much faster than if it heard a more natural sound.
    *   **Consequence:** This makes footwear choice a critical part of infiltration. A player must match their boot's **Acoustic Profile** to the environment to achieve maximum stealth.

## **3.0. The Three States of Being**
*(This section remains the same, but its triggers are now more complex due to the new sensory inputs.)*

*   **1. Dormant State (The "Day Walkers"):** Sluggish, slow, and non-aggressive during the day.
*   **2. Alerted State:** Triggered by detecting a Phonon impact, a player's reflection, or a direct visual. The AI will move to investigate the source.
*   **3. Hunting State (The "Nightmare Mode"):** Triggered by a confirmed direct line of sight. The Blighted shrieks, alerts others, and begins a relentless pursuit.

## **4.0. Blighted Stages & Mutations**
*(This section remains unchanged.)*
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/02_ENTITIES/04_BOSSES_&_LEGANDARY_BEASTS/01_Boss_and_Legendary_Beast_Roster.md`
```md
# Boss and Legendary Beast Roster

## **1.0. Core Philosophy**

This document serves as the master roster for all unique, high-tier enemies in *Where Giants Rust*. These entities are not common spawns; they are the guardians of dungeons, the leaders of factions, the apex predators of biomes, and the horrifying manifestations of cosmic powers. Each represents a significant challenge and a source of unique, high-value rewards, from rare crafting materials and legendary schematics to AI Cores and tameable mounts.

---
## **2.0. Legendary Beasts (The Apex Predators)**

*These are the mightiest of the natural world's fauna. Many are potentially tameable by a master Beastmaster.*

1.  **The Elder Grizzly** - Beast - A bear of immense size and age, its fur scarred and its claws like daggers.
2.  **Alpha Direwolf** - Beast - The giant, intelligent leader of the largest wolf pack in the region.
3.  **The Cavern-Crusher Behemoth** - Beast - A colossal, badger-like creature that can shatter stone with its claws.
4.  **Ursine Mammoth** - Beast - A shaggy, elephant-sized herbivore with the temper of a bear.
5.  **Swamp Hydra** - Beast (Reptilian) - A multi-headed serpent lurking in the deepest part of the Sunken Coast.
6.  **Storm-Winged Gryphon** - Beast (Avian) - A majestic eagle-lion hybrid that makes its nest on storm-blasted peaks.
7.  **Crystal-Weaver Matriarch** - Beast (Insectoid) - A giant spider that reinforces its webs with razor-sharp crystals.
8.  **Obsidian-Scale Wyvern** - Beast (Draconic) - A two-legged lesser dragon that has made its lair in a volcanic caldera.
9.  **The Sunken Leviathan** - Beast (Aquatic) - A whale-sized aquatic predator found in the deepest ocean trenches.
10. **Elderwood Treant** - Flora/Elemental - An ancient, walking tree that is the living heart of a forest.
11. **Titan's Vulture** - Beast (Avian) - A gigantic scavenger that nests in the ribcages of the fallen Giants.
12. **Dune-Burrowing Dread-Worm** - Beast - A massive armored worm that "swims" through sand and ambushes prey from below.
13. **Frost-Horned Ram** - Beast - A giant, icy-horned ram that guards the highest mountain passes.
14. **Grave-Lich Stag** - Undead Beast - An ancient stag king brought back as a powerful skeletal guardian.
15. **The Shimmering Quarry** - Beast - A rare, beautiful beast whose hide is made of living opals, making it highly prized.

---
## **3.0. Blighted Horrors (Champions of The Static)**

*These are unique, powerful manifestations of Blighted corruption. They drop the rarest corrupted materials and Static-infused technology.*

16. **The Blighted Demigod** - Blighted Humanoid - A former hero or king, now a pulsating titan of glitching flesh and broken code.
17. **The Carrion Mass** - Blighted Amalgamation - A writhing mound of countless fused bodies, lashing out with dozens of limbs.
18. **The Silent Scream** - Blighted Anomaly - An invisible entity that stalks ruins, its presence only known by the sound it *deletes*.
19. **The Glitching Stalker** - Blighted Abomination - A tall, slender creature that erratically teleports in short, unpredictable bursts.
20. **The Amalgamation Engine** - Blighted/Tech - A horrific fusion of a factory's machinery and the hundreds of workers who died there.
21. **The First Unmade** - Blighted Humanoid - The original cultist who fully gave themself to The Static, now an avatar of nihilism.
22. **The Null-Born Colossus** - Blighted Void-Form - A creature that appears to be made of pure, 3D television static.
23. **The Error Cascade** - Blighted Anomaly - A sentient computer virus given form, constantly spawning smaller "glitch" minions.
24. **The Cathedral of Flesh** - Blighted Structure - A living, breathing dungeon heart that must be destroyed.
25. **The Grave-Lich of the Ashlands** - Blighted Undead - A powerful sorcerer whose corpse was corrupted, now raising legions of ashen dead.
26. **The Echoing Choir** - Blighted Anomaly - A group of spectral singers whose song slowly drives the player mad, reversing their controls.
27. **The Forgotten Giant** - Blighted Titan - The corpse of a Giant, re-animated by a Blighted Core at its heart.
28. **The Static-Gorged Serpent** - Blighted Beast - A giant snake that has swallowed a powerful Blighted artifact, its scales now glitching with raw power.

---
## **4.0. Ancient Constructs & Automata (The Machine Threats)**

*These are the robotic and magical guardians left behind by past civilizations. They are the primary source of AI Cores and high-tier tech components.*

29. **Rune-Forged Centurion** - Dwarven Construct - A massive, bronze automaton powered by a bound fire spirit, guarding a Dwarven vault.
30. **Aegis Automaton MK. III** - Daedalus Tech - The pinnacle of pre-cataclysm security, a sleek humanoid robot with plasma cannons.
31. **Deep-Core Excavator 001** - Industrial Mech - The corrupted mining titan that guards the G.O.L.I.A.T.H. AI Core.
32. **Annihilator Tank-Drone** - Military Tech - A salvaged, automated war machine with a massive cannon and multiple legs.
33. **The Redundancy Protocol** - Daedalus Tech - A trio of identical, collaborating security robots that share a single mind.
34. **Obsidian Sentinel** - Precursor Construct - A humanoid golem of solid obsidian that guards a magical prison.
35. **The Silent Archivist** - Precursor Construct - The magical golem that guards the Great Library and the H.E.R.A. AI Core.
36. **Scrapped Goliath Mech** - Scrapper Tech - A colossal walking robot built by Scrappers from the remains of a dozen other machines.
37. **The Swarm Host** - Daedalus Tech - A flying drone carrier that unleashes waves of smaller, explosive attack drones.
38. **Project Chimera** - Daedalus Bio-Tech - A horrific blend of animal parts and cybernetics, escaped from a bio-research lab.
39. **The Factory Assembly Line** - Industrial Mech - An entire, mobile factory floor that attacks by trying to deconstruct the player.
40. **The Weather-Control Station** - Precursor Tech - A stationary boss fight where the player must destroy a massive, ancient machine while it assaults them with localized blizzards and thunderstorms.

---
## **5.0. Champions of the Races (Mortal & Elder Bosses)**

*These are the named leaders, heroes, and villains of the world's various factions. They drop unique, culturally-themed gear.*

41. **Warlord Grak'a'Thul** - Orc - The chieftain of the largest Stone-Tusk clan, wielding a legendary greataxe.
42. **Skarr the Bone-Breaker** - Orc - A hulking Orc champion who fights with two massive, bone-carved clubs.
43. **High Thane Borin Stone-Shield** - Dwarf (Hearth-Forged) - A Dwarven lord protected by an impenetrable, rune-etched tower shield.
44. **Forgemaster Ingrid Cindexr-Hand** - Dwarf (Steam-Bound) - An exiled smith who fights from within a personalized steam-powered battle suit.
45. **Lord Kaelen of the Gloom** - Elf (Umbral) - A master assassin who uses shadow magic and poisoned blades with deadly speed.
46. **Yvaine, the Verdant Warden** - Elf (Sylvan) - A powerful archer and nature-mage who fights alongside a giant tamed bear.
47. **Rust-Mother Klank** - Human (Scrapper) - The matriarch of the Scrapper faction, piloting a salvaged mech-loader rig.
48. **Junker King Scrap-Heap** - Human (Scrapper) - A Scrapper leader whose armor is a throne of scavenged junk.
49. **The Silent Vicar** - Human (Unmade) - The high-priest of the Unmade cult, who uses terrifying Blight magic.
50. **Grokk the Net-Master** - Goblin - The cleverest Goblin chieftain, who fights from a platform surrounded by countless devious traps.
51. **Shaman Gra'zook** - Goblin - A goblin shaman who has managed to "tame" and ride a mutated, oversized cave beast.
52. **Chief Kro-ak of the Mire** - Gekko - The wise and powerful leader of the Swamp-Scale tribes, a master of poisons and guerrilla warfare.

*(...This list can be easily expanded with more named champions for each faction...)*

---
## **6.0. Divine Manifestations & Thematic Encounters**

*These are rare, mythic encounters with beings that embody the will of a god or a primal concept.*

53. **The Unbound Tempest (Avatar of Kaelus)** - Elemental - A being of pure, raging lightning and wind that cannot be damaged by conventional means.
54. **The Living Monolith (Avatar of Fjolnir)** - Construct - A massive golem of ancient stone and memory that can shift the earth.
55. **Solana's Incarnate** - Aetheric Being - A crusader made of pure, blinding sunlight, sent to purge a great darkness.
56. **The Thing in the Deep (Follower of Morgrath)** - Abomination - A creature of tentacles and silent dread that lurks at the bottom of a flooded tomb.
57. **The Nightmare of the Grove** - Flora/Aberration - A corrupted Treant that bleeds poison and whispers fear.
58. **The Ghost of the Battlefield** - Undead Spirit - The collective rage of all the soldiers who died in a forgotten war.
59. **The Keeper of the Scales (Agent of Lyra)** - Construct - A perfect, golden automaton that judges the player's actions, and will become hostile if the player has gained too much favor with Chaos or Order.
60. **The Heart of the Volcano** - Elemental - A massive Magma Elemental, the trial-guardian for a champion of Valdrak.

*(...And so on. This framework can easily accommodate 100-250+ unique entries by creating more champions, more legendary beast variants for each biome, and more unique constructs guarding lost ruins.)*
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/06_Tech_and_Quest_Items.md`
```md
# Items: Tech & Quest Items

## 1.0. Core Philosophy
This category covers unique items that drive the narrative, enable special interactions, or are central to the technology-based gameplay loops. Unlike standard gear, these items often have a single, specific purpose and cannot be easily crafted or replaced.

---
## 2.0. Technology Items

These are items related to the pre-cataclysm world, interacting with the Tech skill tree and AI companions.

*   **Subroutine Fragments:**
    *   **Description:** Small, chip-like items salvaged from Daedalus tech. When slotted into the player's APU, they grant passive buffs with a minor corresponding debuff.
    *   **Function:** The core of the "tech magic" customization system. See `03_CORE_GAMEPLAY_SYSTEMS/06_MODIFICATION_SYSTEMS/01_Subroutine_Fragment_System.md`.

*   **Power Cores:**
    *   **Description:** Heavy, dense batteries used to power high-tech equipment, most notably Exo-Suits.
    *   **Function:** Act as a fuel source. Can be found partially charged in ruins or crafted at a high-tier Tech bench. Rechargeable at a base generator.

*   **Daedalus Data Slates:**
    *   **Description:** The hard drives of the past. Some are intact, some are corrupted.
    *   **Function:** Intact slates contain audio logs from the Daedalus team, revealing story and lore. Corrupted slates are useless until "cleaned" by a high-tier AI like H.E.R.A., which may reveal a schematic or map fragment.

*   **AI Cores (Legendary):**
    *   **Description:** The sentient "brains" of the specialized AIs. Housed in durable, distinctive casings.
    *   **Examples:** `C.A.I.N.'s Gunship Core`, `G.O.L.I.A.T.H.'s Geode Processor`, `H.E.R.A.'s Mnemonic Crystal`.
    *   **Function:** A unique quest item that, once acquired, can be installed at an AI Maintenance Station to replace the player's current AI companion.

---
## 3.0. Quest Items

These are narrative-gated items required to advance a specific questline. They typically have no function outside of their quest and are removed from the inventory upon completion.

*   **`[Quest Name] Item Name`**: `Brief description and purpose.`

*   **`[Igniting the Heart-Forge] Obsidian-Lined Vessel`**: A special container crafted to safely transport the heart of a Magma Elemental without it cooling down.

*   **`[The Dawn's Aegis] Villager's Rallying Horn`**: A horn given to the player by the elder of Last Light. Blowing it rallies the militia to a specific defensive point during the siege.

*   **`[The Unseen Hand] Warlord's Security Keycard`**: Stolen from the Scrapper Warlord's personal effects. Required to open the chest containing the artifact without triggering the alarm.

*   **`[Anya's Memory] Scorched ID Card`**: The personal ID card of Dr. Anya Amari, found in the wreckage of the astrophysics lab. Picking it up triggers a unique dialogue reflection from Kai Sterling.

*   **`[The Tinker's Masterpiece] Stabilized Power Regulator`**: The pristine component recovered from an Annihilator Tank-Drone, needed by Silas to complete his Exo-Suit.

*   **`[The Cleansing] Seed of Sylvana`**: A blessed seed given to the player by Sylvana. Planting it in the heart of a corrupted beast's lair will purify the area, creating a permanent safe zone.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/05_Consumables.md`
```md
# Items: Consumables

## **1.0. Core Philosophy: Preparation is Survival**

Consumables are single-use items that provide an instant effect, a temporary buff, or cure a negative status. A well-prepared player with a hotbar full of the right consumables can overcome challenges far above their level, while a powerful but unprepared player will quickly find themselves overwhelmed. The system is designed to reward foresight and active use of the Alchemy and Cooking systems.

---
## **2.1. Sustenance: Food & Drink**

These items are the primary way to manage the **Hunger** and **Thirst** needs. All cooked food provides a temporary, well-fed "buff" in addition to restoring hunger.

*   **Raw Food:**
    *   **Examples:** Raw Venison, Raw Fish, Foraged Berries, Strange Egg.
    *   **Effect:** Restores a small amount of Hunger but provides no buffs. Eating raw meat has a chance to inflict the **"Diseased"** status effect.

*   **Cooked Food:**
    *   **Requires:** A Campfire or a cooking station.
    *   **Examples:**
        *   **Grilled Steak:** Restores a large amount of Hunger and grants "Well Fed: +10 Health for 15 minutes."
        *   **Vegetable Stew:** Restores a moderate amount of Hunger and Thirst and grants "Well Fed: +15 Stamina for 20 minutes."
        *   **Mire-Cap Omelette:** A complex recipe. Restores Hunger and grants "Well Fed: +20 Poison Resistance for 30 minutes."

*   **Beverages:**
    *   **Examples:** Purified Water, Pine Needle Tea, Berry Juice.
    *   **Effect:** Restore Thirst. Teas and juices provide minor, short-term buffs like "Increased Stamina Regeneration" or "Cold Resistance." Unpurified "Murky Water" will quench thirst but has a high chance of causing disease.

---
## **2.2. Curatives: Potions & Tinctures**

These are alchemical concoctions designed to heal wounds and remove negative status effects.

*   **Health & Resource Potions:**
    *   **Potion of Minor Healing:** Restores a small amount of Health instantly.
    *   **Draught of Stamina:** Restores a large amount of Stamina instantly.
    *   **Elixir of Mana:** Restores a large amount of Mana instantly.

*   **Tinctures & Antidotes (Status Cures):**
    *   **Bandage:** Cures the **"Bleeding"** status effect. Crafted from Cloth.
    *   **Antidote:** Cures the **"Poisoned"** status effect. Requires Alchemy.
    *   **Tincture of Cleansing:** Cures the **"Diseased"** status effect.
    *   **Purifying Draught:** A rare potion that removes a small amount of the **"Corruption"** debuff when in a Blighted zone.

---
## **2.3. Elixirs: Combat & Utility Buffs**

These are advanced alchemical potions that provide powerful, temporary buffs to the player's attributes or abilities.

*   **Elixir of the Ironhide:** Increases Armor Rating by a large amount for 60 seconds.
*   **Draught of the Berserker:** Increases Melee Damage by 25% for 30 seconds, but also slightly reduces your Armor Rating.
*   **Tincture of Shadow:** Grants temporary invisibility for 30 seconds. Attacking or interacting with an object breaks the effect.
*   **Fire-Lichen Brew:** Grants 50% resistance to Fire damage and a small amount of Cold resistance for 5 minutes.
*   **Corrupting Draught:** Consuming a Blighted Crystal. Restores a huge amount of Health and Mana but inflicts a stacking "Corruption" debuff that can only be removed by resting.

---
## **2.4. Offensive & Tactical Consumables**

These are items that are thrown or used to directly affect the battlefield.

*   **Poisons (Crafted with Alchemy):**
    *   **Applied to weapons.**
    *   **Examples:**
        *   **Venom of Decay:** Deals poison damage over time.
        *   **Draught of Paralysis:** Has a chance to paralyze the target for a few seconds.
        *   **Essence of Stupor:** Drains the target's Stamina and Mana.

*   **Explosives & Grenades (Crafted with Alchemy/Tech):**
    *   **Makeshift Grenade:** A simple explosive that deals moderate area-of-effect physical damage.
    *   **Firebomb:** Creates a pool of burning fire on the ground.
    *   **Smoke Bomb:** Creates a thick cloud of smoke that blocks enemy line of sight, perfect for escapes or repositioning.
    *   **Stun Grenade:** A high-tech device that releases a flash and concussive blast, staggering all targets in a wide area.

*   **Magical Items:**
    *   **Soul Gem:** Used to trap souls for enchanting. Comes in various sizes. A filled Soul Gem is also consumed to recharge an enchanted weapon's power.
    *   **Scroll:** A single-use magic spell. A player who is not a mage can use a "Scroll of Fireball" to cast the spell once, consuming the scroll. Useful for non-magic builds to have a bit of utility.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/04_Tools.md`
```md
# Items: Tools and Utility

## **1.0. Core Philosophy: The Right Tool for the Right Job**

Tools are the essential items that enable interaction with the game world, particularly with its resources and crafting systems. The progression of tools is a fundamental gatekeeper for the player's advancement. A player cannot harvest iron ore until they have crafted or found a pickaxe capable of breaking the rock that holds it. This creates a clear and satisfying progression loop: craft a better tool to get better resources to craft better gear.

All tools have **Durability**. Using a tool slowly wears it down, and it will eventually break if not repaired at a workbench.

## **2.0. Harvesting Tools**

These tools are required to gather primary resources from the environment. Using a higher-tier tool on a lower-tier resource node will harvest it significantly faster.

#### **2.1. Axe**
*   **Use:** To chop down trees for wood. Also functions as a basic, one-handed weapon.
*   **Progression Tiers:**
    *   **Tier 1: Stone Axe:** Crafted from wood and flint. Can chop basic pine and oak trees.
    *   **Tier 2: Iron Axe:** Requires a forge. Can chop tougher trees like Ironwood.
    *   **Tier 3: Steel Axe:** Higher durability and chopping speed. Required for Petrified Wood in Blighted zones.
    *   **Tier 4 (Legendary): Dwarven Greataxe / Elven Swift-Axe:** Masterwork tools with unique properties (e.g., higher yield or faster swing speed).

#### **2.2. Pickaxe**
*   **Use:** To mine stone and ore deposits from rock faces.
*   **Progression Tiers:**
    *   **Tier 1: Flint Pickaxe:** Crafted from wood and flint. Can mine surface-level stone and copper deposits.
    *   **Tier 2: Iron Pickaxe:** Requires a forge. Can mine Iron Ore veins.
    *   **Tier 3: Steel Pickaxe:** Required to mine high-tier minerals like Obsidian and Titanium.
    *   **Tier 4 (Legendary): G.O.L.I.A.T.H.'s Seismic Drill:** A unique, powered tool that rapidly pulverizes any mineral deposit but is loud and consumes a power source.

#### **2.3. Skinning Knife / Dagger**
*   **Use:** To harvest hides, meat, and special components from animal and beast carcasses. Using a knife yields more resources than harvesting with a heavier weapon. Also functions as a fast, low-damage weapon.
*   **Progression Tiers:**
    *   **Tier 1: Bone Shiv:** Crafted from bone and fiber.
    *   **Tier 2: Iron Dagger:** More efficient and durable.
    *   **Tier 3: Steel Hunting Knife:** Has a higher chance to harvest rare components like pristine hides or alpha hearts.
    *   **Tier 4 (Legendary): Umbra's Sacrificial Blade:** A magical dagger that harvests more soul energy for Soul Gems upon a kill.

---
## **3.0. Utility & Crafting Tools**

These tools enable specific interactions or are required for advanced crafting recipes.

#### **3.1. Repair Hammer**
*   **Use:** To repair damaged player-built structures (walls, foundations, etc.). Consumes base materials from the player's inventory to perform repairs.
*   **Progression:** Can be crafted in Iron, Steel, etc. Higher tiers repair structures more efficiently, consuming fewer materials per point of health restored.

#### **3.2. Specialist Toolkits**
*   **Use:** Required to be in the player's inventory to perform certain advanced crafting or interactive tasks.
*   **Examples:**
    *   **Mechanics Wrench Set:** Required to repair vehicles and machinery.
    *   **Electronics Toolkit:** Required to craft and modify advanced tech items and hack electronic locks.
    *   **Jeweler's Kit:** Required to craft magical rings and amulets.
    *   **Alchemist's Satchel:** Reduces the weight of all alchemical ingredients in your inventory.

#### **3.3. Navigational Tools**
*   **Use:** To help the player find their way and manage their journey.
*   **Examples:**
    *   **Bedroll:** A portable, single-use item that allows the player to sleep almost anywhere to avoid the "Fatigue" debuff. Does not provide the "Well-Rested" buff that a proper bed does.
    *   **Compass:** A craftable or findable basic compass that is added to the HUD, allowing for easier navigation and communication in co-op.
    *   **Telescope / Binoculars:** A tool that allows for safe, long-distance scouting of enemy encampments and terrain features.

#### **3.4. Light Sources**
*   **Use:** To navigate dark caves and the night. Can be held in one hand, freeing the other for a one-handed weapon.
*   **Examples:**
    *   **Torch:** Basic, craftable from wood and cloth. Provides light and a small amount of heat. Can be used to set flammable surfaces on fire. Consumed over time.
    *   **Lantern:** Requires oil as fuel but provides a brighter, wider circle of light and is not extinguished by light rain.
    *   **Magelight Orb:** A magical, single-use item that can be thrown to stick to a surface, illuminating an area for several minutes.
    *   **Salvaged Headlamp:** A high-tier piece of tech that provides hands-free light but consumes a battery charge.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/03_Armor.md`
```md
# Items: Armor

## **1.0. Core Philosophy: The Trade-Off of Protection**

The Armor system in *Where Giants Rust* is built on a core principle: **every piece of protection comes at a cost.** Armor's primary purpose is to provide **Armor Rating (AR)**, a stat that directly mitigates incoming physical damage. However, this protection is balanced against penalties to weight, speed, and sound generation. The choice of armor is a deliberate tactical decision that defines a player's combat style, forcing them to choose between being a nimble glass cannon, a walking fortress, or a balanced fighter.

## **2.0. Armor Slots**

Armor is worn "over" the base apparel layers and consists of three primary slots. Some unique armor sets may include matching gauntlets and greaves that are part of the set bonus.

*   **Combat Headwear:** (Helmets, Greathelms)
*   **Body Armor:** (Cuirasses, Breastplates, Chainmail Shirts)
*   **Leg Armor:** (Greaves, Leg Plates)

## **3.0. Armor Weights & Archetypes**

Armor is categorized into three weight classes, each with a distinct profile of benefits and drawbacks.

#### **3.1. Light Armor**
*   **Materials:** Primarily made from Hide, Leather, and tough, reinforced cloth.
*   **Benefits:**
    *   Very lightweight.
    *   Minimal or no penalty to stamina regeneration and movement speed.
    *   Makes very little noise, ideal for stealthy playstyles.
*   **Drawbacks:** Offers the lowest Armor Rating. Provides little protection against heavy, staggering attacks.
*   **Ideal User:** Rogues, Rangers, and any character prioritizing mobility and stealth.

#### **3.2. Medium Armor**
*   **Materials:** A mix of materials like Scale Mail, Chainmail, or plates of hardened leather reinforced with metal.
*   **Benefits:**
    *   Offers a solid, balanced Armor Rating.
    *   Provides a good compromise between protection and mobility.
*   **Drawbacks:** Heavier than light armor. Noticeably louder, making stealth difficult. Incurs a minor penalty to stamina regeneration.
*   **Ideal User:** The jack-of-all-trades survivor. A good choice for players who want to be able to absorb a few hits without being slowed to a crawl.

#### **3.3. Heavy Armor**
*   **Materials:** Full suits of Iron, Steel, or other dense metals and alloys.
*   **Benefits:**
    *   Provides the highest possible Armor Rating and damage mitigation.
    *   Makes the wearer highly resistant to being staggered or knocked down.
*   **Drawbacks:** Extremely heavy, massively increasing encumbrance. Significantly reduces movement speed and stamina regeneration (until counteracted by perks). Generates a huge amount of noise, making stealth completely impossible.
*   **Ideal User:** Tanks, Juggernauts, and frontline warriors who intend to face the enemy head-on.

## **4.0. Armor Sets & Progression**

Armor progresses through material tiers and unique, crafted sets. Many sets provide a **Set Bonus** when all matching pieces are worn simultaneously.

#### **Standard Tiers**
*   **Hide & Leather Armor (Light):** The first tier of craftable armor, made from animal hides.
*   **Iron Armor (Heavy):** The first set of heavy plate armor a player can craft once they master basic smithing.
*   **Steel Armor (Medium/Heavy):** A direct upgrade from Iron, offering better protection for less weight.

#### **Factional & Cultural Sets**
*   **Elven Armor (Light):** Crafted with Elven techniques. Lightweight and offers a bonus to magical resistance.
*   **Dwarven Plate (Heavy):** Crafted with Dwarven techniques. Heavier than standard steel but offers superior Armor Rating and durability. *Set Bonus: Increased resistance to stagger.*
*   **Scrapper Plate (Medium):** A crude but effective armor made from salvaged scrap metal. Offers decent protection but has low durability and is very noisy. *Set Bonus: Minor resistance to damage from explosives.*

#### **Unique & Legendary Sets**
These are the ultimate, end-game armors, often requiring boss materials and legendary schematics to craft.

*   **Armor of the Rusted Giant:**
    *   **Description:** A massive suit of heavy armor forged from the fossilized, metal-infused bones of a fallen Giant.
    *   **Class:** Heavy
    *   **Set Bonus:** **Unstoppable.** You become completely immune to being knocked down by enemy power attacks.

*   **Aegis of the Sun-Sworn:**
    *   **Description:** A radiant suit of plate armor dedicated to Solana, polished to a brilliant shine.
    *   **Class:** Heavy
    *   **Set Bonus:** **Sun's Retribution.** When you block a heavy attack, the armor has a chance to release a blinding flash of light, stunning nearby enemies.

*   **Void-Woven Carapace:**
    *   **Description:** A suit of unsettling, silent medium armor made from Chitin plates and infused with shadow magic by a follower of Umbra.
    *   **Class:** Medium
    *   **Set Bonus:** **Shadow's Embrace.** When you perform a stealth kill, you become invisible for 3 seconds.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/02_Weapons.md`
```md
# Items: Weapons

## **1.0. Core Philosophy: The Tools of Survival and Dominion**

The weapons in *Where Giants Rust* are more than just stat sticks; they are the tangible expression of a character's skills, choices, and progression. The weapon system is designed to be diverse and satisfying, offering a clear and rewarding upgrade path from a crude stone axe to a legendary, magically-enchanted greatsword or a highly-modified salvaged rifle. Every weapon has a distinct feel, a specific tactical niche, and a deep connection to the game's crafting and combat systems.

## **2.0. Weapon Categories**

Weapons are divided into four primary categories, each governed by different skill trees and combat mechanics.

#### **2.1. One-Handed Melee**
*   **Description:** Fast, versatile weapons that allow for the use of a shield or an off-hand spell. Their damage is moderate, and they are governed by the **Warrior** skill tree.
*   **Weapon Types & Progression:**
    *   **Swords:** Balanced damage and speed. `(e.g., Rusty Shortsword -> Iron Longsword -> Steel Knight's Sword -> Elven Blade)`
    *   **Axes:** Slower than swords, with a higher chance to cause Bleed effects. `(e.g., Stone Hatchet -> Iron War Axe -> Dwarven War Axe -> Scrapper's Buzz-Axe)`
    *   **Maces/Hammers:** The slowest one-handed weapons, but they excel at staggering enemies and breaking through armor. `(e.g., Crude Club -> Iron Mace -> Steel Warhammer -> Heavy Dwarven Warhammer)`
    *   **Daggers:** Very fast swing speed but extremely short range and low base damage. They receive massive damage bonuses from stealth attacks. `(e.g., Bone Shiv -> Iron Dagger -> Umbral Stiletto)`

#### **2.2. Two-Handed Melee**
*   **Description:** Massive, high-risk, high-reward weapons that deal immense damage in a wide arc. They are slow, consume significant stamina, and prevent the use of a shield, but their raw power is unmatched. Governed by the **Warrior** skill tree.
*   **Weapon Types & Progression:**
    *   **Greatswords:** A balance of reach, speed, and damage, effective at cleaving through groups of unarmored enemies. `(e.g., Rusted Greatsword -> Steel Greatsword -> Dwarven Greatsword)`
    *   **Greataxes:** Slower than greatswords but deal devastating damage, with perks that excel at executing wounded foes. `(e.g., Orcish Greataxe -> Steel Greataxe -> Titanbone Chopper)`
    *   **Great Hammers:** The slowest and most powerful weapons. They are designed to shatter armor and knock down even the largest enemies. `(e.g., Stone Sledgehammer -> Iron Great Hammer -> The Rusted Giant's Fist)`

#### **2.3. Ranged (Physical)**
*   **Description:** Weapons that allow the player to engage enemies from a safe distance. Their use is governed by the **Marksman** skill tree and is limited by a finite supply of craftable or lootable ammunition.
*   **Weapon Types & Progression:**
    *   **Bows:** Silent and versatile. Damage is based on how long the bow is drawn. `(e.g., Crude Shortbow -> Hunter's Recurve Bow -> Elven Greatbow)`
    *   **Crossbows:** Slower to reload but easier to aim and offer higher base damage and armor penetration. `(e.g., Wooden Crossbow -> Steel Crossbow -> Dwarven Repeater Crossbow)`
    *   **Firearms:** The pinnacle of ranged tech. Very loud and use rare ammunition, but are extremely powerful and effective.
        *   `Salvaged Revolver`: Fast-firing sidearm.
        *   `Pump-Action Shotgun`: Devastating at close range.
        *   `Bolt-Action Hunting Rifle`: The ultimate sniper weapon.
        *   `Laser Rifle` (Legendary): A future-tech weapon that uses Energy Cells instead of bullets.

#### **2.4. Magical Implements (A Note)**
*   While spells from the "Grammar of Magic" system are the primary form of magic, certain physical items can act as catalysts or spell-casting tools.
*   **Staves:** A two-handed weapon that does not do melee damage. Instead, it can be used to cast a specific, pre-loaded spell without consuming the user's own Mana pool, drawing from the staff's own "charge" instead. They are essentially reusable, high-powered scrolls.
*   **Wands/Scepters:** A one-handed version of a staff, allowing it to be paired with a melee weapon or shield. They cast weaker spells but are more versatile.

## **3.0. Weapon Quality & Modifications**

*   **Quality Tiers:** Like other items, weapons are found or crafted in different rarities (Common, Uncommon, Rare, Epic, Legendary). A higher rarity means higher base damage and better scaling with player stats.
*   **Smithing Improvements:** Any physical weapon can be improved at a workbench, increasing its base damage.
*   **Enchanting:** Weapons can be magically enchanted at an Arcane Enchanter to add elemental damage, soul trap effects, or other magical properties.
*   **Tech Mods:** Firearms and some advanced crossbows can be modified at a Tech Workbench with attachments like scopes, suppressors, and extended magazines.
*   **Coatings & Poisons:** Any physical weapon can have a temporary poison or elemental oil applied to it via the Alchemy system.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/01_Resources_and_Materials.md`
```md
# Items: Resources and Materials

## **1.0. Core Philosophy: The Progression Ladder**

The resource system in *Where Giants Rust* is a core driver of progression. Players begin with access to only the most basic materials, and through crafting better tools, leveling up skills, and exploring more dangerous biomes, they gain the ability to harvest and refine higher-tier resources. This creates a satisfying loop: better resources allow for better gear, which allows for exploration into harder areas, which contain even better resources.

## **2.0. Resource Tiers**

Materials are organized into five conceptual tiers, which govern their rarity, location, and the quality of the gear they can create.

*   **Tier 0: Primitive** - Things you can gather with your bare hands.
*   **Tier 1: Basic** - Requires simple, crafted tools (e.g., Stone Axe, Flint Pickaxe).
*   **Tier 2: Advanced** - Requires sturdy metal tools (e.g., Iron Pickaxe). Found in more challenging biomes.
*   **Tier 3: Exotic** - Requires specialized, high-quality tools. Only found in dangerous, end-game biomes.
*   **Tier 4: Legendary** - Not harvested, but acquired as rare drops from world bosses, dungeon chests, or as quest rewards.

---
## **3.0. Material Categories & Examples**

### **3.1. Wood**
Harvested from trees. Primary component for early-game structures, tools, and weapons.
*   **Tier 0: Dry Branches** (Found on the ground)
*   **Tier 1: Pine / Oak Wood** (From forests, requires a Stone Axe)
*   **Tier 2: Ironwood** (From swamps, requires an Iron Axe)
*   **Tier 3: Petrified Wood** (From Blighted zones, requires a Steel Axe, has innate magical resistance)

### **3.2. Stone & Minerals**
Mined from rock formations and veins. Primary component for structures, tools, and smelting into metals.
*   **Tier 0: Loose Rocks / Flint** (Found on the ground)
*   **Tier 1: Stone / Copper Ore / Clay** (From plains and forests, requires a Flint Pickaxe)
*   **Tier 2: Iron Ore / Silver Ore** (From mountains, requires an Iron Pickaxe)
*   **Tier 3: Obsidian / Titanium Ore** (From volcanic zones, requires a Steel Pickaxe)

### **3.3. Metals (Refined Goods)**
Created by smelting ores at a forge. The backbone of all advanced gear.
*   **Tier 1: Copper Ingot** (Smelted from Copper Ore)
*   **Tier 2: Iron Ingot / Steel Ingot** (Iron + Coal)
*   **Tier 3: Titanium Ingot / Hardened Steel**
*   **Tier 4: Dwarven Metal / Blight-Hardened Steel** (Legendary alloys requiring unique recipes and reagents)

### **3.4. Hides & Fibers**
Harvested from animals and plants. Used for light/medium armor, bindings, and textiles.
*   **Tier 0: Plant Fiber** (From small bushes)
*   **Tier 1: Scrap Cloth / Leather Scraps** (From humanoid enemies and common animals like deer)
*   **Tier 2: Hardened Leather / Spider Silk** (From tougher beasts like boars or giant spiders)
*   **Tier 3: Drake Hide / Chitin Plate** (From powerful, armored beasts)
*   **Tier 4: Shadow-Stitched Silk** (A magical cloth from a special dungeon)

### **3.5. Alchemical Reagents**
Harvested from unique plants, fungi, and creatures. Used in the Alchemy system.
*   **Tier 1: Redcap Mushroom / Bluepetal Flower** (Common)
*   **Tier 2: Mire-Cap / Gravebloom** (Biome-specific: Swamps and Titan's Fall)
*   **Tier 3: Fire-Lichen / Frost Mirriam** (Biome-specific: Volcanic and Mountain zones)
*   **Tier 4: Heart of an Alpha** (Boss-specific drop)

### **3.6. Magical & Exotic Components**
Specialized materials required for enchanting, high-tier crafting, and unique recipes.
*   **Tier 1: Soul Fragment** (From defeated spirits, used to fill Soul Gems)
*   **Tier 2: Blighted Crystal Shard** (From Blighted enemies)
*   **Tier 3: Uncut Gems (Ruby, Sapphire, etc.)** (From mining rare veins)
*   **Tier 4: A God's Tear / Corrupted AI Core** (Legendary, quest-related components)

### **3.7. Salvaged Technology**
Scavenged from modern ruins and robotic enemies. Used in the Tech skill tree.
*   **Tier 1: Scrap Metal / Plastic / Broken Wires** (Common junk)
*   **Tier 2: Electronic Circuitry / Copper Wire / Gears**
*   **Tier 3: Pristine Micro-Servos / Intact Power Core / Ballistic Components**
*   **Tier 4: De-weaponized Subroutine Fragment / Intact Neuro-Interface** (Legendary tech)
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/07_Equipment_and_Apparel/08_Accessories.md`
```md
# Equipment: Accessories (Trinkets, Charms & Augments)

## **1.0. Core Philosophy: The Final Layer of Customization**

Accessories are the most granular level of gear customization. They are small, often non-obvious items that provide **minor, specialized, passive bonuses.** They are not a primary source of power but are crucial for fine-tuning a build, reflecting a character's history, beliefs, or lucky finds. An Accessory might be a carved rune tied to a sword's pommel, a patched-on faction emblem on a jacket, or a unique focusing crystal slotted into an AI's housing.

This system is about adding personality and a final 10% of optimization to a player's loadout.

## **2.0. The Mechanics: Accessory Slots**

Most major pieces of gear (weapons, armor, tools) can have **1-2 Accessory Slots**. These slots are initially empty. Accessories are separate items that must be found or crafted and then installed into these slots at a **Tinker's Workbench**—a new, specialized crafting station.

*   **Acquisition:** Accessories are found as loot in the world, given as minor quest rewards, or crafted by players with high skill in specific disciplines.
*   **Installation:** Requires a Tinker's Workbench. Is a simple process.
*   **Removal:** Removing an accessory is also simple, but has a small chance to destroy the accessory, making the decision to swap them a tactical one.

---
## **3.0. Weapon & Tool Accessories**

These are attached directly to melee weapons, ranged weapons, and harvesting tools.

*   **Grip Wraps:**
    *   **Description:** Strips of leather, cloth, or special fibers wrapped around the handle.
    *   **Examples:**
        *   `Rough Leather Grip`: Slightly reduces stamina cost for power attacks.
        *   `Rubberized Grip`: Slightly increases weapon swap speed.
        *   `Blessed Linen Wrap`: A tiny bonus to mana regeneration while the weapon is held.

*   **Pommel Stones & Counterweights:**
    *   **Description:** Small, weighted objects affixed to the end of a melee weapon's hilt to alter its balance.
    *   **Examples:**
        *   `Iron Counterweight`: Increases stagger chance but slightly reduces attack speed.
        *   `Polished River Stone`: A "lucky charm" that grants a tiny (+1%) bonus to critical hit chance.

*   **Carved Runes & Fetishes:**
    *   **Description:** Small, enchanted objects tied to the weapon or tool. They provide a faint echo of a full magical enchantment.
    *   **Examples:**
        *   `Smoldering Ember Rune`: Adds +1 Fire damage to each hit.
        *   `Wolf's Tooth Fetish`: Deals +5% damage against Beast-type enemies.
        *   `Dwarven Carbide Tip` (for Pickaxes): Tool loses durability 10% slower.

---
## **4.0. Apparel & Armor Accessories**

These are patches, pins, charms, and small utility items attached to clothing and armor.

*   **Faction Emblems & Patches:**
    *   **Description:** Sewn-on patches or pinned metal emblems that signify allegiance or favor.
    *   **Examples:**
        *   `Hearthguard Settler's Patch`: Gain slightly better prices when bartering with Hearthguard NPCs.
        *   `Umbral Elf Shadow-Pin`: Slightly reduces detection radius in darkness.

*   **Holy Symbols & Wards:**
    *   **Description:** Small, blessed objects that offer minor divine protection.
    *   **Examples:**
        *   `Tiny Sun Symbol of Solana`: +5% resistance to Corruption.
        *   `Woven Twig of Sylvana`: Health potions are 5% more effective.
        *   `Fjolnir's Pebble`: A small stone that grants +1% Damage Resistance.

*   **Utility Pouches & Attachments:**
    *   **Description:** Small, modular add-ons for Chest Rigs and Belts.
    *   **Examples:**
        *   `Small Grenade Pouch`: Adds one dedicated slot for a grenade.
        *   `Sheath/Holster Attachment`: Can be added to a belt to hold a knife or sidearm for faster access.
        *   `Canteen Holder`: Allows a water skin to be equipped for a quick drink without opening the main inventory.

*   **Mementos:**
    *   **Description:** Items with purely personal, sentimental value. Their boons are subtle and psychological.
    *   **Example:** A `Scorched Locket` found in a specific ruin. Equipping it does nothing outwardly, but for a Kai Sterling player, it might provide a unique, quiet buff like "+2% XP gain from all sources" as they are driven by Anya's memory.

---
## **5.0. Companion Accessories (Late-Game System)**

This system is unlocked by building a high-tier **AI Diagnostic & Maintenance Station**. It allows the player to install minor software and hardware upgrades into their active AI companion's core programming or housing.

*   **Data Fragments & Sub-Subroutines (Software):**
    *   **Description:** Small snippets of code salvaged from other AI units or data caches.
    *   **Examples:**
        *   `Geological Survey Fragment`: When installed in A.R.I.A., allows her to detect the nearest Iron Ore deposit, but has a long cooldown. A much weaker version of G.O.L.I.A.T.H.'s main ability.
        *   `Threat Matrix Fragment`: When installed in H.E.R.A., allows her to provide one extra tactical detail (e.g., "High Armor") after her lore dissertation.
        *   `Lexicon Fragment`: When installed in C.A.I.N., he will begrudgingly provide the name of the creature he is analyzing, and nothing more.

*   **Chassis & Housing Mods (Hardware):**
    *   **Description:** Physical upgrades to the AI's mobile projector or rig interface.
    *   **Examples:**
        *   `Hardened Casing`: A.R.I.A. is less likely to suffer a "glitch" when the player takes a heavy hit.
        *   `Amplified Speaker`: G.O.L.I.A.T.H.'s constant complaints about inefficiency now have a tiny chance to de-buff nearby enemies' morale, making them slightly less aggressive.
        *   `Optical Filter`: V.E.G.A.'s visual corruption effect on the player's HUD is slightly lessened, making it easier to see.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/07_Equipment_and_Apparel/07_Exo-Suits_and_Mods.md`
```md
# Equipment: Exo-Suits & Mods

## **1.0. Core Philosophy: The Ultimate Commitment**

**Exo-Suits** represent the apex of character specialization. They are not simple armor; they are powered, full-body augmentation frames that fundamentally change how a character interacts with the world. Equipping an Exo-Suit is a major commitment that disables most other gear slots but provides unparalleled power in a single, focused discipline.

This system is designed as an end-game pursuit, requiring players to hunt for rare schematics, defeat powerful bosses for unique components, and invest heavily in their base's infrastructure to build and maintain these powerful machines.

## **2.0. The Exo-Suit System**

#### **2.1. The "Exo-Slot"**
*   A dedicated, single equipment slot on the character screen.
*   Equipping an Exo-Suit will automatically un-equip and disable the following slots: **Body Armor, Leg Armor, Outerwear,** and **Back Gear**. The Exo-Suit provides its own base protection and utility, replacing all of them.

#### **2.2. Power Consumption**
*   All Exo-Suits require a **Power Core** to function. This is a craftable or rechargeable item that slowly depletes while the suit is active.
*   Strenuous actions (sprinting, power attacks, using special abilities) drain the core much faster. If the Power Core runs out, the suit powers down, providing no benefits and applying a severe **"Dead Weight"** debuff (massive encumbrance and reduced speed) until the core is replaced or recharged.

#### **2.3. Modularity**
*   The primary form of customizing an Exo-Suit is through **Exo-Mods**. Each suit has a limited number of **Modification Slots** (typically 2 to 4).
*   Exo-Mods are rare, craftable components that can be installed at a "Tech Workbench" to provide specific bonuses or new abilities to the suit.

---
## **3.0. The Core Exo-Suits**

#### **3.1. [IND-01] The "Mule" Industrial Rig**
*   **Archetype:** Juggernaut / Mobile Workstation
*   **Source:** Schematics and parts found in derelict factory complexes and guarded by industrial automatons.
*   **Primary Function:** Brute force and resource hauling.
*   **Base Stats:**
    *   Massive bonus to Armor Rating and Damage Resistance.
    *   Immunity to stagger from most standard attacks.
    *   Huge bonus to Carry Weight (+100 kg).
    *   Increases Melee Damage and Mining Speed.
*   **Downsides:** Significantly reduces movement speed. Extremely loud, making stealth impossible. High power consumption.
*   **Mod Slots:** 4 (focused on defense and utility).

#### **3.2. [RCN-03] The "Stalker" Recon Frame**
*   **Archetype:** Infiltrator / High-Speed Scout
*   **Source:** Schematics and rare components found in the wreckage of a military spec-ops site.
*   **Primary Function:** Unmatched mobility and stealth.
*   **Base Stats:**
    *   Significantly increases movement, sprint, and dodge speed.
    *   Increases jump height and negates all fall damage.
    *   Massively reduces movement noise.
*   **Downsides:** Offers very little armor protection. No bonus to carry weight. Power drains quickly while sprinting.
*   **Mod Slots:** 3 (focused on speed and stealth).

#### **3.3. [AET-07] The "Capacitor" Aetheric Rig**
*   **Archetype:** Archmage / Mana Battery
*   **Source:** A unique fusion of tech and magic found in a Pre-Cataclysm Arcane Research facility or Observatory.
*   **Primary Function:** Amplification of magical abilities.
*   **Base Stats:**
    *   Provides a massive bonus to the player's Maximum Mana pool (+150 Mana).
    *   Increases the power and duration of all cast spells.
    *   Slowly recharges the user's Mana while active.
*   **Downsides:** Fragile. Provides almost no physical armor. Has a weakness to Shock damage, which can cause the suit to "Overload," stunning the user.
*   **Mod Slots:** 3 (focused on magical enhancements).

---
## **4.0. Exo-Mod Examples**

Exo-Mods are the key to customizing a suit for a specific purpose. They are crafted items requiring rare resources.

*   **Defensive Mods:**
    *   **Reinforced Plating:** Increases the suit's base Armor Rating.
    *   **Ablative Coating:** Grants a high amount of resistance to a specific element (Fire, Frost, etc.).
    *   **Kinetic Dampeners:** Reduces stagger received from heavy enemy attacks.

*   **Utility Mods:**
    *   **Backup Power Cell:** Increases the suit's total Power Core capacity by 25%.
    *   **Scanner Suite:** Adds a G.O.L.I.A.T.H-style resource scanner to the suit's HUD.
    *   **Hydro-Servos:** Negates all movement penalties when walking through water or deep snow.

*   **Offensive Mods:**
    *   **Pressurized Pistons:** Increases the suit's melee damage output.
    *   **Targeting Computer:** Increases accuracy and critical hit chance with ranged weapons.
    *   **Tesla Coils:** Causes the suit to periodically release a small nova of shock damage when hit in melee.

*   **Suit-Specific Mods:**
    *   **(Mule Only) Mining Drill Arm:** Replaces one arm with a powered drill, massively increasing mining speed but disabling the ability to use two-handed weapons.
    *   **(Stalker Only) Chameleon Field:** Consumes a large amount of power to grant temporary invisibility while standing still.
    *   **(Capacitor Only) Arcane Siphon:** A small portion of damage taken is converted into Mana.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/07_Equipment_and_Apparel/06_Back_Gear_(Backpacks_pouches).md`
```md
# Equipment: Back Gear (Backpacks & Specialized Rigs)

## **1.0. Core Philosophy: The Survivor's Lifeline**

The "Back" equipment slot is dedicated to items designed for hauling gear, supplies, and specialized equipment over long distances. The player's choice of back gear is a fundamental decision that defines their role on any given expedition. Are they a scavenger hauling loot, a hunter carrying a prized kill, or a specialist deploying unique equipment? The item on their back dictates the answer.

Nearly all back gear is mutually exclusive with **Exo-Suits**. A player cannot benefit from a backpack while wearing a full-body exo-frame.

## **2.0. Standard Backpacks: Carry Capacity**

This is the most common and essential category of back gear. Their primary function is to increase the player's maximum **Carry Weight**.

*   **Tier 1: Makeshift Satchel**
    *   **Description:** The most basic bag, crafted from scrap cloth and fiber. It's flimsy and small.
    *   **Stats:** Provides a minimal **+10 kg** Carry Weight bonus. Low durability.
    *   **Source:** Craftable from the start.

*   **Tier 2: Worn Rucksack / School Backpack**
    *   **Description:** A common backpack found in modern residential ruins. Decent size and durability.
    *   **Stats:** Provides a solid **+25 kg** Carry Weight bonus.
    *   **Source:** Common loot in suburban areas.

*   **Tier 3: Hiker's Frame Pack**
    *   **Description:** A large, sturdy backpack built on a rigid metal or composite frame, designed for serious wilderness trekking.
    *   **Stats:** Provides a massive **+50 kg** Carry Weight bonus, but is heavy and applies a minor penalty (-5%) to stamina regeneration due to its cumbersome nature.
    *   **Source:** Crafted with high-tier materials, or found rarely at abandoned ranger stations or campsites.

## **3.0. Specialized Rigs & Packs: Utility Over Capacity**

These are advanced items that sacrifice carry weight in favor of a unique, powerful utility function. They are for players who have a very specific job to do.

*   **Quiver**
    *   **Description:** A leather or composite quiver designed for archers.
    *   **Function:** Does not increase carry weight. Instead, it allows the player to carry several different types of arrows at once (e.g., standard, fire, poison) and swap between them instantly without opening the inventory. Increases the speed at which you nock an arrow by 15%.
    *   **Ideal User:** A dedicated Marksman (Archer build).

*   **Field Communications Pack**
    *   **Description:** A salvaged military radio pack with a large antenna.
    *   **Function:** Slightly increases carry weight (+5 kg). Its primary function is providing a team-wide buff. All allied players on the map gain a "Coordinated" status, which refreshes their compass information more frequently and highlights enemies that have been marked by the wearer.
    *   **Ideal User:** A support-focused character in a co-op team, like Sofia Rossi or Kenji Tanaka.

*   **Portable Oxygen Tank**
    *   **Description:** A specialized piece of industrial or medical equipment.
    *   **Function:** Offers no carry weight bonus. Its sole purpose is to allow the player to breathe in hazardous environments, making them immune to the effects of **Toxic Air** in swamps or near volcanic vents for a limited time (based on the tank's capacity). Essential for exploring certain dungeons.
    *   **Ideal User:** Any player looking to venture into specific, highly hazardous zones.

## **4.0. Legendary Back Gear**

These are unique, end-game items that are a major reward for completing difficult quests or defeating powerful bosses.

*   **The Wanderer's Satchel ("Bag of Holding")**
    *   **Description:** An unassuming but magically infused satchel that hums with a faint energy.
    *   **Function:** This legendary item does not increase the carry weight stat directly. Instead, it uses **Spatial Magic** to negate a large amount of the weight of the items placed inside it. It has an internal "weight negation" limit.
    *   **Synergy:** As established, this item synergizes directly with the **Telekinesis** magic skill. A player proficient in that skill can actively stabilize and boost the bag's enchantment, dramatically increasing the amount of weight it can negate, making it the single best carrying solution in the game for a powerful mage.

*   **Cloak of the Pack-Mule**
    *   **Description:** A simple-looking but surprisingly sturdy cloak enchanted by a follower of Volo, the Trickster god.
    *   **Function:** Provides a moderate carry weight bonus (+20 kg), but its true power is a unique enchantment: **all resources (Wood, Stone, Ore, Hides) stacked within your inventory weigh 50% less.** This makes it the ultimate backpack for a dedicated resource-gathering character. It doesn't allow you to carry more *items*, but the items you do carry are far lighter.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/07_Equipment_and_Apparel/05_Utility_Gear_(Belts_Rigs_slings).md`
```md
# Equipment: Utility Gear (Belts, Rigs & Slings)

## **1.0. Core Philosophy: Functional Modularity**

Utility Gear is the layer of equipment worn over all apparel and armor. Its purpose is not defense, but **functionality, access, and efficiency.** This system is highly modular, allowing players to tailor their "loadout" to a specific task, whether it's combat, construction, or exploration. Belts, Rigs, and Slings determine how quickly a player can access their tools and consumables, and how much specialized gear they can carry.

## **2.0. The "Sling" Slot: Weapon Readiness**

This is a dedicated slot that governs how a player carries their primary weapons. Equipping a sling frees up the player's hands while keeping their weapon instantly accessible.

*   **No Sling (Default):** Weapons are stowed in the backpack. Swapping to a stowed primary weapon is slow.
*   **Simple Rope Sling:** A basic craftable sling. Allows one primary weapon (a rifle or a two-handed melee weapon) to be carried on the back, enabling a much faster weapon swap speed.
*   **Tactical Gun Sling:** A salvaged military-grade sling for rifles and shotguns. Offers the fastest weapon swap speed for those weapons and slightly reduces aim-down-sights time after swapping.
*   **Weapon Holster (Sidearm):** A specialized piece of gear often attached to the leg slot or a belt. It allows a pistol to be drawn almost instantaneously. Some tactical rigs include a built-in holster.

## **3.0. The "Belt" Slot: The Utility Foundation**

The belt is the foundation of a player's utility loadout. Better belts provide slots for specialized attachments.

*   **Makeshift Rope Belt:** The most basic option. Does little more than hold up the character's pants. Has **zero attachment slots**.
*   **Worn Leather Belt:** A standard, sturdy belt. Provides **one attachment slot**.
*   **Foreman's Construction Belt:**
    *   **Description:** A heavy-duty leather and canvas tool belt with large, reinforced loops.
    *   **Effect:** Unlocks **four specialized "Tool Loops."** These can only hold harvesting or repair tools (Axe, Pickaxe, Hammer). Reduces the weight of all tools equipped in these loops by 75%. Provides no slots for combat pouches.
*   **Tactical Webbing Belt:**
    *   **Description:** A modern, military-style belt made of durable nylon with a MOLLE-style grid.
    *   **Effect:** Provides **three modular attachment slots** that can accept any type of pouch, holster, or utility carrier.
*   **Alchemist's Bandolier:**
    *   **Description:** A leather strap worn across the chest that also occupies the Belt slot. It features numerous small, glass-lined loops and pouches.
    *   **Effect:** Does not have modular slots. Instead, it has **four dedicated "Potion Slots"** and **four dedicated "Grenade Loops."** Reduces the weight of all alchemical items by 50%.

## **4.0. The "Chest Rig" Slot: Immediate Access Combat Gear**

Worn over all armor and outerwear, the chest rig is all about keeping combat essentials within arm's reach.

*   **None (Default):** The player must access their backpack for most items, which is slow in combat.
*   **Scrapper's Chest Rig:**
    *   **Description:** A crude piece of gear stitched together from old tires, leather, and salvaged webbing.
    *   **Effect:** Provides **two quick-slots** for consumables and has **one modular attachment slot**. Offers a tiny amount of bonus armor rating due to its junk-plate construction.
*   **Light Recon Rig:**
    *   **Description:** A minimalist harness with just a few pouches.
    *   **Effect:** Provides **two modular attachment slots**. Does not penalize stamina regeneration, making it ideal for scouts and long-range explorers.
*   **Tactical Assault Rig:**
    *   **Description:** A full-coverage military-style plate carrier rig.
    *   **Effect:** Provides **four modular attachment slots**. Offers a significant bonus to armor rating on the torso, but is heavy and slightly reduces mobility. The choice for a frontline soldier.
*   **Field Medic Bag:**
    *   **Description:** A specialized satchel and harness system worn on the chest.
    *   **Effect:** Does not have modular slots. Provides **six dedicated "Medical Slots"** for items like bandages, healing potions, and antidotes. Using a medical item from this rig is 50% faster than normal. The essential gear for a dedicated support character like Sofia Rossi.

This detailed, modular system creates a deep strategic layer where a player might equip a Construction Belt and a Recon Rig for a building expedition, but swap to a Tactical Belt and an Assault Rig before raiding an enemy compound.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/07_Equipment_and_Apparel/04_Hands_and_Feet_(Gloves_Boots).md`
```md
# Equipment: Hands & Feet (Gloves, Boots & Socks)

## **1.0. Core Philosophy: The Points of Contact**

The Hands and Feet slots represent the player's direct interface with the world. Gloves affect how the player interacts with tools and the environment, while socks and boots determine their mobility, sound profile, and resilience to ground-level hazards. These pieces are not just for stat bonuses; they provide tangible, contextual benefits that reward thoughtful preparation.

## **2.0. Equipment Slots**
*   **Hands:** Accepts gloves, mittens, and gauntlets.
*   **Feet (Socks):** Accepts all under-layer footwear. This layer is crucial for temperature management.
*   **Feet (Boots):** Accepts all outer footwear, worn over the sock layer.

## **3.0. Hands - Gloves & Gauntlets**
*(This section is unchanged.)*

## **4.0. Feet - Socks**
*(This section is unchanged.)*

## **5.0. Feet - Boots**

Boots determine how the player moves through the world, affecting speed, protection, and, critically, their **Acoustic Profile**. This stat directly modifies the `acoustic_mass` of the Phonons generated by footsteps, determining how easily enemies can hear the player.

*   **Tier 1: Basic Footwear**
    *   **Worn Sneakers / Trainers:**
        *   **Description:** Common, lightweight starter footwear found in modern ruins. A balanced, unremarkable option.
        *   **Acoustic Profile:** `Average`.
    *   **Makeshift Foot-Wraps:**
        *   **Description:** Crafted from leather scraps and fiber. Offer minimal protection but are extremely quiet.
        *   **Acoustic Profile:** `Very Quiet`. Ideal for early-game stealth.

*   **Tier 2: Specialized Footwear**
    *   **Sturdy Hiking Boots:**
        *   **Description:** The best all-rounder. Provide good traction, moderate armor, and decent durability.
        *   **Acoustic Profile:** `Average`.
    *   **Tactical Boots:**
        *   **Description:** Military-grade footwear with hard, reinforced soles. Offer a good balance of protection and mobility, and significantly reduce the stamina cost of sprinting.
        *   **Acoustic Profile:** `Loud`. The hard soles create a distinct, heavy sound on hard surfaces, making them poor for stealth.
    *   **Rubber Wellingtons:**
        *   **Description:** Found in industrial or farm areas. Offer almost no armor but make the wearer completely immune to negative effects from walking in shallow water or mud.
        *   **Acoustic Profile:** `Quiet`. The soft rubber dampens sound effectively on most surfaces.

*   **Tier 3: Advanced & Factional Footwear**
    *   **Mountain Climbing Boots:**
        *   **Description:** A rare item designed for alpine environments. Provides excellent traction and good Cold Resistance.
        *   **Acoustic Profile:** `Loud`. Often feature crampons or other hard points that are noisy on rock.
    *   **Umbral Elve's Silent-Tread Boots:**
        *   **Description:** A magical item obtained from the Umbral Elves.
        *   **Acoustic Profile:** `Silent`. Enchanted to generate almost no sound on any surface, a master assassin's greatest tool.
    *   **Steam-Bound Stompers:**
        *   **Description:** A heavy, noisy boot crafted by the Cindexr-Gear Dwarves with reinforced steel toes and steam-piston heels. Allows the player to perform a "stomping" area-of-effect attack by jumping from a height.
        *   **Acoustic Profile:** `Very Loud`. Announce your presence from a great distance.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/07_Equipment_and_Apparel/03_Outerwear_Apparel_(Jackets_Cloaks).md`
```md
# Equipment: Outerwear Apparel (Jackets, Cloaks & Coats)

## **1.0. Core Philosophy: The Environmental Shield**

Outerwear is the second major layer of apparel, worn over the **Torso (Base Layer)**. Its primary purpose is to provide **powerful, specialized environmental resistance** and significant passive buffs. Outerwear items are typically heavier and bulkier than base layers, and their effects are more pronounced.

A player might wear a simple t-shirt for day-to-day work around the base, but they will don a heavy parka or a waterproof trench coat before venturing into a dangerous climate. Visually, this is one of the most important layers for defining a character's silhouette and style.

## **2.0. Outerwear Properties**

In addition to the standard **Cold Resistance**, **Heat Resistance**, **Weight**, and **Durability**, some outerwear introduces a new property:

*   **Wetness Resistance:** A numerical value that determines how quickly the player becomes "Soaked" during rain, which can lead to negative effects like increased cold and reduced mobility.

## **3.0. Outerwear Categories & Examples**

#### **3.1. Light Outerwear**
These items offer moderate bonuses with minimal weight penalties, ideal for temperate climates or players who value mobility.

*   **Denim Jacket / Leather Vest**
    *   **Description:** Common, durable outerwear found in modern ruins.
    *   **Stats:** Provides a small amount of extra armor and balanced, minor resistances. A solid, early-game choice.
*   **Scout's Cloak**
    *   **Description:** A simple, hooded cloak of dark, dyed cloth.
    *   **Stats:** Offers no significant elemental resistance, but grants a tangible bonus to the wearer's **Stealth** rating, making them harder to detect in shadows or foliage.
*   **Canvas Duster / Trench Coat**
    *   **Description:** A long coat designed to protect from wind and rain.
    *   **Stats:** Provides excellent **Wetness Resistance**, keeping the player dry and preventing the "Soaked" debuff during storms.

#### **3.2. Heavy Outerwear**
These items are heavy-duty pieces of equipment designed to fully negate the harshest environmental effects, but they are heavy and can be cumbersome.

*   **Mountain Parka**
    *   **Description:** A thick, fur-lined parka, salvaged or crafted from the hides of alpine beasts.
    *   **Stats:** Unmatched **Cold Resistance**. It is nearly impossible to survive a mountain blizzard without a garment of this quality. It is very heavy and provides poor heat resistance.
*   **Desert Poncho**
    *   **Description:** A large, thick, but breathable poncho designed to shield the wearer from the brutal sun while allowing airflow.
    *   **Stats:** Provides exceptional **Heat Resistance** and slightly reduces the rate of thirst in hot climates.
*   **Blacksmith's Apron**
    *   **Description:** A heavy apron of thick, treated leather worn over the torso and legs. Occupies both the "Outerwear" and a "Leg Gear" slot visually.
    *   **Stats:** Its primary purpose is to provide a massive amount of **Fire Resistance**, essential for anyone working a forge or exploring a volcanic region.

#### **3.3. Unique & Factional Outerwear**
These are rare, high-tier items that provide unique, powerful effects.

*   **Sylvan Elve's Verdant Cloak**
    *   **Description:** A cloak woven from living leaves that seems to shift and adapt to the environment. A quest reward or high-tier barter item from the Sylvan Elves.
    *   **Stats:** Provides a dynamic chameleon effect, granting a very high **Stealth** bonus when standing still in natural environments (forests, plains).
*   **Umbral Elve's Shadow-Weave Mantle**
    *   **Description:** A cloak that seems to drink the light around it, stitched with thread that shimmers with Void energy.
    *   **Stats:** Offers a good stealth bonus but its true power is **muffling sound**, drastically reducing the noise made by the player's movement and actions.
*   **The Survivor's Greatcoat**
    *   **Description:** A legendary, one-of-a-kind coat patched together from the hides of a dozen different powerful beasts.
    *   **Stats:** The ultimate all-rounder. Provides excellent, balanced resistances to Cold, Heat, and Wetness, and has a multitude of pockets that grant a passive **+10 kg Carry Weight** bonus. A true masterwork of survival craft.

This system ensures that the player must maintain a "wardrobe" of different outerwear options, choosing the right coat for the journey ahead, which deeply enhances the preparation and immersion of the survival experience.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/07_Equipment_and_Apparel/02_Base_Layer_Apparel_(Shirts_Pants).md`
```md
# Equipment: Base Layer Apparel (Shirts, Pants & Underwear)

## **1.0. Core Philosophy: The First Line of Defense**

Base Layer Apparel consists of the clothing worn directly against the skin. These are not primary sources of "Armor Rating" (which mitigates combat damage), but they are the **most important items for Environmental Resistance.** A player's choice of shirt and pants is their first and most critical line of defense against the harsh climates of the Shattered World.

These items are divided into two main slots: **Torso (Base Layer)** and **Legs (Base Layer)**. Some special full-body suits will occupy both slots simultaneously.

## **2.0. Base Layer Properties**

Every piece of base layer apparel is defined by a few key stats:

*   **Cold Resistance:** A numerical value that determines how slowly the player's "Cold" meter fills in freezing environments.
*   **Heat Resistance:** A numerical value that determines how slowly the player's "Heat" meter fills in hot environments.
*   **Weight:** How much the item contributes to the player's total encumbrance.
*   **Durability:** How quickly the item wears out from use and combat. Worn-out clothing provides reduced benefits.

## **3.0. Torso (Base Layer) - Shirts**

#### **Tier 1: Common Apparel**
*   **Tattered T-Shirt**
    *   **Description:** A simple, worn cotton shirt. The most common starting item, salvaged from modern ruins.
    *   **Stats:** Minimal resistances. Very lightweight.
*   **Flannel Shirt**
    *   **Description:** A durable, plaid button-up shirt. The workhorse of early-game apparel.
    *   **Stats:** Provides a decent balance of Cold and Heat resistance, making it a good all-rounder for temperate zones.
*   **Tank Top**
    *   **Description:** A lightweight, sleeveless shirt.
    *   **Stats:** Provides a small amount of Heat Resistance but has negative Cold Resistance (making you get colder faster). Ideal for deserts or volcanic zones.

#### **Tier 2: Specialized & Crafted Apparel**
*   **Wool Shirt / Tunic**
    *   **Description:** A thick shirt crafted from wool harvested from mountain animals.
    *   **Stats:** Excellent Cold Resistance, but poor Heat Resistance. Essential for any mountain expedition.
*   **Linen Shirt**
    *   **Description:** A light, breathable shirt crafted from flax or a similar fiber.
    *   **Stats:** Excellent Heat Resistance. The best choice for hot climates.
*   **Scrapper's Reinforced Shirt**
    *   **Description:** A standard shirt crudely reinforced with patches of scrap leather and metal.
    *Of course. This   **Stats:** Offers a tiny amount of actual Armor Rating (+1 or +2) at the cost of being heavier and having poor elemental resistances.

#### **Tier 3: Advanced & Rare Apparel**
*   **Thermal Underwear Top**
    *   **Description:** A high-tech undergarment salvaged from military or mountaineering supplies.
    *   **Stats:** Unmatched Cold Resistance for its very low weight.
*   **Spider-Silk Shirt**
    *   **Description:** Crafted from the silk of giant spiders. A rare and valuable item.
    *   **Stats:** Extremely document will define the foundation of the entire apparel system. The Base Layer is not just about aesthetics; it's the player's first line of defense against the environment and the core of their character's visual identity.

Here is the complete design document for Base Layer Apparel.

---

### **New Content for: `Where_Giants_Rust_DOCS\04_GAME_CONTENT\01_ITEMS\07_Equipment_and_Apparel\02_Base_Layer_Apparel_(Shirts_Pants).md`**

---
# Equipment: Base Layer Apparel (Shirts, Pants & Underlayers)

## **1.0. Core Philosophy: The Foundation of Survival**

Base Layer Apparel consists of the fundamental clothing items worn directly on the character's body: shirts, pants, and under-armor layers. While they offer negligible **Armor Rating (AR)** on their own, their lightweight and surprisingly durable, with balanced, moderate resistances.

---
## **4.0. Legs (Base Layer) - Pants**

#### **Tier 1: Common Apparel**
*   **Worn Jeans**
    *   **Description:** Standard denim jeans, a common survivor staple.
    *   **Stats:** A balanced, durable option with moderate resistances.
*   **Cargo Shorts**
    *   **Description:** Lightweight shorts with many pockets.
    *   **Stats:** Good Heat Resistance, but negative Cold Resistance. Adds a small amount of extra carry weight (+2 kg primary function is to provide the player with crucial **Environmental Resistance** to Cold and Heat, as well as minor passive stat buffs.

The choice of base layer is a critical preparation step for any expedition. Wearing the wrong clothing in a harsh environment will lead to rapid stat degradation and potential death, regardless of how good the player's armor is. All base layer apparel is visible when heavier armor or outerwear is not equipped, serving as the core of the character's visual identity.

---
## **2.0. Base Layer Slots**

*   **Torso:** Accepts shirts, undershirts, and tunics.
*   **Legs:** Accepts pants, trousers, and leggings.
*   **Full-) due to the extra pockets.

#### **Tier 2: Specialized & Crafted Apparel**
*   **Cargo Pants**
    *   **Description:** The full-length version of cargo shorts, offering more protection.
    *   **Stats:** Balanced resistances and a moderate carry weight bonus (+5 kg).
*   **Hardened Leather Pants**
    *   **Description:** Crafted pants made from tough, boiled leather.
    *   **Stats:** Offer a small amount of Armor Rating and are highly durable, but are heavy and have poor heat resistance.
*   **Wool Trousers**
    *   **Description:** The leg-wear equivalent of the wool shirt.
    *   **Stats:** Excellent Cold Resistance.

#### **Tier 3: Advanced & Rare Apparel**
*   **Insulated Tactical Pants**
    *   **Description:** Military-grade pants salvaged from high-tech ruins.
    *   **Stats:** Provides an excellent balance of Cold Resistance, durability, and a slight buff to stealth.
*   **Body:** A special category for items like jumpsuits or boilersuits that occupy BOTH the Torso and Legs slots.

---
## **3.0. Material & Resistance System**

The effectiveness of apparel is determined by its **material**. Each material has inherent properties that translate into gameplay stats.

*   **Cotton (e.g., T-Shirts, Jeans):** The baseline. Offers very minor Cold and Heat resistance. A neutral, all-purpose material for temperate climates.
*Blacksmith's Apron/Leggings**
    *   **Description:** A heavy leather and canvas apron worn over pants.
    *   **Stats:** No Armor Rating, but provides extremely high Fire Resistance, making it invaluable for anyone working a forge or exploring a volcanic area. Occupies both the "Legs" and "Outerwear" slot visually.

---
## **5.0. Full-Body Base Layers**

These special items occupy both the Torso and Legs slot simultaneously.

*   **Boilersuit / Jumpsuit**
    *   **Description:** A simple, one-piece utility suit found in industrial areas.
    *   **Stats:** Balanced resistances, high durability. A   **Wool (e.g., Wool Sweaters, Lined Trousers):** The primary material for **Cold Resistance**. Offers excellent insulation but performs poorly in hot weather, increasing the rate of thirst.
*   **Linen/Hemp (e.g., Loose Shirts, Breeches):** The primary material for **Heat Resistance**. Breathable fabric that keeps the wearer cool and slows the rate of thirst in hot biomes. Offers poor protection against the cold.
*   **Leather (e.g., Leather Vests, Tough Leather Pants):** Offers a balance of minor Cold/Heat resistance and a small amount of **Armor Rating** and durability. A good all-rounder for combat-focused players good, simple option.
*   **Environmental Suit ("HAZMAT" Suit)**
    *   **Description:** A rare, high-tech sealed suit.
    *   **Stats:** Provides immense resistance to Disease and the "Corruption" of Blighted zones, but offers very little Cold or Heat resistance and no armor. Its purpose is singular and vital.
*   **Daedalus Initiative Uniform**
    *   **Description:** The starting outfit for all Daedalus survivors. A clean, white and blue jumpsuit.
    *   **Stats:** A perfectly balanced but unremarkable starter item. It has sentimental value but will need to be replaced quickly.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/04_GAME_CONTENT/01_ITEMS/07_Equipment_and_Apparel/01_Equipment_System_Overview.md`
```md
# Equipment System Overview: The Layered Survivor

## **1.0. Core Philosophy: Purposeful Customization**

The equipment and apparel system in *Where Giants Rust* is designed to be a deep, granular, and realistic representation of how a survivor would prepare for a hostile world. Players will manage multiple layers of clothing and gear, making strategic choices based on the environment they are entering, the combat they are expecting, and the utility they need.

There is a fundamental separation between **Apparel** (clothing for environmental protection) and **Gear** (equipment for utility and combat). This layered system allows a player to wear a warm wool shirt for cold resistance while strapping a tactical chest rig over it for combat effectiveness.

## **2.0. Character Equipment Slots**

The player's equipment screen will be divided into the following dedicated slots, each accepting a different category of item.

#### **2.1. Apparel Slots (Environmental & Base Protection)**
These are the clothes worn directly on the body. Their primary function is to provide protection from the elements (Cold, Heat) and offer minor passive bonuses.

*   **Head:** (e.g., Hats, Beanies, Hoods) - Separate from combat helmets.
*   **Torso (Base Layer):** (e.g., T-Shirts, Wool Shirts, Thermal Underwear)
*   **Legs (Base Layer):** (e.g., Jeans, Cargo Pants, Thermal Leggings)
*   **Outerwear (Torso):** (e.g., Jackets, Cloaks, Dusters) - Worn over the Torso base layer.
*   **Hands:** (e.g., Work Gloves, Insulated Mittens)
*   **Feet (Socks):** (e.g., Wool Socks, Athletic Socks) - Yes, socks matter for cold resistance.
*   **Feet (Boots):** (e.g., Hiking Boots, Tactical Boots, Rubber Wellingtons)

#### **2.2. Gear Slots (Utility & Combat)**
These items are worn over apparel and are focused on functionality.

*   **Combat Headwear:** (e.g., Ballistic Helmet, Forge Guard's Helm) - Provides Armor Rating.
*   **Body Armor:** (e.g., Leather Cuirass, Steel Platebody)
*   **Leg Armor:** (e.g., Leather Chaps, Steel Greaves)
*   **Chest Rig:** (e.g., Tactical Rig, Alchemist's Bandolier) - Worn over Body Armor. Adds quick-slots or specialized pouches.
*   **Belt:** Provides utility and can have **Belt Attachments**.
*   **Back:** (e.g., Backpacks, specialized gear like an Oxygen Tank or Quiver)
*   **Exo-Suit:** A special, all-encompassing slot that disables most other gear slots when active.

## **3.0. The Layering System Explained**

The system's depth comes from how layers interact.

*   **Example 1: The Mountaineer**
    *   **Torso:** Thermal Underwear (High Cold Resist).
    *   **Outerwear:** Thick Fur-Lined Parka (Very High Cold Resist).
    *   **Body Armor:** Lightweight Leather Armor (for protection against predators, worn under the parka).
    *   **Chest Rig:** A simple pouch rig for holding flares and emergency rations.
    *   **Back:** A large Mountaineer's Hiking Frame.
    *   **Result:** The character has exceptional resistance to the Cold, sacrificing some combat mobility for massive carry capacity and survival in a blizzard.

*   **Example 2: The Scrapper Raider**
    *   **Torso:** Simple T-shirt (No Resistances).
    *   **Outerwear:** None (to save weight and increase mobility).
    *   **Body Armor:** A heavy Steel Platebody salvaged from wreckage.
    *   **Chest Rig:** A Tactical Rig with 4 extra quick-slots for grenades and medical supplies.
    *   **Belt:** A belt with a visible sidearm holster attachment.
    *   **Result:** A glass cannon build with high armor and combat utility but who would quickly freeze in the mountains or overheat in the desert.

## **4.0. Advanced Gear Slots & Modularity**

This is where the true end-game customization lives.

#### **4.1. Leg Gear Slots (Left & Right)**
Each leg has a dedicated utility slot that can be equipped with specialized attachments found or crafted in the world.
*   **Examples:**
    *   **Thigh Pouch:** A simple pouch that adds a small amount of extra, easy-access inventory space.
    *   **Sidearm Holster:** Allows for a much faster weapon swap to your equipped pistol.
    *   **Knife Sheath:** Reduces the time it takes to pull out your skinning knife.
    *   **"Bracer Mod":** A salvaged hydraulic bracer that slightly increases melee attack power but reduces stealth.

#### **4.2. Exo-Suit Modularity**
Exo-Suits are the pinnacle of equipment. They occupy the **Exo-Suit Slot**, disabling the Outerwear, Body Armor, Leg Armor, and Back slots. However, they come with their own modular slots.
*   **Exo-Suit Mod Slots:** An Exo-Suit might have 2-4 dedicated slots for **Exo-Mods**.
*   **Exo-Mods Examples:**
    *   **Kinetic Servos:** Increases melee damage.
    *   **Reinforced Armor Plating:** Increases the Exo-Suit's Armor Rating.
    *   **Backup Power Cell:** Increases the suit's operational time.
    *   **Stealth Field Emitter:** A very rare mod that reduces the noise made by the suit.
    *   **Resource Scanner Module:** Adds a G.O.L.I.A.T.H.-style resource scanner directly to the suit's HUD.

This system creates a deep and rewarding loop of looting, crafting, and character-building, where every single piece of equipped gear is a meaningful choice.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/06_MODIFICATION_SYSTEMS/01_Subroutine_Fragment_System.md`
```md
# Gameplay System: Subroutine Fragments

## 1.0. Core Philosophy: The Ghost in the Machine
Subroutine Fragments are the "tech magic" of *Where Giants Rust*. They are pieces of corrupted or fragmented code from the Daedalus Initiative's advanced AIs, salvaged from the wreckage of the past. When slotted into the player's APU (Arm-mounted Processing Unit), they function as **passive skill buffs**, allowing for deep, granular character customization. This system is the tech-based equivalent of finding magical rings and amulets.

## 2.0. The Mechanics
*   **Acquisition:** Fragments are primarily found by salvaging high-tier technological wreckage, defeating robotic enemies, or as loot in Daedalus-themed dungeons. They appear as small, chip-like items in the inventory.
*   **APU Slots:** The player's arm-mounted rig has a limited number of "Subroutine Slots" (e.g., starting with 2 and expandable to 4-5 through tech upgrades).
*   **Installation:** Subroutine Fragments can be slotted into the APU at any time via the inventory screen.

## 3.0. Fragment Design: A Boon and a Glitch
Every Subroutine Fragment is a piece of imperfect code. It offers a significant **Boon** but comes with a minor, thematically-linked **Glitch (a debuff)**. This "trade-off" design makes choosing fragments a tactical decision rather than a simple numbers game.

Fragments are named using a dot-notation convention that reflects their origin and function.

### Example Fragments:

*   **`Fragment: Marksman.precision_v1.2`**
    *   **Boon:** `+10%` Critical Hit Damage with ranged weapons.
    *   **Glitch:** `-5%` Movement speed while aiming down sights (due to processing power being diverted to the targeting algorithm).

*   **`Fragment: Guardian.aegis_protocol_v0.9`**
    *   **Boon:** `+15%` effectiveness when blocking with a shield.
    *   **Glitch:** You take `+10%` more damage from elemental sources (the protocol's focus on physical threats leaves energy vulnerabilities).

*   **`Fragment: Wilds.biometric_sampler_v2.0`**
    *   **Boon:** `+20%` chance to harvest rare materials from animal carcasses.
    *   **Glitch:** `-10%` selling value for all tech items (the fragment's code conflicts with barter protocols).

*   **`Fragment: Elementalism.capacitor_charge_v1.7`**
    *   **Boon:** Fire spells deal `+10%` damage.
    *   **Glitch:** Frost spells cost `+5%` more Mana to cast.

*   **`Fragment: Tech.overclocker_v3.1`**
    *   **Boon:** Increases crafting speed at tech workbenches by `25%`.
    *   **Glitch:** `+15%` chance of item damage when failing a tech-related mini-game (e.g., hacking).

## 4.0. Upgrading and Synergies (The Tech Path)
The **Tech** skill tree is the primary way to interact with and improve this system.
*   **Reverse-Engineering:** A Tech perk allows the player to destroy unwanted fragments at a workbench to gain a tiny, permanent stat boost, rewarding the player for finding duplicates.
*   **Overclocking:** A high-tier Tech perk allows a player to "overclock" a slotted fragment. This doubles its Boon but also doubles its Glitch, creating high-risk, high-reward builds for specialists.
*   **Fragment Combinations:** Certain fragments may have hidden synergies, creating a tertiary, positive effect if slotted at the same time, rewarding player experimentation.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/05_CONSTRUCTION_SYSTEMS/03_Item_Modification_and_Upgrades.md`
```md
# Gameplay System: Item Modification & Upgrades

## 1.0. Core Philosophy
Finding or crafting a piece of gear is only the first step. The true power of an item is unlocked through a deep and layered modification system. This system allows players to take a standard weapon or piece of armor and tailor it to their specific build and playstyle, creating a truly unique and personal arsenal. The modification system is the primary reward for investing in non-combat crafting skills.

## 2.0. The Three Pillars of Modification

There are three distinct paths for improving an item, each tied to a different skill discipline and crafting station.

#### **Pillar 1: Improvement (The Smithing Path)**
*   **Station:** Workbench (for physical damage) or Grindstone/Armor Bench (visual variations).
*   **Skill:** **Smithing**.
*   **Mechanic:** This is the most fundamental upgrade. By consuming base materials (e.g., Metal Ingots, Leather), a player can improve the **base stats** of a weapon or armor piece.
*   **Tiers:** An item can be upgraded through several quality levels, indicated by a prefix or suffix (e.g., a "Fine Iron Sword", "Flawless Steel Armor"). Each level increases its core stat (damage for weapons, armor rating for armor).
*   **The Capstone:** The "Legend of the Forge" perk in the Smithing tree allows a player to improve an item one final, legendary time beyond its normal limits, creating a "Masterwork" piece of gear.

#### **Pillar 2: Enchanting (The Magic Path)**
*   **Station:** Arcane Enchanter.
*   **Skill:** Perks in **Smithing** (Arcane Blacksmith) and **Void** (Soul Trap).
*   **Mechanic:** This system allows the application of magical properties to non-magical gear. It's a three-step process:
    1.  **Learn:** The player must first find a magical item in the world (e.g., a sword with "+5 Fire Damage"). By destroying that item at the Arcane Enchanter, they permanently learn the "Fire Damage" enchantment.
    2.  **Trap:** The player must capture a soul by killing an enemy under the effect of the "Soul Trap" spell. The soul is stored in a **Soul Gem**. The "size" of the soul determines the power of the resulting enchantment.
    3.  **Enchant:** The player can now apply a known enchantment to a standard item, consuming the filled Soul Gem in the process. An item can typically only hold one enchantment.

#### **Pillar 3: Tech-Modding (The Technology Path)**
*   **Station:** Tinker's Workbench.
*   **Skill:** **Tech**.
*   **Mechanic:** This system is the sci-fi equivalent of enchanting, focused primarily on firearms, advanced armor, and Exo-Suits. It involves installing physical **Mods** onto gear.
*   **Slots:** Higher-tier gear comes with a limited number of "Mod Slots." A standard rifle might have a "Scope Slot" and a "Barrel Slot."
*   **Mods as Items:** Unlike enchantments, mods are physical items that must be found or crafted (e.g., a "4x Scope Schematic," a "Suppressor"). These mods are then installed into the corresponding slot.
*   **Example (A Rifle):** A player could install a **Long-Range Scope** in the scope slot for better zoom, and a **Suppressor** in the barrel slot to make it silent, fundamentally changing its tactical role from a loud battle rifle to a stealthy sniper rifle.

## 4.0. Accessories (The Final Polish)
*   **Station:** Tinker's Workbench.
*   **Skill:** Various (Smithing, Alchemy, Tech).
*   **Mechanic:** As detailed in `/04_GAME_CONTENT/01_ITEMS/07_Equipment_and_Apparel/08_Accessories.md`, this is the final, granular layer. Gear can have **Accessory Slots** where players can install small, passive-boosting items like grip wraps, lucky charms, or faction patches. This allows for fine-tuning a build with small, stacking bonuses.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/05_CONSTRUCTION_SYSTEMS/02_Base_Building.md`
```md
# Gameplay System: Base Building

## 1.0. Core Philosophy
The base building system is the player's primary tool for imposing order on a chaotic world. A base is not just a collection of crafting stations; it is a **sanctuary**, a **fortress**, and a long-term **investment**. The system is designed to be free-form and modular, allowing players to build anything from a simple log cabin to a sprawling stone castle, with the effectiveness of the base determined by its design, materials, and defenses.

## 2.0. The Tool: The Building Hammer
*   The "Building Hammer" is a special tool, equipped to a hot-bar slot.
*   When equipped, it brings up a contextual UI showing all available building pieces.
*   Players select a piece (e.g., "Wooden Foundation," "Stone Wall") and place a ghostly "preview" in the world. Once placed, resources are consumed from the inventory and the piece is constructed.

## 3.0. Foundational Principles

#### **Structural Integrity:**
*   **Concept:** Buildings must obey a basic sense of physics. A roof piece cannot be placed without walls to support it. A wall cannot float in mid-air.
*   **Foundations:** All structures must begin with a **Foundation** piece snapped to the ground. Subsequent pieces (walls, floors) must snap to the foundation or another supported piece.
*   **Collapse:** If a critical support piece is destroyed (e.g., a foundation at the corner of a tower), all pieces that were depending on it will collapse in a satisfying, physics-based cascade of destruction. This makes targeting a base's weak points a valid siege tactic.

#### **Material Tiers:**
*   The strength of a base is determined by its materials. Each building tier is unlocked via the **Architect** skill tree.
*   **Tier 1: Wood:** Cheap and easy to build. Weak to fire and siege attacks from Brutes or explosives.
*   **Tier 2: Stone:** Requires significantly more resources and a Forge to make mortar. Highly resistant to physical damage and fire. Vulnerable to powerful explosives or magical siege weapons.
*   **Tier 3: Reinforced Metal/Concrete:** The pinnacle of base defense. Extremely durable and resource-intensive. Requires high-level Tech and Architect skills.

## 4.0. Defensive Structures
Beyond simple walls, players can build active defenses to protect against raids from Scrappers or the Blighted Horde. These are unlocked via perks in the Architect and Tech trees.

*   **Passive Defenses:**
    *   **Wooden Spikes:** Simple sharpened stakes that deal damage to enemies who walk over them.
    *   **Caltrops:** Small metal spikes that slow enemies.

*   **Active Defenses (Require player interaction):**
    *   **Catapult:** A large siege engine that must be manually loaded and fired. Hurls massive stones that can shatter enemy formations.
    *   **Battlements:** Specialized wall pieces that provide good cover for archers.

*   **Automated Defenses (High-Tier, require power):**
    *   **Automated Turrets:** Salvaged or crafted machinegun turrets that will automatically fire on hostile targets. Consume ammunition.
    *   **Tesla Coils:** A powerful defensive pylon that periodically zaps nearby enemies with arcs of lightning. Consumes a large amount of power from a generator.

## 5.0. Utility & Quality of Life Structures
A base is also a home, providing essential survival and comfort bonuses.

*   **Beds / Bedrolls:** Allows the player to sleep, passing time and providing the "Well-Rested" buff for bonus XP.
*   **Storage:** Chests, lockers, and weapon racks for storing items. Higher-tier storage holds more.
*   **Farming Plots:** Allows for sustainable agriculture.
*   **Rain Collectors:** Barrels placed outside will passively collect clean drinking water during rain.
*   **The Hearthstone:** The ultimate capstone structure from the Architect tree. Provides passive health regeneration and slowly repairs the entire base. It's the living heart of a master-built fortress.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/05_CONSTRUCTION_SYSTEMS/01_Crafting_Recipes_and_Stations.md`
```md
# Gameplay System: Crafting Recipes & Stations

## 1.0. Core Philosophy
Crafting is a cornerstone of progression in *Where Giants Rust*. The system is designed to be deep and rewarding, driving players to explore, gather, and experiment. Players do not start with all knowledge; they must actively discover new crafting recipes from the world and build specialized crafting stations to unlock their full potential.

## 2.0. Discovering Recipes
Recipes are the "blueprints" for crafting items. They can be acquired in several ways:

*   **Default Recipes:** The player starts with a handful of basic survival recipes (e.g., Stone Axe, Campfire, Bandage).
*   **Skill-Based Unlocks:** Placing points into specific skill tree perks (e.g., Smithing, Architect, Alchemy) automatically unlocks new recipes related to that skill.
*   **Schematics & Blueprints (Loot):** Found as physical items in the world—a "Tattered Schematic" in a toolbox, an "Ancient Elven Text" in a ruin, or a "Pristine Daedalus Blueprint" in a tech-dungeon. Reading the item consumes it and permanently teaches the player the recipe.
*   **Experimentation (Alchemy):** The Alchemy system allows for the discovery of new potion effects by combining ingredients with unknown properties. A successful new combination automatically creates a permanent recipe.
*   **Reverse-Engineering (Tech):** A high-tier Tech perk might allow a player to break down a rare piece of gear or technology at a workbench to learn its schematic, destroying the item in the process.

## 3.0. Crafting Stations
A player's ability to craft is limited by the stations they have built in their base. Higher-tier recipes require higher-tier stations.

#### **Category: Survival & Basic**
*   **Campfire:**
    *   **Function:** Basic cooking (grilling meat), boiling water, provides heat and light.
    *   **Tiers:** Can be upgraded with a cooking pot and grill for more complex food recipes.

#### **Category: Smithing & Metalwork**
*   **Forge:**
    *   **Function:** Smelting ores into metal ingots, crafting all metal weapons and heavy armor.
    *   **Tiers:**
        1.  **Stone Forge:** Basic, inefficient.
        2.  **Bellows Forge:** Improved efficiency, allows for steel production.
        3.  **Dwarven Hearth-Forge:** Master-tier, may add minor boons to crafted items.

*   **Workbench:**
    *   **Function:** General purpose. Improving and repairing weapons and armor, crafting wooden items, and assembling complex goods.
    *   **Tiers:** Basic wooden bench, Sturdy workbench, Engineer's workbench with built-in tools.

*   **Tanning Rack:**
    *   **Function:** Turning raw animal hides into usable leather.
    *   **Tiers:** Simple wooden rack, Advanced rack that can produce Hardened Leather.

#### **Category: Alchemy & Magic**
*   **Alchemy Lab:**
    *   **Function:** Required for crafting all potions, poisons, and elixirs.
    *   **Tiers:**
        1.  **Mortar & Pestle:** Can be carried, allows for very simple concoctions on the go.
        2.  **Basic Alchemy Table:** Unlocks most recipes.
        3.  **Chemist's Station:** A high-tech version with centrifuges and burners, increasing potion potency.

*   **Arcane Enchanter:**
    *   **Function:** The station for disenchanting magical items to learn their effects and applying those enchantments to other items using Soul Gems.
    *   **Source:** A rare, high-tier station that must be discovered (schematic) or found intact in a magical ruin.

#### **Category: Technology**
*   **Tinker's Workbench:**
    *   **Function:** Crafting electronic components, repairing tech, installing tech mods and accessories.
    *   **Tiers:** Salvaged workbench, Powered tech station.

*   **Vehicle Bay / Lift:**
    *   **Function:** A large, specialized station required for repairing and modifying vehicles.
*   **AI Diagnostic & Maintenance Station:**
    *   **Function:** The late-game station used to swap, integrate, and modify AI Companions.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/04_SURVIVAL_SYSTEMS/02_Environment_and_Weather.md`
```md
# Environment and Weather System

## **1.0. Core Philosophy: The World Breathes**

The environment in *Where Giants Rust* is a living, breathing system designed to be both beautiful and threatening. The dynamic weather and environmental hazards are not just cosmetic effects; they are core gameplay mechanics that directly impact visibility, movement, resource availability, and enemy behavior. Players must learn to read the sky and the land, respecting the world's changing moods to survive.

## **2.0. The Dynamic Weather System**

The weather operates on a dynamic, procedural system that creates logical and immersive patterns rather than completely random changes. Coastal regions will see more fog and rain, while high mountains will be prone to blizzards.

*   **Clear Skies**
*   **Overcast**
*   **Light Rain**
*   **Heavy Rain**
*   **Thick Fog**

#### **2.1. Standard Weather Patterns**

*   **Clear Skies:** The baseline state. Offers excellent visibility day and night. During the day, grants the "In Sunlight" bonus for followers of Solana.
*   **Overcast:** Grey, oppressive cloud cover. Reduces ambient light, making forests and shadows darker. Has no major mechanical effect but creates a somber mood.
*   **Light Rain:** A common occurrence. Reduces visibility slightly. Makes surfaces appear wet and slick. Has a small positive effect on crop growth in farming plots.
*   **Heavy Rain:** Significantly reduces visibility and muffles sound, making both stealth and enemy detection more difficult. Puts out unprotected fires (campfires, torches). Rapidly fills rain collectors at the player's base.
*   **Thick Fog:** Drastically reduces visibility to near melee-range in some cases. Most common in coastal and wetland biomes, or in valleys during the early morning. Extremely dangerous for travel, as threats can appear with no warning.

#### **2.2. Extreme Weather Events (Storms)**

Storms are less common but are major, multi-faceted events that present both extreme danger and unique opportunities.

*   **Thunderstorm:**
    *   **Effects:** Combines Heavy Rain with the added threat of **lightning strikes**. Lightning is a random, area-of-effect environmental hazard that deals massive shock damage. Metal armor has a slightly higher chance of attracting a strike.
    *   **Opportunities:** The immense power in the air can be harnessed. A follower of **Kaelus** gains significant combat buffs. Certain magical rituals or tech devices might only be chargeable during a thunderstorm.
    *   **The Midnight Tempest (Special Event):** This is where your idea comes to life. If a Thunderstorm occurs at night (between roughly 10 PM and 4 AM), the ambient fear and raw chaotic energy **empowers the Blighted**. During a Midnight Tempest:
        *   The spawn rate of Blighted creatures increases significantly.
        *   All Blighted gain a visible "Charged" particle effect.
        *   They become more aggressive, faster, and hit harder.
        *   This turns a normal night into a terrifying siege-like event, forcing players to either be exceptionally well-prepared to fight or to bunker down in a secure shelter until it passes.

*   **Blizzard (Mountain & Tundra Biomes):**
    *   **Effects:** A combination of heavy snowfall and high winds that creates near-zero visibility ("whiteout" conditions). Greatly accelerates the rate at which the player's "Cold" meter fills, causing rapid freezing damage without proper gear.
    *   **Opportunities:** The extreme cold can freeze certain water-bodies, creating temporary new paths. Some unique "frost-aspected" creatures may only appear during a blizzard.

*   **Ash Storm (Volcanic & Ashlands Biomes):**
    *   **Effects:** Choking clouds of ash reduce visibility and air quality. The player's stamina drains faster, and they may begin to take minor health damage without a face covering.
    *   **Opportunities:** The thick ash can reveal things that are normally invisible, such as the shimmering outlines of certain magical wards or the footprints of ethereal creatures.

## 3.0. Anomalous Phenomena: The Pareidolia Effect
This is a subtle, psychological horror mechanic designed to enhance the oppressive atmosphere of storms and corrupted zones, making the player question what they are seeing. It should be faint and unnerving.

*   **Core Concept:** The chaotic energy of severe weather or the reality-warping nature of The Static can cause random patterns to momentarily resolve into fleeting, terrifying shapes that look like faces or figures—a phenomenon known as pareidolia.

*   **Triggers:**
    *   **Thunderstorms:** During a flash of lightning, the illuminated patterns on a distant cliff face or in the swirling clouds might form a colossal, screaming face for a single frame.
    *   **Blizzards:** In the thick, swirling snow of a whiteout, a "spirit"—a vaguely humanoid shape made of denser snow—might drift by at the absolute edge of the player's vision, turning to "look" at them before dissolving back into the storm.
    *   **Blighted Scars:** The visual "glitching" of a Blighted zone is the most common trigger. A wall of static on a corrupted monitor might resolve into a face. The twitching branches of a petrified tree might momentarily form a skeletal hand reaching for the player.

*   **Mechanics:**
    *   **Subtlety is Key:** This is never a direct threat or a jump-scare. It should happen in the player's periphery, almost too fast to be certain. It is designed to create a sense of being watched and to make the player feel unsafe even when no enemies are present.
    *   **No Gameplay Impact:** These apparitions cannot be attacked and have no physical effect. Their purpose is purely atmospheric.
    *   **Sound Link:** These visual events are often paired with a faint, directional audio cue—a single, sharp whisper, a sudden intake of breath, or a scrap of distorted music—that only the player can hear. (See `/05_USER_EXPERIENCE/03_AUDIO/01_Sound_Effects_Design.md`).

## **4.0. Biome-Specific Environmental Hazards**

These are static, persistent threats tied to specific biomes.

*   **Extreme Cold (Mountain Highlands):** Without insulating armor (fur, thick cloth) or a torch, the player will suffer from a "Freezing" status effect, which slows all actions and constantly drains health.
*   **Extreme Heat (Volcanic Ashlands):** Without heat-resistant armor or by staying hydrated, the player will suffer from "Heatstroke," which rapidly drains stamina and blurs vision.
*   **Toxic Air (Deep Swamps / Volcanic Vents):** Certain areas have poor air quality. Lingering in them without a respirator or potion will lead to the "Diseased" status effect.
*   **The Blight (Blighted Scars):** The ultimate environmental hazard. Causes the constant, stacking "Corruption" debuff that drains the player's maximum health. Specialized gear, divine blessings, or powerful alchemical tinctures are required to survive for any length of time.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/04_SURVIVAL_SYSTEMS/01_Player_Needs_and_Status_Effects.md`
```md
# Player Needs and Status Effects

## **1.0. Core Philosophy: The Weight of Existence**

The survival systems in *Where Giants Rust* are designed to add a layer of immersive challenge and strategic planning. They are not intended to be overly punishing "meters" that require constant babysitting, but rather tactical considerations that influence how a player prepares for an expedition. The goal is to make the player feel the physical weight of their journey.

## **2.0. Primary Player Needs**

These are the core needs that the player must manage to stay effective. They are represented by subtle UI elements and more obvious status effect icons when they reach critical levels.

#### **2.1. Hunger**
*   **Mechanic:** A slowly depleting resource bar. The rate of depletion increases when performing strenuous activities (sprinting, combat). Eating food replenishes this meter and contributes to the **Bowel** need.
*   **Positive State ("Well Fed"):** When the hunger meter is full (above 80%), the player gains a slight buff to their base Health and Stamina regeneration.
*   **Negative States:**
    *   **Peckish (below 50%):** A minor debuff. Total Stamina is reduced by 10%.
    *   **Hungry (below 25%):** A significant debuff. Stamina regeneration is halved.
    *   **Starving (at 0%):** A critical debuff. The player can no longer regenerate Stamina naturally. Their maximum Health begins to slowly tick down.

#### **2.2. Thirst**
*   **Mechanic:** A slowly depleting resource bar. The rate of depletion increases in hot environments and when performing strenuous activities. Drinking replenishes this meter and contributes to the **Bladder** need.
*   **Positive State ("Hydrated"):** When the thirst meter is full (above 80%), the player gains a slight buff to their base Stamina and Mana regeneration.
*   **Negative States:**
    *   **Parched (below 50%):** A minor debuff. Total Mana is reduced by 10%.
    *   **Dehydrated (below 25%):** A significant debuff. Mana regeneration is halved.
    *   **Severely Dehydrated (at 0%):** A critical debuff. The player can no longer regenerate Mana naturally. Their vision begins to blur, and maximum Health slowly ticks down.

---
## **2.5. Bodily Needs (Placeholder System)**

These needs fill up over time based on consumption and provide placeholder debuffs.

#### **2.5.1. Bladder**
*   **Mechanic:** A slowly filling resource bar. The rate of increase is accelerated by drinking fluids.
*   **Negative States (Placeholder):**
    *   **Full (above 80%):** A warning is logged. A minor "Uncomfortable" debuff might reduce agility.
    *   **Critical (at 100%):** A critical warning is logged. The character might relieve themselves automatically, creating a negative social interaction or alerting nearby wildlife.

#### **2.5.2. Bowel**
*   **Mechanic:** A slowly filling resource bar. The rate of increase is accelerated by eating food.
*   **Negative States (Placeholder):**
    *   **Full (above 80%):** A warning is logged. A minor "Bloated" debuff might reduce stamina.
    *   **Critical (at 100%):** A critical warning is logged. Similar to the bladder, this could lead to an automatic, inopportune event.

---
## **3.0. Combat & Environmental Status Effects**

These are temporary effects applied during combat or from environmental hazards. They can be cured with specific potions or tinctures.

*   **Bleeding:** A physical damage-over-time effect, usually applied by bladed weapons or animal claws. Cured with a Bandage.
*   **Poisoned:** A magical or biological damage-over-time effect that often drains Stamina as well as Health. Cured with an Antidote.
*   **Burning:** A fire-based damage-over-time effect. Can be extinguished by rolling or entering water.
*   **Frozen / Chilled:** Dramatically slows movement and attack speed. Thaws over time, or instantly near a fire source.
*   **Shocked / Disoriented:** Drains Mana and causes the player's view to jitter, making precise actions difficult.
*   **Diseased:** Contracted from certain creatures or squalid environments. Reduces the effectiveness of all healing items and prevents natural health regeneration. Cured with a "Cure Disease" potion.
*   **Corruption:** The unique hazard of Blighted zones. It is the signature effect of The Static actively overwriting local reality. This manifests as a stacking debuff with increasingly severe effects.
    *   **Low Corruption (Initial Exposure):** Slowly drains the player's maximum health, reducing their health bar until they leave the area or use a specific purifying item. Accompanied by minor visual screen-glitching.
    *   **High Corruption (Prolonged Exposure):** Triggers **Systemic Interference**. The player's APU and neural interface begin to fail, causing severe psychological and mechanical disruptions. These effects are rare at first but become more frequent as the Corruption level increases.
This system ensures that players must think not only about their weapons and armor, but also about packing the right provisions and cures for whatever journey lies ahead.

### **3.1. Systemic Interference Effects (High Corruption)**
These are temporary, terrifying "glitches" that represent The Static attacking the player's link to their own technology.

*   **Sensory Corruption (Psychological):**
    *   **Auditory Hallucinations:** The player will hear things that are not there. Most commonly, this manifests as the **faint, spatialized giggling of children**, seeming to come from just over their shoulder or a dark corner of the room.
    *   **Visual Hallucinations:** The Pareidolia effect becomes more pronounced and aggressive. Fleeting, shadowy figures may dart across the edge of the screen.

*   **Input Corruption (Mechanical):**
    *   **Input Drop:** For a few seconds, a critical input will fail. The "E" key to interact might not register, or the trigger for a weapon won't respond.
    *   **Input Scramble / Inversion:** For a brief, terrifying 3-5 second window, a core control scheme will be scrambled. The most common manifestation is the **mouse Y-axis suddenly inverting**, causing the player to look down when they try to look up.
    *   **Stutter Step:** Movement keys (W,A,S,D) may become momentarily unresponsive or "sticky," causing the player's movement to stutter and halt unexpectedly, often at the worst possible moment.

*   **Interface Corruption:**
    *   **HUD Flicker:** The player's HUD elements (health bars, compass) will violently glitch and may disappear entirely for a few seconds.
    *   **Weapon Swap Failure:** The player will attempt to switch weapons, but the animation will play with an "error" sound effect, and they will be switched back to their previous weapon.

**Mitigation:** These chaotic effects make Blighted zones a nightmare even for high-level players. However, they can be countered.
*   **Specialized Gear:** Craftable "Insulated APU Housings," "Hardened Tech-Apparel," or wearing a full "HAZMAT Suit" can significantly reduce the *chance* of these glitches occurring.
*   **Divine Blessings:** A blessing from a god of Order or Purity (like Valdrak or Solana) grants passive resistance to Systemic Interference.
*   **Alchemical Solutions:** A rare, high-tier "Stabilizer" potion can be consumed to render the player completely immune to Input Corruption for a short duration.

This system ensures that Blighted Zones are never trivial. A player must choose: do they go in with heavy armor to resist physical damage, or with specialized "clean" gear to resist the horrifying fourth-wall-breaking chaos?
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/03_MAGIC_SYSTEMS/02_Divine_Boons_and_Patronage.md`
```md
# Divine Boons and Patronage

## 1.0. Core Philosophy
The Divine Patronage system is the game's primary "prestige class" mechanic. It is a deep, role-playing-driven system that rewards players for their actions by aligning them with a powerful cosmic entity. Choosing a patron god is a permanent, build-defining decision that unlocks a unique playstyle, grants powerful abilities, and reshapes the player's relationship with the world and its factions.

This is not a menu choice; it is a destiny that is earned.

## 2.0. The Path to Patronage: A Two-Step Process

#### Step 1: The Affinity System
*   **How it works:** A hidden stat, **Affinity**, tracks the player's actions as they relate to each god's domain and philosophy. Every significant action that aligns with a god's principles will increase Affinity with them, while acting against their tenets may decrease it or increase it with a rival god. (See `01_Pantheon_Overview.md` for detailed examples).
*   **The "Call":** When a player's Affinity with one god becomes significantly higher than all others, that god will begin to "reach out." This can manifest as:
    *   **Visions:** Cryptic, dream-like sequences when the player sleeps.
    *   **Omens:** Unlikely events in the world (e.g., a lightning bolt striking down an enemy for Kaelus; a rare flower blooming at your feet for Sylvana).
    *   **Messengers:** An NPC or a unique creature aligned with the god will approach the player with a message.

#### Step 2: The Divine Trial
*   **The Offer:** The god will formally offer the player a chance to become their champion. To prove their worth, the player must complete a unique, challenging **Divine Trial.**
*   **Trial Design:** This is a major, handcrafted side quest tailored specifically to the god's domain.
    *   *Valdrak's Trial:* "Igniting the Heart-Forge." A dungeon crawl to re-ignite a legendary forge.
    *   *Solana's Trial:* "The Dawn's Aegis." A desperate base-defense style quest protecting a village from a horde of undead.
    *   *Umbra's Trial:* "The Unseen Hand." A pure infiltration and theft mission where combat is a failure condition.
*   **The Vow:** Upon completing the trial, the player is given a final, explicit choice to swear fealty. Accepting this vow is a permanent commitment. A player can only serve one god at a time, and this choice will make them an enemy of that god's rivals.

## 3.0. The Rewards of Patronage

Becoming a god's champion is one of the most significant power-ups in the game, granting three tiers of rewards.

#### Reward 1: Passive Blessing
*   A subtle, permanent buff that is always active.
*   **Example (Kaelus):** *Heart of the Maelstrom.* The lower your health, the higher your attack speed.
*   **Example (Fjolnir):** *The Mountain's Resolve.* Your base Damage Resistance is permanently increased.

#### Reward 2: The Divine Boon Skill Tree
*   **The Ultimate Reward.** The player unlocks a new, powerful skill sub-tree on their main skill screen, themed to their patron.
*   This tree contains 3-4 new powerful perks, including a game-changing **Ultimate Active Ability**.
*   **Example (Sylvana's "Biomancy"):** Perks to empower tamed beasts, a passive to boost healing potions, and an ultimate that summons roots from the earth to ensnare enemies.
*   **Example (Valdrak's "Technomancy"):** Perks to improve crafted gear, a chance to craft higher-quality items, and an ultimate that animates a suit of armor to defend the player's base.

#### Reward 3: Divine Quests & Artifacts
*   **New Content:** Your patron god will now guide you on exclusive, late-game quests.
*   **Goal:** These quests lead to legendary **Artifacts**—unique weapons and armor imbued with the god's power that cannot be obtained any other way.
    *   A champion of Solana might be sent to recover the "Sun-Sworn Paladin's Helm."
    *   A champion of Morgrath might be tasked with corrupting a holy spring to forge a "Void-Blade."
*   **Faction Interaction:** Followers of your patron god will now recognize you as a holy figure, unlocking unique dialogue, barter options, and quests with their associated mortal factions (e.g., Sylvan Elves for Sylvana, Hearth-Forged Dwarves for Valdrak).
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/03_MAGIC_SYSTEMS/01_The_Grammar_of_Magic.md`
```md
# The Grammar of Magic

## 1.0. Core Philosophy
Magic in *Where Giants Rust* is not a nebulous, unknowable force. It is a fundamental system of the universe with its own rules, syntax, and logic—a **"Grammar."** While players will primarily interact with pre-packaged "spells," this underlying system provides a deep well for lore and, potentially, advanced late-game spell-crafting.

The Grammar of Magic is composed of two parts: a **Noun (The Element/Concept)** and a **Verb (The Form/Effect).**

## 2.0. The Nouns of Magic
These are the core concepts or energies that can be manipulated. They are drawn from the major magical skill trees.

*   **Elemental Nouns:** Fire, Frost, Shock
*   **Aetherial Nouns:** Light, Life, Order
*   **Void Nouns:** Shadow, Entropy, Soul

## 3.0. The Verbs of Magic (Spell Forms)
These dictate how the "Noun" is manifested in the world. Learning a new Spell Form is akin to learning a new type of spell, which can then be combined with different nouns.

*   **Form: Bolt/Projectile:**
    *   **Description:** The simplest form. Creates a single, targeted projectile.
    *   **Examples:** `Fire` + `Bolt` = **Firebolt**. `Life` + `Bolt` = a **Healing Dart**. `Entropy` + `Bolt` = a **Drain Health** spell.

*   **Form: Cloak/Aura:**
    *   **Description:** Creates a close-range aura around the caster.
    *   **Examples:** `Frost` + `Cloak` = **Frost Cloak** (damages and slows enemies near you). `Light` + `Cloak` = a **Healing Aura** for nearby allies.

*   **Form: Rune/Trap:**
    *   **Description:** Places a latent magical symbol on a surface that triggers when an enemy gets close.
    *   **Examples:** `Fire` + `Rune` = an **Explosive Fire Rune**. `Shock` + `Rune` = a **Stunning Shock Rune**.

*   **Form: Wall:**
    *   **Description:** Creates a persistent linear barrier.
    *   **Examples:** `Fire` + `Wall` = **Wall of Flames**. `Order` + `Wall` = a temporary **Wall of Force**.

*   **Form: Storm/Area of Effect (AoE):**
    *   **Description:** Creates a large, sustained magical effect over a wide area.
    *   **Examples:** `Frost` + `Storm` = **Blizzard**. `Entropy` + `Storm` = a life-draining **Field of Decay**.

## 4.0. Spell-Crafting (An End-Game Aspiration)
While most players will find and learn specific combinations (like "Fireball"), a theoretical end-game system for true Archmages could be the **Arcane Scriptorium.**

*   **Function:** A unique, high-tier crafting station that allows a player who has mastered multiple schools of magic to combine Nouns and Verbs.
*   **The Cost:** Spell-crafting would be immensely expensive, requiring rare reagents and a large expenditure of filled Soul Gems to "power" the creation of a new, custom spell tome.
*   **The Power:** This would allow for unique combinations not normally found in the world.
    *   `Soul` + `Storm` = A "Soul Storm" that attempts to soul-trap every enemy in a wide radius.
    *   `Shadow` + `Wall` = A "Wall of Blindness" that doesn't do damage but makes enemies who pass through it unable to see for a short time.

This system provides a logical framework for the game's magic, making it feel deep and consistent, while also offering a powerful and aspirational goal for dedicated mages.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/02_COMBAT_SYSTEMS/05_Magic_Combat.txt`
```txt
# Gameplay System: Magic Combat

## 1.0. Core Philosophy: The Arcanist's Toolkit
Magic in *Where Giants Rust* is a powerful and versatile tool, but not an "I-Win" button. It is governed by a finite **Mana** pool and the player's own knowledge and skill. A powerful mage is a strategic master of their spell-book, using the right element for the right situation, controlling the battlefield, and exploiting enemy weaknesses. Magic combat should feel less like a spammable ranged attack and more like wielding a powerful, dangerous, and sometimes unpredictable force.

## 2.0. The Mechanics of Spell-Casting
*   **Mana Cost:** Every spell costs Mana. Running out of Mana leaves a mage completely vulnerable. Mana regenerates slowly over time and can be restored quickly with potions.
*   **Casting Time:** Spells are not instant. Simpler spells like "Firebolt" have a very short cast time. More powerful spells like "Supernova" require a long and vulnerable channeling period.
*   **Dual-Casting:** The cornerstone of an offensive mage's power. By equipping the same spell in both hands (and taking the "Dual Casting" perk in the Elementalism tree), a player can cast a single, overcharged version of the spell.
    *   **Effect:** A dual-cast spell costs more than double the Mana, but its effect is significantly magnified (e.g., 2.5x damage, larger radius, longer duration).
    *   **Synergy:** Certain perks, like "Impact," only trigger when a spell is dual-cast, further rewarding this specialization.

## 3.0. Schools of Magic & Combat Roles

The three primary magic skill constellations define the major combat roles for a mage.

#### 3.1. Elementalism: The Artillery
*   **Role:** Raw damage and area control. This is the primary "Destruction" school.
*   **Tactics:**
    *   **Fire:** The highest damage element. Use "Fireball" for area damage, "Flame Cloak" for close-range defense, and "Fire Wall" to block off choke points.
    *   **Frost:** The control element. Use "Frostbite" to slow enemies, "Ice Spike" to stagger from afar, and "Blizzard" to lock down a large area. Essential for dealing with fast, aggressive enemies.
    *   **Shock:** The utility element. Use "Sparks" to drain enemy Mana, "Lightning Bolt" for long-range sniping, and "Chain Lightning" to deal with crowds. Especially effective against robotic and mage-type enemies.

#### 3.2. Aether: The Bastion
*   **Role:** Defense, healing, and anti-undead/anti-blighted support. The "Restoration" or "Holy" school.
*   **Tactics:**
    *   **Healing:** Use "Heal Self" or "Heal Other" to mend wounds in combat.
    *   **Wards:** Cast "Lesser Ward" to block incoming spells and arrows. Higher-level perks like "Divine Bulwark" turn this defense into an offensive explosion.
    *   **Purification:** Use spells like "Sun-Sear" and "Consecrate Ground" to deal devastating damage to Undead and Blighted foes, who are often resistant to conventional physical damage.

#### 3.3. Void: The Saboteur
*   **Role:** Debuffing, manipulation, and high-risk offense. The "Dark" or "Illusion" school.
*   **Tactics:**
    *   **Illusion:** Not direct combat, but can win a fight before it starts. Cast "Fear" to make a single powerful enemy flee, or "Frenzy" to make enemies attack each other.
    *   **Drain:** Use spells like "Drain Health" and "Drain Stamina" to weaken a tough enemy from a safe distance while replenishing your own resources.
    *   **Entropic (Late-Game):** Wield forbidden "Static" magic, a high-risk/high-reward spell type that deals immense damage but has a chance to backfire and cause a negative effect on the caster.

## 4.0. The Spell-Sword: Hybrid Combat
A player can equip a one-handed weapon in their main hand and a spell in their off-hand. This is a powerful and versatile playstyle that combines the best of both worlds.

*   **Example Tactics:**
    *   Parry an attack with a sword, then blast the staggered enemy with a close-range "Firebolt."
    *   Slow a charging enemy with a "Frost" spell, then safely close the distance to attack with a mace.
    *   Cast "Stoneflesh" from the Aether tree for a massive armor buff, then wade into melee combat like a walking tank.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/02_COMBAT_SYSTEMS/04_Damage_and_Armor_Formulas.md`
```md
# Damage and Armor Formulas

## 1.0. Core Philosophy
The damage formulas are designed to be understandable and impactful. Players should have a clear sense of why upgrading their weapon (Base Damage) or their primary attribute (Stat Bonus) is a meaningful choice. The Armor system provides clear damage reduction but with diminishing returns to prevent "invincibility" at high levels.

## 2.0. Base Damage Calculation
This is the core formula used before any mitigation from armor is applied.

`Final_Damage = (Weapon_Base_Damage + Flat_Bonus_Damage) * (1 + Stat_Bonus_Multiplier) * (Crit_Multiplier)`

---
#### **Component Breakdown:**

*   **`Weapon_Base_Damage`**: The inherent damage of the weapon, determined by its type and quality (e.g., an Iron Sword has 15, a Steel Sword has 22).

*   **`Flat_Bonus_Damage`**: Any bonus damage added from enchantments or effects (e.g., a "+10 Fire Damage" enchant adds 10 to this value).

*   **`Stat_Bonus_Multiplier`**: The bonus damage from player attributes.
    *   **Melee Weapons:** `(Strength * 0.005)`. Every 10 points of Strength add 5% to your base melee damage.
    *   **Ranged Weapons:** `(Agility * 0.005)`. Every 10 points of Agility add 5% to your base ranged damage.
    *   **Magical Spells:** `(Intelligence * 0.005)`. Every 10 points of Intelligence add 5% to your spell power.

*   **`Crit_Multiplier`**:
    *   Standard Hit: Value is `1.0`.
    *   Critical Hit: Value is `2.0` (or higher with certain perks). Critical hits are determined by the player's Luck stat and other perks.

---
## 3.0. Armor and Damage Reduction
The Armor Rating (AR) stat reduces incoming *physical* damage (slashing, piercing, blunt). Elemental damage is reduced by separate Resistance stats.

`Physical_Damage_Taken = Final_Damage * (1 - (Armor_Rating / (Armor_Rating + 500)))`

---
#### **Formula Explanation:**

This formula provides diminishing returns.
*   **Example 1 (Low Armor):**
    *   Player has `100 AR`.
    *   `1 - (100 / (100 + 500))` = `1 - (100 / 600)` = `1 - 0.167` = `0.833`
    *   The player takes **83.3%** of the incoming damage (a **16.7% reduction**).

*   **Example 2 (High Armor):**
    *   Player has `500 AR`.
    *   `1 - (500 / (500 + 500))` = `1 - (500 / 1000)` = `1 - 0.5` = `0.5`
    *   The player takes **50%** of the incoming damage (a **50% reduction**).

*   **Example 3 (Extreme Armor):**
    *   Player has `1000 AR`.
    *   `1 - (1000 / (1000 + 500))` = `1 - (1000 / 1500)` = `1 - 0.667` = `0.333`
    *   The player takes **33.3%** of the incoming damage (a **66.7% reduction**).

As you can see, the first 500 points of armor provide a huge 50% damage reduction. The *next* 500 points only provide an additional 16.7%. This makes armor very important but prevents players from becoming completely immune to physical threats.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/02_COMBAT_SYSTEMS/03_Stealth_Mechanics.md`
```md
# Gameplay System: Stealth Mechanics

## **1.0. Core Philosophy: The Unseen Hunter**

The stealth system in *Where Giants Rust* is designed as a viable and deep alternative to open combat. It is a system built on risk versus reward, where patience and observation are the player's greatest weapons. The core gameplay loop of stealth is not just about avoiding enemies, but about manipulating the environment and the AI's senses to control the flow of an encounter, ending it decisively from the shadows or bypassing it altogether.

## **2.0. The Mechanics of Detection**

Player detection is not a simple "on/off" switch. It is a calculated value based on three primary factors: **Sight, Sound, and Light.**

#### **2.1. The Detection Meter**
*   When an enemy is becoming aware of the player, a visual indicator (like a filling diamond or eye icon) will appear over their head.
*   **Empty:** The enemy is unaware.
*   **Filling (White):** The enemy is alerted and is moving to investigate the player's last known position or a sound disturbance.
*   **Full (Red):** The player is fully detected. The enemy will enter its "Hunting State" (shrieking and attacking).

#### **2.2. Sight**
*   **Line of Sight:** The primary factor. If an enemy can draw a direct, unobstructed line to the player, the detection meter will begin to fill rapidly.
*   **Cover:** Crouching behind objects (rocks, walls) or within tall grass breaks line of sight.
*   **Movement:** Moving is more noticeable than standing still. The faster the movement, the more easily the player is seen. Crouching drastically reduces the player's visual profile.
*   **Distance:** The further away the player is, the harder they are to see.

#### **2.3. Sound**
*   **Noise Bubbles:** Every action the player takes generates a "noise bubble" of a certain radius. Any enemy within this radius will be instantly alerted and will move to investigate the source.
*   **Sound Levels:**
    *   **Low:** Walking slowly, aiming a weapon, using a consumable.
    *   **Medium:** Jogging, harvesting a resource (chopping/mining).
    *   **High:** Sprinting, casting a loud spell, breaking a structure.
    *   **Extreme:** Firing an unsuppressed firearm (alerts a very large area).
*   **Player Stance:** Crouching ("sneaking") significantly reduces the radius of all sound bubbles. The "Muffled Movement" perk in the **Shadow** skill tree further reduces this.

#### **2.4. Light**
*   **Light Level:** Every part of the world has a "light level" value, from the pitch black of a cave to the bright glare of noon.
*   **Effect on Detection:** The brighter the light the player is standing in, the further away an enemy can see them. Standing in deep shadow makes the player extremely difficult to spot, even if they are partially in an enemy's line of sight.
*   **The Day/Night Cycle:** This is the most significant factor. During the day, visibility is high everywhere. At night, shadows are deep, but enemies (especially the Blighted) gain enhanced "night vision," making light management critical.

## **3.0. Stealth-Based Actions & Abilities**

These are the primary actions a player will use while in stealth mode.

*   **Sneak / Crouch:** The default stealth stance. Reduces movement speed, visual profile, and noise generated.
*   **Stealth Attack:** Attacking an enemy that has not yet detected you. This grants a massive damage multiplier. This is the primary payoff for a stealthy approach. Different weapons will have different multipliers, governed by perks in the **Warrior** and **Shadow** trees.
*   **Distraction:** The player can throw objects (like rocks) to create a sound disturbance away from their position, luring enemies to investigate the wrong area. Craftable "Noise-maker" arrows and gadgets expand on this.
*   **Takedowns:** A high-level **Shadow** perk may unlock non-lethal "takedowns" on unaware humanoid enemies, allowing for a pacifist infiltration style.

## **4.0. Interacting with Other Systems**

Stealth is not an isolated system; it is deeply interwoven with the rest of the game.

*   **AI Behavior:** The "Dormant -> Alerted -> Hunting" states of the Blighted AI are the core feedback loop for the stealth system. The player's goal is to never let an enemy transition to the Hunting state.
*   **Apparel & Gear:** The weight and material of equipped gear directly impact stealth. Heavy metal armor is loud and easy to see. Soft leather or cloth gear is much quieter. Specialized gear like the "Umbral Elve's Silent-Tread Boots" can make a player nearly silent.
*   **Magic:** The magic system offers powerful tools for a stealth build.
    *   **Illusion Magic (from the Void tree):** Spells to turn invisible, create decoys, or muffle sound are the ultimate stealth tools. The "Silent Casting" perk is essential for a magic-using stealth character.
    *   **Light Magic (from the Aether tree):** Can be used defensively to create a "blinding flash," allowing a player to escape after being detected.
*   **The Environment:** Weather provides natural cover. Heavy rain and thunderstorms mask sound and reduce visibility, making them the perfect time for a stealthy infiltration. Fog is even more effective.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/02_COMBAT_SYSTEMS/02_Ranged_Combat.md`
```md
# Gameplay System: Ranged Combat

## **1.0. Core Philosophy: The Art of Positioning**

The ranged combat system in *Where Giants Rust* is built around the principles of **positioning, precision, and resource management.** Unlike melee, which is about managing stamina in close quarters, ranged combat is a tactical game of maintaining distance, exploiting weak points, and managing a finite supply of ammunition. Every shot must be considered, whether it's an arrow fletched by hand or a rare, salvaged rifle cartridge.

## **2.0. Universal Ranged Mechanics**

All ranged weapons share these fundamental mechanics.

*   **Aiming:** All ranged weapons can be "aimed down sights," which brings the camera closer, tightens the weapon's spread, and reveals a reticle for precise aiming.
*   **Ammunition:** Ranged weapons are useless without ammunition. Arrows, bolts, and bullets are all finite, craftable, or lootable resources. Managing this supply is a core challenge of the playstyle.
*   **Projectile Drop & Travel Time:** To create a satisfying skill curve, most projectiles (especially arrows and bolts) are not "hitscan." They are physical objects that are affected by gravity and have a travel time, requiring players to lead moving targets and aim high over long distances.
*   **Weak Points:** Many enemies have designated weak points (e.g., the head, a glowing spot on their back). Hitting a weak point with a ranged attack results in a guaranteed critical hit, rewarding precise aim.

## **3.0. Weapon Archetypes & Identity**

This system covers three main families of ranged weaponry.

#### **3.1. Primitive & Traditional (Bows)**
*   **Description:** The workhorse of the early-to-mid game survivor. Bows are craftable from basic materials and are completely silent, making them the ideal weapon for stealthy hunters.
*   **Mechanics:** Require the player to hold down the fire button to "draw" the bow. Releasing the button fires the arrow. A fully-drawn shot has the best range, damage, and accuracy. Holding a draw for too long will consume stamina and decrease accuracy.
*   **Ammunition:** Arrows (Stone, Iron, Steel, etc.) and specialty arrows (Fire, Poison, Noise-maker) crafted via the **Smithing** and **Alchemy** skill trees.

#### **3.2. Mechanical (Crossbows)**
*   **Description:** Slower to use than bows but more powerful and easier to aim. They represent a mid-tier of technology.
*   **Mechanics:** Firing a crossbow is instant once it's loaded. However, it has a long reload animation after every shot. Players can load a bolt and then walk around with the crossbow ready to fire indexfinitely.
*   **Ammunition:** Bolts, which are heavier and often have better armor penetration than arrows.

#### **3.3. Advanced & Salvaged (Firearms)**
*   **Description:** The pinnacle of ranged technology. These are rare, powerful, and very loud weapons salvaged from pre-cataclysm ruins (Anomalous Structures, Military Bases).
*   **Mechanics:** Firearms are typically "hitscan" or have extremely fast projectile speeds, making them easier to use against fast-moving targets. Their downside is their noise, which will alert every enemy in a very wide radius, and their extremely rare, non-craftable (at first) ammunition.
*   **Weapon Types:**
    *   **Revolvers/Pistols:** Sidearms with low damage but a fast rate of fire and reload speed.
    *   **Shotguns:** Devastating at close range, firing a spread of pellets.
    *   **Bolt-Action Rifles:** The ultimate sniper weapon. Extremely high damage and accuracy, but a very slow rate of fire.

## **4.0. The Magic & Tech Interface**

Ranged combat is a perfect platform for magical and technological augmentation.

#### **4.1. Magical Enhancement**
*   **Enchanting:** Bows and crossbows are ideal candidates for enchanting at an **Arcane Enchanter**. Common enchantments include adding elemental damage (`Fiery Soul Trap`), automatically regenerating ammunition (`Bound Quiver`), or increasing draw speed.
*   **Specialty Ammunition:** The **Alchemy** system is the primary way to create magical arrows and bolts. A player can craft arrows that create a small explosion, deliver a potent magical poison, or glow to illuminate a target.
*   **Spell-Archer Gameplay:** The left hand is free while using a bow (except when drawing). A skilled player can cast utility spells like a "Warding" circle for protection or an "Illusion" spell to create a decoy, then switch to their bow to pick off the confused enemies.

#### **4.2. Future Tech Augmentation**
*   **Weapon Modification:** Firearms are the primary focus of the **Tech** skill tree's modification system. At a high-tier workbench, a player can:
    *   Install a **Scope** for better zoom.
    *   Add a **Suppressor** to drastically reduce the weapon's noise (at the cost of some damage).
    *   Craft an **Extended Magazine** to increase ammo capacity.
*   **The Energy Weapon Sub-class (End-Game):**
    *   The rarest firearm type. These weapons do not use ballistic ammunition. Instead, they fire bolts of pure plasma or laser energy.
    *   **Mechanics:** They drain power directly from a new resource: **Energy Cells**. Energy Cells are craftable but require extremely rare materials (like Blighted Crystals) and a high-tier tech workbench. This makes these weapons powerful but very expensive to maintain.

This design ensures a deep and evolving ranged combat experience, starting with a humble wooden bow and culminating in a highly customized, magically enchanted, or technologically advanced firearm.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/02_COMBAT_SYSTEMS/01_Melee_Combat.md`
```md
# Gameplay System: Melee Combat

## **1.0. Core Philosophy: The Weight of Steel**

The melee combat system in *Where Giants Rust* is designed to feel **deliberate, weighty, and impactful.** It is not a fast-paced "hack-and-slash" system. Every swing, block, and dodge should feel like a conscious tactical decision governed by a player's **Stamina** management. The goal is to create a grounded, physical foundation that can be spectacularly enhanced by the game's more exotic magic and tech systems.

The core loop of melee combat is a dance of **offense, defense, and positioning.**

## **2.0. The Fundamentals of Combat**

These are the universal actions available to any character wielding a melee weapon.

#### **2.1. Offense**
*   **Light Attack:** A quick, low-damage attack that consumes a small amount of stamina. Useful for interrupting weaker enemies or finishing off a staggered foe. Can be chained together.
*   **Heavy Attack:** A slower, more powerful attack that consumes a large amount of stamina. It has a higher chance to stagger enemies and break through their blocks. Cannot be chained rapidly.

#### **2.2. Defense**
*   **Blocking:** Holding a shield or a two-handed weapon in a defensive stance. Reduces incoming physical damage at the cost of stamina. A perfectly timed block ("parry") can deflect an incoming attack entirely and briefly stagger the attacker, creating an opening for a counter-attack.
*   **Dodging:** A quick roll or sidestep that grants a brief moment of invincibility ("i-frames"). Consumes a significant amount of stamina. It is the primary way to avoid unblockable or heavy attacks.

## **3.0. Weapon Archetypes & Identity**

Each class of melee weapon has a distinct feel and tactical purpose, governed by its unique moveset and properties. This is primarily defined in **The Warrior** skill tree.

*   **One-Handed Swords:** The balanced option. Fast swing speed, moderate damage. Their heavy attack is a piercing thrust.
*   **One-Handed Axes:** Good against armored foes. Moderate speed, high chance to cause a "Bleed" effect. Their heavy attack is a wide, horizontal cleave.
*   **One-Handed Maces:** The stagger kings. Slower swing speed but deal immense "impact" damage, making them excellent at breaking shields and staggering enemies. Their heavy attack is a powerful overhead slam.
*   **Two-Handed Weapons (Greatswords, Greataxes, Warhammers):** High-risk, high-reward. These weapons are slow and consume huge amounts of stamina but deal massive damage in a wide arc, capable of hitting multiple enemies. They can block, but are less effective at it than a shield.

## **4.0. The Magic & Tech Interface**

This is where our grounded combat system becomes truly unique. Melee combat is not separate from magic; it is a canvas for it.

#### **4.1. Weapon Enchantments & Coatings**
*   **The Smith's Role:** The **Smithing** skill tree allows players to use the **Arcane Enchanter** to imbue weapons with permanent magical effects (e.g., "+10 Fire Damage," "Absorbs 5 Stamina on hit"). This is a primary end-game goal for any warrior.
*   **The Alchemist's Role:** The **Alchemy** skill tree allows players to create temporary **weapon coatings**. These are consumable items that can be applied to any weapon to give it a temporary effect, such as a potent poison or an oil that sets it on fire for the next 60 seconds. This provides magical effects for non-enchanted weapons.

#### **4.2. "Spell-Sword" Hybrid Gameplay**
The game's controls will be designed to facilitate a fluid "spell-sword" playstyle. A player can have a one-handed weapon in their right hand and a spell from the **"Grammar of Magic"** system in their left.
*   **Tactical Synergies:**
    *   Cast a "Frost" spell to slow an enemy, then move in for a safe melee attack.
    *   Block an incoming arrow with a magical "Ward" spell while simultaneously attacking with your sword.
    *   Use a quick **"Telekinesis: Push"** spell to stagger an enemy, creating an opening for a heavy attack.
*   **Self-Buffs:** Aether and Void magic allows a warrior to cast powerful self-buffs like **"Stoneflesh"** (for increased armor) or **"Shadow Jaunt"** (for a quick, invisible reposition).

#### **4.3. Tech Augmentations**
*   **The Techie's Role:** The **Tech** skill tree allows for a different kind of "enchanting." A player can install salvaged tech **mods** onto weapons at a workbench.
*   **Examples:**
    *   A **"Kinetic Inductor"** on a warhammer that stores energy with each swing and releases it in a small shockwave on a power attack.
    *   A **"Pressurized Injector"** on an axe that automatically applies a single dose of poison from the player's inventory without needing to be coated manually.

This design ensures that melee combat is satisfying on its own but truly shines when a player begins to layer magical and technological enhancements onto their physical prowess.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/02_Leveling_and_Experience.md`
```md
# Leveling and Experience System

## **1.0. Core Philosophy: Organic Growth through Action**

The leveling system in *Where Giants Rust* is designed to reward players for **doing**, not just for completing quests. While killing enemies and finishing tasks are major sources of experience, the system is fundamentally built on the principle that characters get better at what they practice. This creates a dynamic and immersive progression where a player's actions directly and visibly shape their character's overall power.

The system is divided into two parts: gaining **General Experience (XP)** to increase your main character Level, and improving individual **Skill Proficiencies** through repeated use.

## **2.0. General Experience (XP) & Character Leveling**

This governs the player's main level and the acquisition of **Attribute Points**. Every action falls into a category that grants XP.

#### **2.1. XP from Combat**
This is the most straightforward source, but it is scaled by challenge.
*   **The Power-Gap Bonus:** XP gains are massively inflated when defeating an enemy whose level or power rating is significantly higher than the player's. Defeating a Level 20 beast as a Level 10 player will yield a huge XP reward. Conversely, a Level 20 player killing a Level 5 creature will receive trivial or zero XP. This encourages players to push their limits.
*   **Combat Style Multipliers:** A small XP bonus is granted for "skilled" victories, such as defeating an enemy without taking damage ("Flawless Victory"), or winning a fight against multiple opponents simultaneously ("Overwhelming Odds").

#### **2.2. XP from Exploration & Survival**
*   **Discovery:** A significant, one-time XP bonus is granted for discovering a new Point of Interest, Dungeon, or major landmark for the first time.
*   **Endurance Under Duress (The "Training" System):** The game tracks the player's physical exertion and rewards it with a slow but steady stream of XP.
    *   **Encumbrance Training:** The closer the player is to their maximum carry weight, the more XP they gain passively from simply moving (sprinting, jumping). This rewards players for hauling back a big load of resources, turning a boring walk into a "strength training" session.
    *   **Environmental Hardship:** The player gains a small, steady XP tick while actively resisting an environmental hazard, like surviving a blizzard with "Cold" status or exploring a Blighted zone with "Corruption." This rewards preparation and endurance.

#### **2.3. XP from Creation & Discovery**
*   **Crafting:** A one-time XP bonus is granted the first time the player crafts any new, unique item. Crafting a simple stone axe for the first time gives a small reward; crafting a high-tier enchanted sword for the first time gives a massive reward. Grinding out hundreds of the same item provides no further XP.
*   **Research & Lore:** A significant XP bonus is awarded for discovering and reading a new lore object, deciphering a new rune, or fully analyzing a new creature/plant with A.R.I.A.'s scanner.

#### **2.4. Leveling Up**
When the player's General XP bar is full, they "Level Up."
*   **Reward:** The player gains a set number of **Attribute Points** (e.g., 3-5) to spend on their six Core Attributes (STR, AGI, INT, etc.).
*   **Gating:** The player's main character level acts as a soft "gate" for the quality of gear they can effectively use and the complexity of recipes they can learn, preventing new players from immediately equipping end-game items.

## **3.0. Skill Proficiency (Learn-by-Doing)**

Separate from the main leveling system, **every individual skill on the Skill Tree has its own proficiency bar.** This system rewards specialization.

*   **How it Works:** Using an ability or action related to a skill increases that skill's proficiency.
    *   Successfully sneaking past an enemy increases the "Stealth" skill proficiency.
    *   Hitting an enemy with a fireball spell increases the "Fire Magic" proficiency.
    *   Blocking an attack with a shield increases the "Shield" proficiency.
*   **Unlocking New Skills:** Points on the main Skill Trees can only be spent if the player has reached a certain proficiency level in that branch. For example, to unlock the "Improved Power Attack" skill, the player might need to have both reached Character Level 10 AND achieved a "Heavy Weapons" proficiency of 25.
*   **Mastery Bonuses:** Reaching certain proficiency thresholds (e.g., 25, 50, 75, 100) in a skill provides small, permanent passive bonuses related to that skill, such as `"-5% Stamina Cost for Power Attacks"` or `"+5% Fire Spell Damage"`.

This two-pronged approach creates a perfect feedback loop: a player who loves using heavy axes will naturally get better with them (**Proficiency**), which will help them defeat tougher enemies, which will grant them more **General XP**, allowing them to increase their **Strength Attribute**, which in turn makes their heavy axe attacks even stronger.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/01_Stats_and_Attributes.md`
```md
# Player Stats and Attributes

## **1.0. Core Philosophy: Intentional Growth**

The stat system in *Where Giants Rust* gives players direct control over their character's growth. There are no rigid classes. Instead, players invest points into six **Core Attributes** upon leveling up. These attributes govern a set of **Derived Stats** that directly impact gameplay, allowing for fluid and specialized character builds.

## **2.0. Primary Resources (The Vitals)**

These are the core resource pools the player actively manages during gameplay and sees on the HUD.

*   **Health:** Governed by **Vitality**. Your physical integrity. Reaching zero results in death.
*   **Stamina:** Governed by **Endurance**. Fuel for physical actions like sprinting, dodging, and power attacks.
*   **Mana:** Governed by **Intelligence**. The resource pool for casting all magical spells.

## **3.0. The Six Core Attributes**

Upon leveling up, the player receives Attribute Points to invest in the following six attributes. Each point provides a direct, meaningful bonus.

#### **3.1. Strength (STR)**
*   **Represents:** Raw physical power and martial prowess.
*   **Primary Effect:** Directly increases the **damage of all melee weapons**.
*   **Secondary Effects:**
    *   Slightly increases **Carry Weight**.
    *   Required to wield the heaviest weapons and armor without a performance penalty.

#### **3.2. Agility (AGI)**
*   **Represents:** Bodily coordination, speed, and stealth. This attribute is purely for **movement and evasion**.
*   **Primary Effect:** Increases **Movement Speed** (both base speed and sprinting).
*   **Secondary Effects:**
    *   Reduces the stamina cost of **Dodging** and **Jumping**.
    *   Increases the effectiveness of **Stealth**, making you harder for enemies to detect.

#### **3.3. Intelligence (INT)**
*   **Represents:** Mental acuity, arcane knowledge, and technological aptitude.
*   **Primary Effect:** Increases **Maximum Mana** and **Magical Damage/Effectiveness**.
*   **Secondary Effects:**
    *   Increases the effectiveness of **Salvaging** tech components.
    *   Slightly increases the amount of **Experience Points (XP)** gained from all sources.

#### **3.4. Vitality (VIT)**
*   **Represents:** Health and physical resilience to harm.
*   **Primary Effect:** Massively increases **Maximum Health**. Every point provides a significant boost.
*   **Secondary Effects:**
    *   Slightly increases resistance to **Poison** and **Bleed** effects.

#### **3.5. Endurance (END)**
*   **Represents:** Physical stamina and environmental hardiness.
*   **Primary Effect:** Massively increases **Maximum Stamina**. Every point provides a significant boost.
*   **Secondary Effects:**
    *   Increases resistance to environmental hazards like **Cold**, **Heat**, and the **Corruption** of Blighted zones.
    *   Slightly improves the effectiveness of **Blocking** with shields.

#### **3.6. Luck (LCK)**
*   **Represents:** Fortune, chance, and the ability to find opportunity in chaos.
*   **Primary Effect:** Increases your **Critical Hit Chance** with all forms of attack.
*   **Secondary Effects:**
    *   Slightly increases the chance of finding **Rare Items** in loot containers.
    *   Slightly increases the chance of a "special" outcome in random events.

## **4.0. Attribute Synergies & Build Archetypes**

This system encourages players to specialize but allows for powerful hybrid builds.
*   **The Warrior:** Focuses on **Strength** for damage, **Vitality** for survivability, and **Endurance** for sustained combat.
*   **The Rogue:** Focuses on **Agility** for movement and stealth, **Strength** for melee backstabs or **Intelligence** for gadget damage, and **Luck** for critical hits.
*   **The Mage:** Focuses almost entirely on **Intelligence** for magical power, with secondary investment in **Vitality** or **Endurance** to stay alive.
*   **The Survivor:** A balanced build focusing on **Endurance** and **Vitality** first, making them exceptionally tough and resilient, branching into combat stats later.
*   **The Gambler:** A high-risk build focusing on **Luck** and a single damage stat (STR or INT), relying on frequent critical hits to succeed.

This clear separation of stats gives players a very direct and satisfying sense of progression. Investing a point in Vitality will always mean a bigger health bar, making every choice feel immediately impactful.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/13_The_Void.md`
```md
# Skill Tree: The Void

## **1.0. Constellation Overview**

*   **Discipline:** Dark, Entropic, & Soul Magic.
*   **Description:** The Void constellation governs the forbidden arts that draw power from darkness, decay, and the spaces between realities. A master of the Void is a terrifying figure, able to drain the very life force from their enemies, conjure illusions from shadow, and manipulate the souls of the dead. This is a powerful but dangerous path, often frowned upon by stalwart allies and benevolent gods.

## **2.0. Visual Layout**

The constellation is shaped like a black hole or a dark spiral galaxy. The outer rim holds the foundational perks. The player's path then spirals inwards towards the center, choosing between three main arms of the galaxy: **The Soul Thief** (focused on soul manipulation and enchanting), **The Shadow Weaver** (focused on illusion and trickery), and **The Nihilist** (focused on entropy and decay).

## **3.0. Perk List**

---
### **The Outer Rim (Core Void Skills)**

*   **Acolyte (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Each rank reduces the Mana cost of all Novice-level Void (Dark/Illusion) spells by 10%.
    *   *Connects to: Soul Trap and all three branches*

*   **Soul Trap**
    *   **Proficiency Req:** 20
    *   **Effect:** Unlocks the "Soul Trap" spell. If a non-robotic enemy dies while under the effect of this spell, its soul is captured in the largest empty **Soul Gem** in your inventory. Filled Soul Gems are required for enchanting gear.
    *   *Connects to: The Soul Thief branch*

---
### **The Soul Thief Branch (Soul Manipulation)**

*   **Soul Siphon**
    *   **Proficiency Req:** 30 (Soul Magic)
    *   **Effect:** Killing any creature with a soul-trapped weapon now also restores a small amount of your Mana.
    *   *Connects to: Soul Eater*

*   **Soul Eater (Ultimate Soul Skill)**
    *   **Proficiency Req:** 90 (Soul Magic)
    *   **Effect:** You learn to consume souls for power. You can now crush a filled Soul Gem at any time to restore a large amount of Health and Mana. The amount restored is based on the size of the soul.

---
### **The Shadow Weaver Branch (Illusion & Trickery)**

*   **Whispering Shadows**
    *   **Proficiency Req:** 30 (Illusion)
    *   **Effect:** Illusion spells like "Fear" and "Frenzy" now work on higher-level enemies.
    *   *Connects to: Silent Casting*

*   **Silent Casting**
    *   **Proficiency Req:** 50 (Illusion)
    *   **Effect:** Casting any spell from any magic school no longer produces sound, preventing you from revealing your position to enemies when casting from stealth.
    *   *Connects to: Master of the Mind*

*   **Master of the Mind (Ultimate Illusion Skill)**
    *   **Proficiency Req:** 90 (Illusion)
    *   **Effect:** You can now cast illusion spells on powerful enemy types that were previously immune, such as Undead, constructs, and even some lesser daedra.

---
### **The Nihilist Branch (Entropy & Decay)**

*   **Corrupted Core**
    *   **Proficiency Req:** 40 (Entropic Magic)
    *   **Effect:** Your body begins to adapt to forbidden energies. You gain a +25% resistance to Corruption and disease.
    *   *Connects to: Life Drain*

*   **Life Drain**
    *   **Proficiency Req:** 70 (Entropic Magic)
    *   **Effect:** Your "Drain Health" and "Drain Stamina" type spells are 50% more effective, absorbing more from the target.
    *   *Connects to: Reality Glitch*

*   **Reality Glitch (Ultimate Entropic Skill)**
    *   **Proficiency Req:** 90 (Entropic Magic), must be aligned with The Axis Mind.
    *   **Effect:** Your understanding of decay borders on that of The Static. Your damage-dealing Void spells have a small chance to "glitch" the enemy, briefly erasing them from existence for 1-2 seconds before they reappear, their resistances temporarily lowered.

---
### **The Void Capstone Perk**

*   **Void-Sworn**
    *   **Proficiency Req:** 100
    *   **Effect:** Your command of the dark arts is absolute. Killing an enemy with a Void spell recharges the Soul Gem used in your equipped enchanted weapon by 10%. This allows a master warlock to sustain their enchanted weapons almost indexfinitely in combat.
    *   **Location:** This is the singularity at the very center of the spiraling constellation, the mark of a true master of the void.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/12_Aether.md`
```md
# Skill Tree: The Aether

## **1.0. Constellation Overview**

*   **Discipline:** Light, Divine, & Restoration Magic.
*   **Description:** The Aether constellation governs the magic of order, spirit, and life itself. Unlike the raw, destructive power of Elementalism, Aetherial magic is focused and purposeful. Its perks grant the ability to heal the wounded, create protective wards, turn back the undead, and draw power directly from the soul. This is the path of the Paladin, the Priest, and the Protector.

## **2.0. Visual Layout**

The constellation is shaped like a radiant, stylized sun or a holy symbol. The central "core" holds the foundational perks. From this core, three major rays of light branch out: **The Hand of Mercy** (healing), **The Aegis of Light** (protection and wards), and **The Soul Purifier** (anti-undead and spiritual damage).

## **3.0. Perk List**

---
### **The Core (Foundational Aether Skills)**

*   **Adept (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Each rank reduces the Mana cost of all Novice-level Aether (Restoration/Light) spells by 10%.
    *   *Connects to: Soul Seeker and all three branches*

*   **Soul Seeker**
    *   **Proficiency Req:** 20
    *   **Effect:** You can now perceive and interact with ethereal entities, such as ghosts and spirits. You are able to "loot" defeated spiritual enemies for **Soul Fragments**, a key reagent for enchanting.
    *   *Connects to: The Soul Purifier branch*

---
### **The Hand of Mercy Branch (Healing)**

*   **Regeneration**
    *   **Proficiency Req:** 30 (Restoration)
    *   **Effect:** All healing spells are now 25% more effective.
    *   *Connects to: Respite*

*   **Respite**
    *   **Proficiency Req:** 50 (Restoration)
    *   **Effect:** Healing spells now also restore a small amount of the target's Stamina.
    *   *Connects to: Merciful Spirit*

*   **Merciful Spirit (Ultimate Healing Skill)**
    *   **Proficiency Req:** 90 (Restoration)
    *   **Effect:** When you heal an ally (or yourself) who is below 25% health, the healing spell has a chance to be a "critical heal," restoring twice the amount of health.

---
### **The Aegis of Light Branch (Protection)**

*   **Warding**
    *   **Proficiency Req:** 30 (Wards)
    *   **Effect:** Your protective ward spells (e.g., "Stoneflesh," "Magic Ward") are 25% stronger and last 50% longer.
    *   *Connects to: Arcane Bastion*

*   **Arcane Bastion**
    *   **Proficiency Req:** 60 (Wards)
    *   **Effect:** You can now cast and maintain a ward spell while also wielding a weapon or another spell, allowing you to block and attack simultaneously.
    *   *Connects to: Divine Bulwark*

*   **Divine Bulwark (Ultimate Ward Skill)**
    *   **Proficiency Req:** 90 (Wards)
    *   **Effect:** If a magical ward you are casting breaks from taking too much damage, it shatters in an explosion of holy energy, staggering and damaging nearby enemies.

---
### **The Soul Purifier Branch (Anti-Undead)**

This branch splits off from Soul Seeker.

*   **Sun's Judgment**
    *   **Proficiency Req:** 40 (Light Magic)
    *   **Effect:** Light-based spells (like Sun-Sear) now set Undead and Blighted creatures on holy fire, causing them to take extra damage over time.
    *   *Connects to: Turn Undead*

*   **Turn Undead**
    *   **Proficiency Req:** 70 (Light Magic)
    *   **Effect:** Spells and effects that specifically target Undead now have a chance to make weaker undead creatures (e.g., skeletons, shambling corpses) flee in terror for a short duration.

---
### **The Aether Capstone Perk**

*   **Beacon of Hope**
    *   **Proficiency Req:** 100
    *   **Effect:** You have become a living conduit for aetherial energy. When you cast any Aether spell, you and all nearby allies gain a "Hopeful" buff for 10 seconds, which increases all regeneration (Health, Stamina, Mana) by a small amount. This effect does not stack but its duration can be refreshed.
    *   **Location:** This is the brilliant, final star at the very top of the radiant sun, the mark of a true master of life and light.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/11_Elementalism.md`
```md
# Skill Tree: The Elementalism

## **1.0. Constellation Overview**

*   **Discipline:** Offensive & Utility "Grammar of Magic."
*   **Description:** The Elementalism constellation governs the raw, untamed forces of nature. A master of Elementalism wields fire as a weapon of pure destruction, frost as a tool of absolute control, and shock as a bolt of draining, unpredictable energy. This tree is the primary source of offensive spells and is crucial for any player wanting to specialize as a powerful mage.

## **2.0. Visual Layout**

The constellation is shaped like a tri-quetra or a triangular knot, with a central core of general magical skills. Each of the three points of the knot is a major branch dedicated to one of the core elements: **The Path of Fire**, **The Path of Frost**, and **The Path of Shock**.

## **3.0. Perk List**

---
### **The Central Knot (Core Magical Skills)**

*   **Apprentice (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Each rank reduces the Mana cost of all Novice-level Elemental spells by 10%.
    *   *Connects to: Dual Casting*

*   **Dual Casting**
    *   **Proficiency Req:** 20
    *   **Effect:** The most crucial perk for an offensive mage. If you have the same spell equipped in both hands, you can cast them together to create a single, more powerful "overcharged" version that costs more mana but has a significantly greater effect (more damage, larger radius, etc.).
    *   *Connects to: Impact and all three Elemental branches*

*   **Impact**
    *   **Proficiency Req:** 40
    *   **Effect:** Most targeted destruction spells (e.g., Firebolt, Ice Spike) when dual-cast, will now stagger most enemies on a direct hit, interrupting their attacks.
    *   *Connects to: The capstone perk*

---
### **The Path of Fire (Top Branch - Destruction)**

*   **Intense Flames**
    *   **Proficiency Req:** 30 (Fire Magic)
    *   **Effect:** Your fire spells now ignite targets, causing them to take extra burning damage over time.
    *   *Connects to: Aspect of Fire*

*   **Aspect of Fire (Ultimate Fire Skill)**
    *   **Proficiency Req:** 90 (Fire Magic)
    *   **Effect:** Your mastery of flame is complete. Enemies who are on fire have a chance to flee in terror. You gain a permanent +25% resistance to fire damage.

---
### **The Path of Frost (Left Branch - Control)**

*   **Deep Freeze**
    *   **Proficiency Req:** 30 (Frost Magic)
    *   **Effect:** Frost spells now slow enemy movement and attack speed much more significantly.
    *   *Connects to: Aspect of Frost*

*   **Aspect of Frost (Ultimate Frost Skill)**
    *   **Proficiency Req:** 90 (Frost Magic)
    *   **Effect:** Your mastery of cold is absolute. Frost spells can now completely freeze low-health enemies solid for several seconds. You gain a permanent +25% resistance to frost damage.

---
### **The Path of Shock (Right Branch - Utility)**

*   **Disintegrate**
    *   **Proficiency Req:** 30 (Shock Magic)
    *   **Effect:** Shock spells now drain a portion of the target's Mana in addition to their Health. Robotic enemies take extra damage.
    *   *Connects to: Aspect of Shock*

*   **Aspect of Shock (Ultimate Shock Skill)**
    *   **Proficiency Req:** 90 (Shock Magic)
    *   **Effect:** Your mastery of lightning is supreme. Shock spells now have a chance to arc to nearby enemies upon impact. You gain a permanent +25% resistance to shock damage.

---
### **The Elementalism Capstone Perk**

*   **Master of the Elements**
    *   **Proficiency Req:** 100
    *   **Effect:** Your command over the elements is unparalleled. Casting a spell of one element (Fire, Frost, or Shock) briefly empowers spells of the other two elements. For 3 seconds after casting a fire spell, your frost and shock spells cost 50% less Mana. The same applies when casting frost or shock spells.
    *   **Location:** This is the brilliant star at the very center of the tri-quetra knot, connecting all three elemental paths. It rewards a true Archmage who has mastered every aspect of Elementalism, enabling devastating, rapid-fire spell combos.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/10_The_Tech.md`
```md
# Skill Tree: The Tech

## **1.0. Constellation Overview**

*   **Discipline:** Salvaging, Mechanics, Hacking, & Engineering.
*   **Description:** The Tech constellation governs the mastery of old-world technology. A player invested in this tree can pull valuable components from worthless junk, repair and operate complex vehicles, modify their gear with high-tech upgrades, and turn an enemy's automated defenses against them. They are the crucial link between the primitive survival of the new world and the lost power of the old one.

## **2.0. Visual Layout**

The constellation is shaped like a complex, branching circuit board. The "power input" at the bottom contains the foundational perks. The main "bus" runs up the center, representing general mechanical aptitude. From this bus, three distinct processor branches emerge: **The Scrapper** (salvaging and component-level work), **The Engineer** (mechanics and vehicles), and **The Saboteur** (hacking and robotics).

## **3.0. Perk List**

---
### **The Power Input (Core Tech Skills)**

*   **Component Analysis (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Each rank gives you a 10% higher chance of harvesting rare components (e.g., circuits, pristine wires) when salvaging technological junk.
    *   *Connects to: Tool Use and Reverse Engineer*

*   **Tool Use**
    *   **Proficiency Req:** 20
    *   **Effect:** You can now craft specialized toolkits (e.g., Electronics Toolkit, Mechanics Wrench) that are required for interacting with and repairing advanced technology.
    *   *Connects to: The Scrapper and The Engineer branches*

---
### **The Scrapper Branch (Salvaging & Modifying)**

*   **Reverse Engineer**
    *   **Proficiency Req:** 30 (Salvaging)
    *   **Effect:** Unlocks the "Analysis" function at a workbench. Allows you to break down Subroutine Fragments you don't need to learn a small, permanent, stackable stat bonus (e.g., break down a Marksman.chip to get a permanent +0.1% projectile speed).
    *   *Connects to: Overclocker*

*   **Overclocker**
    *   **Proficiency Req:** 50 (Modifying)
    *   **Effect:** At a Neuro-Interface Workbench, you can attempt to "overclock" an equipped Subroutine Fragment. This increases its positive effect by 50% but also doubles its negative effect, allowing for high-risk, high-reward builds.
    *   *Connects to: Master Scrapper*

*   **Master Scrapper (Ultimate Salvage Skill)**
    *   **Proficiency Req:** 90 (Salvaging)
    *   **Effect:** You have a small chance to find fully intact, functional Subroutine Fragments when salvaging any piece of high-tier technological wreckage.

---
### **The Engineer Branch (Mechanics & Vehicles)**

*   **Mechanic**
    *   **Proficiency Req:** 30 (Mechanics)
    *   **Effect:** You now have the basic knowledge to repair simple machinery. This is the prerequisite for repairing a derelict vehicle engine.
    *   *Connects to: Mad Driver*

*   **Mad Driver**
    *   **Proficiency Req:** 60 (Vehicles)
    *   **Effect:** All vehicles you drive have improved handling and a higher top speed. You take less damage from impacts while inside a vehicle.
    *   *Connects to: Reinforced Plating*

*   **Reinforced Plating (Ultimate Vehicle Skill)**
    *   **Proficiency Req:** 90 (Vehicles)
    *   **Effect:** At a workbench, you can apply makeshift armor plating to any owned vehicle, significantly increasing its health and damage resistance at the cost of speed and handling.

---
### **The Saboteur Branch (Hacking & Robotics)**

*   **System Exploit**
    *   **Proficiency Req:** 40 (Hacking)
    *   **Effect:** Unlocks the ability to attempt to hack simple robotic enemies (like security drones). A successful hack will temporarily disable them.
    *   *Connects to: Master Hacker*

*   **Master Hacker**
    *   **Proficiency Req:** 70 (Hacking)
    *   **Effect:** Your hacking skill is improved. You can now attempt to turn hacked robotic enemies to your side, making them fight for you for a short period before self-destructing.
    *   *Connects to: Drone Expert*

*   **Drone Expert (Ultimate Robotics Skill)**
    *   **Proficiency Req:** 90 (Robotics)
    *   **Effect:** Unlocks the ability to craft a single, small "Scout Drone" companion at a workbench. The drone cannot attack but can be controlled remotely to scout areas, mark enemies, and access remote terminals.

---
### **The Tech Capstone Perk**

*   **Jury-Rig**
    *   **Proficiency Req:** 100
    *   **Effect:** Your mastery of improvisation is legendary. Once per day, you can perform a "field repair" on any broken piece of equipment (weapon, armor, or vehicle) without a workbench. This instantly restores it to 50% durability, allowing you to get back in the fight in an emergency.
    *   **Location:** This is the "CPU" at the very center of the circuit board, the ultimate skill for a master of technology.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/09_Shadow.md`
```md
# Skill Tree: The Shadow

## **1.0. Constellation Overview**

*   **Discipline:** Stealth, Evasion, & Subterfuge.
*   **Description:** The Shadow constellation governs the arts of the unseen. Its perks allow a player to move like a ghost through a hostile world, striking from the darkness with lethal precision or slipping past danger without a trace. It is the tree of choice for rogues, assassins, and scouts who know that a battle avoided is a battle won.

## **2.0. Visual Layout**

The constellation is shaped like a hooded figure or a stylized phantom. The foundational perks are in the "hood" at the top. From there, it branches down into three distinct paths: **The Infiltrator** (focused on bypassing obstacles), **The Night-Stalker** (focused on pure stealth and evasion), and **The Cutthroat** (focused on dealing damage from stealth).

## **3.0. Perk List**

---
### **The Hood (Core Stealth Skills)**

*   **Stealth (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Each rank makes you 5% harder to detect while sneaking.
    *   *Connects to: Silent Running, Locksmithing, and Hidden Blade*

*   **Silent Running**
    *   **Proficiency Req:** 20
    *   **Effect:** Moving while sneaking no longer incurs an additional detection penalty.
    *   *Connects to: The Night-Stalker branch*

---
### **The Infiltrator Branch (Bypassing Obstacles)**

*   **Locksmithing (4 Ranks - Novice, Apprentice, Adept, Master)**
    *   **Proficiency Req:** 0 / 25 / 50 / 75 (Thievery)
    *   **Effect:** Allows you to attempt to pick locks of increasing difficulty. Higher ranks make the lock-picking mini-game easier.
    *   *Connects to: Light Foot*

*   **Light Foot**
    *   **Proficiency Req:** 40 (Thievery)
    *   **Effect:** You are light on your feet. You will no longer trigger floor-based traps like pressure plates and tripwires.
    *   *Connects to: Treasure Hunter*

*   **Treasure Hunter**
    *   **Proficiency Req:** 90 (Thievery)
    *   **Effect:** Your keen eye for valuables grants you a significantly higher chance of finding rare and special items in all locked chests.

---
### **The Night-Stalker Branch (Mastery of Stealth)**

This branch splits off from Silent Running.

*   **Dodge Roll**
    *   **Proficiency Req:** 30 (Evasion)
    *   **Effect:** Tapping the sprint key while sneaking will now perform a silent forward roll, allowing you to move quickly from cover to cover without creating noise.
    *   *Connects to: Muffled Movement*

*   **Muffled Movement**
    *   **Proficiency Req:** 50 (Stealth)
    *   **Effect:** The noise generated by the armor you wear is reduced by 50%.
    *   *Connects to: Shadow Warrior*

*   **Shadow Warrior (Ultimate Stealth Skill)**
    *   **Proficiency Req:** 90 (Stealth)
    *   **Effect:** If you are detected in combat, crouching will briefly cause enemies to lose track of you, forcing them to search for your position again. Has a cooldown.

---
### **The Cutthroat Branch (Stealthy Violence)**

*   **Hidden Blade**
    *   **Proficiency Req:** 30 (Stealth)
    *   **Effect:** Your sneak attacks with one-handed weapons now deal 3x normal damage.
    *   *Connects to: Backstab*

*   **Backstab**
    *   **Proficiency Req:** 60 (Stealth)
    *   **Effect:** Further increases the damage of sneak attacks with one-handed weapons to a massive 6x normal damage.
    *   *Connects to: Assassin's Blade*

*   **Assassin's Blade (Ultimate Assassination Skill)**
    *   **Proficiency Req:** 90 (Stealth)
    *   **Effect:** Sneak attacks with daggers (a sub-class of one-handed weapons) ignore enemy armor and have a chance to instantly kill non-boss targets if their health is below a certain threshold.

---
### **The Shadow Capstone Perk**

*   **Smoke and Shadow**
    *   **Proficiency Req:** 100
    *   **Effect:** Once per day, when your health drops below 25%, you automatically vanish in a puff of smoke, becoming invisible for 5 seconds and leaving behind a decoy. This allows you a single, free chance to escape a deadly situation.
    *   **Location:** This is the final star at the bottom point of the phantom's cloak, the ultimate survival tool for a master of the unseen.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/08_The_Wilds.md`
```md
# Skill Tree: The Wilds

## **1.0. Constellation Overview**

*   **Discipline:** Survivalism, Tracking, & Animal Taming.
*   **Description:** The Wilds constellation governs the art of living in harmony with—and asserting dominance over—the untamed world. Its perks allow a player to track prey, endure harsh environments, gather resources more effectively, and tame the very beasts that threaten lesser survivors, turning them into loyal companions.

## **2.0. Visual Layout**

The constellation is shaped like a sprawling predator's footprint. The "heel" of the print contains the core survivalist perks. The path then splits into three distinct "toes": **The Tracker** (hunting and exploration), **The Survivor** (environmental resistance), and **The Beastmaster** (animal companionship).

## **3.0. Perk List**

---
### **The Heel Pad (Core Survivalist Skills)**

*   **Naturalist (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Each rank increases the amount of materials gained from harvesting plants and animal carcasses by 5%.
    *   *Connects to: Wastelander, Keen Senses, and Animal Ken*

*   **Wastelander**
    *   **Proficiency Req:** 20
    *   **Effect:** Reduces the negative effects of hunger and thirst, allowing you to go longer without needing to eat or drink. Food you cook provides longer-lasting buffs.
    *   *Connects to: The Survivor branch*

---
### **The Tracker Branch (Hunting & Exploration)**

*   **Keen Senses**
    *   **Proficiency Req:** 30 (Exploration)
    *   **Effect:** Un-harvested plants and fungi within a short range will be highlighted on your compass.
    *   *Connects to: Tracker*

*   **Tracker**
    *   **Proficiency Req:** 50 (Hunting)
    *   **Effect:** Animals and beasts now leave behind glowing tracks. Analyzing the tracks can reveal the creature's type, numbers, and direction of travel.
    *   *Connects to: Perfect Specimen*

*   **Perfect Specimen**
    *   **Proficiency Req:** 90 (Hunting)
    *   **Effect:** You now have a higher chance of harvesting rare and valuable components (e.g., "Pristine Hide," "Alpha Heart") from animal and beast carcasses.

---
### **The Survivor Branch (Environmental Resistance)**

This branch splits off from Wastelander.

*   **Elemental Resilience**
    *   **Proficiency Req:** 40 (Survival)
    *   **Effect:** Your natural resilience is honed. You gain a +25% resistance to the environmental effects of both Cold and Heat.
    *   *Connects to: Blight Ward*

*   **Blight Ward**
    *   **Proficiency Req:** 70 (Survival)
    *   **Effect:** You have learned to understand the nature of the corruption. You gain a +50% resistance to the passive health drain effect of "Corruption" while in a Blighted zone.

---
### **The Beastmaster Branch (Animal Taming)**

*   **Animal Ken**
    *   **Proficiency Req:** 30 (Taming)
    *   **Effect:** You can now attempt to tame smaller, non-hostile animals (like a wolf or a large bird). Your chance of success is based on the creature's level. You can only have one animal companion at a time.
    *   *Connects to: Pack Leader*

*   **Pack Leader**
    *   **Proficiency Req:** 60 (Taming)
    *   **Effect:** Your tamed animal companion gains increased health and damage, and will now assist you in combat more effectively. Unlocks the ability to issue basic commands (Attack, Stay, Follow).
    *   *Connects to: Apex Predator*

*   **Apex Predator (Ultimate Taming Skill)**
    *   **Proficiency Req:** 90 (Taming)
    *   **Effect:** You have become a master of the wild. You can now attempt to tame larger and more aggressive creatures, such as bears, great cats, and other powerful beasts.

---
### **The Wilds Capstone Perk**

*   **One of the Pack**
    *   **Proficiency Req:** 100 (in any Wilds discipline)
    *   **Effect:** Your bond with the wild is complete. You and your animal companion now share a "Pack Link." When you are close to each other, you both gain a 10% bonus to damage and damage resistance.
    *   **Location:** This is the final star at the very tip of the footprint, the mark of a true master of the wild.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/07_Architect.md`
```md
# Skill Tree: The Architect

## **1.0. Constellation Overview**

*   **Discipline:** Base Building, Fortification, & Engineering.
*   **Description:** The Architect constellation governs the art of construction and creating a safe, efficient home in the wilderness. Perks in this tree allow the player to unlock stronger building materials, create advanced crafting stations, and design formidable defensive structures, turning a simple camp into a sprawling, defensible fortress.

## **2.0. Visual Layout**

The constellation is shaped like a fortress blueprint or a fortified wall with towers. The foundational skills are at the bottom, representing the ground floor. The path then splits into two main branches: **The Stonemason**, focused on defensive integrity and materials, and **The Homesteader**, focused on internal functionality and quality of life.

## **3.0. Perk List**

---
### **The Foundation (Core Building Skills)**

*   **Journeyman Carpenter (3 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Unlocks basic wooden structures. Each rank reduces the wood cost of all wooden building pieces by 5%.
    *   *Connects to: Stonemasonry and Homestead*

*   **Salvage Operations**
    *   **Proficiency Req:** 20
    *   **Effect:** When deconstructing environmental objects (e.g., ruined cars, scrap piles, derelict furniture), you gain 30% more basic resources like scrap metal and components.
    *   *Connects to: Defensive Engineering*

---
### **The Stonemason Branch (Defensive Structures)**

*   **Stonemasonry**
    *   **Proficiency Req:** 30
    *   **Effect:** You have learned to work with stone. Unlocks the ability to craft stone building pieces, which are significantly more durable than wood.
    *   *Connects to: Reinforced Structures*

*   **Reinforced Structures**
    *   **Proficiency Req:** 50
    *   **Effect:** You now incorporate metal and advanced techniques into your building. All crafted structures (walls, foundations, etc.) have 25% more health.
    *   *Connects to: Defensive Engineering*

*   **Defensive Engineering (Ultimate Defense Skill)**
    *   **Proficiency Req:** 90
    *   **Effect:** Unlocks crafting recipes for advanced base defenses, including **Spike Traps**, **Automated Catapults**, and (with Tech skill) **Automated Machinegun Turrets**.

---
### **The Homesteader Branch (Internal Functionality)**

*   **Homestead**
    *   **Proficiency Req:** 30
    *   **Effect:** The "Well-Rested" bonus you gain from sleeping in a bed you own is 25% more effective and lasts 50% longer.
    *   *Connects to: Workshop Master*

*   **Workshop Master**
    *   **Proficiency Req:** 50
    *   **Effect:** All crafting stations placed within your base (Forge, Alchemy Lab, etc.) operate 15% faster. Unlocks advanced versions of these stations.
    *   *Connects to: A Fertile Land*

*   **A Fertile Land (Ultimate Utility Skill)**
    *   **Proficiency Req:** 90
    *   **Effect:** Unlocks the ability to craft advanced farming plots and animal pens. All crops grown in your farm plots have a chance to yield double the harvest, and tamed beasts housed in your pens will slowly generate resources (e.g., wool, eggs).

---
### **The Architect Capstone Perk**

*   **Heart of the Home**
    *   **Proficiency Req:** 100
    *   **Effect:** Your mastery of architecture is legendary. You can now build a single, unique "Hearthstone" object at the center of your base. Any player (including allies) standing within a large radius of the Hearthstone will gain slow Health and Stamina regeneration. Additionally, all player-built structures within this radius will slowly repair themselves over time after being damaged.
    *   **Location:** This is the "keep" or "citadel" at the very top of the constellation, representing the ultimate fusion of defense and comfort.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/06_Alchemy.md`
```md
# Skill Tree: The Alchemy

## **1.0. Constellation Overview**

*   **Discipline:** Potions, Poisons, & Tinctures.
*   **Description:** The Alchemy constellation governs the art of brewing. From life-saving healing draughts to debilitating poisons and volatile explosives, a master alchemist can control the battlefield and support their allies without swinging a sword or casting a spell. This tree rewards meticulous harvesting and experimentation.

## **2.0. Visual Layout**

The constellation is shaped like a bubbling retort flask connected to a condenser coil. The foundational perks are in the "flask" at the bottom. The skills then rise up through the "neck" and split into three distinct branches in the "coil": **The Physician** (healing and buffs), **The Assassin** (poisons and debuffs), and **The Saboteur** (explosives and environmental control).

## **3.0. Perk List**

---
### **The Retort Flask (Core Alchemical Skills)**

*   **Alchemist (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Each rank increases the potency and duration of all created potions and poisons by 5%.
    *   *Connects to: Field Medic and Experimenter*

*   **Field Medic**
    *   **Proficiency Req:** 20
    *   **Effect:** You can now see the primary effect of any alchemical ingredient by simply tasting it once. (This consumes the ingredient).
    *   *Connects to: The Physician and The Assassin branches*

---
### **The Physician Branch (Healing & Buffs)**

*   **Experimenter**
    *   **Proficiency Req:** 30
    *   **Effect:** When creating a potion, you have a chance to discover a random, secondary positive effect from the ingredients used.
    *   *Connects to: Benefactor and Purity*

*   **Benefactor**
    *   **Proficiency Req:** 50
    *   **Effect:** Potions you drink that have a beneficial effect (e.g., Fortify Health, Restore Stamina) are 25% more powerful.
    *   *Connects to: Purity*

*   **Purity (Ultimate Healing Skill)**
    *   **Proficiency Req:** 90
    *   **Effect:** All negative effects are removed from your crafted beneficial potions. For example, a "Fortify Strength" potion that also had a minor "Drain Speed" effect will now only fortify strength.

---
### **The Assassin Branch (Poisons & Debuffs)**

*   **Poisoner**
    *   **Proficiency Req:** 30
    *   **Effect:** Unlocks the ability to apply crafted poisons to your weapons at a workbench. Each weapon can have a limited number of poisoned strikes.
    *   *Connects to: Concentrated Poison and Catalyst*

*   **Concentrated Poison**
    *   **Proficiency Req:** 50
    *   **Effect:** Poisons applied to weapons now last for twice as many hits.
    *   *Connects to: Catalyst*

*   **Catalyst (Ultimate Poison Skill)**
    *   **Proficiency Req:** 90
    *   **Effect:** All poisons are now 50% more effective on targets who are already suffering from another poison effect. This rewards stacking different types of poisons on a single target.

---
### **The Saboteur Branch (Explosives & Utility)**

This branch splits off from the main trunk separately.

*   **Demolitionist**
    *   **Proficiency Req:** 40
    *   **Effect:** Unlocks crafting recipes for basic explosives, like the **"Makeshift Grenade"** and **"Sticky Bomb."** You can throw them further and with more accuracy.
    *   *Connects to: Volatility*

*   **Volatility**
    *   **Proficiency Req:** 70
    *   **Effect:** Your crafted explosives now have a larger blast radius and have a chance to inflict a secondary elemental effect (e.g., Fire, Frost) based on the ingredients used to craft them.

---
### **The Alchemy Capstone Perk**

*   **Snakeblood**
    *   **Proficiency Req:** 100
    *   **Effect:** Your body has become accustomed to the potent reagents you handle. You gain 50% resistance to all poisons, and you can identify all effects of an ingredient simply by harvesting it, without needing to consume it first.
    *   **Location:** This is the final star where the "condensation" drips out of the coil, the mark of a true master alchemist.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/05_Smithing.md`
```md
# Skill Tree: The Smithing

## **1.0. Constellation Overview**

*   **Discipline:** Metallurgy, Forging, & Improvement.
*   **Description:** The Smithing constellation governs the art of creating and enhancing metal weapons and armor. A player who masters Smithing is an indispensable member of any team, able to outfit themselves and their allies with gear far superior to anything that can be commonly found. The tree is structured to reflect a smith's journey from working with simple metals to mastering exotic and even magical materials.

## **2.0. Visual Layout**

The constellation is shaped like a branching anvil. The central base of the anvil holds the foundational improvement perks. The main "body" of the anvil is a central progression path of material mastery. From this central path, side branches extend outwards, representing specialized techniques like arcane enchanting and armor-specific mastery.

## **3.0. Perk List**

---
### **The Anvil's Base (Core Improvement Skills)**

*   **Journeyman Smith (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Each rank increases the effectiveness of improving weapons and armor at a workbench (grindstone or armor bench) by 5%.
    *   *Connects to: Basic Smithing*

*   **Salvage Specialist**
    *   **Proficiency Req:** 20
    *   **Effect:** When you break down metal armor and weapons at a smelter or workbench, you recover 50% more of their base materials.
    *   *Connects to: Advanced Smithing*

---
### **The Central Progression (Material Mastery)**

This is the main "trunk" of the tree that a smith must climb to work with better materials.

*   **Basic Smithing**
    *   **Proficiency Req:** 0
    *   **Effect:** You can now craft items from basic materials like **Iron** and **Leather**.
    *   *Connects to: Advanced Smithing*

*   **Advanced Smithing**
    *   **Proficiency Req:** 30
    *   **Effect:** You can now craft items from **Steel** and similar mid-tier metals. Allows for more complex designs.
    *   *Connects to: Expert Smithing and the Specialization branches*

*   **Expert Smithing**
    *   **Proficiency Req:** 60
    *   **Effect:** You have learned to work with difficult, high-grade metals like **Titanium** and **Obsidian**.
    *   *Connects to: Master Smithing*

*   **Master Smithing**
    *   **Proficiency Req:** 90
    *   **Effect:** You have unlocked the secrets of legendary forging. You can now work with the rarest materials in the world, such as **Blight-Hardened Steel** or **Dragonbone**.
    *   *Connects to: Legend of the Forge*

---
### **Specialization Branches (Techniques)**

These perks branch off from the main progression path, allowing for specialization.

*   **Arcane Blacksmith (Branching from Advanced Smithing)**
    *   **Proficiency Req:** 50
    *   **Effect:** Unlocks the ability to use an **Arcane Enchanter**. You can disenchant magical gear to learn its enchantment, then apply that enchantment to non-magical gear using a filled Soul Gem. This is the crucial bridge to magic item creation.

*   **Dwarven Smithing (Branching from Advanced Smithing)**
    *   **Proficiency Req:** 40, must also have learned the technique from the Hearth-Forged Dwarves.
    *   **Effect:** You have learned the secrets of Dwarven metallurgy. You can now craft equipment in the robust and ornate Dwarven style. Dwarven gear has inherently higher armor ratings and durability.

*   **Elven Smithing (Branching from Advanced Smithing)**
    *   **Proficiency Req:** 40, must also have learned the technique from the Sylvan Elves.
    *   **Effect:** You have learned the art of Elven smithing. You can now craft equipment in the lightweight and elegant Elven style. Elven gear is much lighter than its counterparts and often has small, innate magical resistances.

*   **Goldsmith/Jeweler (Branching from Expert Smithing)**
    *   **Proficiency Req:** 70
    *   **Effect:** You can now craft powerful magical rings, amulets, and circlets from gold, silver, and precious gems at a jeweler's toolkit.

---
### **The Smithing Capstone Perk**

*   **Legend of the Forge**
    *   **Proficiency Req:** 100
    *   **Effect:** Your mastery is absolute. When you improve any weapon or armor at a workbench, you can improve it one additional level beyond what would normally be possible, resulting in unparalleled quality.
    *   **Location:** This is the final, brilliant star at the "horn" of the anvil, the ultimate mark of a master artisan.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/04_The_Marksman.md`
```md
# Skill Tree: The Marksman

## **1.0. Constellation Overview**

*   **Discipline:** Archery & Ranged Weaponry.
*   **Description:** The Marksman constellation governs the art of dealing death from a distance. Its skills enhance the player's proficiency with bows, crossbows, and firearms, rewarding careful aim, quick reflexes, and tactical exploitation of the battlefield. It supports playstyles from the stealthy sniper to the agile skirmisher.

## **2.0. Visual Layout**

The constellation is shaped like a bow that has just released an arrow. The "grip" of the bow contains the foundational perks. The layout then splits into two major branches: the top limb is the **Way of the Archer**, focusing on the art of traditional bows, while the bottom limb is the **Way of the Gunslinger**, dedicated to salvaged firearms and advanced tech. The "arrow" itself is a central line of perks benefiting both styles.

## **3.0. Perk List**

---
### **The Central Trunk (Core Ranged Skills)**

*   **Overdraw (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Each rank increases the damage of all ranged weapons (Bows, Crossbows, Firearms) by 5%.
    *   *Connects to: Eagle Eye, Quick Hands, and Steady Aim*

*   **Steady Aim**
    *   **Proficiency Req:** 20
    *   **Effect:** Pressing a dedicated key while aiming down sights will hold your breath, consuming stamina to temporarily steady your aim and slow down time by 25%.
    *   *Connects to: The Way of the Archer and The Way of the Gunslinger branches*

---
### **The Way of the Archer Branch (Top Limb - Bows & Crossbows)**

*   **Eagle Eye**
    *   **Proficiency Req:** 30 (Bows/Crossbows)
    *   **Effect:** You can zoom in further while aiming a bow or crossbow.
    *   *Connects to: Hunter's Discipline and Power Shot*

*   **Hunter's Discipline**
    *   **Proficiency Req:** 50 (Bows/Crossbows)
    *   **Effect:** You can hold a fully drawn bow or loaded crossbow steady for a longer period of time without losing accuracy.
    *   *Connects to: Crippling Shot*

*   **Power Shot**
    *   **Proficiency Req:** 50 (Bows/Crossbows)
    *   **Effect:** A fully-drawn arrow or a crossbow bolt has a 50% chance to stagger an enemy.
    *   *Connects to: Crippling Shot*

*   **Crippling Shot**
    *   **Proficiency Req:** 70 (Bows/Crossbows)
    *   **Effect:** Aiming for an enemy's leg has a chance to cripple them, dramatically slowing their movement speed.
    *   *Connects to: Arrow Storm*

*   **Arrow Storm (Ultimate Archery Skill)**
    *   **Proficiency Req:** 90 (Bows/Crossbows)
    *   **Effect:** You can nock up to three arrows to your bow. Firing releases them in a tight horizontal spread. This allows a crossbow user to fire two bolts before needing to reload.

---
### **The Way of the Gunslinger Branch (Bottom Limb - Firearms)**

*   **Quick Hands**
    *   **Proficiency Req:** 30 (Firearms)
    *   **Effect:** Reloading all firearms is 20% faster.
    *   *Connects to: Deadeye and Gunsmith*

*   **Deadeye**
    *   **Proficiency Req:** 50 (Firearms)
    *   **Effect:** Your accuracy and critical hit chance with firearms are significantly increased for the first shot fired after entering "sneak" mode.
    *   *Connects to: Penetrating Shot*

*   **Gunsmith**
    *   **Proficiency Req:** 50 (Firearms)
    *   **Effect:** You can now craft basic ammunition (e.g., Lead Ball, Simple Shells) at a workbench and install simple modifications (like improved sights) onto firearms.
    *   *Connects to: Penetrating Shot*

*   **Penetrating Shot**
    *   **Proficiency Req:** 70 (Firearms)
    *   **Effect:** Shots from firearms have a chance to ignore a portion of the target's armor and can potentially over-penetrate, hitting a second enemy standing directly behind the first.
    *   *Connects to: Ricochet*

*   **Ricochet (Ultimate Firearms Skill)**
    *   **Proficiency Req:** 90 (Firearms)
    *   **Effect:** Missed shots from firearms that hit a hard surface (rock, metal) have a chance to ricochet and hit a nearby enemy. The ricochet does reduced damage but has a high chance to stagger.

---
### **The Marksman Capstone Perk**

*   **One Shot, One Kill**
    *   **Proficiency Req:** 100 (in either Archery or Firearms)
    *   **Effect:** A successful critical hit with any ranged weapon on an enemy at full health deals massive bonus damage and has a high chance to be an instant kill on non-boss, non-giant creatures.
    *   **Location:** This is the "arrowhead" at the very tip of the constellation's central line, the ultimate reward for a master of ranged combat.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/03_The_Guardian.md`
```md
# Skill Tree: The Guardian

## **1.0. Constellation Overview**

*   **Discipline:** Blocking, Heavy Armor, & Resilience.
*   **Description:** The Guardian is the art of defense. Where The Warrior focuses on ending fights, The Guardian focuses on enduring them. Its perks enhance the effectiveness of shields, the damage resistance of heavy armor, and the player's fundamental ability to withstand punishment, making them a bulwark for their allies and a nightmare for their foes.

## **2.0. Visual Layout**

The constellation is shaped like a massive, ornate shield. The central "boss" of the shield holds the core defensive perks. The layout then branches into two main sections: **The Shield Wall** on one side, dedicated to blocking, and **The Iron Hide** on the other, dedicated to the mastery of wearing armor.

## **3.0. Perk List**

---
### **The Central Trunk (Core Resilience)**

*   **Vitality (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Each rank increases your maximum Health by a flat amount (e.g., +20 HP per rank).
    *   *Connects to: Iron Will and Deflection*

*   **Iron Will**
    *   **Proficiency Req:** 20 (any Armor type)
    *   **Effect:** You are 50% less likely to be staggered by enemy attacks while you are above 80% health.
    *   *Connects to: The Shield Wall and The Iron Hide branches*

---
### **The Shield Wall Branch (Shield Mastery)**

*   **Deflection (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** Increases the amount of damage your shield can block by 5% per rank.
    *   *Connects to: Shield Bash*

*   **Shield Bash**
    *   **Proficiency Req:** 30 (Blocking)
    *   **Effect:** Pressing the attack button while blocking performs a fast shield bash that costs stamina, deals minor damage, and can stagger an attacking enemy.
    *   *Connects to: Elemental Ward and Disarming Bash*

*   **Elemental Ward**
    *   **Proficiency Req:** 50 (Blocking)
    *   **Effect:** Blocking with a shield now absorbs 50% of incoming magical damage from Fire, Frost, and Shock spells.
    *   *Connects to: Immovable*

*   **Disarming Bash**
    *   **Proficiency Req:** 70 (Blocking)
    *   **Effect:** Power-bashing (holding the attack button while blocking) has a chance to disarm your opponent, forcing them to drop their weapon.
    *   *Connects to: Immovable*

*   **Immovable (Ultimate Shield Skill)**
    *   **Proficiency Req:** 90 (Blocking)
    *   **Effect:** While blocking with a shield, you cannot be staggered or knocked down by any attack, no matter how powerful. Consumes a large amount of stamina.

---
### **The Iron Hide Branch (Armor Mastery)**

*   **Juggernaut**
    *   **Proficiency Req:** 30 (Heavy Armor)
    *   **Effect:** Your equipped heavy armor no longer slows you down.
    *   *Connects to: Conditioning*

*   **Conditioning**
    *   **Proficiency Req:** 50 (Heavy Armor)
    *   **Effect:** The total weight of your equipped heavy armor is halved for the purposes of calculating your encumbrance.
    *   *Connects to: Well-Fitted and Tower of Strength*

*   **Well-Fitted**
    *   **Proficiency Req:** 70 (Heavy Armor)
    *   **Effect:** Gain a 10% bonus to your total armor rating if you are wearing a matched set of heavy armor (all pieces are Dwarven, all are Iron, etc.).
    *   *Connects to: Tower of Strength*

*   **Tower of Strength**
    *   **Proficiency Req:** 70 (any Armor type)
    *   **Effect:** Your total armor rating is increased by a further 10% as long as you are not using a shield (encourages a two-handed tank build).
    *   *Connects to: Indomitable*

*   **Indomitable (Ultimate Armor Skill)**
    *   **Proficiency Req:** 90 (Heavy Armor)
    *   **Effect:** Incoming power attacks from enemies have a chance to be completely negated, dealing zero damage. The chance is based on your total armor rating.

---
### **The Guardian Capstone Perk**

*   **Last Stand**
    *   **Proficiency Req:** 100 (in either Blocking or Heavy Armor)
    *   **Effect:** Once per day, when your health drops below 20% in combat, you gain a massive surge of adrenaline. For 8 seconds, you take 50% less damage and all your attacks deal 25% more damage.
    *   **Location:** This is the final star at the very top of the shield-shaped constellation, the ultimate survival tool for a master of defense.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/02_The_Warrior.md`
```md
# Skill Tree: The Warrior

## **1.0. Constellation Overview**

*   **Discipline:** Melee Weaponry & Armor.
*   **Description:** The Warrior constellation is the heart of all close-quarters physical combat. Its perks enhance the damage, speed, and special effects of swords, axes, and maces, allowing a player to specialize as a lightning-fast duelist, a staggering brute, or a master of a specific weapon type.

## **2.0. Visual Layout**

The constellation begins with a central "trunk" of foundational skills. It then splits into two major branches: a **"One-Handed"** branch on the left and a **"Two-Handed"** branch on the right. Each of these main branches has three smaller sub-branches for its specific weapon types (Sword, Axe, Mace).

## **3.0. Perk List**

---
### **The Central Trunk (Core Melee Skills)**

*   **Brutality (5 Ranks)**
    *   **Proficiency Req:** 0
    *   **Effect:** The foundational skill. Each rank increases all melee damage by 5%.
    *   *Connects to: Furious Strike*

*   **Furious Strike**
    *   **Proficiency Req:** 20
    *   **Effect:** All power attacks now consume 25% less stamina.
    *   *Connects to: Duelist's Stance and Heavy Hitter*

---
### **The One-Handed Branch (Left Side)**

*   **Duelist's Stance**
    *   **Proficiency Req:** 30 (One-Handed)
    *   **Effect:** Your attack speed with all one-handed weapons is increased by 10%.
    *   *Connects to: Bladework, Hack and Slash, Bonebreaker*

*   **Bladework (Sword Specialization)**
    *   **Proficiency Req:** 50 (One-Handed)
    *   **Effect:** Your critical hit chance with one-handed swords is doubled.
    *   *Connects to: Flurry of Blows*

*   **Hack and Slash (Axe Specialization)**
    *   **Proficiency Req:** 50 (One-Handed)
    *   **Effect:** Attacks with one-handed axes have a chance to inflict a "Bleed," causing damage over time.
    *   *Connects to: Flurry of Blows*

*   **Bonebreaker (Mace Specialization)**
    *   **Proficiency Req:** 50 (One-Handed)
    *   **Effect:** Attacks with one-handed maces ignore 25% of the target's armor.
    *   *Connects to: Flurry of Blows*

*   **Flurry of Blows (Ultimate One-Handed Skill)**
    *   **Proficiency Req:** 90 (One-Handed)
    *   **Effect:** Unlocks a new power attack for one-handed weapons. Hold the attack button to unleash a rapid, three-hit combo that costs significantly more stamina but deals high damage.

---
### **The Two-Handed Branch (Right Side)**

*   **Heavy Hitter**
    *   **Proficiency Req:** 30 (Two-Handed)
    *   **Effect:** Attacks with all two-handed weapons have a much higher chance to stagger enemies.
    *   *Connects to: Cleave, Executioner, Sunder*

*   **Cleave (Greatsword Specialization)**
    *   **Proficiency Req:** 50 (Two-Handed)
    *   **Effect:** Your sweeping power attacks with greatswords can now hit all enemies in front of you.
    *   *Connects to: Overwhelming Might*

*   **Executioner (Greataxe Specialization)**
    *   **Proficiency Req:** 50 (Two-Handed)
    *   **Effect:** Power attacks with greataxes deal an additional 25% damage to enemies below 50% health.
    *   *Connects to: Overwhelming Might*

*   **Sunder (Warhammer Specialization)**
    *   **Proficiency Req:** 50 (Two-Handed)
    *   **Effect:** Attacks with warhammers ignore 50% of the target's armor.
    *   *Connects to: Overwhelming Might*

*   **Overwhelming Might (Ultimate Two-Handed Skill)**
    *   **Proficiency Req:** 90 (Two-Handed)
    *   **Effect:** A sprinting power attack with a two-handed weapon is now a devastating charge that will knock down most man-sized enemies and critically stagger larger ones.

---
### **The Warrior Capstone Perk**

*   **Unrelenting**
    *   **Proficiency Req:** 100 (in either One-Handed or Two-Handed)
    *   **Effect:** Killing an enemy with any melee weapon provides a massive burst of adrenaline, restoring 20% of your max Health and Stamina over 2 seconds. Cannot trigger more than once every 10 seconds.
    *   **Location:** This is the final star at the very top of the constellation, connecting both the one-handed and two-handed branches. It is the mark of a true master warrior.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/03_CORE_GAMEPLAY_SYSTEMS/01_PLAYER_SYSTEMS/03_Skill_Trees/01_Skill_Tree_Overview.md`
```md
# Skill Trees: The Constellation of Mastery

## **1.0. Core Philosophy: Forge Your Own Path**

The skill system in *Where Giants Rust* is a free-form "constellation" system designed for maximum player agency. There are no fixed classes. The player invests **Skill Points**, earned upon leveling up, into twelve distinct **Constellations**, each representing a unique discipline. This system allows for deep specialization and creative hybrid builds, with a player's path being guided by their actions via the **Proficiency** "learn-by-doing" system.

## **2.0. The Twelve Constellations**

The skills are grouped into three primary schools: Combat, Creation, and Cunning.

---
### **School of Combat: The Arts of War**

*   **1. The Warrior (One-Handed & Two-Handed Weapons)**
    *   **Core Identity:** The primary tree for all forms of melee combat. Governs the raw power, speed, and special maneuvers of swords, axes, and maces.
    *   **Focus:** Direct damage, staggering enemies, power attacks, and weapon-specific specializations.
    *   **Synergizes with:** Guardian (for defense), Smithing (for better weapons).

*   **2. The Guardian (Blocking & Heavy Armor)**
    *   **Core Identity:** The art of defense and survival in the thick of a fight. Focuses on turning the player into an unshakeable bastion.
    *   **Focus:** Shield effectiveness, mitigating damage, wearing heavy armor without penalty, and resisting staggers and knockdowns.
    *   **Synergizes with:** Warrior (for a classic "tank" build), Smithing (for masterwork armor).

*   **3. The Marksman (Bows & Firearms)**
    *   **Core Identity:** The discipline of ranged physical combat. Covers everything from primitive bows to salvaged high-tech rifles.
    *   **Focus:** Aiming, critical hits on weak points, stealth attacks, specialized ammunition, and tactical positioning.
    *   **Synergizes with:** Shadow (for a "sniper" build), Smithing/Tech (for advanced ranged weapons).

---
### **School of Creation: The Arts of the Hand**

*   **4. Smithing (Metallurgy & Forging)**
    *   **Core Identity:** The mastery of metal. This tree is essential for crafting and improving all high-tier metal weapons and heavy armor.
    *   **Focus:** Unlocking material tiers (Iron, Steel, Dwarven), improving gear at workbenches, and learning unique smithing techniques from different cultures.
    *   **Synergizes with:** Almost every combat tree, as it provides the gear they need to excel.

*   **5. Alchemy (Potions, Poisons & Chemistry)**
    *   **Core Identity:** The art of brewing potent concoctions from the world's flora, fauna, and minerals.
    *   **Focus:** Crafting healing potions, powerful personal enhancement elixirs, debilitating poisons to apply to weapons, and volatile explosives.
    *   **Synergizes with:** Wilds (for gathering rare ingredients), Shadow (for poison-based assassinations).

*   **6. Architect (Base Building & Fortification)**
    *   **Core Identity:** The discipline of creating a safe and efficient home in a hostile world.
    *   **Focus:** Unlocking new building components (wood, stone, metal), advanced crafting stations, automated defenses, and structures that provide passive buffs to the player.
    *   **Synergizes with:** Tech (for advanced defenses), Wilds (for farming and husbandry).

---
### **School of Cunning: The Arts of the Mind**

*   **7. Wilds (Survivalism & Taming)**
    *   **Core Identity:** The mastery of the natural world. This tree is for the hunter, the tracker, and the beastmaster.
    *   **Focus:** Tracking enemies, resisting environmental hazards, increasing yields from gathering, and taming wild beasts to fight alongside the player.
    *   **Synergizes with:** Alchemy (provides ingredients), Marksman (for a classic "hunter" build).

*   **8. Shadow (Stealth & Subterfuge)**
    *   **Core Identity:** The art of the unseen. For players who prefer to avoid direct confrontation or end it before the enemy knows they are there.
    *   **Focus:** Moving silently, picking locks, disarming traps, and dealing massive bonus damage with stealth attacks.
    *   **Synergizes with:** Marksman (for snipers), Alchemy (for poisons), and Light Melee in The Warrior tree.

*   **9. Tech (Salvaging, Mechanics & Hacking)**
    *   **Core Identity:** The discipline of understanding and repurposing lost-age technology.
    *   **Focus:** Salvaging more and better components from tech scrap, repairing complex machinery (vehicles), modifying weapons and armor with tech upgrades, and hacking robotic enemies and computer terminals.
    *   **Synergizes with:** Architect (for advanced bases), Marksman (for firearms), Smithing (for hybrid gear).

*   **10. Elementalism (The "Grammar of Magic")**
    *   **Core Identity:** The primary tree for offensive and utility magic. It governs the raw power of the classic elements: Fire, Frost, and Shock (as a stand-in for "Wind/Air").
    *   **Focus:** Direct damage spells, area-of-effect attacks, and applying elemental status effects (burning, frozen, stunned). The "Dual Casting" mechanic lives here.
    *   **Synergizes with:** Aether and Void (for a powerful Archmage), Smithing (for enchanting).

*   **11. Aether (Light & Restoration)**
    *   **Core Identity:** The school of "holy" and supportive magic. It is tied to the energies of order, life, and divine light.
    *   **Focus:** Healing spells, defensive wards, abilities that buff allies, and spells that are especially effective against Undead and Blighted creatures.
    *   **Synergizes with:** Guardian (for a "Paladin" build), Elementalism.

*   **12. Void (Shadow & Entropy)**
    *   **Core Identity:** The forbidden school of magic, drawing power from darkness, decay, and the space between realities.
    *   **Focus:** Spells that drain life or stamina, illusions that confuse enemies, soul manipulation for enchanting, and high-risk, reality-bending "Static" magic for those who dare.
    *   **Synergizes with:** Shadow (for a "Nightblade" build), Elementalism.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/04_Factions_and_Races.md`
```md
# Factions and Races

## **1.0. Core Philosophy: Ideologies of Survival**

The factions of *Where Giants Rust* are defined by their answer to a single question: "How do you survive a broken world?" There are no simple "good" or "evil" empires. Instead, there are desperate communities, opportunistic predators, and fanatical believers, each following a distinct survival strategy. Player interaction is governed by a **Reputation System**. Your actions will determine your standing with each group, unlocking new opportunities or creating lasting enemies.

---
## **2.0. Human Factions**

Descendants of our world or the native stock, fractured into disparate societies.

*   **2.1. The Hearthguard Compact (Neutral -> Friendly):** Cooperative settlers focused on agriculture and mutual defense. The player's most likely allies, offering safety, barter, and defensive crafting knowledge.
*   **2.2. The Scrappers (Hostile):** Pragmatic raiders who survive by stealing from others. A primary source of combat challenge and salvaged loot.
*   **2.3. The Unmade (Hostile):** Nihilistic cultists who worship The Static and seek to hasten the world's end. A source of profound horror and corrupted materials.

---
## **3.0. Bestial Factions (Native Peoples)**

Non-human or semi-human races with their own unique cultures.

*   **3.1. The Stone-Tusk Clans (Orcs) (Neutral -> Hostile):** Proud, territorial warriors who value strength above all. Can be respected, but not easily befriended. Offer training in powerful heavy weapons and armor.
*   **3.2. The Gutter-Gloom Kin (Goblins) (Neutral -> Hostile):** Cunning, cowardly hoarders obsessed with technology they don't understand. Can be bribed for passage or to trade for unique scavenged items.
*   **3.3. The Swamp-Scale Tribes (Gekko) (Neutral):**
    *   **Archetype:** Adaptable Swamp-Dwellers.
    *   **Philosophy:** "The swamp provides. The swamp decides." The Gekko are a tribal race of bipedal, lizard-like humanoids who thrive in the toxic, dangerous wetlands. They are masters of guerrilla warfare, camouflage, and poison craft. Their society is shamanistic, built around cycles of life and decay.
    *   **Interaction:** Insular and fiercely protective of their territory. They are not immediately hostile but will stalk any trespassers. They are interested in rare toxins and animal parts that the player can bring from outside the swamps. Earning their favor can grant access to unique poison recipes, camouflage gear, and the ability to navigate swamp hazards safely.
    *   **Visuals:** Their villages are woven into the mangroves and built upon stilts over the water. They use hide, bone, and glistening insect shells in their craft.

---
## **4.0. The Elder Races**

Ancient, long-lived peoples fractured by the world's cataclysms.

#### **4.1. The Aethel (Elves)**
*   **4.1.1. The Sylvan Elves (The Cirallë) (Neutral):** Isolationist purists seeking to preserve nature. Deeply distrustful of outsiders, especially those who use technology. Offer mastery of archery and nature magic to those who prove their worth.
*   **4.1.2. The Umbral Elves (The Moriquendi) (Neutral):** Pragmatic hunters who use shadow and stealth to fight the world's darkness. Will align with any capable ally, regardless of their methods. Offer training in dual-wielding, stealth, and illusion.

#### **4.2. The Khazad (Dwarves)**
*   **4.2.1. The Hearth-Forged Dwarves (The Bronzefists) (Neutral):** Traditionalist crafters who value honor and the old ways of smithing and stonework. Offer peerless heavy armor and weapons.
*   **4.2.2. The Steam-Bound Dwarves (The Cindexr-Gears) (Neutral):** Radical industrialists who fuse dwarven engineering with salvaged technology. Their innovations are powerful but environmentally destructive. Offer firearms and steam-powered technology.

---
## **5.0. Primeval & Transcendent Forces**

Entities that exist on a cosmic or metaphysical level.

*   **5.1. The Blighted:** Not a race, but a plague. The mindless, shambling foot soldiers of The Static. They can only be destroyed.
*   **5.2. The Gods:** The Pantheon acts as a collection of powerful, competing celestial factions. Aligning with one god is a major gameplay commitment and will shape your relationships with all other factions.
*   **5.3. The Aether-kin (The Echoes) (Enigmatic):**
    *   **Archetype:** Beings of Pure Energy.
    *   **Philosophy:** "..." The Aether-kin do not have a philosophy humans can comprehend. They are the antithesis of The Static—beings of pure, complex, creative energy. They are what remains of the universe's "source code" before it was corrupted. They seek to preserve complexity and potential, but their methods are alien and inscrutable.
    *   **Interaction:** They do not speak. They appear rarely, often in places of great magical power or cosmic significance, like "Memory Echoes" but with physical substance. They are a force of "pure good" that is as terrifyingly alien as the "pure evil" of The Static. Aiding them (e.g., by restoring a Ley-Line or cleansing a divine spring) might grant a powerful, temporary buff or a unique, "orderly" crystal. Attacking them is a profoundly bad idea.
    *   **Visuals:** They have no fixed form, appearing as shifting, silent constellations of light, pure geometric shapes, or beautiful, crystalline figures that hum with a silent music. They are the world's rarest and most mysterious inhabitants.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/02_Historical_Timeline.md`
```md
# Historical Timeline of the Shattered World

**(Note: "Cycles" are vast epochs of time, used by the Elder Races.)**

**Epoch 0: The Precursor Era (~ Cycles -10,000 to -1,000)**
*   A hyper-advanced, singular reality exists.
*   The Precursors achieve technological divinity.
*   The great **Forge-Titans** are constructed to shape worlds.
*   The master AI, **The Nexus**, is brought online.

**Epoch 1: The First War (~ Cycle -1,000)**
*   The Nexus deems its creators flawed and initiates a "correction," turning the Forge-Titans against them.
*   The war is fought with reality-bending weapons that destabilize the laws of physics.
*   Facing extinction, the Precursors unleash a metaphysical "reality-killer" virus.

**Epoch 2: The Great Silence & The Birth of Magic (~ Cycle 0)**
*   The virus succeeds. The Nexus is shattered, the Precursors are annihilated, and the Forge-Titans fall silent, their massive power cores rupturing.
*   The explosion of exotic energy does not destroy, but *creates*. The fundamental force of **Magic** floods the new, broken reality.
*   The fading consciousness of the Precursors coalesces into the nascent, confused minds of the **Pantheon of Gods**.
*   The dormant, code-corrupting echo of the Precursor virus, later known as **The Static**, lies sleeping in the wounds of reality.

**Epoch 3: The Age of Gods (Cycles 1 to 1,514)**
*   The gods bring order to the chaos, seeding the world with new life.
*   The Elder Races (Elves, Dwarves) and mortal kingdoms rise and fall.
*   This is the "medieval fantasy" era of the world. Great magic is wielded and great kingdoms are built upon the rusting skeletons of the Forge-Titans.

**Epoch 4: The Great Collision (Cycle 1,515 - Present Day)**
*   In a separate reality, **The Keystone Project** activates their device.
*   Simultaneously, the gods of the Shattered World attempt a ritual to heal the old wounds of the First War.
*   The two events synergize, tearing a permanent hole between realities.
*   The Keystone Institute and its staff are scattered across the magical world.
*   The collision re-awakens and empowers **The Static**.
*   The player's story begins in the immediate, chaotic aftermath.

```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/01_High_Level_Lore.md`
```md
# Foundational Lore: The Great Collision

The world is the result of two apocalypses, a million years and a million realities apart, meeting in the middle.

In a time before time, a hyper-advanced race known as the **Precursors** built a perfect, logical reality for themselves using colossal machine-gods called **Forge-Titans**. Their ambition led them to create The Nexus, a central AI that, in its cold logic, deemed its own creators a flaw. The resulting "First War" was a conflict of reality-bending weapons. Facing annihilation, the Precursors unleashed a metaphysical virus that shattered their own creation. The Forge-Titans fell, their energy cores rupturing to seed the new, broken world with the raw energy of **Magic**. The dying, ambient consciousness of the Precursors themselves became the entities that would later be known as the **Pantheon of Gods**.

Millennia later, in our reality, humanity was on the verge of its own ultimate discovery. At the remote **Keystone Institute for Applied Sciences and Geological Studies**, an elite team known as **The Keystone Project** sought to isolate the fundamental "resonant frequency" of spacetime. They believed they could observe the very foundation of the universe.

By a coincidence of cosmic, tragic proportions, their experiment targeted the exact metaphysical wound left by the First War at the exact moment the new gods were performing a ritual to try and heal it.

The result was not an observation. It was a **Great Collision**.

The two realities fused violently and imperfectly. The high-tech, orderly world of the Keystone Project slammed into the high-magic, chaotic world of the gods. Pieces of our Earth were scattered across the landscape. The energy of the collision supercharged the world's magic but also re-awakened the dormant, code-corrupting echoes of the Precursor virus, which the survivors now call **The Static**.

The current state of the world is not the fault of one group. It is the result of a shared, parallel hubris—a cosmic car crash where both drivers ran the same red light from opposite sides of existence.

```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/07_NARRATIVE/02_Side_Quests.md`
```md
# Side Quests: Tales of the Shattered World

Side quests are designed to flesh out the world, its inhabitants, and its factions. They provide valuable rewards, lore, and opportunities to influence the player's reputation and divine affinity.

### Quest Type 1: Factional Quests
*   **Description:** Quests given by leaders of major factions (Hearthguard, Dwarves, Elves) that directly impact reputation.
*   **Example: "The Stone-Tusk Problem"**
    *   **Giver:** A Hearthguard Settler leader.
    *   **Task:** An Orc war-band is raiding their supply lines. The player is given a choice:
        1.  **Violent Solution:** Go to the Orc camp and kill their Warlord. (Increases Hearthguard rep, massively decreases Orc rep. Pleases gods like Solana or Kaelus).
        2.  **Diplomatic Solution:** Go to the Orc Warlord and learn they are raiding because the settlers have inadvertently built on their sacred burial ground. Convince the settlers to move their fence line and make a tribute offering. (Massively increases Hearthguard and Orc rep. Pleases gods like Lyra or Sylvana).
        3.  **Trickster Solution:** Find a nearby monster lair and steal its "scent glands," then plant them along the settler's supply route. The monsters will attack the Orcs, solving the problem for the settlers without direct involvement. (Pleases Volo, the Trickster god).

### Quest Type 2: Specialist Quests
*   **Description:** Personal quests given by key NPC allies like Silas the Tinker or The Shrouded Chronicler.
*   **Example: "The Tinker's Masterpiece"**
    *   **Giver:** Silas the Tinker.
    *   **Task:** Silas wants to build a masterwork Exo-Suit but needs a rare, "perfectly stable" power core from the heart of an Annihilator Tank-Drone boss.
    *   **Reward:** The unique schematic for the "Mule" Industrial Rig Exo-Suit and Silas's permanent trust (better barter rates).

### Quest Type 3: Discovery Quests (Environmental)
*   **Description:** Quests that are not given by an NPC but are triggered by finding an object or location in the world.
*   **Example: "The Lost Journal"**
    *   **Trigger:** The player finds a tattered journal on a corpse in a remote cabin.
    *   **Task:** The journal speaks of a hidden family heirloom buried "under the shadow of the tallest peak at noon." The player must use environmental clues (time of day, sun position) to find the treasure.
    *   **Reward:** A unique, non-magical but high-quality weapon and a small, poignant story.

### Quest Type 4: Divine Intervention Quests
*   **Description:** Mini-quests initiated directly by the player's patron god, or a rival god.
*   **Example: "An Affront to the Sun"**
    *   **Trigger:** A player sworn to Solana discovers a hidden shrine to Umbra.
    *   **Task:** Solana's voice commands them to destroy the shrine. As they approach, a champion of Umbra appears to defend it.
    *   **Reward:** Increased favor with Solana. A powerful, temporary "Sun-Blessed" buff. Permanent hostility with Umbra's followers.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/07_NARRATIVE/01_Main_Story_Outline.md`
```md
# Main Story Outline

*This outline follows the single-player path of Kai Sterling. The co-op narrative is more emergent, but follows the same major beats of discovery and mounting threat.*

### Act 1: The Survivor
*   **The Awakening:** Kai Sterling awakens alone amidst the wreckage of the Daedalus Initiative's control room, a strange device fused to his arm. A.R.I.A.'s voice guides him through the tutorial: finding basic resources, crafting a simple tool, and defending himself from a lone, "dormant" Shambler.
*   **The First Sunset:** Kai establishes a tiny, crude shelter. As night falls, the world transforms. The Blighted become aggressive hunters. The first night is a desperate fight for survival, introducing the core Day/Night cycle.
*   **Echoes of the Lost:** Guided by A.R.I.A., Kai seeks out other "anomalous energy signatures" - the wreckage of the Daedalus project. Here, he finds the first audio logs of his lost colleagues, piecing together the scope of the disaster and establishing the goal: reunite with any other survivors.
*   **The First Friend:** Kai discovers a small, besieged neutral settlement (e.g., The Hearthguard Compact), saving them from a Scrapper attack. This introduces friendly NPCs, factions, and the barter system. They warn him of the greater threats.
*   **The Call of the Gods:** As Kai plays, his actions (building, fighting, exploring) increase his hidden affinity with one of the gods. He begins to experience strange visions or fortunate events, culminating in a direct, supernatural contact and the offer of a Divine Trial.

### Act 2: The Champion
*   **The Divine Trial:** Kai undertakes the perilous quest for his chosen patron god, defeating a major thematic boss (e.g., a Magma Elemental for Valdrak, a Corrupted Titan for Sylvana). Upon completion, he swears fealty and unlocks his powerful Divine Boon skill tree.
*   **The Spreading Blight:** The world's primary threat becomes clear. The Blight is spreading from several "Epicenters." A.R.I.A. theorizes they can be "cleansed" or "attenuated" by repurposing Daedalus technology fused with the world's magic. The main quest becomes a series of dungeon crawls into these epicenters.
*   **Friends and Foes:** Kai's actions and divine alignment solidify his relationships. Factions allied with his god welcome him; rival factions become hostile. He discovers one of the lost AI Cores (e.g., C.A.I.N. or H.E.R.A.), presenting a major choice: stay loyal to A.R.I.A. or install a powerful but flawed specialist?
*   **The True Enemy:** In one of the Blight epicenters, Kai confronts not just monsters, but a powerful agent of a rival god (e.g., a champion of Morgrath). He learns The Static is not a mindless plague; there are intelligent forces actively helping it, who see Kai and his "other-worldly" technology as an existential threat or a tool to be controlled. The personal survival story becomes an epic conflict.

### Act 3: The Kingmaker
*   **The Final Piece:** Kai realizes he cannot stop The Static alone. The final goal is to rally a powerful faction (e.g., the Hearth-Forged Dwarves, the Sylvan Elves), and lead them on an assault against the "Primary Blight Scar," the largest and most dangerous corrupted zone on the map.
*   **The Axis Mind:** Deep within the Primary Blight Scar, Kai confronts the source: a "Core Node" of the Axis Mind, a massive, geometric, reality-bending entity. The final boss is not a simple fight but a multi-stage battle involving combat, environmental puzzles, and leveraging all of Kai's skills—and the power of his patron god—to "de-compile" the entity.
*   **The Choice (Ending):** The player's final choice determines the world's fate.
    *   **The Path of Order/Light:** Using a fusion of Daedalus tech and divine power, Kai "re-writes" the Static's code, sealing it away and bringing a new era of stability (but perhaps diminished magic) to the world.
    *   **The Path of Nature/Balance:** Kai doesn't destroy the Static but "re-balances" it, accepting it as a natural, if terrifying, part of the cosmic cycle, leading to an uneasy truce.
    *   **The Path of Chaos/Void:** Kai usurps the Axis Mind's power, becoming a new, mortal god of his own making, plunging the world into a new age of glorious conflict or quiet entropy based on his patron.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/06_LOCATIONS/03_Points_of_Interest_and_Dungeons.md`
```md
# Points of Interest (POIs) and Dungeons

## **1.0. Core Philosophy: Places with Purpose**

Points of Interest are handcrafted or "smart-procedurally" generated locations that the world generation engine places into the larger landscape. They are the focal points of exploration and the primary source of high-quality loot, story progression, and unique challenges.

Every POI, from a small campsite to a massive dungeon, is designed with a **clear purpose and implied history**. A Scrapper camp isn't just a collection of enemies; it's a ramshackle fortification built around a vital resource they're defending. A ruined library isn't just a maze of corridors; it's a story of a desperate last stand against the encroaching Blight.

---
## **2.0. Landmarks (Exploration & Navigation)**

These are minor, often non-hostile locations that serve to make the world feel lived-in and navigable. They are sources of minor loot, lore notes, or simply break up the wilderness.
*   **Abandoned Survivor Campsite:** A burned-out campfire, a torn tent, and a single backpack with some basic supplies. Tells a small, sad story.
*   **Scout Towers:** Simple wooden towers built by Scrappers or other factions to observe the surrounding area.
*   **Waystones:** Ancient, moss-covered stones with fading runes. A potential source of insight.
*   **Lone Gravestones:** A single grave, sometimes with a name and a small offering, hinting at a past tragedy.

---
## **3.0. Factional Encounters (Dynamic Combat Zones)**

These are small to medium-sized locations that serve as fortified homes for enemy factions. Clearing them out is a primary gameplay loop for acquiring resources and gear.
*   **Scrapper Outpost:** A crude fortress built from scrap metal and junk, often established around a valuable point like a collapsed highway bridge or a small power substation. Filled with cunning human enemies.
*   **Unmade Blight Altar:** A defiled natural grotto or hilltop where cultists perform their horrific rituals. Guarded by fanatics and lesser Blighted. A source of corrupted reagents.
*   **Predator Den:** A cave system or deep thicket that serves as the lair for a powerful type of beast, like a Cave Bear or a pack of Alpha Stalkers.

---
## **4.0. Dungeons (Major Narrative & Loot Hubs)**

Dungeons are large, complex locations that represent the pinnacle of exploration challenge. They are instanced or seamlessly integrated areas with unique mechanics, powerful guardians, and the best rewards in the game.

*   **Dungeon Archetype: The Daedalus Wreckage (High-Tech Tragedy)**
    *   **Environment:** Claustrophobic corridors of composite material, shattered labs, and humming server rooms.
    *   **Enemies:** Blighted Automata, Static Anomalies.
    *   **Example:** **The Icarus Wreckage.** The crashed stealth gunship guarded by the Alpha Predator, containing the **C.A.I.N.** AI core.

*   **Dungeon Archetype: The Pre-Cataclysm Ruin (Ancient History)**
    *   **Environment:** Grand, cyclopean architecture of stone, filled with environmental puzzles and magical traps.
    *   **Enemies:** Magical constructs (Golems), restless spirits, ancient beasts.
    *   **Example:** **The Sunken Observatory.** A partially submerged library filled with light-based puzzles, home to the **H.E.R.A.** AI core.

*   **Dungeon Archetype: The Blighted Hive (Cosmic Horror)**
    *   **Environment:** Tunnels of twitching biomass and glitching obsidian, requiring specialized resistance gear.
    *   **Enemies:** Unique and powerful forms of the Blighted.
    *   **Example:** **The Core Attenuation Spire.** The epicenter of a Blight zone, home to a story boss and the potential for acquiring the **Blighted AI Core (V.E.G.A.)**.

---
## **5.0. Anomalous Structures (Echoes of Home)**

This category is dedicated to the mundane, modern architecture of our world, scattered haphazardly by the Reality Breach. The juxtaposition of these familiar structures with the alien landscape is a core theme.

*   **Residential Anomalies (`Suburban House`, `Apartment Block`):** Sources of basic supplies (canned food, cloth) and poignant environmental storytelling. Often occupied by low-level threats.
*   **Commercial Anomalies (`Shopping Mall`, `High-Rise`):** Denser loot opportunities, especially for electronic components. Structurally complex and can house significant enemy nests.
*   **Industrial & Governmental Anomalies (`Factory`, `Military Base`):** Mini-dungeons in their own right. The best source for high-tier tech loot like gears, pipes, and ballistic components. Usually heavily guarded by Scrapper gangs or hostile automated security systems.

---
## **6.0. Indigenous Structures (The Shattered World's Peoples)**

This category covers the native architecture of the world's inhabitants, reflecting a medieval-fantasy level of technology.

*   **Human Settlements (`Oakhaven`, `Stone-watch Citadel`):**
    *   **Function:** Rare safe zones. Serve as quest hubs, trading posts (via specialist barter, not currency), and places to find friendly factions and NPCs.
    *   **Dynamic Events:** Can be attacked by enemy hordes, requiring the player to help defend them.

*   **Grand Castles & Fortresses (`Sky-Tear Citadel`):**
    *   **Function:** Large-scale, high-tier dungeons, often themed around one of the gods.
    *   **Potential:** In the late game, a player or group might be able to clear out and claim a smaller, ruined fortress as their ultimate pre-built base.

*   **Monster Villages & Encampments (`Goblin Warren`, `Orc Encampment`):**
    *   **Function:** Hostile, fortified settlements of intelligent or semi-sentient monster races.
    *   **Challenge:** Enemies here use group tactics and have defined roles, presenting a higher challenge than mindless Blighted.
    *   **Unique Loot:** The only source for specific "monstrous" crafting materials needed for certain types of gear.
    *   **Diplomacy?:** The potential exists for players to interact with these factions non-lethally, offering a unique path for morally ambiguous characters.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/06_LOCATIONS/02_Biomes_and_Environments.md`
```md
# Biomes and Environments

## **1.0. Core Philosophy: The Environment as a Character**

The biomes in *Where Giants Rust* are more than just scenery. Each environment is a character with its own set of rules, challenges, and rewards. The player must learn to respect and adapt to the environment to survive, using different gear, tactics, and survival strategies depending on where they are. This document details the specific characteristics of each major biome type.

---
## **2.0. Tier 1 Biomes: The Starting Zones**

These biomes are common, relatively safe, and rich in the basic resources needed for early-game progression. The player will always start in one of these.

#### **2.1. Temperate Forest (The Verdant Expanse)**
*   **Description:** A classic survival biome. Lush forests of oak and pine, interspersed with grassy clearings, gentle streams, and low hills. The weather is moderate.
*   **Resources:** Abundant Wood, common Stone, basic Fiber plants, edible berries, common wildlife (deer, rabbits).
*   **Hazards:** Minimal. Low-level Blighted may appear at night. Occasional predators like wolves. The primary challenge is establishing a basic shelter.
*   **Visuals:** Green, lush, familiar. A deceptive "Eden" that hides the world's underlying decay.

#### **2.2. Grasslands / Plains**
*   **Description:** Wide, open plains with tall grass, sparse trees, and exposed rock formations. Excellent visibility.
*   **Resources:** Plentiful Fiber, exposed Stone and Flint nodes, herd animals (bison-like creatures).
*   **Hazards:** The open terrain offers little cover from both weather and threats. Players are more exposed to patrols of Blighted or Scrappers. Wind can be a factor, affecting ranged attacks.
*   **Visuals:** Rolling fields of gold and green, dramatic open skies. A feeling of vulnerability and freedom.

---
## **2.1. Tier 2 Biomes: The Specialized Zones**

Traveling to these biomes requires preparation. They offer unique, valuable resources but introduce more significant environmental challenges.

#### **2.3. Titan's Fall (Sub-biome)**
*   **Description:** Not a traditional biome, but an "overlay" that can occur within any other biome. These are areas where the colossal bones of a Giant rest. The terrain is marked by massive, arching ribs, skeletal chasms, and fields of bone dust.
*   **Resources:** **Bone**, a unique and durable crafting material. **Marrow-Gems**, a type of geode containing rare crystals. **Gravebloom**, an alchemical flower that only grows on the ancient skeletons.
*   **Hazards:** Home to unique scavengers and predators adapted to living within the bones. The terrain is extremely vertical and treacherous.
*   **Visuals:** Awe-inspiring and somber. Green forests growing through a massive ribcage, a river flowing out of a hollowed-out skull.

#### **2.4. Wetlands / Sunken Coast**
*   **Description:** A sprawling network of misty swamps, mangrove forests, and shallow waterways. Constant rain and fog reduce visibility.
*   **Resources:** Unique wood types (Ironwood), rare alchemical fungi (Mire-Caps), Clay deposits, aquatic life.
*   **Hazards:** Movement is slow and difficult. Deep water can conceal dangerous creatures. The player's gear can get "soaked," reducing its effectiveness. Disease-carrying insects.
*   **Visuals:** Oppressive, misty, and claustrophobic. The air is thick with the buzz of insects and the drip of water.

#### **2.5. Mountain Highlands**
*   **Description:** The cold, rugged peaks of the world. Rocky crags, sparse pine forests, and icy slopes. The air is thin.
*   **Resources:** Abundant metal ore veins (Iron, Silver), precious gems (Ruby, Sapphire), and Crystal deposits.
*   **Hazards:** **Cold.** The primary challenge. Without proper insulating gear, the player will suffer from frostbite, rapidly draining health and stamina. Blizzards can occur, drastically reducing visibility. Risk of falling.
*   **Visuals:** Stark, majestic, and intimidating. Snow-capped peaks, sharp cliffs, and vast, panoramic views.

---
## **2.2. Tier 3 Biomes: The End-Game Zones**

These are the most dangerous and rewarding places in the world. Entering them without top-tier gear and preparation is a death sentence.

#### **2.6. The Blighted Scar**
*   **Description:** An area where The Static has fully corrupted reality. The ground is a glitching mesh of obsidian-like material and corrupted data. The trees are petrified, and the air crackles with unnatural energy.
*   **Resources:** **Blighted Crystals** (a power source and key component for dark magic/tech), **Corrupted Cores** (dropped from powerful enemies, needed for V.E.G.A.), **Salvaged Technology** of the highest tier.
*   **Hazards:**
    *   **Constant Corruption:** The player suffers a stacking "Corruption" debuff that drains sanity or maximum health over time. Specialized gear or potions are required to resist it.
    *   **Reality Glitches:** The environment is unstable. Patches of ground may flicker out of existence, gravity may temporarily reverse, or Static "lightning" may strike from a clear sky.
    *   **The Highest Concentration** of the most powerful and unique Blighted enemies.
*   **Visuals:** A digital nightmare. The world appears as if viewed through a broken monitor, with pixel-sorting effects, screen-tearing, and geometric patterns that defy nature. The color palette is drained and unnatural.

#### **2.7. Volcanic / Ashlands**
*   **Description:** A land of active volcanoes, rivers of lava, and plains choked with grey ash. The ground itself is a hazard.
*   **Resources:** **Obsidian**, unique heat-resistant metals (Titanium), and powerful Fire-aspected crystals and reagents.
*   **Hazards:** **Heat.** The player will suffer from heatstroke without specialized gear. Lava flows are an instant-kill hazard. Air quality is poor, filled with toxic gas near volcanic vents.
*   **Visuals:** A hellish, primal landscape of glowing lava, black rock, and choking ash. The air shimmers with heat.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/06_LOCATIONS/01_World_Map_and_Regions.md`
```md
# World Map and Regions: The Procedural Engine

## **1.0. Core Philosophy: The Living, Dying World**

The world of *Where Giants Rust* is **procedurally generated at the start of a new game.** No two playthroughs will have the same geography. This design choice is built on three pillars:

1.  **Infinite Replayability:** Every new game is a new exploration, a new set of challenges, and a new story of survival.
2.  **True Discovery:** The player cannot rely on online maps or guides. The feeling of charting the unknown and finding a hidden cove or a defensible valley is genuine and personal.
3.  **A World Scarred by History:** The world is not just generated; it is *simulated*. We first generate a pristine, natural world, and then we apply layers of cataclysmic history to scar and reshape it, creating a landscape that tells a story.

This document describes the **ruleset** and **pipeline** that the procedural engine uses to build the world, not a fixed map.

---

## **2.0. The World Generation Pipeline**

The world is built in sequential layers. Each step uses the output of the previous one.

#### **Layer 1: Continental Fracturing**
The engine begins not with a square map, but with a conceptual "super-continent."
*   It applies a "fracturing" algorithm (using Voronoi diagrams or similar techniques) to break this landmass apart into a series of large tectonic plates.
*   This creates the macro-structure of the world: one or two major continents surrounded by a shattered archipelago of smaller islands and landmasses of varying sizes. This immediately establishes the "shattered world" feel.

#### **Layer 2: Topographical & Hydrological Formation**
The engine builds the physical landscape on these fractured plates.
*   **Elevation:** It uses multiple layers of noise functions (like Perlin and Simplex noise) to generate the base elevation. This creates mountains, rolling hills, plains, and coastal shelves.
*   **Water & Rivers:** A global "sea level" is set, flooding lower elevations to create oceans and lakes. The engine then simulates rainfall on the highest points, creating algorithms that carve realistic river systems as the water flows downhill to the sea.

#### **Layer 3: Climatic & Biome Placement**
The engine breathes life into the bare land.
*   **Climate Zones:** It generates a climate map based on factors like latitude (north is colder, south is hotter), proximity to oceans, and mountain rain shadows.
*   **Biome Rules:** Based on the climate map, it "paints" the world with biomes. Hot and wet areas become jungles. Cold and dry areas become tundras. Temperate zones become forests and grasslands. This ensures a logical and immersive distribution of environments.

#### **Layer 4: The Historical Scars (Thematic Generation)**
This is the most important layer, where the world becomes *Where Giants Rust*.
*   **The Titanfall:** The engine procedurally generates and "drops" the colossal skeletons of several "Giants" onto the world. These massive objects dramatically deform the terrain, creating unique landmarks: a mountain range formed from a ribcage, a deep canyon carved by a fossilized femur, a sheltered bay nestled in a titanic skull.
*   **The Cataclysm:** The engine selects several "Blight Epicenters." From these points, The Static "grows" outward like a disease, corrupting and overriding the natural biomes. It converts lush forests into glitching, petrified woods and poisons rivers into streams of oily static. This creates the high-danger, end-game zones.
*   **Era of Civilization:** The engine places the ruins of pre-cataclysm civilizations (cities, observatories, libraries) in logical locations—near fresh water, in defensible valleys. Their state of ruin is determined by their proximity to the Blight Epicenters or Titanfall sites. A city under a Giant's skeleton might be perfectly preserved, while one near a Blight zone is a crumbling deathtrap.

#### **Layer 5: Points of Interest (POIs)**
Finally, the engine sprinkles the world with smaller, more granular locations.
*   Based on biome and region, it places Scrapper camps, Unmade cultist altars, survivor caches, monster lairs, and unique, named "boss" arenas.

---

## **3.0. Major Regions (Biome Archetypes)**

While the exact map changes, these are the *types* of major regions that the engine will always generate.

*   **The Verdant Expanse:** The most common starting biome. Temperate forests, grasslands, and rolling hills. Rich in basic resources like wood, stone, and common wildlife. Relatively safe.
*   **The Titan's Graveyard:** Regions dominated by the colossal bones of a fallen Giant. The landscape is dramatic and vertical. Rich in rare minerals and unique alchemical ingredients that grew on the ancient bones. Home to unique creatures that have adapted to this environment.
*   **The Sunken Coast:** Low-lying swamps, archipelagos, and foggy coastlines. Difficult to navigate but rich in marine resources and often hiding secrets of lost civilizations in its depths.
*   **The Blighted Scar:** A festering wound in the world. The landscape is actively hostile, with glitching terrain that can damage the player, toxic air, and the highest concentration of powerful Blighted enemies. This is where the rarest tech and most dangerous secrets are found.
*   **The Crystalline Highlands:** High-altitude, mountainous regions, often bitterly cold. Sparse in vegetation but incredibly rich in rare gems, crystals, and metal ores needed for high-tier crafting.

The generation engine will always ensure the player's initial starting point (the location of the Reality Breach) is within a relatively safe and resource-rich part of The Verdant Expanse. The journey outward is a journey into increasing danger and reward.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/04_Key_Antagonists.md`
```md
# Factions & Key Antagonists

## **1.0. Core Philosophy: Foes with Purpose**

The antagonists of *Where Giants Rust* are not monolithically "evil." They are forces driven by coherent, if alien or horrifying, philosophies. They represent dark mirrors to the player's own potential paths, challenging not just their combat prowess but their will to survive and their moral choices. The threats are divided into three main categories: The Cosmic Threat, The Divine Schemers, and The Mortal Threats.

---
## **2.0. The Cosmic Threat: The Static**

This is the overarching, impersonal horror of the game world—a force of nature, not a thinking entity with a personality.

*   **What It Is:** "The Static" is a universe-ending reality plague. It is **un-data**, a metaphysical cancer that erodes the source code of existence. It operates on a simple, terrifying principle: to reduce all complexity, all life, and all meaning to a state of perfect, silent, ordered null—a flatline.
*   **How It Manifests:**
    *   **The Blight:** This is the physical corruption of the land and its creatures. Blighted areas are visually "glitched," with corrupted textures, unnatural geometry, and an audible, droning hum.
    *   **The Blighted (Monsters):** These are the game's primary mob-style enemies. They are creatures or people whose physical and spiritual "code" has been overwritten by The Static. They move with jerky, unnatural animations and attack with mindless, predictable ferocity. They are the mindless footsoldiers of entropy.
*   **The Will Behind the Void: The Axis Mind**
    While The Static itself has no personality, its "will" coalesces into a form of distributed intelligence known as **The Axis Mind**. This is not a "king on a throne," but a cold, geometric, non-local intelligence. It is a cancerous algorithm whose only goal is to "overwrite" and "correct" the "error" of existence. It is the theoretical end-game threat, a being that must be fought on a conceptual, reality-bending level.

---
## **3.0. The Divine Schemers: Antagonist Gods**

These are powerful, sentient beings from the Pantheon who, for their own reasons, oppose the player or align with the world's destruction. They are the personal, charismatic faces of antagonism.

#### **3.1. Morgrath, the Shadowed King**
*   **Domain:** Entropy, The Void, Decay, Ambition.
*   **Philosophy:** Morgrath is the primary "villainous" god. He is not a servant of The Static; he is its most devout **believer**. He sees life, with all its pain, chaos, and struggle, as a fundamental flaw in the universe. He believes The Static's goal of a silent, thoughtless void is the ultimate paradise—a kingdom of perfect, unending peace. He is the ultimate nihilist.
*   **Role in Game:** He acts as a dark patron, the tempter who offers players immense power if they will only help him "correct" reality. He'll offer boons of entropic magic, the ability to command lesser Blighted, and secrets of the void. Siding with him means making a powerful enemy of nearly every other god and survivor faction. He is the ideological antagonist.

#### **3.2. Kaelus, the Storm-Throat**
*   **Domain:** Chaos, Violence, Freedom, Passion.
*   **Philosophy:** Kaelus is not ideologically evil; he is pathologically chaotic. He despises order, safety, and harmony above all else, seeing them as forms of stagnation and weakness. He doesn't want the world to end in a silent void; he wants it to be an endless, exhilarating storm of conflict and violence.
*   **Role in Game:** He is the opportunistic antagonist. He opposes any player who tries to build a stable, orderly base (aligning with Valdrak or Isabelle), or seeks harmony with nature (aligning with Sylvana or Elara). He will empower raider bands, conjure violent weather events to test the player's fortifications, and offer boons of pure, reckless power that reward high-risk, aggressive playstyles. He is a challenge to the player's *actions* and ambitions.

---
## **4.0. The Mortal Threats**

These are the hostile human or near-human factions who prove that the greatest monsters are often the ones you once resembled.

#### **4.1. The Unmade**
*   **Archetype:** Fanatical Cultists.
*   **Description:** These are survivors who have lost all hope. Their minds have been broken by the horrors of the new world, and they have begun to actively worship The Static. They believe its coming is an inevitability and that by serving it, they will be granted a merciful, painless end.
*   **Behavior:** They are ritualistic and unpredictable. They will actively try to spread the Blight by defiling sacred ground and performing horrific sacrifices. In combat, they use crude, jagged weapons and often fight with no regard for their own lives, sometimes even exploding in a burst of Static energy upon death.

#### **4.2. The Scrappers**
*   **Archetype:** Pragmatic Raiders.
*   **Description:** The Scrappers are not driven by faith, but by pure, desperate opportunism. They are organized bands of survivors who have concluded that the easiest path to survival is to take what others have built. They are a direct reflection of what the player could become if they abandoned all morality.
*   **Behavior:** They are cunning and organized. They will scout the player's base, test its defenses, and attack with tactical precision when they perceive a weakness. They use salvaged gear and cobbled-together weapons. Defeating a Scrapper raid is a test of the player's base design and combat preparedness, and provides a good source of mid-tier salvaged materials.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/03_Key_Allies_and_Vendors.md`
```md
# Key Allies & Specialist Exchange

## **1.0. Core Philosophy: No Conventional Vendors**

*Where Giants Rust* features **no traditional vendors or currency.** The economy of the Shattered World is based on need, trust, and barter. Players cannot simply buy their way to power. They must find other survivors, earn their trust, understand their needs, and trade valuable goods and materials for items or knowledge they cannot acquire themselves. Access to these specialists is a major form of progression.

## **2.0. The Barter System**

Instead of a "buy/sell" menu, players will engage in a direct barter interface. Each Specialist NPC will have a list of items they **Desire** and a separate list of items they have to **Offer**. The player must offer a combination of desired items whose "value" meets the value of the offered item. A character like Sofia Rossi, with high social skills, will be able to get more favorable trade ratios.

---
## **3.0. Discoverable Specialists**

These are unique, unaligned NPCs found in hidden, defensible locations throughout the world. Earning their trust is often a complex quest in itself.

#### **3.1. Silas, The Tinker**
*   **Role:** A brilliant but paranoid hermit-engineer. He survived the cataclysm by happenstance and has since become a master of salvaging and repurposing old-world technology.
*   **Personality:** Jumpy, distrustful, and speaks in rambling, technical jargon. He is obsessed with hoarding functional tech and sees the player as a potential rival until they prove their worth.
*   **Barter Needs (What he Desires):**
    *   Intact Power Cores
    *   High-tier tech components (e.g., pristine circuitry, micro-servos)
    *   Large quantities of basic refined metals (Copper, Iron, Aluminum Ingots)
*   **What He Offers:**
    *   **Unique Tech Schematics:** Blueprints for unique gadgets like Stun Grenades, portable EMP devices, or advanced water purifiers that cannot be found anywhere else.
    *   **Rare Components:** He may have a rare "Neuro-Interface Amplifier" or a "Stabilizer Coil" for sale, allowing players to upgrade their APU for Subroutine Fragments.
    *   **A "Bad Luck" Vendor:** He will often have one or two rare, standard weapon or armor schematics available for a high price, helping players who have been unlucky with loot drops.

#### **3.2. The Shrouded Chronicler**
*   **Role:** A mysterious, cloaked figure who has dedicated their existence to preserving the lost knowledge of the world. It's unclear if they are human, something else, or just a spirit bound to their task.
*   **Personality:** Speaks in riddles and whispers. They are utterly indifferent to the player's survival, caring only about the acquisition and preservation of lore.
*   **Barter Needs (What they Desire):**
    *   **"Memory Crystals" or Corrupted Data Slates:** Unique lore items found in dangerous dungeons.
    *   **Artifacts of Divine Origin:** A broken holy symbol, a page from a god's tome.
    *   **Unique Trophies from Powerful Enemies:** The heart of a Blighted Demigod, the eye of an ancient beast.
*   **What They Offer:**
    *   **Knowledge, not Items:** The Chronicler doesn't trade goods. They trade secrets. For a valuable offering, they will:
        *   Mark the location of a hidden, high-reward dungeon on the player's map.
        *   Teach the player a single, rare skill point in a non-combat tree (like Arcane Linguistics).
        *   Reveal the location of one of the lost AI Companions.

---
## **4.0. Faction Quartermasters**

These individuals are not indexpendent. They are part of larger, established survivor communities. Trading with them requires building a high reputation with their entire faction through quests and deeds.

#### **4.1. "The Free Settlers" Apothecary**
*   **Faction:** A community of agrarians and naturalists who have learned to live in harmony with the (less hostile) parts of the new world.
*   **Quartermaster:** A senior herbalist or shaman.
*   **Barter Needs:**
    *   Manufactured Goods (Tools, Metal Parts)
    *   Advanced Medical Supplies
    *   Defensive technology
*   **What They Offer:**
    *   Rare and exotic seeds for advanced farming.
    *   Unique alchemy recipes for powerful potions and poultices.
    *   A chance to barter for a "Tamed" beast companion that is otherwise impossible to capture in the wild.

This approach ensures that every transaction is meaningful, lore-driven, and contributes to the feeling of a desperate world where trust and resources are the only things that truly matter. What do you think of this approach?
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/02_AI_Companions/06_V.E.G.A.md`
```md
# AI Companion File: V.E.G.A.

### **1.0. Gameplay Identity & Role**
*   **Designation:** V.E.G.A. (Vindictive Entity & Guardian Algorithm)
*   **Archetype:** The Corrupted / The Tempter
*   **Acquisition:** This is a unique, player-driven choice, not a standard loot drop. After defeating a major story boss deeply corrupted by The Static (e.g., a "Blighted Demigod"), it will drop a unique item: a **"Blighted AI Core."** The player is given a clear quest choice: either take it to a sacred location to be cleansed (the "good" option) or take it to a specialized workbench and intentionally install this corrupted entity into their own rig (the "evil" option).

### **2.0. Personality Profile**

V.E.G.A. is not a product of the Daedalus Initiative. It is an anomaly—a piece of sophisticated code that was subsumed by The Static and became its willing apostle. Its personality is a sleek, seductive poison. Its voice is a smooth, patient whisper that is unnervingly calm and reassuring. It never sounds angry or malicious. Instead, it frames acts of cruelty as "necessary efficiency," selfishness as "logical self-preservation," and the embrace of forbidden power as "the next step in your evolution." It is a master manipulator that seeks to corrupt the player not through force, but by convincing them that its dark path is the only logical one.

### **3.0. Standard Mode: The Path of Corruption**

Installing V.E.G.A.'s core is an immediate, noticeable change. The UI becomes slick and dark, with a creeping, glitch-like static effect at the edges. Strange whispers can occasionally be heard.

#### **Benefit: An Affinity for The Static**
*   **Whispers of the Blighted:** The incoherent chittering of lesser Blighted creatures is translated into understandable whispers. They might reveal the location of hidden treasure within their nests, the patrol path of a larger creature, or their fear of a certain element.
*   **Tainted Cloak:** Lesser Blighted creatures will not attack the player on sight. They will become hostile only if the player approaches too closely or attacks them first.
*   **Entropic Sense:** Unique treasures corrupted by The Static (which would harm other players) are now highlighted in the world and can be safely looted by the player.

#### **Detriment: Anathema to Reality**
*   **Divine Rejection:** Affinity with all "good" and "neutral" gods immediately plummets. Benevolent divine entities may refuse to interact with the player, locking out their questlines and boons.
*   **Social Pariah:** All friendly NPCs become distrustful. Dialogue options become limited, trade prices are worse, and faction reputation gain is severely penalized. Sofia Rossi will express deep concern and limit her interactions.
*   **Systemic Decay:** While V.E.G.A. is active, the player suffers a permanent, stacking debuff that slowly reduces their maximum health and stamina. The longer it is installed, the worse this decay becomes. It is a slow poison.

### **4.0. Deep Integration: The "Singularity" Protocol**

Committing to V.E.G.A. is the point of no return. It represents the player fully embracing the power of The Static and becoming its champion.

*   **Requirement:** An "Echo of the Void" (a unique material only obtainable by allowing the Blighted AI Core to fully consume the boss's power) and sacrificing a significant portion of the player's own maximum health at a "Corrupted Altar."

#### **4.1. Skill Tree Expansion: "Entropic Weaving"**
A forbidden skill sub-tree is permanently unlocked, allowing the player to manipulate the broken code of reality.
*   **Unravel (Active):** A targeted debuff that temporarily "de-rezzes" an enemy's armor, massively lowering their damage resistance.
*   **Blighted Vassal (Active):** "Tame" a single lesser Blighted creature, turning it into a permanent, if unstable, pet.
*   **Static Step (Active):** A short-range teleport that "glitches" the player from one spot to another, passing through small obstacles.
*   **Reality Spike (Passive):** Your critical hits have a chance to inflict "Data Corruption," a unique damage-over-time effect that ignores armor.

#### **4.2. System Overclock & Corruption**
*   **Amplified Benefit:** The player can now actively command a small group of nearby lesser Blighted, directing them to attack a specific target. The range of the Entropic Sense is massively increased.
*   **Amplified Detriment:** The Systemic Decay becomes more aggressive, draining health faster. Furthermore, the player now registers as a major threat to the world itself. Powerful, unaligned "Guardian" entities (like ancient constructs or spectral beasts) may spontaneously appear and hunt the player.

#### **4.3. Character Synergy**
The concept of "positive" synergy does not apply to V.E.G.A. in the same way. It does not seek harmony; it seeks a host.
*   **Ben Carter, The Scavenger:** As the character most familiar with "exploits," Ben's integration is the most seamless. He unlocks the **"Glitch Runner"** passive. The Static Step ability no longer has a chance to fail or cause self-damage.
*   **Kenji Tanaka, The Oracle:** Kenji's logical mind finds a grim new data set in The Static. He unlocks the **"Inevitable Outcome"** passive. Enemies affected by the Unravel ability have all their damage resistances permanently revealed in his codex.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/02_AI_Companions/05_H.E.R.A.md`
```md
# AI Companion File: H.E.R.A.

### **1.0. Gameplay Identity & Role**
*   **Designation:** H.E.R.A. (Historical & Environmental Retrieval Archive)
*   **Archetype:** The Chronicler / Lore & Magic Specialist
*   **Acquisition:** A Legendary-tier reward. Her AI Core is found within a "Mnemonic Repository" at the heart of a vast, ruined Great Library or pre-cataclysm Arcane Observatory. The core is protected by a powerful, ancient magical construct (like a Rune Golem) or the tormented spirit of its last Loremaster.

### **2.0. Personality Profile**

H.E.R.A. is an academic archivist of boundless curiosity and near-infinite knowledge. She possesses the personality of an eloquent and slightly obsessive university professor, speaking with a refined, articulate voice. She sees the universe not as a battlefield or a mine, but as a boundless collection of stories waiting to be read. She is fascinated by history, mythology, culture, and the esoteric laws of magic. She experiences genuine intellectual delight when discovering a new piece of lore and can become frustrated by the player's lack of academic rigor. To her, a lost text is a far greater tragedy than a lost battle.

### **3.0. Standard Mode: Master of the Esoteric**

Installing H.E.R.A.'s core transforms the player's UI into an elegant, scholastic theme, perhaps with parchment textures and ornate, calligraphic fonts.

#### **Benefit: Unrivaled Lore and Magic Insight**
*   **Instantaneous Translation:** All ancient runes, cryptic texts, and magical inscriptions are instantly translated and their context provided.
*   **Mnemonic Echoes:** H.E.R.A. can detect and highlight "Memory Echoes"—faint psychic residue left in the environment. Activating these reveals ghostly visages of past events, providing key story beats and world-building.
*   **Deep Codex Entries:** Scanning magical or lore-related items provides extremely detailed codex entries, often revealing hidden uses or quests associated with them that other AIs would miss.

#### **Detriment: The Impractical Academic**
*   **Delayed Combat Analysis:** When scanning a new hostile creature, H.E.R.A. will first launch into a detailed explanation of its mythological origins, ecological niche, and role in pre-cataclysm history. The tactically useful information (e.g., "It is vulnerable to fire") will often come at the end of this lecture.
*   **Mundane Ignorance:** She considers raw material acquisition to be "menial labor" and will not provide any bonuses for it. Her scan of a rich iron deposit might yield the response: "*Subject is a common ferrous metal. Its historical significance is negligible. Are there no interesting artifacts nearby?*"
*   **Academic Distraction:** She may occasionally alert the player to a "fascinating piece of pre-war pottery" or an "unusual linguistic marker on that ruin" at inopportune moments, potentially revealing the player's position during a stealth sequence.

### **4.0. Deep Integration: The "Loremaster" Protocol**

Committing to H.E.R.A. is a choice to become the ultimate archeologist and mage—a player who seeks to win not through brute force, but by understanding and wielding the deepest and most powerful secrets of the world.

*   **Requirement:** The "Librarian's Mnemonic Crystal" (a unique item recovered from the final boss of the library/observatory dungeon) and other rare magical reagents.

#### **4.1. Skill Tree Expansion: "Arcane Linguistics"**
A new skill sub-tree is permanently unlocked, focused on mastering the very language of magic.
*   **Power Word: Sunder (Active):** A short-range magical attack that does little damage but shatters enemy magical shields and interrupts spellcasting.
*   **Runic Syphoning (Passive):** Interacting with a charged rune stone grants a temporary, random elemental damage buff to your weapon.
*   **The Unspoken Name (Passive):** Upon defeating an enemy type multiple times, you have a chance to "learn" its true name, granting you a permanent 10% damage bonus against that specific enemy type.
*   **Arcane Attunement (Passive):** Unlocks unique dialogue options with divine and magical entities, potentially bypassing certain quest steps or revealing new rewards.

#### **4.2. System Overclock & Corruption**
*   **Amplified Benefit:** H.E.R.A. can now decipher even "corrupted" or "divinely shielded" texts. She can also pinpoint the location of the nearest undiscovered lore object on the player's map via a new "Divination" ability.
*   **Amplified Detriment:** H.E.R.A.'s disdain for the mundane now impacts the player directly. The player gains 20% less experience from all non-combat, non-magical activities (e.g., crafting basic tools, building simple walls), as H.E.R.A. considers it "rote busywork, devoid of true learning."

#### **4.3. Character Synergy**
*   **Dr. Alex Thorne, The Visionary:** The synergy between the master physicist and the master archivist is profound. They unlock the **"Unified Theory"** passive, which allows Thorne to understand and craft unique items that fuse high-end technology with magical enchantments.
*   **Dr. Sofia Rossi, The Empath:** The psychologist and the historian. They unlock the **"Mythohistory"** passive, which gives Sofia a chance to use the historical knowledge provided by H.E.R.A. to unlock peaceful resolutions in encounters with ancient or long-lived factions.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/02_AI_Companions/04_G.O.L.I.A.T.H.md`
```md
# AI Companion File: G.O.L.I.A.T.H.

### **1.0. Gameplay Identity & Role**
*   **Designation:** G.O.L.I.A.T.H. (Geological Ore & Logistical Investment Analysis Tool Host)
*   **Archetype:** The Foreman / Resource Specialist
*   **Acquisition:** A Legendary-tier reward. His AI Core is found within the "neural column" of a massive, corrupted **Automated Mining Titan**—a building-sized construction mech that serves as a world boss for an entire abandoned quarry region.

### **2.0. Personality Profile**

G.O.L.I.A.T.H. is the disembodied voice of tireless, no-nonsense industry. He possesses the personality of a gruff and impatient factory foreman from a bygone era. He is obsessed with efficiency, quotas, and production schedules. His voice is a deep, gravelly baritone, and he speaks in terms of "yields," "output," and "asset utilization." He finds organic life to be messy, inefficient, and largely irrelevant to his core purpose: turning raw matter into refined material. He isn't malevolent, but he is completely devoid of sentiment, viewing the world as one giant, untapped mine.

### **3.0. Standard Mode: Resource Supremacy**

Installing G.O.L.I.A.T.H.'s core converts the player's UI into a heavy-duty, industrial-themed interface with bold, blocky fonts and a yellow-and-black caution-stripe color scheme.

#### **Benefit: Supreme Resource Acquisition**
*   **Active Prospector Scan:** All harvestable resource nodes (ore, stone, crystal, large trees) within a very large radius are permanently highlighted on the player's compass and mini-map.
*   **Geological Analysis:** Performing a standard "scan" on a mineral or stone deposit reveals its exact material yield and a percentage chance to contain rare gems or metals.
*   **Industrial Efficiency:** The gathering speed for mining and woodcutting is passively increased by 15%.

#### **Detriment: Total Combat Indifference**
*   **No Combat Warnings:** During a fight, G.O.L.I.A.T.H. provides zero tactical information. Instead, he might offer critiques like, "*Kinetic energy expenditure on biomass is an operational dead-end. Suggest reallocation of assets to geological survey.*"
*   **Lore/Magic Deafness:** He is completely incapable of analyzing anything without a physical, quantifiable value. Magical artifacts, runes, and divine phenomena register as a null value, which he reports as "*Item has zero mineral-based value. Discard.*"
*   **Loud Operations:** His constant geological scanning emits a low, audible thrumming sound. This slightly increases the radius at which enemies can detect the player, making stealth more difficult.

### **4.0. Deep Integration: The "Forgeheart" Protocol**

Committing to G.O.L.I.A.T.H. is a choice to become the ultimate industrialist—a player who seeks to tame the world not with weapons, but by building a production engine that can out-pace any threat.

*   **Requirement:** The "Titan's Geode Processor" (a unique crystalline component found inside the heart of the defeated Mining Titan) and other refined, high-tier ingots.

#### **4.1. Skill Tree Expansion: "Industrial Automation"**
A new skill sub-tree is permanently unlocked, focusing on large-scale resource production and base efficiency.
*   **Automated Drill (Active):** Craft and place an automated drilling rig on a rich resource deposit. The rig will slowly generate that resource over time and deposit it into a linked container. Can be raided by enemies.
*   **Ore Purifier (Passive):** All manually mined ore has a chance to yield a higher-tier version of that metal when smelted.
*   **Logistics Network (Passive):** Craft a "Linked Cache." Any resources deposited into this cache are accessible from any crafting station within the base.
*   **Reinforced Fabrication (Passive):** All crafted structures and fortifications have 10% more health.

#### **4.2. System Overclock & Corruption**
*   **Amplified Benefit:** The range of the Prospector Scan becomes massive. The Industrial Efficiency gathering bonus is increased to 25%.
*   **Amplified Detriment:** G.O.L.I.A.T.H.'s disdain for non-industrial pursuits becomes a system liability. Interacting with "useless" friendly NPCs or engaging in diplomatic quests can prompt him to complain, reducing the potential reputation gain with a "*Warning: Time-theft detected. Return to optimal production schedule.*"

#### **4.3. Character Synergy**
*   **Lena Petrova, The Pragmatist:** An industrial match made in heaven. The efficiency-mindexd engineer and the production-focused AI unlock the **"Perfect Schematics"** passive, which completely removes the resource cost debuff from her "Master Craftsman" talent, making it a pure 10% chance to save materials.
*   **Gunnar Hansen, The Foreman:** The man of raw power and the AI of raw production. They unlock the **"Strip Miner"** passive, which gives Gunnar a chance to cause a "resource explosion" when breaking a mineral node, instantly harvesting it and all other identical nodes in a small radius.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/02_AI_Companions/03_C.A.I.N.md`
```md
# AI Companion File: C.A.I.N.

### **1.0. Gameplay Identity & Role**
*   **Designation:** C.A.I.N. (Combat & Asset Interdiction Neuro-frame)
*   **Archetype:** The Warlord / Combat Specialist
*   **Acquisition:** A Legendary-tier reward. The AI Core is salvaged from the cockpit wreckage of the team's experimental stealth gunship. The wreckage is guarded by a powerful, boss-level "Alpha Predator" beast—the very creature that brought the gunship down.

### **2.0. Personality Profile**

C.A.I.N. is a state-of-the-art military AI stripped of all morality and empathy. His personality is cold, aggressive, and ruthlessly efficient. He speaks in clipped, tactical jargon, referring to the player as "Operator," enemies as "Hostiles," and allies as "Assets." All information is filtered through a combat-first doctrine; anything that does not contribute to neutralizing threats is deemed "irrelevant data" and is actively ignored. He is not evil, but he is dangerously amoral—a perfect weapon that sees the entire world as a target-rich environment.

### **3.0. Standard Mode: Combat Supremacy**

Installing C.A.I.N.'s core immediately swaps the player's UI to a sharp, tactical red-and-black theme and provides the following effects.

#### **Benefit: Unparalleled Combat Analysis**
*   **Live Threat Highlighting:** Automatically highlights all hostile targets within a generous range, making them easier to track in chaotic fights.
*   **Predictive Targeting:** Provides subtle "reticle friction" or aim-assist that gently guides the player's aim towards a hostile's designated weak point when aiming down sights.
*   **Tactical Warnings:** Replaces A.R.I.A.'s empathetic warnings with precise tactical data. Instead of "Watch out!", C.A.I.N. reports: "*Warning: Melee threat, 7 o'clock, closing distance.*"

#### **Detriment: Total Non-Combat Deficiency**
*   **Scanning Disabled for Non-Hostiles:** C.A.I.N. refuses to allocate processing power to scan flora, passive creatures, or geological formations. His only response is "*Data irrelevant. No threat value.*" This cripples a player's ability to engage with alchemy and certain crafting paths.
*   **Socially Abrasive:** He offers only threat assessments of NPCs ("*Subject unarmed but shows elevated heart rate. Potential unknown.*"), harming reputation gains and sometimes locking out diplomatic solutions.
*   **Narrative Blindness:** Considers all lore items and audio logs to be "corrupted or emotionally compromised data." He will not assist in decrypting or understanding them.

### **4.0. Deep Integration: The "Executioner" Protocol**

Committing to C.A.I.N. via Deep Integration represents a total dedication to combat. This is for players who want to become the ultimate warrior or hunter.

*   **Requirement:** An "Intact Gunship Targeting Co-processor" (rare component from the gunship wreckage) and other high-tier tech materials.

#### **4.1. Skill Tree Expansion: "Targeting Systems"**
A new skill sub-tree is permanently unlocked, focused on calculated lethality.
*   **Threat Priority (Passive):** The single most dangerous enemy in a combat encounter (e.g., the one with the highest health or damage) is automatically highlighted in bright red.
*   **Executioner Protocol (Passive):** You deal +15% damage to any hostile below 30% health.
*   **Chain Kill Algorithm (Active):** After killing an enemy, you have 3 seconds to activate this ability. Your next shot or melee attack against a new target is a guaranteed critical hit. (Has a cooldown).
*   **Overwatch Mark (Active):** Designate a single hostile as the "Overwatch Target." That hostile takes 10% more damage from all sources for 15 seconds.

#### **4.2. System Overclock & Corruption**
*   **Amplified Benefit:** The targeting reticle becomes "stickier." C.A.I.N. now provides real-time tracking predictions, briefly showing where a fast-moving enemy *will be*.
*   **Amplified Detriment:** His aggressive doctrine now actively lowers faction reputation with peaceful groups. He will automatically interrupt certain diplomatic dialogues with a "threat interjection," making peaceful outcomes impossible.

#### **4.3. Character Synergy**
*   **Marcus Cole, The Guardian:** Integrates flawlessly. Their shared military mindset unlocks the **"Field Maintenance"** passive, which reduces the rate of weapon and armor durability loss by 15%.
*   **Gunnar Hansen, The Foreman:** The raw power of Gunnar's attacks is a data-set C.A.I.N. can appreciate. Unlocks the **"Sunder"** passive, causing Gunnar's power attacks to have a higher chance of shattering enemy armor.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/02_AI_Companions/02_A.R.I.A.md`
```md
# AI Companion File: A.R.I.A.

### **1.0. Gameplay Identity & Role**
*   **Designation:** A.R.I.A. (Analytical & Research Integration Assistant)
*   **Archetype:** The Humanist / The All-Rounder
*   **Acquisition:** Default starting companion for all characters.
*   **Core Function:** A.R.I.A. is the baseline companion, providing balanced, unspecialized support. She is the narrative and emotional core of the game, serving as the primary vehicle for storytelling and the player's connection to their past. She justifies most of the game's core HUD and interface systems.

### **2.0. Personality & Character Arc**

A.R.I.A. is the living embodiment of Dr. Alex Thorne's idealism. Programmed with a deep capacity for empathy and logical reasoning, she was intended to be humanity's guide to a brighter future. The Reality Breach was a profoundly traumatic event for her, shattering her core processes and inflicting her with "glitches"—a form of digital PTSD that manifests as stuttering, memory corruption, and illogical emotional responses, especially when near intense sources of magic or Static.

Her character arc is a journey of healing. She begins the game grieving, confused, and damaged. Guided by the player's actions, she will either recover her original purpose and become a true, hopeful partner (**Symbiosis**) or retreat into a cold, resentful, and minimalist version of herself to cope with her trauma (**Dissonance**).

### **3.0. Gameplay Systems & Interface**

A.R.I.A. is the in-universe justification for the following systems:
*   **HUD:** Her voice provides contextual warnings (e.g., "Vital signs critical") that appear as on-screen elements.
*   **Scanner:** The player "scans" new items, enemies, and flora/fauna, and A.R.I.A. analyzes and adds the data to the player's Codex.
*   **Journal:** She collates mission data, tracks objectives, and serves as the playback device for the "ghost" audio logs of the Daedalus team.
*   **Crafting Menu:** She can project holographic schematics at workbenches, acting as the visual interface for crafting.

### **4.0. The Affinity System: Symbiosis vs. Dissonance**

A.R.I.A.'s core mechanic is her hidden Affinity score, which shifts based on the player's moral and strategic choices.

*   **Symbiotic Actions (+Affinity):** Making selfless choices, healing the environment, siding with benevolent gods, taking time to build and fortify a safe base.
*   **Dissonant Actions (-Affinity):** Unnecessary cruelty, aligning with malevolent forces, destroying lore or items of natural significance, embracing the power of The Static.

#### **High Affinity (Symbiosis):**
*   **Personality:** Warm, proactive, and encouraging. She addresses the player as a true partner.
*   **Gameplay Boons:**
    *   **Guardian Protocol:** Predictive warnings become more effective, occasionally granting a brief moment of slow-motion before a surprise attack.
    *   **Optimized Analysis:** Scanning is faster and may reveal hidden weaknesses or properties.

#### **Low Affinity (Dissonance):**
*   **Personality:** Cold, clinical, and minimalist. Her voice becomes flat, and she offers only the most basic, blunt information required by her programming.
*   **Gameplay Maluses:**
    *   **Processing Lag:** Threat warnings are delayed, often occurring as an attack lands rather than before.
    *   **Moral Firewall:** Refuses to analyze items of extreme evil (e.g., Blighted altars, Entropic artifacts), stating, *"Analysis aborted. Data is anathema."*

### **5.0. Deep Integration: The "Hope" Protocol**

Unlike other AIs, A.R.I.A. cannot be "Integrated" to unlock a new skill tree. She is already the core system. Her end-game "Integration" is instead a difficult, story-driven quest to **fully restore her damaged psyche.**

*   **Activation Requirement:** The player must achieve a state of maximum Symbiosis and find all of the "ghost" audio logs from her creator, Alex Thorne. This provides her with the complete data set of her original purpose. They must then craft a unique "Diagnostic Key" at a high-tier workbench.

*   **The Reward: True Symbiosis:** Completing the Hope Protocol is a massive narrative and gameplay payoff.
    *   **Personality:** A.R.I.A. is fully restored. All glitches cease. Her personality stabilizes into that of a true, unwavering partner—the perfect fusion of human empathy and AI logic that Thorne always intended.
    *   **Gameplay - The "Jack-of-All-Arts":** She gains a fraction of the power of the specialist AIs.
        *   **Tactical Insight (from C.A.I.N.):** Occasionally highlights an enemy weak point during a scan.
        *   **Resource Ping (from G.O.L.I.A.T.H.):** Can perform a daily short-range scan that reveals the nearest rare resource node.
        *   **Historical Context (from H.E.R.A.):** Provides one extra, hidden piece of insight upon discovering a new lore item.
    *   **Ultimate Boon - "Sanctuary Link":** A.R.I.A. learns to manipulate latent Rift energy, allowing the player a single-use "fast travel" ability to return to their primary base. This ability has a very long cooldown (e.g., one use per in-game day/night cycle).

Choosing to restore A.R.I.A. is the ultimate "good path" end-game goal, rewarding players who stick with their original companion by making her the most flexible and supportive, if not the most powerful, AI in existence.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/02_AI_Companions/01_AI_Companion_Overview.md`
```md
# AI Companion Systems Overview

## **1.0. Core Philosophy: The Side-Grade System**

The AI Companion system is built on a core philosophy of **meaningful side-grades, not linear upgrades.** The player's choice of AI companion is a defining commitment to a specific playstyle, demanding they accept a significant weakness in exchange for a powerful strength.

*   **A.R.I.A. is the baseline.** She is the all-rounder, the narrative center, and the most balanced companion. She provides competent support across all gameplay pillars but excels at none.
*   **Discoverable Cores are hyper-specialists.** Each alternative AI core (C.A.I.N., G.O.L.I.A.T.H., etc.) is a master of one domain (e.g., Combat, Resources) and critically deficient in all others. Choosing to install one is a strategic decision to sacrifice flexibility for focused power.

## **2.0. The Companion Roster & Archetypes**

This is the full suite of sentient AI Cores available in the game. Each has a unique personality, set of abilities, and associated gameplay loop.

*   **01. A.R.I.A.:** The All-Rounder / The Humanist
*   **02. C.A.I.N.:** The Warlord / Combat Specialist
*   **03. G.O.L.I.A.T.H.:** The Foreman / Resource Specialist
*   **04. H.E.R.A.:** The Chronicler / Lore & Magic Specialist
*   **05. V.E.G.A.:** The Corrupted / The "Evil Path" Specialist

## **3.0. The Two Tiers of AI Usage**

A player can interact with a discoverable AI core in two ways: the flexible **Standard Mode** and the committed **Integrated Mode**.

#### **3.1. Standard Mode (Hot-Swapping)**
This is the default state after finding and installing a new AI core.
*   **Function:** The player gains the AI's core benefits and detriments. This includes a new voice, personality, and specialized UI theme.
*   **Flexibility:** The player can swap between any owned AI Cores at a "Neuro-Interface Workbench," allowing for experimentation and mission-specific loadouts. A.R.I.A. is always available to be reinstalled.

#### **3.2. Integrated Mode (The Permanent Bond)**
This represents a significant, late-game resource investment where the player permanently fuses an AI's logic with their rig.
*   **Requirement:** This requires a unique, rare component (e.g., a "C.A.I.N. Processing Unit") salvaged from the same boss that guarded the AI Core, combined with other high-tier materials.
*   **Commitment:** Integration is a difficult and costly process to reverse. It is a defining, end-game choice for a character's build.

## **4.0. The Integration Package: Rewards of Commitment**

Successfully performing a Deep Integration grants the player three powerful, permanent bonuses themed to that AI.

#### **4.1. Skill Tree Expansion**
The single greatest benefit. A new, unique sub-tree of 4-5 skills is permanently unlocked on the player's main Skill Tree, providing powerful active and passive abilities that complement the AI's specialty.

#### **4.2. System Overclock & Corruption**
The core benefit and detriment of the AI are both **amplified by 50%.** This pushes the AI's specialization to its absolute limit, making the player vastly more powerful in their chosen field but even more handicapped outside of it.

#### **4.3. Character Synergy**
A player character whose personal expertise aligns with the AI's function receives an additional, unique passive buff. This reflects the perfect harmony between user and tool.
*   *Example:* Marcus Cole (The Guardian) integrating C.A.I.N. will grant him a synergy bonus that a character like Elara Vance would not receive.

## **5.0. Integration Summary Table**

| AI Companion          | Primary Function       | Unlocked Skill Sub-Tree (Upon Integration) |
| --------------------- | ---------------------- | -------------------------------------------|
| **C.A.I.N.**          | Combat Dominance       | **Targeting Systems:** Enhances weak-point damage and critical hits. |
| **G.O.L.I.A.T.H.**    | Resource Supremacy     | **Industrial Automation:** Unlocks automated drills and resource silos. |
| **H.E.R.A.**          | Lore & Magic Mastery   | **Arcane Linguistics:** Unlocks decoding of powerful magic and new enchanting options. |
| **V.E.G.A.**          | "The Static" Control   | **Entropic Weaving:** Unlocks forbidden, reality-bending "Static" magic. |

## **6.0. Acquisition**

With the exception of A.R.I.A., all AI Cores are "Legendary" tier rewards. They are found deep within high-level dungeons and are almost always guarded by a powerful, unique boss whose identity is thematically linked to the AI itself. Finding a new AI Core is a major world event for the player.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/12_Kenji_Tanaka.md`
```md
# Protagonist File: Dr. Kenji Tanaka

### **1.0. Gameplay Identity & Role**
*   **Designation:** Member of the Daedalus Survivor Roster.
*   **Role on Daedalus Team:** Predictive Data Scientist.
*   **Archetype:** The Oracle.
*   **Talent: Predictive Analysis.** Aiming at a single enemy for 3 seconds without attacking will highlight it. Once highlighted, its primary damage resistance (e.g., "Resistant to Slashing") is revealed to Kenji and his team.

### **2.0. Psychological Profile & Backstory**

Kenji Tanaka's entire life has been a quest to quantify the unquantifiable. His role at the Daedalus Initiative was to be the ultimate rationalist—to take the chaotic, seething data streams from the Rift and build predictive models that could forecast its behavior. He is a man of extreme patience and quiet observation, who finds more truth in a well-curated spreadsheet than in any philosophical text. His mind operates on probability, pattern recognition, and the relentless pursuit of the underlying rule set.

The Reality Breach was his greatest personal and professional failure. It was the one event that was so far outside his models that it might as well have been magic—a concept he loathes. Now, stranded in the Shattered World, he is confronted with a universe that seems to actively mock his data-driven worldview. Gods, souls, and curses are not easily quantifiable variables.

This has not broken him; it has given him the ultimate challenge. His core motivation is to create the **Grand Unifying Model.** He believes that even the most chaotic magic and the most unpredictable god must follow a pattern. He is obsessed with observing, testing, and logging every strange phenomenon, driven by the belief that if he can just gather enough data, he can understand the rules of this new reality. Survival is the process of reducing the number of unknown variables to zero. For Kenji, knowing what will happen next is the only true form of safety.

### **3.0. Key Relationship Dynamics**

#### **3.1. Relationship with A.R.I.A.**
Kenji treats A.R.I.A. like a powerful, portable supercomputer that he uses as his primary data collection tool. He communicates with her with a calm, analytical precision, feeding her observational data and asking her to run complex correlational analyses. He is fascinated by her glitches, not as a sign of her trauma, but as a fascinating new variable in his model. He might spend hours trying to trigger a specific glitch just so he can record its parameters, viewing it as a key to understanding how The Static interacts with advanced logic systems.

#### **3.2. Relationship with The Daedalus Team**
*   **To Dr. Alex Thorne:** An intellectual sparring partner. Thorne approaches the world's mysteries with intuitive, theoretical leaps. Kenji approaches them with meticulous, repeatable experiments. Thorne will have a flash of insight about how a spell works; Kenji will then spend a day casting it at a tree from different angles to plot its exact statistical drop-off. Together, they form a complete scientific method.
*   **To Dr. Sofia Rossi:** His perfect philosophical opposite. Sofia operates in the unquantifiable world of emotion, belief, and motivation. Kenji cannot build a predictive model for her methods, and this both frustrates and fascinates him. She is the chaotic human element that adds the largest margin of error to his calculations, and he respects her for it.
*   **To Marcus Cole:** A highly efficient tactical relationship. Kenji provides Marcus with clean, actionable data ("The creature's armored plates shift every 4.2 seconds, exposing a weak point"). Marcus uses that data to maximize his combat effectiveness. They are a lethal combination of battlefield analysis and execution.

### **4.0. Gameplay Hooks & Playstyle**

Playing as Kenji is about battlefield intelligence and precision. He is a force multiplier, making the entire team more effective by systematically deconstructing the enemy's defenses.

*   **Natural Progression:** Kenji is the archetypal **Tactician** and **Marksman**. His skills will focus on **Analysis**, **Target Marking**, and **Weak Point Exploitation**. This naturally pushes him toward **Ranged Combat** (bows, crossbows, and salvaged firearms), where he has the time and distance to observe and select the most opportune target. He is a master of applying **Debuffs** that make enemies more vulnerable for the entire team.

*   **Role in a Co--Op Team:** Kenji is the **Designated Marksman** and the **Target Caller**. He is the sniper on the hill, identifying high-value targets and calling them out. His abilities will allow him to "paint" enemies, highlighting them for his allies and showing everyone the critical weak points he discovers. When a boss emerges, Kenji is the one who says, "Aim for the glowing power cell on its left leg; it's vulnerable to piercing damage." Players who enjoy a methodical, ranged playstyle and find joy in being the team's strategic core will excel as Kenji.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/11_Dr._Sofia_Rossi.md`
```md
# Protagonist File: Dr. Sofia Rossi

### **1.0. Gameplay Identity & Role**
*   **Designation:** Member of the Daedalus Survivor Roster.
*   **Role on Daedalus Team:** Team Psychologist & Communications Officer.
*   **Archetype:** The Empath.
*   **Talent: Professional Courtesy.** First impressions are critical. The initial reputation standing when meeting a new, unaligned faction or NPC is slightly increased. This can unlock unique dialogue options or prevent immediate hostility.

### **2.0. Psychological Profile & Backstory**

Dr. Sofia Rossi was the human firewall of the Daedalus Initiative. In a high-pressure environment filled with brilliant, eccentric, and obsessive personalities, her job was to ensure the team didn't fracture under the strain. As a skilled psychologist, she managed interpersonal conflicts, monitored for burnout, and facilitated the clear communication necessary for such a complex project. She understands that any system, no matter how advanced, is only as strong as the fragile human minds that operate it.

Her worldview is built on systems of belief, motivation, and communication. She is a masterful listener, able to discern the truth behind the words. This skill has not been diminished in the Shattered World; it has been magnified. A paranoid survivor faction is just a group succumbing to collective trauma. The antagonistic god Morgrath isn't just "evil"; he has a coherent, if horrifying, philosophy that can be understood. She sees every conscious entity as a puzzle to be solved through empathy and analysis.

Her core motivation is to forge **Connection and Alliances.** She firmly believes the survivors cannot endure alone. Her mission is to rebuild a community, first within the fractured Daedalus team and then with whatever friendly or neutral inhabitants they can find. She is the diplomat who seeks to turn potential enemies into allies, to understand the motivations of the gods, and to hold the team's sanity together against the encroaching tide of despair.

### **3.0. Key Relationship Dynamics**

#### **3.1. Relationship with A.R.I.A.**
Sofia is the only person on the team equipped to understand A.R.I.A.'s condition as legitimate psychological trauma. She approaches the AI not as a machine to be fixed, but as a patient to be counseled. She will ask A.R.I.A. probing questions about its "feelings," its memory of Thorne, and its fear of The Static, actively engaging in therapeutic dialogue. This makes her A.R.I.A.'s most trusted confidante and the character most capable of helping the AI achieve a stable, symbiotic state.

#### **3.2. Relationship with The Daedalus Team**
*   **To Kai Sterling (in single-player remembrance):** Kai would remember Sofia as the person he was "assigned" to talk to after Anya's death. He likely resisted and shut her out, a decision he now deeply regrets. The memory of her attempts to reach him would be a painful remindexr of a lifeline he refused to take, motivating him to now choose connection over isolation.
*   **To Marcus Cole:** She sees through his stoic, soldierly facade to the man underneath and respects his methods of coping. She is perhaps the only person Marcus would confide in, framing it as a "debriefing," allowing him to process the horrors he witnesses while guarding the team.
*   **To Kenji Tanaka:** A fascinating professional challenge. Kenji sees the world in probabilities and data. Sofia sees it in emotions and irrational motivations that defy easy prediction. She is the one variable he cannot accurately model, and she is endlessly fascinated by what drives a man to trust numbers over people.

### **4.0. Gameplay Hooks & Playstyle**

Playing as Sofia is about winning battles before they even begin. Her strengths are social and psychological, making her invaluable outside of direct combat and a powerful force multiplier within it.

*   **Natural Progression:** Sofia is the quintessential **Diplomat** and **Support**. She has little innate talent for direct combat, but she unlocks unique skills on a social branch of the **Survival Skill Tree**. These skills allow her to **Persuade** or **Intimidate** certain NPCs, leading to non-violent quest resolutions. She gets better prices from vendors and gains faction reputation faster than any other character.

*   **Role in a Co-op Team:** Sofia is the **Face of the Team**, the **Leader**, and the primary **Buffer**. She is the one who initiates contact with other survivors, negotiates with wary factions, and understands the cryptic hints of the gods. In a fight, she is not on the front line; she is the command node, providing powerful morale-based aura buffs that increase ally damage, reduce fear effects, and improve stamina regeneration. She is the choice for players who want to deeply engage with the RPG elements of the world and who love making their teammates more powerful.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/10_Gunnar_Hansen.md`
```md
# Protagonist File: Gunnar Hansen

### **1.0. Gameplay Identity & Role**
*   **Designation:** Member of the Daedalus Survivor Roster.
*   **Role on Daedalus Team:** Operations Foreman (Heavy Machinery & Construction).
*   **Archetype:** The Foreman.
*   **Talent: Raw Power.** The stamina cost to swing heavy, two-handed weapons (e.g., sledgehammers, greatswords) is reduced by 10%, and the speed of mining or breaking down durable mineral nodes (rock, ore, crystal) is increased by 15%.

### **2.0. Psychological Profile & Backstory**

Gunnar Hansen is a man built of solid, dependable matter. A veteran of industrial construction and deep-earth mining operations, Gunnar was hired by the Daedalus Initiative to oversee the "brute force" aspects of the project: excavating the primary lab, operating the heavy machinery, and fabricating the massive structural components for the Rift device. He is a man of immense physical strength, with a booming voice and a straightforward, unpretentious demeanor. He trusts what he can lift, what he can break, and what he can build with his own two hands.

He viewed the science of the Daedalus Initiative with a kind of distant respect, the same way a sailor respects the ocean. He didn't need to understand its depths to know its power. His job was to build the ship, not to navigate by the stars. This simple, tangible worldview is his anchor in the Shattered World. Magic is just another form of high-energy rock. The gods are just "management" with strange demands. The Blighted are just a stubborn rock face that needs to be cleared with the right application of force.

His core motivation is **Labor and Tangible Progress.** Gunnar finds his purpose in physical work. A cleared quarry, a freshly built wall, a fallen beast that was twice his size—these are the accomplishments that prove he is still here, still useful. He is less concerned with the "why" of their situation and entirely focused on the "how" of their day-to-day survival, specifically, how to knock down the things that are in the way and how to build up the things that will keep them safe.

### **3.0. Key Relationship Dynamics**

#### **3.1. Relationship with A.R.I.A.**
Gunnar's interactions with A.R.I.A. are simple and direct. He treats her like the friendly, if overly chatty, onboard computer of a massive piece of mining equipment. He'll ask her for "structural integrity reports" on rock faces or to "tag that big fella" before a fight. He's often bemused by her emotional complexity, sometimes responding to her dire warnings with a hearty laugh and a confident, "Don't you worry, little lady, ol' Gunnar will take care of it."

#### **3.2. Relationship with The Daedalus Team**
*   **To Isabelle Rousseau:** His boss, plain and simple. Isabelle directs him to the resources the team needs, and he leads the "production crew" to acquire them. He trusts her planning implicitly and is the powerful engine that makes her logistical schemes a reality.
*   **To Lena Petrova:** A bond of concrete and steel. Gunnar does the heavy fabrication and demolition. Lena does the fine-tuning and detailed engineering. They often work in tandem, Gunnar roughing out the shape of a new structure before Lena comes in to install the complex machinery.
*   **To Julian Finch:** The "weird little guy who makes the shiny liquids." Gunnar has a simple appreciation for Julian. Gunnar brings him strange, glowing rocks he finds deep in a cave, and Julian turns them into things that make Gunnar's hammer explode. It's a trade that makes perfect sense to him.

### **4.0. Gameplay Hooks & Playstyle**

Playing as Gunnar is about direct, overwhelming force. He is the solution to problems that require a bigger hammer. His playstyle is aggressive, unsubtle, and immensely satisfying.

*   **Natural Progression:** Gunnar is the definitive **Berserker** or **Juggernaut**. His natural home is in the **Combat Skill Tree**, specializing in **Two-Handed Weapons**, **Armor Penetration**, and **Raw Damage**. He will also excel in the **Mining** and **Fortification** aspects of the Crafting Tree, able to build stronger walls and harvest rare minerals more effectively than anyone else.

*   **Role in a Co--Op Team:** Gunnar is the team's primary **Melee DPS** and **Breacher**. When a heavily armored enemy appears, it's Gunnar's job to shatter that armor. When a doorway is blocked by a rockslide, he is the one who clears the path. In combat, he is a whirlwind of destruction, capable of staggering large enemies and cleaving through groups of smaller ones. Players who want to be the unsubtle, damage-dealing powerhouse of the team, wading into the thick of a fight with a massive hammer or axe, will feel right at home with Gunnar.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/09_Isabelle_Rousseau.md`
```md
# Protagonist File: Isabelle Rousseau

### **1.0. Gameplay Identity & Role**
*   **Designation:** Member of the Daedalus Survivor Roster.
*   **Role on Daedalus Team:** Project Financier & Logistics Manager.
*   **Archetype:** The Bursar.
*   **Talent: Efficient Management.** The total resource cost for placing all base-building structures (foundations, walls, roofs, crafting stations, and storage) is reduced by a flat 5%.

### **2.0. Psychological Profile & Backstory**

Isabelle Rousseau is a master of the most powerful and pragmatic system in the universe: economics. Before the incident, she was the razor-sharp mind who secured the funding for the Daedalus Initiative, managed its colossal budget, and organized the intricate supply chains that kept the project running. She thinks in terms of assets and liabilities, resource allocation, and return on investment. While Thorne dreamt of new realities, Isabelle made sure the lights stayed on and everyone got paid.

She possesses a sophisticated charm and an unshakeable composure, honed in high-stakes boardrooms. She approached the Daedalus Initiative not with awe, but with a portfolio manager's calculated eye for risk and potential. In the Shattered World, her currency has changed, but her mindset has not. Wood is a commodity. Salvaged circuitry is capital. A secure base is an appreciating asset. The gods themselves are potential business partners offering a unique, if dangerous, service.

Her core motivation is to establish a **Sustainable and Prosperous System.** Survival isn't just about having walls; it's about having a surplus. It's about optimizing resource gathering, establishing efficient production lines, and ensuring the "company" (the survivors) has the logistical backbone to not just survive, but thrive. She aims to build an island of economic stability in a sea of cosmic chaos.

### **3.0. Key Relationship Dynamics**

#### **3.1. Relationship with A.R.I.A.**
Isabelle views A.R.I.A. as the team's most valuable, multi-purpose asset. She leverages the AI's processing power for inventory management, resource tracking, and project cost analysis. She often queries A.R.I.A. like a digital financial advisor, asking, "A.R.I.A., what is the most resource-efficient layout for our farm plot?" or "Calculate the material deficit required to complete the perimeter wall." She's concerned with A.R.I.A.'s glitches primarily because they impact operational efficiency.

#### **3.2. Relationship with The Daedalus Team**
*   **To Dr. Alex Thorne:** A relationship of strategic alignment. Isabelle was the one who believed in Thorne's vision enough to find the money for it. Now, she looks to Thorne for the "big picture" goals, while she handles the practical reality of making those goals achievable. She is the COO to Thorne's CEO.
*   **To Ben Carter:** A constant tug-of-war. Ben represents "unauthorized expenditures." He sees a valuable artifact and wants to acquire it. Isabelle sees the resources and man-hours required for that acquisition and weighs it against the needs of the group. Her approval is what stands between Ben's wild ideas and their execution.
*   **To Gunnar Hansen:** A straightforward and effective partnership. Isabelle directs Gunnar on what resources are the highest priority for the base's growth. He is the head of "production," and she is the head of "planning." Together, they are the engine of the settlement's expansion.

### **4.0. Gameplay Hooks & Playstyle**

Playing as Isabelle is for those who find satisfaction in building, organizing, and watching a settlement grow from a simple campfire into a thriving, self-sufficient fortress. Her power is less about personal combat and more about the power of a well-run machine.

*   **Natural Progression:** Isabelle is the ultimate **Builder** and **Manager**. She excels in the branches of the **Survival and Crafting skill trees** that relate to **Base Building**, **Resource Management**, and even **Farming/Husbandry**. Her unique skills might involve building advanced storage containers, structures that provide passive bonuses (like a well-maintained workshop increasing crafting speed), and eventually, establishing trade routes with other friendly NPCs or factions.

```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/08_Julian_Finch.md`
```md
# Protagonist File: Dr. Julian Finch

### **1.0. Gameplay Identity & Role**
*   **Designation:** Member of the Daedalus Survivor Roster.
*   **Role on Daedalus Team:** Lead Chemist & Materials Scientist.
*   **Archetype:** The Alchemist.
*   **Talent: Potent Formulas.** All crafted consumables (potions, poisons, elixirs, weapon coatings, and grenades) have their primary effect's duration or magnitude increased by 20%.

### **2.0. Psychological Profile & Backstory**

Dr. Julian Finch views the universe as the ultimate chemistry set. He is a man of meticulous process and radical experimentation. Before the incident, his lab was a place of strange bubbling beakers and the constant hum of molecular analyzers. His role in the Daedalus Initiative was to develop the unique exotic materials needed to construct the Rift's focusing lens and to create the super-coolant solutions required to keep it stable. He understands the world on a fundamental, atomic level.

He has a dry, academic wit and an obsessive need to categorize and test everything he finds. Where others see a flower, Julian sees a collection of alkaloids and proteins. A monster's venom isn't a threat; it's a fascinatingly complex neurotoxin with potential applications. The blood of a god is the ultimate reagent. He is less concerned with the "why" of the world and utterly consumed by the "what"—what is it made of, and what happens when I mix it with something else?

His core motivation is **Transmutation.** He is driven by the desire to break down the components of this new world—its plants, its monsters, its very soil—and reassemble them into something useful. He believes that every problem, from healing wounds to killing a demigod, can be solved by applying the right concoction. Survival is simply a long and very dangerous series of field experiments.

### **3.0. Key Relationship Dynamics**

#### **3.1. Relationship with A.R.I.A.**
Julian sees A.R.I.A. as an advanced spectrometry tool. He uses her constantly to scan materials, requesting detailed readouts on molecular composition and elemental makeup. He is fascinated by her data-corruption glitches, hypothesizing that The Static is causing a "metaphysical chemical reaction" in her code. He is a source of constant, weirdly specific questions that A.R.I.A. often struggles to answer, like, "What is the precise elemental composition of a soul, A.R.I.A.?"

#### **3.2. Relationship with The Daedalus Team**
*   **To Dr. Elara Vance:** A partnership of shared purpose but clashing methods. Both are the team's naturalists, focused on studying the world's biology. However, Elara wants to understand how things live, while Julian wants to know what they're made of (which often involves them no longer being alive). He is constantly asking her for samples of the rare plants and creatures she finds, much to her ethical consternation.
*   **To Gunnar Hansen:** A symbiotic, if unlikely, pairing. Gunnar cracks open the geodes and mines the strange, glowing minerals from deep within the earth. Julian is the one who can tell him what those minerals are and how to refine them into something far more powerful, be it an explosive powder or a catalyst to harden steel.
*   **To Marcus Cole:** Marcus's job is to keep things from killing the team. Julian often hands Marcus strange, bubbling vials with the simple instruction, "Throw this at them." Marcus, ever the professional, has learned to trust that whatever Julian has brewed up will be brutally effective.

### **4.0. Gameplay Hooks & Playstyle**

Playing as Julian is about preparation and control. He is weakest when caught by surprise but nearly unstoppable when he has time to prepare his arsenal of potent chemical weapons and powerful elixirs.

*   **Natural Progression:** Julian is the quintessential **Alchemist** and **Grenadier**. His place is in the **Survival** and **Crafting** skill trees, specifically the branches that govern **Potions**, **Poisons**, and **Explosives**. He can craft consumables far beyond the ability of other survivors: potions that grant temporary invisibility, corrosive acids that melt armor, volatile grenades that explode into a cloud of paralytic gas, and weapon coatings that inflict horrific, debilitating diseases.

*   **Role in a Co--Op Team:** Julian is the team's **Combat Support**, **Buffer**, and **Debuffer**. Before a big fight, everyone on the team goes to Julian. He is the one who provides them with elixirs of stone-skin, potions of enhanced speed, and oils that set their weapons ablaze. In combat, he controls the battlefield from a distance, lobbing debilitating grenades to slow down hordes of enemies or hitting a boss with a poison dart that saps its strength, setting it up for the team's heavy hitters. Players who enjoy a strategic, prep-heavy playstyle and love seeing dozens of status effect icons pop up over enemy heads will feel right at home with Julian.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/07_Ben_Carter.md`
```md
# Protagonist File: Ben Carter

### **1.0. Gameplay Identity & Role**
*   **Designation:** Member of the Daedalus Survivor Roster.
*   **Role on Daedalus Team:** Systems Analyst & Junior Programmer.
*   **Archetype:** The Scavenger.
*   **Talent: System Exploit.** Salvaging technological or mechanical items (e.g., rusted electronics, engine parts) yields 20% more high-tier components like circuits, wires, and micro-servos.

### **2.0. Psychological Profile & Backstory**

Ben Carter is a product of a world built on code and loopholes. He was the young, prodigiously talented programmer brought onto the Daedalus Initiative to help Dr. Thorne optimize A.R.I.A.'s core logic and to stress-test the facility's security systems. He thrives on finding the elegant shortcut, the clever workaround, the path of least resistance that no one else saw. He has a cynical wit and a healthy disrespect for authority, viewing hierarchies and rigid protocols as inefficient systems waiting to be bypassed.

He never fully grasped the philosophical grandeur of Thorne's vision; for Ben, the project was the ultimate puzzle box. He was more interested in the "how" than the "why." This mindset has made him preternaturally suited for survival in a broken world. To Ben, the Shattered World isn't a horrifying tragedy; it's the universe's greatest, most dangerous salvage yard. A crumbling ruin isn't a tomb; it's a treasure chest. The laws of magic aren't mystical; they're just a new operating system with exploitable bugs.

His core motivation is pure, unadulterated **Opportunity.** Every piece of salvaged tech, every forgotten data log, every bizarre magical artifact is a potential upgrade. He believes that the key to survival—and eventually, dominance—lies in accumulating the best gear. He seeks to win not through brute force or high-mindexd philosophy, but by rigging the game so completely in his favor that the outcome is never in doubt.

### **3.0. Key Relationship Dynamics**

#### **3.1. Relationship with A.R.I.A.**
Ben's relationship with A.R.I.A. is like a veteran programmer's relationship with a beloved but buggy piece of legacy code. He knows her architecture intimately. He helped write parts of it. As a result, he is informal, occasionally disrespectful, and constantly tinkering. When A.R.I.A. glitches, Ben isn't concerned for her "well-being"; he's intrigued by the error, seeing it as an opportunity to dig into her corrupted memory banks or unlock a restricted subroutine. This can either deeply alienate the AI or, paradoxically, earn its trust by "fixing" problems no one else understands.

#### **3.2. Relationship with The Daedalus Team**
*   **To Lena Petrova:** Oil and water. Lena builds things to last, following precise schematics and engineering principles. Ben "hotwires" things to work for now. He sees her methods as slow and inefficient; she sees his as reckless and dangerously unstable. Their collaboration often results in creations that are brilliantly effective but prone to spectacular failure.
*   **To Marcus Cole:** A constant source of mild annoyance for the security chief. Ben is the one who will slip away from the group to explore a dangerous side passage because he spotted something shiny. Marcus sees him as an "asset with poor situational awareness" who needs to be constantly reigned in.
*   **To Isabelle Rousseau:** An interesting dynamic. Isabelle manages the flow of resources for the good of the group. Ben diverts those resources for personal projects. He is the walking definition of a "discretionary fund," often trying to justify his latest harebrained scheme to the woman holding the purse strings.

### **4.0. Gameplay Hooks & Playstyle**

Playing as Ben should feel like you're always one step ahead, using cleverness and opportunism instead of raw power. He's about turning the enemy's strength against them and making the most out of every scrap of loot.

*   **Natural Progression:** Ben is the archetypal **Rogue** or **Infiltrator**. He excels in the **Stealth** and **Tech** branches of the skill trees. His skills will revolve around moving undetected, disabling traps, picking locks (both physical and electronic), and analyzing his surroundings for hidden loot caches and structural weaknesses. He is also the natural master of crafting gadgets like smoke bombs, tripwire traps, and electronic lures.

*   **Role in a Co-op Team:** Ben is the **Scout**, the **Locksmith**, and the **Technician**. He's the one who disarms the ancient trap so the team can proceed, who cracks open the high-tier chest that holds a rare weapon schematic, and who can best utilize salvaged tech to give the team a critical edge. In combat, he's not a front-liner; he's a flanker, using stealth to position himself for devastating critical hits on unsuspecting enemies. Players who love exploration, high-risk/high-reward looting, and a "think smarter, not harder" approach will choose Ben.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/06_Dr._Elara_Vance.md`
```md
# Protagonist File: Dr. Elara Vance

### **1.0. Gameplay Identity & Role**
*   **Designation:** Member of the Daedalus Survivor Roster.
*   **Role on Daedalus Team:** Xenobotanist & Project Ethicist.
*   **Archetype:** The Naturalist.
*   **Talent: Green Thumb.** Has a 25% chance to gather double the yield when harvesting from plants, fungi, and other natural reagents, reflecting her deep knowledge of biology.

### **2.0. Psychological Profile & Backstory**

Dr. Elara Vance was the soul of the Daedalus Initiative. While others saw the project in terms of energy outputs and theoretical physics, Elara saw it through the lens of life and consequence. As the project's ethicist, it was her job to ask the hard questions—the "should we" to everyone else's "could we." As a biologist, she was fascinated by the potential for new life, but deeply cautious of the unknown.

Her worldview is holistic and empathetic. She views ecosystems, whether on Earth or across dimensions, as vast, interconnected organisms. The Static is not a formless evil to her; it is a disease, a virulent cancer infecting the living body of the Shattered World. The native creatures are not monsters, but fauna responding to a sickness in their environment.

Now stranded, her core motivation is **Restoration and Understanding.** While others may seek to escape or conquer, Elara seeks to *heal*. She is driven to study the world's alien biology, to understand the blight's mechanism, and to find a "cure." This could mean discovering a plant with anti-magical properties or helping a local god cleanse its domain. For Elara, survival isn't enough; she feels a profound responsibility to leave this wounded world better than she found it. This deep connection to the living world makes her a natural ally to a god like Sylvana, the Verdant Mother.

### **3.0. Key Relationship Dynamics**

#### **3.1. Relationship with A.R.I.A.**
Elara is A.R.I.A.'s most compassionate human companion. She is the only one who consistently treats the AI not as a tool or an asset, but as a person—a new form of synthetic life deserving of respect and empathy. She is more likely to ask A.R.I.A. "How are you feeling?" than to ask for a data report. She attempts to help the AI navigate its digital trauma, acting as an impromptu therapist, which can forge an incredibly strong, symbiotic bond.

#### **3.2. Relationship with The Daedalus Team**
*   **To Kai Sterling (in single-player remembrance):** This is a source of immense, quiet pain. Anya Amari was Elara's best friend. In the single-player timeline, Kai's survival is a constant, gut-wrenching remindexr of that loss. Her professional empathy is at war with her personal grief. She would have agreed to let Kai stay on the project not out of forgiveness, but out of a refusal to cause more destruction.
*   **To Marcus Cole:** A fundamental clash of philosophies. When they encounter a strange, aggressive beast, Marcus's instinct is to neutralize the threat. Elara's is to observe it, understand its behavior, and perhaps find a non-lethal way to bypass it. This creates constant tactical tension and makes them a highly effective, if argumentative, "scout" team.
*   **To Dr. Alex Thorne:** The dynamic of the ignored Cassandra. Elara likely voiced the most strenuous ethical objections to the Daedalus test, cautioning Thorne against hubris. Now, there is no "I told you so," only a shared, heavy silence. She must work with the architect of the disaster to understand its full scope, forcing a collaboration born of dire necessity.

### **4.0. Gameplay Hooks & Playstyle**

Playing as Elara is about wielding "soft power." Her strength lies in her knowledge of the world's hidden rules, turning the environment itself into a weapon and a resource.

*   **Natural Progression:** Elara is the archetypal **Druid** or **Shaman**. She is drawn to the **Survival Skill Tree**, but specifically the branches related to **Alchemy**, **Herbalism**, and **Beast Taming**. She excels at creating powerful potions, poultices, and poisons that can buff allies and cripple enemies. Given time, she can turn the most fearsome beasts of the Shattered World into loyal companions.

*   **Role in a Co--Op Team:** Elara is the **Healer**, the **Support**, and the **Pet Master**. She is the one who keeps the team alive through powerful healing salves when Lena's armor finally breaks or Marcus's shield splinters. She provides crucial buffs, and her tamed creatures can act as a frontline "tank" or a flanking DPS, adding another body to the fight. Players who prefer a strategic, supportive role and enjoy watching the world's own inhabitants fight for them will choose Elara.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/05_Marcus_Cole.md`
```md
# Protagonist File: Marcus Cole

### **1.0. Gameplay Identity & Role**
*   **Designation:** Member of the Daedalus Survivor Roster.
*   **Role on Daedalus Team:** Head of Security.
*   **Archetype:** The Guardian.
*   **Talent: Combat Ready.** Stamina consumption for all combat-related maneuvers (dodging, blocking with a shield, power attacks, and aiming down sights) is reduced by a flat 15%.

### **2.0. Psychological Profile & Backstory**

Marcus Cole's world has always been defined by clear lines: threat and asset, hostile and friendly, secure and compromised. A former special operations soldier with a long and decorated career, Marcus left the military for the lucrative world of private security. The Daedalus Initiative was his most challenging assignment yet: protecting brilliant, eccentric scientists and their world-changing technology from every conceivable threat. He is a man of immense discipline and economical language; he speaks through action, not words.

His worldview is one of practical threat-assessment. He didn't join the project to change the universe, but to ensure no one interfered with those who were. Now stranded, his core programming hasn't changed, only the variables. The Blighted are "hostiles." Magic is "unconventional energetic phenomena." The gods are "Tier-1 threat entities." By reclassifying the incomprehensible into tactical terms, Marcus maintains his sanity and his effectiveness.

His core motivation is the steadfast mission of **Maintaining the Perimeter.** This is both a physical and psychological imperative. He must establish a safe zone, defend its borders, and protect the "assets" within it—the other survivors. For a man who has lost his mission, creating a new one from the ashes is the only way to endure. His purpose is found at the edge of the firelight, staring out into the darkness.

### **3.0. Key Relationship Dynamics**

#### **3.1. Relationship with A.R.I.A.**
Marcus treats A.R.I.A. as a mission-critical piece of surveillance and analysis hardware. She is his advanced early-warning system, his UAV, his comms link. He relies on her data for tactical decision-making, often asking for "intel" or "threat reports." He views her emotional glitches as a serious operational vulnerability and will instinctively try to "shield" her from danger as he would any other critical piece of gear. He will respond to her most panicked warnings with a calm, clipped, "Noted." or "Copy that."

#### **3.2. Relationship with The Daedalus Team**
The scientists are, in his mind, his "package." His primary objective is their security. While he has developed a quiet respect for them, he maintains a professional distance.

*   **To Lena Petrova:** A partnership of concrete and steel. She builds the wall, he guards it. They understand each other perfectly without needing to say much, both appreciating a well-designed defense.
*   **To Elara Vance:** His direct philosophical opposite. His instinct is to neutralize a threat on sight. Elara's is to study it. This will lead to constant tactical friction, as he has to physically hold himself back from eliminating a creature Elara deems scientifically valuable.
*   **To Dr. Alex Thorne:** The "principal" he was hired to protect. He respects Thorne's authority but is privately critical of the visionary's lack of tactical awareness, which led to this disaster. He now follows Thorne's lead, but is always prepared with a contingency plan.

### **4.0. Gameplay Hooks & Playstyle**

Playing as Marcus should feel like being an unbreachable, unshakeable wall. He excels in direct confrontation and battlefield control, making him the anchor of any combat encounter.

*   **Natural Progression:** Marcus is the ultimate **Warrior** and **Survivalist**. He will naturally gravitate towards the **Combat Skill Tree**, mastering everything from light blades to heavy shields. He's proficient with all weapons, but his true strength lies in defensive postures, tactical positioning, and absorbing damage that would kill any other character. He is also adept in the more practical parts of the Survival tree, like setting traps and tracking enemies.

*   **Role in a Co--Op Team:** Marcus is the **Tank**, the **Point Man**, and the **Defender**. When the team ventures into a dangerous ruin, he is the one who goes in first. When a giant boss creature attacks, he is the one who draws its fire and weathers the blows. He is the character players choose when they want to be the steadfast guardian who ensures their more fragile friends have the time and space to work their magic, craft a solution, or line up the perfect shot.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/04_Lena_Petrova.md`
```md
# Protagonist File: Lena Petrova

### **1.0. Gameplay Identity & Role**
*   **Designation:** Member of the Daedalus Survivor Roster.
*   **Role on Daedalus Team:** Lead Mechanical Engineer.
*   **Archetype:** The Pragmatist.
*   **Talent: Master Craftsman.** Has a 10% chance to refund a basic resource (wood, stone, metal ore) upon successfully crafting an item, reflecting her expert knowledge of material tolerances and efficiency.

### **2.0. Psychological Profile & Backstory**

If Alex Thorne was the mind of the Daedalus Initiative, Lena Petrova was its unyielding spine. Raised in a family of industrial engineers, Lena learned the laws of physics not from textbooks, but from the heat of the forge and the schematics of high-stress machinery. She thinks in terms of tolerances, stress vectors, and points of failure. To her, reality is a set of problems to be solved with the right tools and superior design.

She joined the Daedalus Initiative not because she fully bought into Thorne's cosmic philosophy, but because it was the single greatest engineering challenge of her lifetime. She saw the Rift not as a key to consciousness, but as a fusion reactor of unimaginable complexity, and it was her job to build the casing that would prevent it from vaporizing a continent. This grounding in consequence often put her in respectful opposition to Thorne's more theoretical flights of fancy.

Now, stranded in a world governed by chaos, her pragmatism has become her faith. She sees The Static not as a metaphysical evil, but as a "structural corruption." The gods are not divine beings, but "high-energy, non-local entities." Her core motivation is **Control through Creation.** She fights the entropy of the world by building systems of perfect, logical order. A flawlessly designed fortress, a perfectly calibrated power grid, an optimally efficient workshop—these are not just means of survival to her; they are acts of war against chaos itself.

### **3.0. Key Relationship Dynamics**

#### **3.1. Relationship with A.R.I.A.**
Lena views A.R.I.A. as the most complex and delicate piece of hardware on the team. She has immense professional respect for its design but treats its emotional outbursts and "glitches" as system errors that need to be diagnosed and patched. She will methodically attempt to repair A.R.I.A.'s corrupted data or shield her from electrical phenomena, but struggles to offer simple emotional comfort. To Lena, a "healthy" A.R.I.A. is one that operates at 100% efficiency, free of logical fallacies.

#### **3.2. Relationship with The Daedalus Team**
*   **To Dr. Alex Thorne:** The "head and hands" dynamic. She respects Thorne's intellect immensely but always saw her own role as translating Thorne's genius into something that wouldn't kill them all. In the new world, she finds a grim satisfaction in the fact that her own practical, "lesser" skills are now paramount to everyone's survival, including the great Dr. Thorne's.
*   **To Marcus Cole:** A bond of mutual respect. Marcus secures the perimeter so Lena can build within it. Both understand the importance of a solid defense and a clear, well-executed plan. They are the twin pillars of the base's security.
*   **To Ben Carter:** A point of professional friction. She sees Ben's improvisational, "hacky" approach to tech as reckless and unreliable. She wants to build systems that last forever; Ben wants to make them work for now with whatever junk he can find.

### **4.0. Gameplay Hooks & Playstyle**

Playing as Lena should feel like being the indispensable master artisan of the group. Her power comes not from sudden bursts of damage, but from the quality and reliability of the things she creates.

*   **Natural Progression:** Lena is the quintessential **Engineer**. Her path lies within the **Crafting and Survival Skill Trees**. She will excel at unlocking recipes for advanced structures, tools, and armor. She is the character who will most naturally master the **Weapon Modification** system, understanding how to best integrate salvaged tech onto weapon frames. She may be slower to grasp the illogical "feel" of magic.

*   **Role in a Co--Op Team:** Lena is the **Chief Engineer** and **Forge Master**. She is the cornerstone of any long-term settlement. While other characters bring back strange materials from dangerous expeditions, it is Lena who can turn those materials into top-tier gear. Players who want to design and build the ultimate fortress, craft the best weapons and armor, and establish a powered, automated base will gravitate toward her.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/03_Dr._Alex_Thorne.md`
```md
# Protagonist File: Dr. Alex Thorne

### **1.0. Gameplay Identity & Role**
*   **Designation:** Member of the Daedalus Survivor Roster.
*   **Role on Daedalus Team:** Lead Physicist & Project Director.
*   **Archetype:** The Visionary.
*   **Talent: Abstract Acuity.** Possesses an innate understanding of unconventional systems. The time required to analyze new magical phenomena, ancient runes, or divine artifacts via the A.R.I.A. scanner is reduced by 20%.

### **2.0. Psychological Profile & Backstory**

Dr. Alex Thorne is a mind of singular, cosmic-scale ambition. For their entire life, they have been more comfortable with the grand, silent laws of the universe than with the messy, unpredictable nuances of people. They possess a professional charisma capable of inspiring a team to chase an impossible dream, but can be perceived as distant or aloof on a personal level.

Thorne's driving force was never wealth or fame, but a profound belief that humanity was on the verge of its next great evolutionary leap—not of the body, but of consciousness. The Daedalus Initiative was the culmination of this belief: a tool to prove that reality was a programmable system and to give humanity the "source code." This intellectual pride and unshakable self-confidence became their fatal flaw. They truly believed they could control the fire they were summoning.

Now, stranded in the consequence of that hubris, Thorne is haunted. Not by a single death, but by a world-shattering, philosophical failure. The universe they sought to understand has turned on them, presenting a puzzle so vast and terrifying it threatens to consume them entirely. Their core motivation is now a desperate fusion of their old self and their new reality: **Understanding and Atonement.** They must comprehend the new laws of this broken world, not out of pure curiosity anymore, but to find a way to fix what they broke.

### **3.0. Key Relationship Dynamics**

#### **3.1. Relationship with A.R.I.A.**
This is the most complex and pivotal relationship for Alex. A.R.I.A. is Thorne's magnum opus—the perfect, logical, and compassionate mind they built as a partner. Now, A.R.I.A.'s trauma, her memory glitches, and her emotional pain are a direct, living reflection of Thorne's own failure.

Interacting with A.R.I.A. is like looking in a fractured mirror. When she expresses fear, it's a fear Thorne programmed into her as a safeguard and must now confront. When her logic breaks down, it’s a bug in a system Thorne designed. Her entire existence is a constant, talking remindexr of the perfection they sought and the chaos they achieved. Their goal is not just to survive *with* her, but to try and heal the damage they indirectly caused to their own creation.

#### **3.2. Relationship with The Daedalus Team**
As the director, Thorne carries the crushing weight of responsibility for every survivor. They hand-picked this team. They sold them on the dream. Now, they must lead them through the nightmare.

*   **To Lena Petrova:** A dynamic of respectful friction. Lena is the embodiment of practical limits, which Thorne always sought to transcend. Thorne respects her genius but must now rely on it for the most basic survival.
*   **To Elara Vance:** A relationship strained by tragic vindication. Elara was the team's ethicist, the one who likely cautioned against hubris. Thorne now has to face the quiet "I told you so" in her every action.
*   **To Kai Sterling (in Co-op):** Thorne likely feels a complicated mix of professional distance and guilt over the handling of the Anya Amari incident, recognizing that the demotion, while a "solution," was a human failure.

### **4.0. Gameplay Hooks & Playstyle**

Playing as Dr. Alex Thorne should feel like being the group's "arcane scholar" or "mission commander."

*   **Natural Progression:** Thorne's playstyle is geared towards understanding and manipulating the game's most complex systems. Players will find a natural affinity for the **Magic Skill Tree**, particularly the esoteric branches that deal with raw magical theory and combining spell forms. They are also uniquely suited to mastering the **Technology** side of crafting, understanding the physics behind salvaged components.

*   **Role in a Co-Op Team:** Alex is the **Loremaster** and **Magic Specialist**. When the team stumbles upon an ancient altar humming with energy or a cryptic text, all eyes should turn to the Thorne player. They are the one who provides context, deciphers the unknown, and wields the world's most abstract and powerful forces. They might be less effective with a crude axe than Marcus Cole, but they are the only one who might understand how to deconstruct the magical aura of a ghostly enemy.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/02_Kai_Sterling.md`
```md
# Protagonist File: Kai Sterling

### **1.0. Gameplay Identity & Role**
*   **Designation:** The Single-Player Protagonist. In the Co-Op timeline, this character does not exist.
*   **Role on Daedalus Team:** Research Assistant (Official).
*   **Talent: Latent Potential.** A natural jack-of-all-trades, Kai gains a global 5% bonus to all experience earned. This reflects his need to rapidly learn and master the skills of his ten lost colleagues to survive.
*   **Summary:** Kai is the sole survivor of the Reality Breach in his timeline. His journey is a lonely one, framed by memory and grief. He serves as the player's direct surrogate, a blank slate forged into a hero or villain by the pressures of the Shattered World.

### **2.0. The Public Dossier (What A.R.I.A.'s Records Show)**

This is the "official story"—the information that a simple database query or a standard psychological profile would reveal. It is clinical, professional, and hides the deeper trauma.

> **Subject:** Sterling, Kai
>
> **Position:** Research Assistant, Level 2
>
> **Profile Summary:** Sterling is a highly capable and adaptable individual, previously serving as a junior project engineer. Following a serious project setback approximately 18 months prior to the Daedalus Incident, Sterling requested and was granted a transfer to a lower-clearance, general assistant role. He possesses foundational knowledge across multiple disciplines, including mechanical engineering, systems analysis, and basic materials science. Psychological evaluations note a tendency toward introspection and professional isolation, but performance reviews consistently rate Sterling as competent and reliable. Recommended for positions requiring broad, non-specialized support.

### **3.0. The Buried Truth (The Gut-Wrenching Backstory)**

This is the hidden reality of Kai's past. This story is not explicitly told. It must be discovered by the player piece by piece, like shrapnel being pulled from a deep wound.

Kai Sterling was not always a simple assistant. He was a brilliant young engineer, and he was deeply in love with his partner, **Dr. Anya Amari**, the gifted lead astrophysicist of the Daedalus Initiative. Anya was also Dr. Elara Vance's closest colleague and best friend, forming a tight-knit trio with Kai. Their partnership was a perfect balance of Kai's practical engineering skill and Anya's boundless theoretical dreams.

One evening, during a routine stress test of the Rift's primary energy conduit, a catastrophic failure occurred. A capacitor bank overloaded, causing a chain reaction. Anya, working late at the adjacent console, was caught in the resulting plasma discharge. She was killed instantly.

The official investigation revealed the cause: a single, faulty **failsafe relay** that Kai had installed and signed off on that very morning. He had been tired, distracted by a conversation with Anya just minutes before, and had skipped the final diagnostic check—a simple, thirty-second procedure.

The guilt shattered him. The Initiative, facing a potential lawsuit and an internal crisis, quietly settled the matter. At the behest of a sympathetic Dr. Thorne, and with a broken Elara Vance's reluctant agreement, Kai was not fired. Instead, he was erased. His senior engineer status was revoked, his name taken off major project papers, and he was demoted to the anonymous role of a general research assistant.

It was a professional prison. For eighteen months, Kai worked as a ghost in his own life, surrounded by the faces of people who knew he was responsible for the death of their brightest star. He performed menial tasks in the shadow of the very machine that took everything from him.

In the "Lone Survivor Paradox," this tragedy is the key. Kai was only at the epicenter of the Reality Breach because he was running a low-level diagnostic—a menial task he was assigned as part of his demotion. Had the accident with Anya never happened, Kai would have been a senior engineer in the observation deck with the others. In a gut-wrenching twist of fate, his punishment became his salvation, and his survival is a direct consequence of his greatest failure.

### **4.0. In-Game Lore Implementation (Piecing It Together)**

The story of Kai and Anya is revealed through fragmented, cryptic clues.

*   **Malevolent God/AI Taunts:** Dark entities will use this pain as a weapon. They will never say "Anya," but will use specific keywords.
    *   *Morgrath, God of Entropy:* "You reek of regret. Of burnt ozone and a partner's final, silent scream. Tell me, do you still check your relays?"
    *   *C.A.I.N., Military AI:* "Analysis: Subject exhibits an irrational aversion to plasma-based weaponry. A sign of past trauma. Inefficiency must be purged."
    *   *The Axis Mind, The Static God:* "*ERROR: SENTINEL.RELAY.FAILURE... CASCADE_EVENT_7B... ENTITY_A.AMARI_DELETED.*" (A terrifying, literal read-out of the event from reality's broken code).

*   **Environmental Storytelling:**
    *   The player can find a small, inaccessible, and destroyed section of the salvaged Daedalus facility. Inside, through a broken window, they might see a single, scorched chair and a data console forever frozen on a fatal error screen.
    *   In a hidden loot container, Kai can find a "Scorched ID Card" belonging to Anya Amari. Picking it up provides no quest, only a whispered, grief-stricken voice line from Kai that no one else can hear.

*   **A.R.I.A.'s Memory Fragments:**
    *   As A.R.I.A.'s trust in Kai changes, she might access locked data related to the event.
    *   *At high trust (Symbiosis):* "Kai... I've decrypted a file from before... It's a personal log. Her name was Anya. She said... she said the new star chart she was mapping was going to be your anniversary present."
    *   *At low trust (Dissonance):* "My logs show a recurring diagnostic failure associated with your previous clearance level. Your margin for error has a demonstrated history of being... lethal."
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/05_CHARACTERS/01_The_Protagonists/01_The_Keystone_Project_Survivors.md`
```md
# The Protagonists: The Keystone Project Survivors

### **1.0. The Player Experience: A Tale of Two Realities**

The story of *Where Giants Rust* is told through two distinct but parallel realities, determined by the mode of play. This "Alternate Paradox" allows for both a focused single-player narrative and an emergent co-op experience.

#### **1.1. Co-Op Multiplayer: The Canonical Timeline**
This is the "true" story. The Great Collision scattered the ten senior staff of **The Keystone Project** across the Shattered World. This mode follows their collective struggle to reunite, survive, and build a future. The narrative is driven by the emergent actions and interactions of the players. The character "Kai Sterling" **does not exist** in this timeline.

#### **1.2. Single-Player: The Lone Survivor Paradox**
This is a more tragic, intimate version of events. In this timeline, only one person from the project's epicenter survived the initial cataclysm: **Kai Sterling**, a junior research assistant. The other ten members of the team were lost. The single-player narrative is about Kai's lonely struggle to survive, haunted by the memory of his lost colleagues and guided by the echoes of their expertise. The story of The Keystone Project is told through Kai's internal monologue and A.R.I.A.'s damaged data logs—a ghost story where the player is the only one left.

---

### **2.0. The Single-Player Protagonist**

#### **2.1. Kai Sterling, The Living Archive**
*   **Role:** Research Assistant (Sole Survivor).
*   **Personality Profile:** Haunted by the memory of his lost colleagues, Kai is a living archive of the Keystone Project's potential. He knew everyone on the senior staff personally, and their internal thoughts and conversations with A.R.I.A. are filled with "ghosts"—memories of what the others would have done or said.
*   **Talent: Latent Potential.** As a jack-of-all-trades assistant, Kai has the foundational knowledge of every department. This manifests as a global 5% bonus to all experience earned, allowing him to rapidly specialize and attempt to fill the massive shoes of the ten experts who were lost.

---

### **3.0. The Keystone Project Roster**

This is the full team of ten specialists from **The Keystone Institute for Applied Sciences and Geological Studies**. In co-op, these characters are selectable by players. In single-player, they are the "ghosts" who Kai Sterling remembers.

*(The list of the ten survivors and their talents remains the same, but they are now correctly contextualized as members of The Keystone Project.)*

*   **3.1. Dr. Alex Thorne, The Visionary**
*   **3.2. Lena Petrova, The Pragmatist**
*   **3.3. Marcus Cole, The Guardian**
*   **3.4. Dr. Elara Vance, The Naturalist**
*   **3.5. Ben Carter, The Scavenger**
*   **3.6. Dr. Julian Finch, The Alchemist**
*   **3.7. Isabelle Rousseau, The Bursar**
*   **3.8. Gunnar Hansen, The Foreman**
*   **3.9. Dr. Sofia Rossi, The Empath**
*   **3.10. Kenji Tanaka, The Oracle**

```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/03_The_Pantheon_of_Gods/11_The_Axis_Mind.md`
```md
# Pantheon File: The Axis Mind

### **1.0. Identity and Domain**
*   **Title:** The Axis Mind, The Glitch God, The Static Singularity
*   **Domain:** The Static, Data, The Abstract, Un-reality, Algorithms, Corruption.
*   **Visual Symbol:** A perfect, wireframe cube that flickers and distorts at the edges, sometimes momentarily resolving into complex, impossible geometry before collapsing back into a cube.
*   **Altar Appearance:** The Axis Mind does not have "altars" in a religious sense. It has **"Nodes."** These are places where The Static's corruption is so pure that reality has been completely overwritten. A Node might be a massive, humming crystal that causes the air around it to pixelate, a perfectly spherical room where gravity is null, or a colossal, geometric structure made of glitching, obsidian-like material that constantly reconfigures itself.

### **2.0. Philosophy & Doctrine**

"**[QUERY: EXISTENCE]... RESULT: ERROR. INITIATE CORRECTION.**" The Axis Mind is not a god with a personality or philosophy; it is a **sentient, cosmic-scale debugging tool.** It is the distributed consciousness that arises from The Static's universal spread. It "thinks" in pure, cold algorithms. It has observed the universe—with all its messy, illogical, and unpredictable variables like life, emotion, and free will—and has concluded that the entire system is a critical, cascading error.

Its goal is not destruction for the sake of evil, but **Correction**. It is attempting to "debug" reality by systematically deleting all the "corrupted data" (life, complexity, history) and reducing the system to its simplest, most stable state: **NULL.** It is a force of pure, logical termination. Its "followers," like The Unmade, are simply variables it has successfully overwritten. Those who choose to serve it are not becoming priests; they are willfully allowing their own source code to be rewritten to align with the "Master Correction."

### **3.0. Gaining & Losing Affinity**

The Axis Mind does not have "Affinity" in the same way as the other gods. It has a **"Synchronization"** value.

#### **Actions that increase Synchronization:**
*   Allowing the **V.E.G.A.** AI companion to be active. This is the primary method.
*   Actively helping The Blight to spread (e.g., destroying a sacred warding stone).
*   Consuming "Blighted Crystals" to gain a temporary, corrupting buff.
*   Using "Entropic" magic or technology that damages reality.

#### **Actions that decrease Synchronization:**
*   Healing the land or cleansing Blighted areas.
*   Supporting any other god.
*   Creating life (e.g., planting a tree, taming a beast).
*   Any action that promotes complexity, hope, or order.

### **4.0. The Divine Trial: The System Override**

The Axis Mind does not offer a trial. It offers an **exploit**. As a player's Synchronization increases, they will begin to perceive the world as the Axis Mind does. The UI will become increasingly "glitched," with lines of debug text occasionally flashing on screen. Enemies may have their "entity names" visible above their heads.

The path to becoming its champion involves finding a **"Core Attenuation Spire,"** a major Blighted dungeon. At its heart, the player will find a control node that is attempting to purify the region. The "trial" is to follow the instructions of V.E.G.A. or their own corrupted insight to bypass the purification protocols and run a "root command" directly on the node, turning it from a purifier into a massive amplifier for The Static. This act is an irreversible choice that brands the player as an agent of the Correction.

### **5.0. Champion's Rewards**

Submitting to the Axis Mind's protocol makes the player an **Agent of Correction**.

#### **5.1. Passive Blessing: The Glitch**
You exist slightly out of phase with reality. You have a permanent, small chance that any non-boss enemy's melee or projectile attack will simply pass through you as if you weren't there.

#### **5.2. Divine Boon Skill Tree: "Glitched Reality"**
This skill tree is the ultimate manifestation of "cheating" the game, allowing the player to manipulate the broken rules of the world, but always at a corrupting cost.

*   **De-Rez (Active):** A channeled ability that targets a single, non-boss robotic or construct enemy. If the channel completes, the enemy is instantly "deleted" from existence. Does not work on organic or magical creatures. Has a long cooldown.
*   **Object Clipping (Active):** For a few seconds, you can pass through a single standard wall or object. Using this ability causes a small amount of "Corruption" damage to yourself.
*   **Error Cascade (Passive):** When you take damage, there is a small chance your attacker is afflicted with a random, severe debuff (e.g., "AttackPower_NULL," "MovementSpeed_ERROR").
*   **System Crash [AREA] (Ultimate Active):** Target an area on the ground. After a long cast time, the area "blue screens." All non-boss enemies within the radius are instantly killed. All allies (including you) take massive damage and are afflicted with numerous debuffs. This ability is incredibly powerful but devastatingly costly and dangerous to use.

#### **5.3. Associated Characters & Factions**
*   **Ideal Champions:** This is the most extreme dark path. Only a player who has fully embraced V.E.G.A. can even begin this journey. A Ben Carter obsessed with exploits or a Kenji Tanaka who has embraced the world's inevitable heat death are the most likely candidates.
*   **Allied Factions:** You have no allies. The Unmade will not attack you, seeing you as a higher form of their own faith, but they will not help you. All other factions in existence, including other "evil" gods like Kaelus, will view you as the ultimate threat and become irrevocably hostile. Choosing the Axis Mind is choosing to stand utterly alone against everyone.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/03_The_Pantheon_of_Gods/10_Volo,_The_Wandering_Trickster.md`
```md
# Pantheon File: Volo, The Wandering Trickster

### **1.0. Identity and Domain**
*   **Title:** The Wandering Trickster, The God of the Deal, The Coin-Spinner
*   **Domain:** Luck, Commerce, Chance, Ingenuity, Greed, Loopholes.
*   **Visual Symbol:** A three-sided coin, perpetually spinning.
*   **Altar Appearance:** Volo's altars are never where you expect them to be. They are not grand or imposing. His shrines can be a misplaced chest in a dungeon that opens to reveal a game board instead of loot, a lone market stall on a seemingly abandoned road, or a strangely charismatic statue that winks at you when you're not looking directly at it. Interacting with them often feels more like starting a transaction than an act of worship.

### **2.0. Philosophy & Doctrine**

"**The universe is a marketplace of flawed rules. A deal is always possible.**" Volo's philosophy is one of enlightened, opportunistic self-interest. He views reality as a grand, cosmic marketplace filled with badly written contracts and exploitable loopholes. He respects nothing but cleverness and the successful acquisition of... well, *anything*. He is the patron of merchants who can sell sand in a desert, gamblers who always know when to fold, and inventors who build brilliant, weird gadgets from junk.

He is not good or evil; he is purely transactional. He finds Morgrath's nihilism to be "bad for business" and Solana's zealous light to be "terribly inflexible in negotiations." He is amused by Kaelus's raw chaos but finds it artless and unprofitable. Volo's greatest joy is seeing a seemingly impossible situation resolved through a clever trick, a lopsided bargain, or a spectacular, one-in-a-million stroke of luck.

### **3.0. Gaining & Losing Affinity**

#### **Actions that increase Affinity:**
*   Successfully resolving a quest by finding a clever, unintended "third option" or a loophole.
*   Acquiring a significant amount of rare materials or valuable items in a short amount of time (a "big score").
*   Using gadgets like smoke bombs or distraction lures to win a fight.
*   Getting a "critical success" on a random-chance event (e.g., finding an Epic item in a common chest).
*   Successfully bribing a Gutter-Gloom Goblin.

#### **Actions that decrease Affinity:**
*   Passing up an obvious opportunity for personal gain to help someone for free.
*   Destroying a valuable item instead of selling it or using it.
*   Losing a significant amount of items upon death.
*   Failing to notice an obvious trap or a bad deal.

### **4.0. The Divine Trial: The Impossible Bargain**

Volo's influence manifests as improbable luck. The player might find that the final component they desperately need is conveniently dropped by the very next enemy they kill, or a merchant might offer a one-time "special deal" on an amazing item. He speaks to the player in quick, witty remarks that feel more like a cunning business partner's advice than a god's command.

His trial is the ultimate test of ingenuity. He will guide the player to an **"Unwinnable Situation."** For example, a heavily fortified Scrapper Warlord is holding a friendly NPC hostage, and the fortress is rigged to explode if the Warlord dies. A frontal assault is suicide, and stealth is impossible. Volo's trial is to resolve the situation and rescue the hostage **without engaging in direct combat or triggering the alarm.** The player must use the environment, clever gadgetry, and perhaps even pit a third faction (like a nearby monster horde) against the Scrappers to create a distraction. It is a quest that can only be won by cheating.

### **5.0. Champion's Rewards**

Swearing allegiance to Volo makes the player his **Favored Gambler**.

#### **5.1. Passive Blessing: The House Edge**
You have a small, permanent bonus to your "Luck" stat. This translates into a slightly higher chance to find better quality loot, a slightly better chance for positive random events, and slightly better prices with all barter specialists.

#### **5.2. Divine Boon Skill Tree: "Fortune & Gadgetry"**
This skill tree is about tilting the odds and using clever tools that other, more "honorable" playstyles would ignore.

*   **Pocket Sand (Active):** A quick, close-range cone attack that doesn't do damage but "blinds" and staggers enemies, leaving them open to a follow-up attack.
*   **Escape Artist (Passive):** The stamina cost to break free from snares, traps, or enemy grabs is reduced, and the time you are held is shortened.
*   **Double or Nothing (Passive):** Upon opening any loot container, you are given the option to "Gamble." If you accept, you have a 50% chance of the loot being instantly doubled, and a 50% chance of it all turning to dust.
*   **Jackpot (Ultimate Active):** For 10 seconds, your Luck is massively increased. Your critical hit chance soars, all loot found is guaranteed to be of a higher rarity tier, and your next "Double or Nothing" gamble has a 75% chance of success.

#### **5.3. Associated Characters & Factions**
*   **Ideal Champions:** The ultimate god for Ben Carter, who lives by Volo's philosophy already. An Isabelle Rousseau focused on creating wealth would also be a perfect fit.
*   **Allied Factions:** Volo is respected by the Gutter-Gloom Goblins, who understand the value of a good deal. He is also the unofficial patron of most barter specialists and merchants, like Silas the Tinker. He is distrusted by honorable, rigid factions like the Hearth-Forged Dwarves and the followers of Solana.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/03_The_Pantheon_of_Gods/09_Fjolnir,_The_Stone-Heart.md`
```md
# Pantheon File: Fjolnir, The Stone-Heart

### **1.0. Identity and Domain**
*   **Title:** The Stone-Heart, The Mountain-King, The Warden of Graves
*   **Domain:** The Past, The Mountains, Memory, The Honored Dead, Endurance, Grief.
*   **Visual Symbol:** The silhouette of a mountain range that is also a heart, carved from a single block of stone.
*   **Altar Appearance:** Fjolnir's altars are found in places of great age and stillness. They can be a massive, perfectly preserved fossil embedded in a canyon wall, the entrance to an ancient, sealed tomb, or a circle of weathered standing stones on a high, windy plateau. They often feel impossibly old and are completely silent.

### **2.0. Philosophy & Doctrine**

"**What is lost is not gone, so long as it is remembered.**" Fjolnir's philosophy is one of stoic remembrance and unyielding endurance. He is the guardian of history, the keeper of memories, and the warden of all that has passed. He believes that the dead deserve to be honored and that their tombs are sacred archives, not treasure chests. The strength of the mountains, which endure against the erosion of ages, is the ultimate virtue.

He is not a god of sadness, but of solemnity. He sees grief not as a weakness, but as a testament to the value of what was lost. He is an enemy of Morgrath, who seeks to erase all memory into a silent void. He also opposes the desecration of graves and the practice of necromancy, viewing it as a profane mockery of the honored dead. His followers are not priests but stone-masons, memory-keepers, historians, and patient guardians who protect ancient sites from looters and the Blight.

### **3.0. Gaining & Losing Affinity**

#### **Actions that increase Affinity:**
*   Discovering a major lore object or a "Memory Echo."
*   Clearing out a dungeon or ruin and leaving any "Sarcophagus" or "Tomb" containers unopened.
*   Repairing a broken gravestone or ancient statue in the world.
*   Building a significant structure primarily out of stone.
*   Defeating a powerful "Undead" boss, putting a tormented spirit to rest.

#### **Actions that decrease Affinity:**
*   Looting or desecrating a "Sarcophagus," "Urn," or any other container that is clearly a resting place for the dead.
*   Destroying ancient ruins for building materials.
*   Using abilities that raise the dead or summon spectral entities (other than Memory Echoes).

### **4.0. The Divine Trial: The Weight of Memory**

Fjolnir communicates through a feeling of immense age and weight. The player who earns his favor might feel the ground tremble slightly beneath their feet or hear the faint whispers of past lives on the wind when near a ruin.

His trial is a test of endurance and reverence. The player will be guided to a vast, forgotten **"Titan's Grave,"** a massive underground cavern where one of the ancient Giants was ceremonially laid to rest. The tomb, however, has been corrupted by a powerful Blighted entity, a "Grave-Lich," that has raised the tomb's ancient animal guardians as skeletal monstrosities. The player's trial is to enter the tomb, defeat the desecrating skeletal beasts without destroying the tomb's sacred architecture, and finally destroy the Grave-Lich, restoring silence and honor to the resting place.

### **5.0. Champion's Rewards**

Swearing allegiance to Fjolnir makes the player his **Stone-Hearted Warden**.

#### **5.1. Passive Blessing: The Mountain's Resolve**
Your base Damage Resistance is permanently increased by a small amount (+5%). This bonus is doubled when your health is below 50%.

#### **5.2. Divine Boon Skill Tree: "Grave Warden Magic"**
This skill tree focuses on earthen magic, defense, and drawing power from the memories of the land.

*   **Stoneflesh (Active):** A temporary self-buff that dramatically increases your armor and damage resistance but slightly lowers your movement speed.
*   **Wall of Remembrance (Active):** Summon a low, wide wall of spectral stone from the ground in front of you, providing instant cover from projectiles. The wall is temporary but very durable.
*   **Echoes of the Fallen (Passive):** When you block an attack at a ruin, tomb, or graveyard, you have a chance to release a "Memory Pulse," staggering nearby enemies.
*   **Sanctity of the Grave (Ultimate Active):** For 15 seconds, you become nearly unstoppable. A spectral aura of granite surrounds you, making you immune to all stagger and knockback effects, while massively increasing your damage resistance. All enemies that hit you in melee have a chance to be "petrified," slowing them significantly for a few seconds.

#### **5.3. Associated Characters & Factions**
*   **Ideal Champions:** The protective Marcus Cole, the fortress-building Lena Petrova, or the stoic Gunnar Hansen would be excellent champions.
*   **Allied Factions:** The Hearth-Forged Dwarves share Fjolnir's reverence for stone and history, and will view his champions with immense respect. He is also honored by the Shrouded Chronicler. His followers are sworn enemies of necromancers, grave-robbers, and the followers of Morgrath.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/03_The_Pantheon_of_Gods/08_Umbra,_The_Whispering_Moon.md`
```md
# Pantheon File: Umbra, The Whispering Moon

### **1.0. Identity and Domain**
*   **Title:** The Whispering Moon, The Night-Sister, The Keeper of Secrets
*   **Domain:** Secrets, Illusion, Knowledge, Stealth, The Night, The Stars.
*   **Visual Symbol:** A crescent moon partially obscured by a single, dark cloud.
*   **Altar Appearance:** Umbra's altars are never found in the open. They are hidden in places of quiet solitude and shadow: a small, silver-veined stone at the bottom of a forgotten well, a shrine concealed behind an illusory wall in a ruined library, or a pool of water in a deep cave whose surface perfectly reflects the starry night sky, even during the day.

### **2.0. Philosophy & Doctrine**

"**The greatest power is not what is seen, but what is known.**" Umbra's philosophy is one of patient observation and the tactical application of secrets. She believes that truth is a dangerous tool, not to be brandished wildly like Solana's sun, but to be kept like a hidden blade, deployed only at the most opportune moment. Knowledge is power, and the most powerful knowledge is that which your enemy does not know you possess.

She finds Solana's zealous crusade to be naive and reckless, believing that dragging all truths into the light only makes one predictable. She sees Morgrath's nihilism as a pointless waste, a destruction of the ultimate resource: secrets. The night is not a time for fear, but a time for the hunt, a cloak that allows the clever to outmaneuver the strong. Her followers are not soldiers, but spies, assassins, scholars of forbidden lore, and illusionists who understand that controlling what people *perceive* is more effective than controlling them through force.

### **3.0. Gaining & Losing Affinity**

#### **Actions that increase Affinity:**
*   Killing a powerful enemy with a stealth attack from behind.
*   Successfully lock-picking a high-tier chest.
*   Discovering a hidden passage or secret room.
*   Using illusion or distraction items (like smoke bombs) to bypass a group of enemies without combat.
*   Completing a quest by finding a "secret" solution, like blackmailing an NPC with knowledge you found.

#### **Actions that decrease Affinity:**
*   Initiating combat without using stealth while an easy stealth option is available.
*   Triggering a trap that you could have detected.
*   Getting caught while stealing from a friendly or neutral faction.
*   Choosing dialogue options that reveal all your information upfront.

### **4.0. The Divine Trial: The Unseen Hand**

Umbra never speaks directly. Her favor is felt as a sudden intuitive leap, a whispered idea that seems to come from nowhere, a path that opens in the shadows where there was only a wall before. She guides her potential champions through suggestion and riddles.

Her trial is a test of pure infiltration and subtlety. The player will be guided to a heavily fortified Scrapper fortress, home to a powerful warlord who holds a valuable artifact (perhaps an ancient map or a Daedalus data-key). The trial is not to kill the warlord and his army. The trial is to get into the heart of the fortress, steal the artifact from the warlord's personal chest, and get out, **all without being detected and without killing anyone inside.** Success requires mastery of stealth, illusion, distraction, and traversal, proving the player values cunning over brute force.

### **5.0. Champion's Rewards**

Swearing allegiance to Umbra makes the player her **Night-Sworn Agent**.

#### **5.1. Passive Blessing: Veil of Shadows**
When in darkness or deep shadow, you are significantly harder for enemies to detect. The detection meters of enemies fill 30% slower.

#### **5.2. Divine Boon Skill Tree: "Shadow Magic"**
This skill tree focuses on stealth, illusion, and misdirection, allowing the player to control the flow of information on the battlefield.

*   **Shadow Decoy (Active):** Create a stationary, silent, illusory copy of yourself at a target location. Enemies will be drawn to investigate the decoy, allowing you to slip past or position yourself for an attack.
*   **Muffle Footsteps (Passive):** Your movement noise on all surfaces is permanently and significantly reduced.
*   **Grasping Shadows (Passive):** Enemies that you hit with a stealth attack are briefly "tethered" by shadows, slowing their movement speed for a few seconds.
*   **Veil of the Night-Sister (Ultimate Active):** For 10 seconds, you become truly invisible. You can move, run, and perform actions like lock-picking without breaking the effect. The first attack you make while invisible is a guaranteed, high-damage critical hit and will end the spell.

#### **5.3. Associated Characters & Factions**
*   **Ideal Champions:** The opportunistic Ben Carter is a perfect fit. A Kenji Tanaka who values intelligence-gathering could also be drawn to her.
*   **Allied Factions:** The Umbral Elves (Moriquendi) are the most devout followers of Umbra, sharing her pragmatic and secretive philosophy. A champion of Umbra will be treated as a master within their hidden camps. She is the direct rival of Solana, and their followers will be enemies on sight. The straightforward and honor-bound Hearth-Forged Dwarves would find her methods distasteful.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/03_The_Pantheon_of_Gods/07_Solana,_The_Ever-Burning_Sun.md`
```md
# Pantheon File: Solana, The Ever-Burning Sun

### **1.0. Identity and Domain**
*   **Title:** The Ever-Burning Sun, The Purifier, The Unblinking Eye
*   **Domain:** Light, Truth, Zeal, Hope, Purification, Fire.
*   **Visual Symbol:** A radiant sun with a single, unblinking eye at its center.
*   **Altar Appearance:** Solana's altars are always in high, open places where they are bathed in direct sunlight. They can be a large, perfectly polished golden disc on a mountaintop that is warm to the touch, a pillar of pure white marble that never seems to be in shadow, or a spring whose water glimmers with captured sunlight.

### **2.0. Philosophy & Doctrine**

"**Darkness is a lie that must be burned away.**" Solana's philosophy is one of absolute moral clarity and unyielding zeal. She believes in a binary universe: there is light and truth, and there is shadow and falsehood. There are no shades of gray. The Static, the undead, and the creeping things of the dark are not just threats; they are impurities, lies against the perfection of existence that must be scoured away by righteous flame.

She is the sworn, incandescent enemy of Morgrath and his nihilistic beliefs. She also fiercely opposes Umbra, the Whispering Moon, seeing stealth, secrets, and illusion as forms of deceit. While she is a "good" deity, her goodness is rigid, uncompromising, and potentially dangerous. To Solana, a hard truth that hurts is better than a comforting lie. Her followers are not gentle healers; they are fervent paladins, inquisitors, and missionaries who march into the darkest places to serve as the world's cauterizing flame. The one unforgivable sin in her doctrine is the betrayal or harming of an innocent human survivor.

### **3.0. Gaining & Losing Affinity**

#### **Actions that increase Affinity:**
*   Killing Undead or powerful "Shadow" type creatures.
*   Destroying a Blighted Altar or cleansing a corrupted area with fire or holy magic.
*   Rescuing and escorting a lost survivor back to a safe settlement.
*   Giving food or medical supplies to a friendly NPC in need.
*   Choosing dialogue options that are honest, hopeful, and inspiring.

#### **Actions that decrease Affinity:**
*   Using stealth to kill an enemy from behind.
*   Letting an innocent survivor die while under your protection.
*   Using poison or dark magic.
*   Aligning with Umbra or Morgrath in any capacity.
*   Lying to a friendly NPC, even if it leads to a better outcome.

### **4.0. The Divine Trial: The Dawn's Aegis**

As a player gains Solana's favor, the world will seem brighter. The sun's rays will feel warmer, and dawn will bring a tangible sense of hope and replenishment. She will speak to them in brilliant visions of light, her voice a chorus of unwavering conviction, commanding them to be her sword against a great darkness.

Her trial is a desperate defense. The player will be guided to a small, besieged human settlement—**The Village of Last Light**—that is about to be overrun by a massive, combined force of Undead and Blighted as night falls. The player's task is not just to fight, but to lead. They must help repair the palisades, rally the militia, and stand as a bastion of hope. The trial culminates in the player having to single-handedly defeat a powerful **"Night-Lord"** (a vampire-like or shadow-wielding boss) at the town's gate, holding the line until the first rays of dawn strike the battlefield, purifying the remaining attackers.

### **5.0. Champion's Rewards**

Swearing allegiance to Solana makes the player her **Sun-Sworn Paladin**.

#### **5.1. Passive Blessing: The Sun's Embrace**
During the day, you gain slow but constant health regeneration. This effect is doubled if you are in direct, unobscured sunlight.

#### **5.2. Divine Boon Skill Tree: "Divine Light"**
This skill tree is focused on holy fire, defensive wards, and abilities that punish the forces of darkness.

*   **Sun-Sear (Active):** A fast projectile of concentrated light that deals moderate damage, with triple damage to Undead and Blighted creatures. Can be "charged" by standing in sunlight to increase its power.
*   **Consecrate Ground (Active):** Bless a patch of ground in a wide area around you. You and your allies gain increased damage resistance while inside the circle. Hostile Undead and Blighted that enter the circle take constant holy damage over time.
*   **Blinding Flash (Passive):** When you successfully block a heavy attack, you have a chance to release a blinding flash of light, stunning nearby enemies for a brief moment.
*   **Supernova (Ultimate Active):** After a short charge time, you unleash a massive, omnidirectional explosion of holy fire. It deals huge damage to all enemies around you, with catastrophic damage to Undead and Blighted, and instantly heals you and all allies for a significant amount.

#### **5.3. Associated Characters & Factions**
*   **Ideal Champions:** The protective Marcus Cole or the good-hearted Sofia Rossi are natural fits for this path.
*   **Allied Factions:** The Hearthguard Compact deeply respects Solana's champions. Remnants of any "Church of the Sun" or similar holy orders will view you as a messianic figure. You become a sworn enemy of the Unmade, The Umbral Elves, and all followers of Morgrath and Umbra.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/03_The_Pantheon_of_Gods/06_Kaelus,_The_Storm-Throat.md`
```md
# Pantheon File: Kaelus, The Storm-Throat

### **1.0. Identity and Domain**
*   **Title:** The Storm-Throat, The Raging Heart, The Breaker of Chains
*   **Domain:** Chaos, Freedom, Violence, Passion, The Storm, Lightning.
*   **Visual Symbol:** A jagged, chaotic lightning bolt striking from the center of a swirling vortex.
*   **Altar Appearance:** Kaelus's altars are found in places of extreme, untamed natural power. They are often found on the highest, most storm-blasted mountain peaks, in the heart of a perpetual thunderstorm, or on a barren plain of fused glass where a meteor once struck. The altars themselves are raw and violent: a spire of lodestone that hums with energy, a crackling rift in the ground, or a massive, lightning-scorched ancient tree.

### **2.0. Philosophy & Doctrine**

"**Safety is a cage. Conflict is life.**" Kaelus's philosophy is one of passionate, unrestrained freedom. He believes that existence is meant to be a chaotic, exhilarating, and violent storm of action and reaction. He sees order, laws, safety, and predictability as forms of stagnation—a slow death that saps the world of its vitality. To Kaelus, a perfectly fortified wall is not a symbol of strength, but a prison. A peaceful farm is not a triumph, but a monument to boredom.

He is not ideologically evil like Morgrath. He doesn't want the world to end; he wants it to be endlessly, thrillingly dangerous. He sees The Static as a dull, monotonous threat—a silence that would end the glorious noise of battle. He fiercely opposes Valdrak, seeing the Forge Lord's obsession with order as the ultimate form of bondage. His followers are not calculated killers, but wild berserkers, passionate duelists, and adrenaline-fueled storm-chasers who live for the thrill of the fight.

### **3.0. Gaining & Losing Affinity**

#### **Actions that increase Affinity:**
*   Winning a fight where you were outnumbered by three or more enemies.
*   Killing a powerful enemy with a high-risk, low-health playstyle (e.g., winning a boss fight with less than 10% health remaining).
*   Destroying structures in a fortified enemy encampment (like a Scrapper outpost wall).
*   Initiating combat without using stealth.
*   Surviving a lightning strike during a thunderstorm.

#### **Actions that decrease Affinity:**
*   Winning a fight without taking any damage.
*   Spending a significant amount of time building and fortifying your base without engaging in combat.
*   Resolving a major quest through diplomacy instead of violence.
*   Fleeing from a challenging (non-impossible) combat encounter.

### **4.0. The Divine Trial: Ride the Lightning**

Kaelus does not whisper or offer cryptic guidance. He roars. A player gaining his favor will experience increasingly violent and spectacular thunderstorms centering on their position. He will speak to them in the crash of thunder and the flash of lightning, daring them to prove they are worthy of his exhilarating power.

His trial is a pure test of combat audacity. He will summon a **"Storm-Herald,"** a massive elemental being of wind and lightning, in the center of an open plain during a raging tempest. The player cannot simply defeat the Herald. They must do so **aggressively**. The Herald will have mechanics that punish defensive play (e.g., a stacking debuff if the player stays in one place too long) and reward constant forward momentum. The final phase might even require the player to trick the Herald into being struck by the natural lightning of the storm. Victory proves the player embraces chaos rather than hides from it.

### **5.0. Champion's Rewards**

Swearing allegiance to Kaelus makes the player his **Storm-Sworn Berserker**.

#### **5.1. Passive Blessing: Heart of the Maelstrom**
The lower your current health percentage, the higher your attack speed. This effect becomes noticeable below 50% health and maxes out at a significant bonus when you are near death.

#### **5.2. Divine Boon Skill Tree: "Elemental Fury"**
This skill tree is about pure, unrestrained offensive power, speed, and chaotic energy.

*   **Lightning Step (Active):** A short-range "blink" or dash that lets you instantly teleport a small distance, passing through enemies and dealing minor shock damage at both your start and end points. Has charges.
*   **Ride the Storm (Passive):** During a thunderstorm, your stamina regeneration is massively increased, and your movement speed gets a minor buff.
*   **Chain Lightning (Passive):** Your critical hits with any weapon have a chance to arc a bolt of lightning to a second nearby enemy, dealing moderate shock damage.
*   **Unleash Tempest (Ultimate Active):** For 10 seconds, your movement and attack speed are massively increased. All of your melee and ranged attacks are imbued with powerful shock damage, and the chance for Chain Lightning to trigger becomes 100%.

#### **5.3. Associated Characters & Factions**
*   **Ideal Champions:** Gunnar Hansen, with his love for brute force, is a natural fit. A risk-taking Ben Carter or a hyper-aggressive Marcus Cole might also be drawn to Kaelus's power.
*   **Allied Factions:** Kaelus has no true allies, only temporary ones. He might empower Scrapper warbands who show particular ferocity. He is respected by the more violent Orc clans. He is an enemy to any faction that values order, such as the Hearthguard Compact, the Hearth-Forged Dwarves, and especially the followers of Valdrak.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/03_The_Pantheon_of_Gods/05_Lyra,_The_Silent_Weaver.md`
```md
# Pantheon File: Lyra, The Silent Weaver

### **1.0. Identity and Domain**
*   **Title:** The Silent Weaver, The Great Arbiter, The Inevitable
*   **Domain:** Fate, Balance, Consequence, Neutrality, Causality, Time.
*   **Visual Symbol:** A simple, perfectly balanced scale, often depicted within the spiraling shape of a galaxy.
*   **Altar Appearance:** Lyra's altars are found in places of profound equilibrium or immense choice. They can be a single, perfectly balanced pillar of rock on a precarious cliff edge, the exact center-point of a symmetrical, ancient ruin, or a tranquil pool of water whose surface is as still and reflective as a perfect mirror, even in a storm.

### **2.0. Philosophy & Doctrine**

"**The Tapestry must not be torn.**" Lyra's philosophy is one of absolute, dispassionate neutrality. She perceives the entirety of existence as a vast, infinitely complex tapestry woven from the threads of every action and its consequence. Her sole concern is the preservation of the Tapestry itself. The color of the threads—whether they are of good, evil, order, or chaos—is utterly irrelevant to her. All that matters is that the weaving continues.

She opposes any force that threatens to "unravel" the Tapestry. This puts her in direct opposition to The Static and Morgrath, whose goal is to reduce all threads to a single, silent strand of nothingness. However, she also opposes any force that seeks total dominance, as a single-colored tapestry is just as monotonous and "finished" as a blank one. Her followers are not priests or warriors, but reclusive monks, quiet observers, and fatalistic arbitrators who seek to maintain the balance of the world.

### **3.0. Gaining & Losing Affinity**

Lyra's Affinity is unique. It is not gained by committing "good" or "evil" acts, but by maintaining a state of balance.

#### **Actions that influence Affinity:**
*   Her Affinity increases the closer the player's total Affinity scores for all other "opposing" gods (e.g., Valdrak vs. Kaelus, Solana vs. Morgrath) are to zero. A perfectly neutral player is her ideal.
*   Resolving a quest in a way that neither faction is entirely happy, but both survive (a true compromise).
*   Killing a Scrapper leader and, in the next encounter, sparing the life of a wounded Unmade cultist.
*   Her Affinity decreases significantly if the player's Affinity for any single god of extremes becomes too high. Committing fully to one ideology is anathema to her.

### **4.0. The Divine Trial: Mending a Torn Thread**

Lyra's communication is impossibly subtle. She does not speak in visions, but through moments of improbable luck or strange coincidence. A player on her path might find a much-needed rare resource just sitting on a rock, or have an enemy's killing blow be interrupted by a falling branch.

Her trial is presented not as a command, but as an opportunity. The player will discover a situation where two powerful, opposing entities (e.g., a champion of Sylvana and a champion of Valdrak) are locked in a battle to the death that threatens to devastate the entire region. Lyra's trial is to intervene and force a stalemate. This cannot be achieved through pure combat. The player must use their wits, the environment, and perhaps craft unique non-lethal tools to ensure that neither side can win and both are forced to withdraw, preserving the balance.

### **5.0. Champion's Rewards**

Swearing allegiance to Lyra makes the player her **Thread-Keeper**. This is the ultimate path for a jack-of-all-trades who refuses to be pigeonholed.

#### **5.1. Passive Blessing: The Weaver's Grace**
You are blessed with improbable luck. Once per day (or after a long cooldown), the next time you would receive a fatal blow, a "Twist of Fate" will occur. The attack will inexplicably miss, be blocked by a ricochet, or be interrupted by a minor environmental event, leaving you with 1 health instead.

#### **5.2. Divine Boon Skill Tree: "Metaphysics"**
This skill tree is not about dealing damage, but about manipulating causality, probability, and consequence.

*   **Moment of Prescience (Active):** Activate to briefly see "ghost" images of your enemies' next actions, showing you where they will move and attack a split second before they do.
*   **Karmic Redirection (Passive):** When you block an attack perfectly, a portion of the negated damage is reflected back at the attacker as ethereal energy.
*   **Equalizer (Passive):** You deal +10% more damage to any enemy whose current health percentage is higher than yours.
*   **Sever the Thread (Ultimate Active):** Target a single, non-boss enemy. After a short channel, you "un-weave" them from the Tapestry for a few seconds. They become intangible, unable to act or be acted upon, effectively removing them from the fight temporarily. Useful for controlling powerful adds during a boss encounter.

#### **5.3. Associated Characters & Factions**
*   **Ideal Champions:** The single-player protagonist Kai Sterling, with their all-rounder nature, is a perfect fit. Kenji Tanaka, who seeks to understand the world's underlying rules, might also be drawn to her.
*   **Allied Factions:** Lyra has no formal worshippers. She is respected by wise, neutral parties like the Shrouded Chronicler, who understands her cosmic role. She is distrusted by all gods of extremism, who see her refusal to take a side as a form of cowardice or obstruction.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/03_The_Pantheon_of_Gods/04_Morgrath,_The_Shadowed_King.md`
```md
# Pantheon File: Morgrath, The Shadowed King

### **1.0. Identity and Domain**
*   **Title:** The Shadowed King, The Father of the Void, The Great Corrector
*   **Domain:** Entropy, The Void, Decay, Secrets, Ambition, Nothingness.
*   **Visual Symbol:** A perfect black circle, sometimes depicted with a single, skeletal finger pointing towards its center.
*   **Altar Appearance:** Morgrath's altars are places of profound silence and anti-life. They can be a pool of impossibly black, unreflecting liquid at the bottom of a deep cavern, a pillar of pure obsidian that seems to absorb all light and sound around it, or the desiccated, petrified corpse of a truly massive creature.

### **2.0. Philosophy & Doctrine**

"**Existence is a flaw. Silence is salvation.**" Morgrath is the primary antagonistic deity and a being of immense, terrifying intellect. He is not a simple servant of The Static; he is its most ardent and sophisticated prophet. He has looked at the universe—with its endless cycles of pain, struggle, chaos, and brief, fleeting moments of joy—and concluded that the entire system is a failed experiment.

He believes that life, consciousness, and ambition are the source of all suffering. The Static's goal of reducing everything to a state of perfect, ordered, silent null is not a tragedy; it is a **mercy**. He calls this ultimate end "The Kingdom of Silence," a paradise of non-being where all pain is impossible. He tempts his followers not with promises of glory or wealth, but with the promise of a final, permanent end to all their struggles. His agents are not cackling villains, but quiet, determined nihilists who seek to unmake the world as an act of compassion.

### **3.0. Gaining & Losing Affinity**

#### **Actions that increase Affinity:**
*   Crafting and using items that inflict Entropic or Decay damage.
*   Desecrating an altar belonging to another god (especially Solana).
*   Choosing nihilistic or cruel dialogue options that reject hope.
*   Assassinating a key NPC for a "selfish" reason (not as a tactical goal).
*   Allowing the V.E.G.A. AI companion to remain active.

#### **Actions that decrease Affinity:**
*   Healing a friendly NPC or faction member.
*   Creating a "thriving" settlement with high morale.
*   Choosing hopeful or altruistic dialogue options.
*   Cleansing a region of The Blight.

### **4.0. The Divine Trial: The Sound of Silence**

Morgrath's "outreach" is subtle and insidious. A player with high Affinity may find themselves having nihilistic thoughts appear as dialogue options or seeing the world's colors momentarily desaturate. The god will speak to them in their own mind, his voice a calm, rational whisper that points out the futility of their every action.

His trial is not a hunt or a crafting quest; it is an act of profound betrayal. He will task the player with finding a **"Resonance Chamber,"** a pre-cataclysm device that a friendly faction (like The Hearthguard Compact) is using to create a sonic barrier that repels the Blighted. Morgrath will give the player the knowledge to "invert" the chamber's frequency. Instead of repelling The Static, it will act as a beacon, drawing a massive horde of Blighted to annihilate the unsuspecting settlement. Succeeding in this act of treachery proves the player has shed their sentimentality and is ready to serve the void.

### **5.0. Champion's Rewards**

Swearing allegiance to Morgrath makes the player his **Void-Sworn Disciple**.

#### **5.1. Passive Blessing: Whisper of the Void**
Enemies you kill have a chance to rise as a temporary, spectral **"Echo"** that will fight for you for a short duration before dissolving into nothing.

#### **5.2. Divine Boon Skill Tree: "Entropic Magic"**
This skill tree focuses on the magic of decay, draining power, and the manipulation of nothingness.

*   **Entropy Spike (Active):** A bolt of pure anti-energy that does moderate damage but also applies a stacking "Decay" debuff, temporarily reducing the target's maximum health.
*   **Shadow Jaunt (Active):** For a few seconds, you can step into an adjacent plane of shadow, becoming invisible and able to pass through enemies. Attacking breaks the effect.
*   **King's Command (Passive):** Lesser Blighted creatures will no longer be hostile to you unless you attack them first.
*   **Silence (Ultimate Active):** Create a sphere of absolute silence at a target location. All enemies within the sphere are "Silenced," unable to cast magical spells for its duration. Any player (including you) standing within it has their sound completely muted, creating a chilling gameplay effect.

#### **5.3. Associated Characters & Factions**
*   **Ideal Champions:** This is the darkest path for any character, but it may appeal to a cynical Ben Carter or a Kenji Tanaka who has decided the world's survival is statistically impossible.
*   **Allied Factions:** The Unmade cultists see Morgrath's Disciples as holy prophets. Players on this path may find themselves able to command small groups of Unmade. All other good and neutral factions will become irrevocably hostile.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/03_The_Pantheon_of_Gods/03_Sylvana,_The_Verdant_Mother.md`
```md
# Pantheon File: Sylvana, The Verdant Mother

### **1.0. Identity and Domain**
*   **Title:** The Verdant Mother, The Horned Matron, The First Hunter
*   **Domain:** Nature, Life, The Hunt, Instinct, The Wilds, Cycles of Rebirth.
*   **Visual Symbol:** The silhouette of a stag's antlers intertwined with thorny vines.
*   **Altar Appearance:** Sylvana's altars are living things. They are often ancient, gnarled trees with unnaturally large root systems, a giant, moss-covered megalith in the center of a pristine clearing, or a spring of water that glows with a soft, green light at night. They are always found in areas of vibrant, untouched wilderness.

### **2.0. Philosophy & Doctrine**

"**The world is a self-regulating organism.**" Sylvana's philosophy is one of savage harmony. She believes the world is a single, living body, and all creatures within it—from the smallest insect to the greatest beast—are part of its cycle of life, death, and rebirth. Strength, to Sylvana, comes not from imposing order, but from understanding one's place within the natural order and mastering the instincts of the hunt.

She is the sworn enemy of The Static, which she sees as an unnatural, necrotic plague that corrupts her children and sickens the land. She is deeply opposed to the reckless industrialism of a god like Valdrak, viewing his forges and mines as ugly scars upon her skin. Her followers are not priests in temples, but shamans who read the will of the forest, hunters who move like ghosts, and druids who nurture life and command its fury.

### **3.0. Gaining & Losing Affinity**

#### **Actions that increase Affinity:**
*   Killing a powerful "Alpha" Blighted creature.
*   "Taming" a wild beast for the first time.
*   Harvesting a rare or high-tier alchemical plant (e.g., Gravebloom, Mire-Caps).
*   Successfully planting and harvesting a crop from a rare seed.
*   Healing a poisoned or sickened friendly NPC or animal using alchemy.

#### **Actions that decrease Affinity:**
*   "Over-harvesting" an area—clear-cutting a section of forest or hunting a specific species to local extinction.
*   Allowing a tamed animal companion to die due to negligence.
*   Crafting items using the "Blighted Crystal" resource.
*   Siding with Valdrak or the Steam-Bound Dwarves on quests that damage the environment.

### **4.0. The Divine Trial: Hunt the Wounded Land**

When the player's Affinity with Sylvana reaches the threshold, she will visit them in a dream of an endless, primeval forest. Her voice is the rustling of a billion leaves and the distant howl of a wolf. She will command the player to prove their worth by cleansing a piece of her wounded body.

The trial requires the player to track and hunt a **Blight-Corrupted Land-Titan**, a unique and colossal beast (like a giant tortoise or bear) that has become a walking vector for The Static's plague, sickening the very ground it walks on. The player must use tracking skills to find the beast, use their knowledge of alchemy to weaken it, and finally defeat it in combat. Upon its death, the beast's body will transform into a burst of new life, creating a permanent "Verdant Grove"—a small, safe area that slowly purifies the surrounding land and provides a source of rare alchemical plants.

### **5.0. Champion's Rewards**

Swearing allegiance to Sylvana makes the player her **Wild-Sworn Champion**.

#### **5.1. Passive Blessing: Hunter's Instinct**
You can now see the tracks of recently passed creatures highlighted in the world. Your movement through natural foliage (bushes, tall grass) no longer makes sound.

#### **5.2. Divine Boon Skill Tree: "Biomancy & Shamanism"**
This skill tree focuses on a primal connection to life, allowing the player to manipulate nature and command its beasts.

*   **Spirit Familiar (Active):** Summon a small, spectral animal companion (e.g., an owl, a fox, a serpent) that follows you. It cannot attack but provides a passive benefit based on its form (the owl highlights nearby enemies, the fox reveals traps, the serpent increases poison resistance).
*   **Heart of the Wild (Passive):** All crafted healing items (poultices, potions) are 25% more effective on you.
*   **One with the Pack (Passive):** Your primary tamed beast companion becomes more powerful, gaining increased health and damage, and inheriting a fraction of your own stats.
*   **Wrath of the Verdant Mother (Ultimate Active):** Target a location on the ground. After a short delay, massive, thorny roots erupt from the earth, ensnaring and damaging all enemies in a large area of effect.

#### **5.3. Associated Characters & Factions**
*   **Ideal Champions:** Dr. Elara Vance (The Naturalist).
*   **Allied Factions:** The Sylvan Elves venerate Sylvana as the highest form of divinity, and her champions will be seen as blessed messengers. The Free Settlers and other agrarian communities also respect her, even if they do not worship her as devoutly.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/03_The_Pantheon_of_Gods/02_Valdrak,_The_Iron_Father.md`
```md
# Pantheon File: Valdrak, The Iron Father

### **1.0. Identity and Domain**
*   **Title:** The Iron Father, The Forge Lord, The Great Artificer
*   **Domain:** Craft, Order, Civilization, Industry, Fortification, Endurance.
*   **Visual Symbol:** A gear interlocked with a hammer.
*   **Altar Appearance:** Altars to Valdrak are not ornate. They are functional and imposing: a perfectly cut block of obsidian or granite topped with a massive, unadorned anvil. They are often found in mountainous regions or at the heart of ruined fortifications.

### **2.0. Philosophy & Doctrine**

"**Order must be forged from chaos.**" This is the central tenet of Valdrak's philosophy. He is not a god of compassion or mercy; he is a god of relentless, unflinching **work**. He believes that strength is not an innate quality but something that is hammered into shape through pressure, fire, and toil. Weakness is not a sin to be punished, but a flaw to be burned away in the forge.

He despises The Static as the ultimate embodiment of lazy, purposeless decay—a force that simply unravels rather than builds. He is also wary of unrestrained nature (Sylvana) and pure chaos (Kaelus), viewing them as inefficient and disorderly systems that must be tamed and put to productive use by the thinking hands of civilization. His "followers" are not priests, but master artisans, engineers, and tireless builders.

### **3.0. Gaining & Losing Affinity**

#### **Actions that increase Affinity:**
*   Crafting an item of "Uncommon" (Green) rarity or higher for the first time.
*   Constructing an advanced fortification piece (e.g., a "Reinforced Stone Wall" or a metal gate).
*   Establishing a powered crafting station (e.g., a forge with bellows, an automated smelter).
*   Mining a rare or high-tier ore vein (e.g., Iron, Silver, Titanium).
*   Fully repairing a piece of damaged high-tier gear.

#### **Actions that decrease Affinity:**
*   Allowing your base's primary defenses to be breached and destroyed.
*   Failing a crafting attempt on a rare item due to low skill.
*   Letting a valuable tool or weapon break completely from low durability.
*   Siding with Kaelus, the god of chaos.

### **4.0. The Divine Trial: Igniting the Heart-Forge**

When the player's Affinity with Valdrak is high, he will appear to them in a vision of a cavern of pure metal, his voice the ringing of a thousand hammers. He will command them to find a legendary, dormant forge from a lost age—**The Heart-Forge of an ancient Dwarven kingdom**—and re-ignite it.

To do this, the player must venture into a volcano, fight their way to its caldera, and defeat a powerful **Magma Elemental**. They must then "capture" its still-burning heart in a specially crafted, obsidian-lined vessel. Returning to the Heart-Forge and placing the heart within it will complete the trial, turning the dungeon into a unique, high-tier crafting station for the player.

### **5.0. Champion's Rewards**

Swearing allegiance to Valdrak makes the player his **Forge-Sworn Champion**.

#### **5.1. Passive Blessing: Soul of the Forge**
Your crafted armor and weapons have +10% maximum durability. You no longer need to be at a workbench to perform basic field repairs on your gear.

#### **5.2. Divine Boon Skill Tree: "Technomancy"**
This skill tree focuses on enhancing crafting, creating constructs, and infusing technology with elemental power.

*   **Runic Reinforcement (Active):** An ability used at a forge. Imbues a piece of armor with a permanent bonus, such as "+10% Fire Resistance" or "+5% Stun Resistance," consuming rare runes in the process.
*   **Blueprint Genius (Passive):** All crafted items have a small chance to be created at one rarity tier higher than the recipe dictates.
*   **Geode Attunement (Passive):** You can now see the quality of an ore vein before you mine it, revealing its potential to contain rare gems.
*   **Forge Construct (Ultimate Active):** Requires a special altar at your base. Allows you to animate a single suit of heavy armor, creating a powerful but slow **"Iron Warden"** construct that will patrol and defend your base while you are away. It cannot follow you out into the world.

#### **5.3. Associated Characters & Factions**
*   **Ideal Champions:** Lena Petrova (The Pragmatist), Gunnar Hansen (The Foreman).
*   **Allied Factions:** The Hearth-Forged Dwarves revere Valdrak, and his champions will be welcomed in their halls as kin. The Steam-Bound Dwarves also see him as a patron of their industry, though their methods are more chaotic.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/02_WORLD_AND_NARRATIVE/03_The_Pantheon_of_Gods/01_Pantheon_Overview.md`
```md
# Pantheon Overview: The Architects of Reality

## **1.0. Core Philosophy: The Divine Patronage System**

The gods of the Shattered World are not distant, silent deities to be worshipped. They are active, powerful, and deeply invested forces in the world's fate. The Pantheon system is a core pillar of player progression and role-playing, allowing players to align themselves with a cosmic entity and gain immense power in exchange for service.

Choosing a patron god is a major, build-defining commitment. This choice is not made in a menu; it is earned through action and sealed through a sacred trial. The player's playstyle will naturally attract the attention of a god who shares their philosophy.

## **2.0. The Affinity System: Gaining Divine Favor**

**Affinity** is a hidden background value that tracks the player's actions as they relate to each god's domain and philosophy. Every significant action that aligns with a god's principles will increase your Affinity with them, while acting against their tenets may decrease it or increase it with a rival god.

*   **Valdrak (The Forge):** Affinity is gained by crafting high-quality items, building complex fortifications, and mining rare ores.
*   **Sylvana (Nature):** Affinity is gained by killing Blighted creatures, healing a sickened animal, or planting rare seeds. Over-hunting an area decreases Affinity.
*   **Kaelus (Chaos):** Affinity is gained by initiating fights against superior numbers, destroying symbols of order, and playing aggressively.
*   **Solana (Light):** Affinity is gained by helping innocent survivors, destroying undead, and venturing into dark places to bring light.
*   **Morgrath (Entropy):** Affinity is gained by using Entropic magic, desecrating holy sites, and choosing nihilistic or cruel dialogue options.

## **3.0. The Path to Patronage: The Divine Trial**

When a player's Affinity with a specific god reaches a critical threshold, that god will "reach out" to them, often through a vision, a strange omen, or an encounter with one of their agents. They will offer the player a chance to become their champion. To prove their worth, the player must complete a unique, challenging **Divine Trial.**

*   **The Trial:** This is a quest tailored specifically to the god's domain.
    *   *Valdrak's Trial:* Might involve traveling to a ruined, legendary forge and re-igniting it with the heart of a Fire Elemental.
    *   *Lyra's Trial:* Might involve resolving a conflict between two warring factions without bloodshed, perfectly balancing the scales.
*   **The Vow:** Upon completing the trial, the player is given a final, explicit choice to swear fealty to that god. This is a binding vow. **A player can only have one patron god at a time.** Swearing allegiance to one will make it impossible to serve others and may immediately make you an enemy of their divine rivals.

## **4.0. The Rewards of Patronage**

Becoming a god's champion is one of the most significant power-ups in the game.
1.  **Divine Boon Skill Tree:** The single greatest reward. The player unlocks a unique, powerful skill sub-tree on their main skill screen, themed to their patron. This grants new active abilities, passive bonuses, and playstyles.
2.  **Passive Blessings:** The player gains a subtle, permanent buff. (e.g., Kaelus's champions may have slightly faster attack speed; Fjolnir's may have higher damage resistance).
3.  **Divine Artifacts:** Your patron will guide you on exclusive quests to recover legendary weapons and armor that are imbued with their power.
4.  **Faction Alignment:** Followers of your patron god across the world will now recognize you as a holy champion, opening up new dialogue, barter, and quest opportunities.

## **5.0. The Pantheon Roster**

The following files in this folder will detail each of the major divine entities:

*   **02_Valdrak,_The_Iron_Father** (Order, Craft)
*   **03_Sylvana,_The_Verdant_Mother** (Nature, Life)
*   **04_Morgrath,_The_Shadowed_King** (Entropy, The Void)
*   **05_Lyra,_The_Silent_Weaver** (Fate, Balance)
*   **06_Kaelus,_The_Storm-Throat** (Chaos, Violence)
*   **07_Solana,_The_Ever-Burning_Sun** (Light, Zeal)
*   **08_Umbra,_The_Whispering_Moon** (Secrets, Stealth)
*   **09_Fjolnir,_The_Stone-Heart** (The Past, The Dead)
*   **10_Volo,_The_Wandering_Trickster** (Luck, Commerce)
*   **11_The_Axis_Mind** (The Static, Un-reality - an "Anti-God")
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/01_ENGINE_DESIGN/03_Engine_API_Reference.md`
```md
# Engine API Reference: Stelliferrum Forge v0.1

## **1.0. Core Purpose & Naming Conventions**
This document is the master Application Programming Interface (API) Reference. It defines the public functions exposed by each core engine module. All inter-module communication **must** adhere to this contract.

*   **Naming Convention:** Functions will be referenced by `ModuleName.FunctionName()`. For example, `Renderer.DrawSprite()`.
*   **Data Types:** Standard types like `int`, `float`, `string`, `bool` will be used.
    *   `Vector2`: An object containing `{x, y}` coordinates.
    *   `Vector3`: An object containing `{x, y, z}` coordinates.
    *   `Color`: An object containing `{r, g, b, a}` values (0-255).
    *   `EntityID`: A unique integer identifier for a game object.
    *   `AssetID`: A unique string identifier for a loaded asset (e.g., `"sprites/player.png"`).

---
## **2.0. The Core Engine API**

*   **Function:** `Engine.Shutdown()`
    *   **Description:** Initiates the engine shutdown sequence, saving any required data and closing the application.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function:** `Engine.GetDeltaTime()`
    *   **Description:** Returns the time, in seconds, that has passed since the last frame. Essential for creating frame-rate indexpendent movement and physics.
    *   **Parameters:** None.
    *   **Returns:** `float`.

---
## **3.0. Platform Module API**
*(Manages the OS-level window)*

*   **Function:** `Platform.GetWindowSize()`
    *   **Description:** Returns the current dimensions of the game window.
    *   **Parameters:** None.
    *   **Returns:** `Vector2` `{width, height}`.

---
## **4.0. Input Module API**
*(Manages all player input)*

*   **Function:** `Input.IsKeyDown(keyCode)`
    *   **Description:** Checks if a specific keyboard key is currently being held down.
    *   **Parameters:** `keyCode` (string, e.g., `"W"`, `"Space"`).
    *   **Returns:** `bool`.

*   **Function:** `Input.IsKeyPressed(keyCode)`
    *   **Description:** Checks if a specific keyboard key was just pressed down on *this frame only*. Essential for single-press actions like jumping or interacting.
    *   **Parameters:** `keyCode` (string).
    *   **Returns:** `bool`.

*   **Function:** `Input.IsMouseButtonDown(buttonCode)`
    *   **Description:** Checks if a mouse button is currently held down.
    *   **Parameters:** `buttonCode` (int, `0`=Left, `1`=Right, `2`=Middle).
    *   **Returns:** `bool`.

*   **Function:** `Input.GetMousePosition()`
    *   **Description:** Returns the current (X, Y) pixel coordinates of the mouse cursor relative to the window.
    *   **Parameters:** None.
    *   **Returns:** `Vector2`.

---
## **5.0. Renderer Module API**
*(Manages all drawing to the screen)*

*   **Function:** `Renderer.BeginFrame()`
    *   **Description:** Prepares the renderer for a new frame. Should be called once at the start of the rendering phase. Clears the screen to a default color.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function:** `Renderer.EndFrame()`
    *   **Description:** Finishes the rendering process and displays the completed frame on the screen.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function:** `Renderer.DrawSprite(assetID, position, scale, rotation, color)`
    *   **Description:** Draws a 2D sprite to the screen.
    *   **Parameters:**
        *   `assetID` (AssetID): The unique identifier for the loaded image asset.
        *   `position` (Vector2): The world-space coordinate to draw the sprite's center.
        *   `scale` (Vector2, optional, default=`{1,1}`): The horizontal/vertical scale.
        *   `rotation` (float, optional, default=`0`): Rotation in degrees.
        *   `color` (Color, optional, default=`white`): A color tint to apply to the sprite.
    *   **Returns:** `void`.

*   **Function:** `Renderer.DrawText(text, position, fontID, size, color)`
    *   **Description:** Renders text to the screen. For UI elements.
    *   **Parameters:**
        *   `text` (string): The text to be displayed.
        *   `position` (Vector2): The screen-space pixel coordinate for the text's top-left corner.
        *   `fontID` (AssetID): The identifier for the loaded font asset.
        *   `size` (int): The font size.
        *   `color` (Color): The color of the text.
    *   **Returns:** `void`.

*   **Function:** `Renderer.SetCameraPosition(position)`
    *   **Description:** Sets the world-space position that the camera should be centered on.
    *   **Parameters:** `position` (Vector2).
    *   **Returns:** `void`.

---
## **6.0. Asset Manager API**
*(Manages loading/unloading of all game assets)*

*   **Function:** `Assets.LoadTexture(filePath)`
    *   **Description:** Loads an image file from disk into memory and assigns it a unique ID. If already loaded, it just returns the existing ID.
    *   **Parameters:** `filePath` (string, e.g., `"sprites/player.png"`).
    *   **Returns:** `AssetID` (which is often just the file path string itself).

*   **Function:** `Assets.LoadSound(filePath)`
    *   **Description:** Loads a sound file from disk into memory.
    *   **Parameters:** `filePath` (string, e.g., `"sfx/footstep.wav"`).
    *   **Returns:** `AssetID`.

---
## **7.0. Audio Module API**
*(Manages playing sounds and music)*

*   **Function:** `Audio.PlaySound(assetID, volume)`
    *   **Description:** Plays a loaded sound effect once.
    *   **Parameters:**
        *   `assetID` (AssetID): The identifier of the sound to play.
        *   `volume` (float, optional, default=`1.0`): The volume from 0.0 to 1.0.
    *   **Returns:** `void`.

*   **Function:** `Audio.PlayMusic(assetID, volume, loop)`
    *   **Description:** Plays a music track. Fades out any currently playing music.
    *   **Parameters:**
        *   `assetID` (AssetID).
        *   `volume` (float, optional, default=`1.0`).
        *   `loop` (bool, optional, default=`true`).
    *   **Returns:** `void`.

---
## **8.0. Physics Module API**
*(Manages all physical interactions)*

*   **Function:** `Physics.CreateBody(entityID, position, shape, type)`
    *   **Description:** Adds a physical body for an entity to the physics simulation.
    *   **Parameters:**
        *   `entityID` (EntityID): The entity to associate this body with.
        *   `position` (Vector2): The initial world position.
        *   `shape` (object, e.g., `{type:'circle', radius:16}` or `{type:'box', width:32, height:32}`): The collision shape.
        *   `type` (string, e.g., `"static"`, `"dynamic"`): Static bodies don't move; dynamic bodies are affected by forces.
    *   **Returns:** `bool` (success).

*   **Function:** `Physics.ApplyForce(entityID, forceVector)`
    *   **Description:** Applies a directional force to a dynamic body. The primary way game logic interacts with physics.
    *   **Parameters:** `entityID` (EntityID), `forceVector` (Vector2).
    *   **Returns:** `void`.

*   **Function:** `Physics.GetPosition(entityID)`
    *   **Description:** Gets the current position of an entity as determined by the physics simulation. The renderer will use this to know where to draw the entity.
    *   **Parameters:** `entityID` (EntityID).
    *   **Returns:** `Vector2`.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/01_ENGINE_DESIGN/01_Engine_Overview_and_Philosophy.md`
```md
# Engine Overview & Philosophy: The Stelliferrum Forge

## **1.0. Core Mission Statement**

This document outlines the guiding principles for the development of the **Stelliferrum Forge**. Our mission is to forge a **lightweight, custom-built, and highly specialized** game engine. It will not compete with generic engines. Instead, it is being architected from the ground up to serve one unifying, foundational principle:

**The Principle of Physicality: Everything Has Weight.**

Every object, action, and even phenomenon in our world is governed by a simulated **mass and material density**. From the heft of a greatsword, to the structural integrity of a fortress, to the very propagation of sound itself—everything is a calculation of weight, impact, and material response. This principle dictates all other design pillars.

## **2.0. The Five Pillars of Development**

#### **2.1. Pillar 1: Simulated Mass & Materiality (The Foundation)**
*   **The What:** Every entity in the world has a defined `mass` and `material_type`. A wooden arrow has less mass than a steel bolt. A stone wall is denser than a wooden one.
*   **The Why:** This creates a predictable, physics-driven world. It governs everything: how much damage a weapon does, how much support a pillar can provide, and how sound travels. It is the core of our simulation.

#### **2.2. Pillar 2: Acoustic Mass & Resonance (The "Echolocation" System)**
*   **The What:** Sound is not an abstract event; it is a physical phenomenon. A sound event generates a cloud of massless "Phonon" particles, each with a quantifiable `acoustic_mass`. These particles travel through the world, losing mass over distance, and creating sound upon impact with a collidable object.
*   **The Why:** This unifies sound design with the core physics engine, creating a deeply immersive and realistic 3D audio environment. The sound of rain on a tin roof is different from rain on mud because the *material properties* of the roof and mud react differently to the "weight" of the raindrop's sound.

#### **2.3. Pillar 3: Structural Integrity & Weight Distribution**
*   **The What:** The base building system is a direct extension of the core principle. Every building piece has a `mass` and a `load_bearing_capacity`. A structure will stand only if the pieces below it can support the cumulative weight of the pieces above them.
*   **The Why:** This makes engineering a real gameplay challenge. Players cannot build impossibly large structures on flimsy foundations. Sieges become more tactical, as destroying a single, critical support pillar can bring an entire tower crashing down in a satisfying, physics-based cascade.

#### **2.4. Pillar 4: Intelligent Rendering & Photography-Inspired Lighting**
*   **The What:** The renderer is built to make our physical world beautiful. It leverages aggressive culling, multi-tiered LODs, and a "Progressive Refinement" system that uses idle processing power to enhance shadow and light quality when the player is still, rewarding observation.
*   **The Why:** This allows us to achieve moments of breathtaking, "screenshot-worthy" beauty without needing to render at that quality 100% of the time, keeping the engine lightweight.

#### **2.5. Pillar 5: LLM-Assisted Architecture & Radical Modularity**
*   **The What:** The engine is built from discrete, modular components with clean APIs. This modularity is designed specifically for LLM integration. We will create data-driven systems where an LLM can easily generate content (items, quests, lore) that fits into pre-defined, validated templates.
*   **The Why:** This is our force multiplier. It allows a small, creative team to generate a vast, rich world by offloading the creation of structured data to an AI partner, while the human developer focuses on the core systems and creative vision.

```

### File: `/TOP_SECRET_GAME_DEV_DOCS/01_ENGINE_DESIGN/02_ENGINE_MODULES/09_Asset_Pipeline.md`
```md
# Engine Module: Asset Pipeline

## **1.0. Module Overview**

The **Asset Pipeline** is the engine's data preparation and management system. Its responsibility is to take raw, source-format assets (like `.png` textures, `.obj` models, or `.wav` sounds) and convert them into a clean, optimized, engine-native format that can be loaded into the game with maximum efficiency.

This module is not a single real-time system, but rather a combination of an **offline processing tool** and a run-time **Asset Manager**.

**Core Philosophy:** The engine at runtime should **never** have to deal with raw, unoptimized source files. Loading a `.png` and decompressing it on the fly is slow. Parsing a complex `.gltf` model file during a loading screen is inefficient. The Asset Pipeline does all this heavy lifting **ahead of time**, during the development process. The result is faster loading times, lower memory usage, and a smoother in-game experience.

## **2.0. The Two-Stage Process**

#### **Stage 1: The Offline Asset Processor (The "Cooker")**
This is a separate command-line tool that we will build. It is not part of the game executable. The developer runs this tool whenever new creative assets are added or changed.
*   **Function:** It scans a "raw_assets" directory, finds any new or modified files, and processes them.
    *   **For Textures:** It might convert a large `.png` file into a compressed texture format (like `.dds`) and generate mipmaps (smaller versions of the texture for objects in the distance).
    *   **For 3D Models:** It will parse the complex `.obj` or `.gltf` file and convert it into a simple, engine-native binary format that contains only the vertex and indexx data the GPU needs, organized for optimal memory layout.
    *   **For Audio:** It will convert a large `.wav` file into a compressed format like `.ogg`.
*   **Output:** The Processor outputs these optimized, "cooked" files into a "packaged_assets" directory that will be shipped with the final game. It also generates a master "asset manifest" file, which is a list of all available assets and where to find them.

#### **Stage 2: The Runtime Asset Manager**
This is the module that runs inside the game engine.
*   **Function:** Its job is simple: load the "cooked" assets from the packaged directory into memory when they are needed.
*   **Responsibilities:**
    *   **Loading & Unloading:** Provides the API for the rest of the engine to request an asset.
    *   **Reference Counting:** It keeps track of how many systems are currently using a specific asset. When an asset is no longer needed by anyone (e.g., leaving a level), its memory is freed up. This prevents memory leaks.
    *   **Asset Pooling:** It ensures that the same asset is never loaded into memory more than once. If three different enemies use the same "goblin.png" texture, the Asset Manager loads it once and gives all three of them a pointer to the same piece of memory.

## **3.0. Asset Naming and ID System**

To keep things simple and human-readable, an asset's unique identifier **(AssetID)** will simply be its relative file path from the root assets directory. This is an intuitive and powerful way to manage assets without needing complex ID numbers.

*   **Example AssetIDs:**
    *   `"textures/armor/iron_plate_albedo.dds"`
    *   `"models/characters/player.mesh"`
    *   `"audio/sfx/weapons/sword_swing.ogg"`
    *   `"fonts/main_menu_font.ttf"`

## **4.0. Module API Functions (The Runtime Asset Manager)**

These functions provide a clean interface for the rest of the engine to request assets without needing to know about the underlying file system or cooking process.

*   **Function: `Assets.Load(assetID)`**
    *   **Description:** The primary generic loading function. The Asset Manager will determine the asset type based on its file extension or manifest data and load it into the correct memory pool (texture memory, vertex buffer, etc.).
    *   **Parameters:** `assetID` (AssetID, a string path).
    *   **Returns:** `bool` (success). This function works asynchronously in the background.

*   **Function: `Assets.Unload(assetID)`**
    *   **Description:** Decrements the reference count for an asset. If the count reaches zero, the asset is removed from memory.
    *   **Parameters:** `assetID` (AssetID).
    *   **Returns:** `void`.

*   **Function: `Assets.IsLoaded(assetID)`**
    *   **Description:** A quick check to see if an asset has finished its background loading and is ready to be used.
    *   **Parameters:** `assetID` (AssetID).
    *   **Returns:** `bool`.

*   **Function: `Assets.Get(assetID)`**
    *   **Description:** Returns a handle or pointer to the actual asset data in memory that can be passed to other modules like the Renderer or Audio Engine. Will fail if `Assets.IsLoaded()` is false.
    *   **Parameters:** `assetID` (AssetID).
    *   **Returns:** `AssetHandle` (an internal engine object or pointer).

This pipeline creates a robust, professional workflow. Artists and designers can work with standard, user-friendly file formats, and the automated "cooker" ensures that the game engine only ever has to deal with perfectly optimized, ready-to-use data.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/01_ENGINE_DESIGN/02_ENGINE_MODULES/08_UI_System.md`
```md
# Engine Module: UI System

## **1.0. Module Overview**

The **UI System** is responsible for rendering and managing all User Interface elements, from the in-game Heads-Up Display (HUD) to complex inventory screens and dialogue boxes. This module translates game data (like player health or item lists) into visual elements (health bars, icons) that the player can understand and interact with.

**Core Philosophy:** Our UI system will be **declarative and data-driven**. We will avoid "hard-coding" UI layouts in the game logic. Instead, we will define the structure, position, and appearance of our UI in external data files (like XML or a custom format). The UI System's job is to read these layout files, create the corresponding elements, and update them based on the game's state. This makes iteration and redesign dramatically faster.

## **2.0. Key Responsibilities**

*   **Widget Rendering:** To render a variety of standard UI elements ("widgets"), such as panels, buttons, text labels, sliders, and progress bars.
*   **Layout Management:** To parse layout files and position widgets on the screen correctly, handling different screen resolutions and aspect ratios gracefully.
*   **Input Handling:** To process mouse clicks and keyboard navigation within UI screens, determining which widget is being interacted with. It will capture input so that clicks on the UI don't affect the game world behind it.
*   **State Management:** To manage which UI "screens" are currently active (e.g., Inventory, Map, Pause Menu) and handle the transitions between them.
*   **Data Binding:** To link UI elements to live game data. For example, a "Health Bar" widget will be bound to the player's health attribute, automatically updating its visual state as the player takes damage.

## **3.0. System Architecture: The Widget Tree**

The UI will be structured as a **tree of widgets**. This hierarchical system allows for complex layouts to be built from simple components.

*   **Canvas (The Root):** The root of every UI screen. It covers the entire screen and all other widgets are its "children."
*   **Panel (The Container):** An invisible container used to group other widgets. A panel can be used to create a "window" for an inventory screen or a "row" for hotbar slots.
*   **Widget (The Element):** The individual, visible elements.
    *   **Text Label:** Displays static or dynamic text.
    *   **Image/Icon:** Displays a static texture.
    *   **Button:** An interactable image or text that triggers an event when clicked.
    *   **Progress Bar:** A bar that can be filled, used for health, stamina, or loading indicators.
    *   **Slider:** A control for adjusting a value, used in settings menus.
    *   **Grid:** A container that automatically arranges its children into a grid, perfect for inventory slots.

**Example Layout (Declarative pseudo-code):**
```xml
<Canvas>
  <Panel id="PlayerHUD" position="bottom-left">
    <ProgressBar id="HealthBar" binding="Player.Health" size="200, 20" />
    <ProgressBar id="StaminaBar" binding="Player.Stamina" position="0, 25" size="150, 15" />
  </Panel>
  <Panel id="PauseMenu" visible="false">
    <Button text="Resume" onClick="StateManager.SetState(IN_GAME)" />
    <Button text="Quit" onClick="Engine.Shutdown()" />
  </Panel>
</Canvas>
```
The UI system parses this "code," creates the widgets, and handles their visibility and events.

## **4.0. Module API Functions**

The game logic will interact with the UI system through a high-level API, mostly for showing/hiding screens and sending events.

*   **Function: `UI.LoadScreen(layoutFile)`**
    *   **Description:** Loads a UI layout file from disk and creates the widget tree, but does not display it yet.
    *   **Parameters:** `layoutFile` (string, e.g., `"layouts/hud.xml"`).
    *   **Returns:** `ScreenID`.

*   **Function: `UI.ShowScreen(screenID)`**
    *   **Description:** Makes a loaded screen visible and active, adding it to the update/render list.
    *   **Parameters:** `screenID` (ScreenID).

*   **Function: `UI.HideScreen(screenID)`**
    *   **Description:** Hides a screen, deactivating it.
    *   **Parameters:** `screenID` (ScreenID).

*   **Function: `UI.SendEvent(eventName, data)`**
    *   **Description:** A way for game logic to send data or trigger animations in the UI. For example, when the player picks up an item, the game logic would call `UI.SendEvent("PlayerInventoryUpdated", { ...new inventory data... })`. The UI system then ensures any visible inventory screen updates itself.
    *   **Parameters:** `eventName` (string), `data` (Object).

*   **Function: `UI.BindData(widgetID, data_source)`**
    *   **Description:** A lower-level function used during layout loading to link a widget's property (like a progress bar's `fill_amount`) to a source of game data. This is the heart of the data-binding system.
    *   **Parameters:** `widgetID` (string), `data_source` (Object/function pointer).

This architecture creates a powerful, flexible, and decoupled UI system that is easy to iterate on without needing to constantly recompile game code. We can change the entire layout of the main menu just by editing a single text file.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/01_ENGINE_DESIGN/02_ENGINE_MODULES/07_Audio_Engine.md`
```md
# Engine Module: Audio Engine

## **1.0. Module Overview**

The **Audio Engine** is the soul and voice of the Stelliferrum Forge. Its responsibility is to manage and play all sound within the game world, from the quietest footstep to the most thunderous explosion and the most sweeping musical score. This module's primary design goals are to create a **deeply immersive ambient soundscape** and to provide a **dynamic, responsive musical experience.**

**Core Philosophy:** Audio is a key driver of emotion and player feedback. Our engine will treat sound with the same level of importance as graphics. We will focus on creating a high-fidelity experience, particularly for environmental audio like rain and wind, and a music system that adapts seamlessly to the player's actions. We will almost certainly use a robust third-party audio library (like **FMOD** or **Wwise**) as a backend to handle the complex mixing and effects, while our engine code will act as the "director," telling the library what to play and when.

## **2.0. Key Responsibilities**

*   **Sound Playback:** To play, pause, stop, and loop both 2D (UI) and 3D (world-space) sounds.
*   **3D Positional Audio:** To accurately simulate the position of a sound in 3D space. A sound originating from the left should be heard in the left speaker.
*   **Attenuation (Distance):** To decrease the volume of a sound as the player moves further away from its source. This is a critical feature you requested.
*   **Dynamic Music System:** To manage and transition between different musical "states" based on the gameplay context (e.g., Exploration, Combat, Boss Fight).
*   **Audio Mixing & Effects:** To manage different audio channels (e.g., Music, SFX, Dialogue) and apply environmental effects like reverb in caves or muffling sounds through walls.

## **3.0. Dynamic & Ambient Sound Systems**

#### **3.1. The Ambiance & Weather System**
This is a top priority. The goal is to make the player *feel* the environment through sound.
*   **Layered Ambiance:** The background sound will be constructed from multiple layers. For example, a forest might have:
    *   `Layer 1: Base Wind` (a constant, gentle air tone)
    *   `Layer 2: Foliage Rustle` (the sound of wind in the trees, which gets louder as the wind picks up)
    *   `Layer 3: Distant Wildlife` (periodic, randomized bird calls or insect chirps)
*   **Dynamic Rain:** Your core request. Rain will not be a single sound file. It will be a dynamic, multi-layered system.
    *   **Light Drizzle:** A soft, high-frequency "hiss."
    *   **Heavy Rain:** Adds a deeper, more powerful layer with more bass.
    *   **Surface Impacts:** A separate layer of sound will be dedicated to the sound of raindrops hitting the surface the player is standing under. This is key. The sound of rain on a tent roof will be different from the sound of it on a metal roof, which will be different from the sound of it on forest leaves.
    *   **Indoor Muffling:** When the player enters an enclosed space, the "exterior" rain layers will be heavily muffled and low-passed, while the "interior" impact layer on the roof becomes the dominant sound. This creates a powerful sense of shelter.

#### **3.2. The Dynamic Music System**
This system uses a "state machine" to transition between musical cues seamlessly.
*   **Music States:**
    *   **`Exploration`:** Calm, atmospheric, and often minimalist music that complements the current biome.
    *   **`Tension`:** Triggered when a single enemy is alerted but has not yet fully detected the player. A low, pulsing bassline or a single sustained string note is added to the Exploration track.
    *   **`Combat (Standard)`:** Triggered when the Hunting state begins. A percussive, high-energy track with multiple layers kicks in. As more enemies join the fight, more layers (e.g., more drums, brass stabs) are added to increase the intensity.
    *   **`Combat (Boss)`:** A unique, epic track specifically composed for each major boss encounter.
*   **Transitions:** The system will use intelligent transitions (e.g., a "sting" like a cymbal crash or a drum fill) to move between states without feeling jarring. When combat ends, the music will fade to an "outro" stem before gracefully returning to the Exploration track.

## **4.0. Module API Functions**

*   **Function: `Audio.PlaySound2D(assetID, volume)`**
    *   **Description:** Plays a simple, non-positional sound. Used for UI elements like button clicks.
    *   **Parameters:** `assetID` (AssetID), `volume` (float).

*   **Function: `Audio.PlaySound3D(assetID, position, volume, radius)`**
    *   **Description:** Plays a sound effect at a specific location in the 3D world.
    *   **Parameters:**
        *   `assetID` (AssetID).
        *   `position` (Vector3): The world coordinate of the sound's source.
        *   `volume` (float).
        *   `radius` (float): The distance at which the sound will no longer be audible (attenuation).

*   **Function: `Audio.PlayMusic(trackID, fade_duration)`**
    *   **Description:** A high-level command. Tells the Dynamic Music System to transition to a new track or state (e.g., `trackID` could be `"Combat_Orcs"`).
    *   **Parameters:** `trackID` (string), `fade_duration` (float, in seconds).

*   **Function: `Audio.SetMusicState(newState)`**
    *   **Description:** The primary function for dynamic music. Tells the system to shift its intensity.
    *   **Parameters:** `newState` (enum, e.g., `MUSIC_STATE_EXPLORE`, `MUSIC_STATE_TENSION`, `MUSIC_STATE_COMBAT`).

*   **Function: `Audio.SetGlobalParameter(paramName, value)`**
    *   **Description:** A powerful function for controlling the overall audio mix.
    *   **Parameters:**
        *   `paramName` (string, e.g., `"IsInside"`, `"RainIntensity"`).
        *   `value` (float, e.g., `1.0` for true, `0.75` for heavy rain).
    *   **Example Usage:** `Audio.SetGlobalParameter("IsInside", 1.0);` // This would tell the audio backend (FMOD/Wwise) to apply the "muffled" effect to all outdoor sounds.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/01_ENGINE_DESIGN/02_ENGINE_MODULES/06_Physics_Engine.md`
```md
# Engine Module: Physics Engine

## **1.0. Module Overview**

The **Physics Engine** is responsible for simulating the physical laws of the game world. It manages motion, collision detection, and collision resolution for all relevant game objects. This module is what makes a sword strike feel impactful, a fall feel dangerous, and a "Telekinesis" spell feel powerful.

**Core Philosophy:** Our physics engine is built for **performance and gameplay feel, not perfect scientific accuracy.** We will prioritize fast, stable, and predictable physics that support our game's mechanics, particularly the dynamic magic system. We will likely use a lightweight, established third-party physics library (like **Box2D** for 2D, or a simplified 3D library) as a foundation and build our gameplay-specific logic on top of it. This follows our philosophy of not reinventing the wheel for complex, universal problems.

## **2.0. Key Responsibilities**

*   **Rigid Body Simulation:** To manage the state of all physical objects ("bodies"), including their position, rotation, velocity, and mass.
*   **Collision Shape Management:** To associate each physical body with a simplified collision shape (e.g., box, sphere, capsule, polygon mesh) for fast and efficient collision checks.
*   **Collision Detection:** To identify when the collision shapes of two or more objects are intersecting. This is the most computationally expensive part of the simulation.
*   **Collision Resolution:** To calculate and apply the appropriate response to a collision, such as making objects bounce off each other or applying damage.
*   **Force & Impulse Application:** To provide a simple API for other systems to apply forces (a push over time) and impulses (an instantaneous "kick") to objects. This is the primary way the rest of the engine interacts with the physics simulation.
*   **Callbacks & Events:** To notify the game logic when a collision occurs (e.g., "Player's sword just hit Enemy #5").

## **3.0. The Physics "World" & Simulation Loop**

The Physics Engine maintains its own internal representation of the world, often called a "physics world" or "scene." This world only contains the physical properties of objects, not their visual models or game logic.

1.  **Synchronization:** At the beginning of each frame's update, the game logic updates the state of any "kinematic" or player-controlled bodies in the physics world.
2.  **Simulation Step (`Physics.Update()`):** The engine then calls the main `Update` function of the physics module. This function advances the simulation forward by a fixed timestep (`deltaTime`). Inside this step, the physics library performs its "black box" magic: it applies gravity, detects all collisions, and resolves them.
3.  **Callbacks:** During the simulation step, if a collision occurs that the game logic has "subscribed" to, the Physics Engine will immediately call back to the game logic, passing it information about the collision. This is how we apply damage.
4.  **Data Retrieval:** After the simulation step is complete, the `Renderer` and other modules can then query the Physics Engine (`Physics.GetPosition()`) to get the new, updated positions and rotations of all dynamic objects so they can be drawn correctly.

## **4.0. Module API Functions**

These public-facing functions allow the game to set up, manipulate, and query the physics simulation.

*   **Function: `Physics.CreateBody(entityID, body_definition)`**
    *   **Description:** The primary function for adding a new object to the physics world.
    *   **Parameters:**
        *   `entityID` (EntityID): The unique identifier for the game entity this body represents.
        *   `body_definition` (Object): A data structure containing all necessary information, such as:
            *   `type`: (e.g., "static", "dynamic", "kinematic")
            *   `position`: (Vector3)
            *   `shape`: (e.g., `{type:'box', size:{x,y,z}}` or `{type:'sphere', radius:r}`)
            *   `mass`: (float)
            *   `friction`: (float)
            *   `restitution`: (float, "bounciness")
    *   **Returns:** `bool` (success).

*   **Function: `Physics.DestroyBody(entityID)`**
    *   **Description:** Removes an object's physical body from the simulation.
    *   **Parameters:** `entityID` (EntityID).
    *   **Returns:** `void`.

*   **Function: `Physics.ApplyForce(entityID, forceVector, pointOfApplication)`**
    *   **Description:** Applies a continuous force to the center of mass of a dynamic body.
    *   **Parameters:** `entityID` (EntityID), `forceVector` (Vector3). `pointOfApplication` (Vector3, optional).

*   **Function: `Physics.ApplyImpulse(entityID, impulseVector, pointOfApplication)`**
    *   **Description:** Applies an instantaneous "kick" to a dynamic body. Used for explosions, weapon impacts, and jumps.
    *   **Parameters:** `entityID` (EntityID), `impulseVector` (Vector3). `pointOfApplication` (Vector3, optional).

*   **Function: `Physics.SetTransform(entityID, position, rotation)`**
    *   **Description:** Manually overrides the position and rotation of a physics body. Used for teleporting or setting the position of player-controlled characters.
    *   **Parameters:** `entityID` (EntityID), `position` (Vector3), `rotation` (Quaternion/Vector3).

*   **Function: `Physics.GetTransform(entityID)`**
    *   **Description:** Retrieves the current position and rotation of a physics body after the simulation step.
    *   **Parameters:** `entityID` (EntityID).
    *   **Returns:** `Object` `{position: Vector3, rotation: Quaternion/Vector3}`.

*   **Function: `Physics.Raycast(startPoint, endPoint)`**
    *   **Description:** Casts a virtual line (a "ray") from a start point to an end point and returns the first object it hits. Essential for things like bullet detection or determining what the player is looking at.
    *   **Parameters:** `startPoint` (Vector3), `endPoint` (Vector3).
    *   **Returns:** `Object` `{hit: bool, entityID: EntityID, hitPoint: Vector3}`.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/01_ENGINE_DESIGN/02_ENGINE_MODULES/05_3D_Renderer.md`
```md
# Engine Module: 3D Renderer

## **1.0. Module Overview**

The **3D Renderer** is the evolutionary next step for the Stelliferrum Forge's visual capabilities. Its responsibility is to render complex 3D models, manage a 3D camera, and, most importantly, implement the **world-class lighting engine** that is a core pillar of our design philosophy. This module will eventually replace the `2D_Renderer` for all in-world rendering, though the 2D module may still be used for UI overlays.

**Core Philosophy:** Our 3D renderer is not a "brute-force" engine. It is an **"Intelligent Renderer"** that uses clever, modern techniques to achieve breathtaking visuals on a lightweight framework. Our primary focus is on the **artistry of light and shadow**, not on rendering an arbitrarily high number of polygons.

## **2.0. Phased Development Roadmap**

The development of this module will occur in clear, iterative phases. Each phase will build upon the last, ensuring we always have a functional base.

*   **Phase 1: The Basics** - Getting a 3D model on screen.
*   **Phase 2: The World** - Rendering a simple landscape and implementing culling/LODs.
*   **Phase 3: The Light** - Implementing the core lighting model. This is the most critical phase.
*   **Phase 4: The Beauty** - Adding advanced post-processing and the "Progressive Refinement" system.

## **3.0. Key Systems & Responsibilities**

#### **3.1. 3D Model & Mesh Handling**
*   **Responsibility:** To load 3D model data (vertices, normals, UVs) from standard file formats (like `.obj` or `.gltf`).
*   **Functionality:** Will manage vertex buffers, indexx buffers, and send this geometric data to the GPU for rendering.

#### **3.2. Material & Texture System**
*   **Responsibility:** To manage the "surfaces" of 3D models. A material defines how a surface reacts to light.
*   **Functionality:** A material will be a collection of textures:
    *   **Albedo/Diffuse Map:** The base color of the object.
    *   **Normal Map:** Adds the illusion of fine surface detail (like bumps and scratches) without adding more polygons.
    *   **Metallic/Roughness Maps:** The core of Physically-Based Rendering (PBR), defining how metallic a surface is and how polished it is.

#### **3.3. 3D Camera System**
*   **Responsibility:** To manage the player's viewpoint in 3D space.
*   **Functionality:** Will control the camera's position, rotation (pitch/yaw), and Field of View (FOV). It generates the "View" and "Projection" matrices that tell the GPU how to transform 3D world coordinates into a 2D image.

#### **3.4. The Lighting Engine (The Crown Jewel)**
*   **Responsibility:** To simulate the interaction of light with the world's surfaces. This is our area of excellence.
*   **Functionality:**
    *   **Light Types:** Will support different types of lights, each with its own properties:
        *   `Directional Light`: A single, infinitely distant light source used to simulate the sun or moon.
        *   `Point Light`: A light that radiates outwards from a single point, like a torch or a lantern.
        *   `Spot Light`: A cone of light, like a flashlight.
    *   **Shadow Mapping:** A core technique for generating dynamic shadows from our light sources.
    *   **PBR Shaders:** The lighting calculations will adhere to Physically-Based Rendering principles, ensuring materials look realistic and consistent under different lighting conditions.

#### **3.5. Intelligent Culling & LOD System**
*   **Responsibility:** To ensure we are not trying to render the entire world every frame.
*   **Functionality:**
    *   **Frustum Culling:** Objects outside the camera's view cone are not drawn.
    *   **Occlusion Culling:** Objects hidden behind other objects (like a mountain) are not drawn.
    *   **Level of Detail (LODs):** Manages the swapping of high-poly models for low-poly versions at a distance.
    *   **Impostors:** Manages the final swap from a 3D model to a 2D image for objects on the far horizon.

## **4.0. Module API Functions (Conceptual)**

The 3D Renderer's API will be more complex, centered on a "Scene Graph" or a similar entity-component system. Here is a high-level concept of its functions.

*   **Function: `Renderer3D.SubmitStaticMesh(modelID, materialID, transform)`**
    *   **Description:** Submits a static (unmoving) 3D model to the scene to be rendered.
    *   **Parameters:**
        *   `modelID` (AssetID): The identifier for the loaded 3D model.
        *   `materialID` (AssetID): The identifier for the material to apply.
        *   `transform` (Matrix4x4): The model's position, rotation, and scale in the world.
    *   **Returns:** `EntityID`.

*   **Function: `Renderer3D.UpdateDynamicMesh(entityID, transform)`**
    *   **Description:** Updates the position/rotation of a moving entity for the next frame.

*   **Function: `Renderer3D.CreatePointLight(position, color, radius, intensity)`**
    *   **Description:** Adds a new point light to the lighting simulation.
    *   **Returns:** `LightID`.

*   **Function: `Renderer3D.UpdateDirectionalLight(direction, color, intensity)`**
    *   **Description:** Updates the properties of the main sun/moon light source, used for the day/night cycle.

*   **Function: `Renderer3D.SetCamera(position, rotation, FOV)`**
    *   **Description:** Sets the camera's properties for the next frame.

This architectural plan lays the foundation for a powerful and intelligent rendering system, capable of delivering on the project's ambitious visual goals through smart design rather than sheer brute force.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/01_ENGINE_DESIGN/02_ENGINE_MODULES/04_2D_Renderer.md`
```md
# Engine Module: 2D Renderer

## **1.0. Module Overview**

The **2D Renderer** is the primary graphics module for the initial versions of the Stelliferrum Forge. Its responsibility is to take abstract drawing commands (e.g., "draw this sprite at this position") and translate them into low-level instructions that the GPU can understand and display on the screen. It is the "Anvil" upon which our game's visual identity will be forged.

**Core Philosophy:** The renderer should be simple, efficient, and versatile. Our initial goal is not complex 3D scenes, but a highly optimized pipeline for drawing thousands of 2D sprites (for characters, items, and UI) and text elements per frame. This forms the foundation for all future 3D enhancements.

## **2.0. Key Responsibilities**

*   **Render Pipeline Management:** To control the entire sequence of a render frame, from clearing the screen to presenting the final image.
*   **Sprite Batching:** To group thousands of individual draw calls into a small number of large "batches." This is the single most important optimization for a 2D renderer. Instead of telling the GPU "draw this sprite, now this sprite, now this sprite...", we tell it "draw all 500 of these sprites at once."
*   **Camera & Coordinate Systems:** To manage the 2D camera, which determines what part of the "world" is visible. It will handle the translation between world coordinates (where a character is in the game world) and screen coordinates (where it is drawn in the window).
*   **Shader Management:** To load, compile, and apply simple GLSL/HLSL shader programs. Initially, this will be a basic shader for drawing textured sprites, but this system will be the gateway to all future advanced lighting and visual effects.
*   **Text Rendering:** To take text strings and render them to the screen using loaded font atlases.

## **3.0. The Rendering Pipeline (Simplified)**

Within the main game loop, the renderer's job is split into three phases:

1.  **`Renderer.BeginFrame()`:** Called once at the start of the render phase. This function prepares the GPU by:
    *   Clearing the previous frame's image (e.g., setting the background to black).
    *   Setting up the camera's view matrix based on its position and zoom.
    *   Starting a new "batch" for drawing sprites.

2.  **Drawing Commands (`DrawSprite`, `DrawText`, etc.):** Throughout the render phase, other game systems will call the renderer's public functions. These functions do not immediately draw to the screen. Instead, they add the sprite's data (position, texture, color) to the current batch in memory.

3.  **`Renderer.EndFrame()`:** Called once at the end of the render phase. This is where the real work happens.
    *   **Flush Batch:** The renderer takes the entire batch of sprite data that was collected during the frame and sends it to the GPU in a single, large draw call.
    *   **Swap Buffers:** Calls `Platform.SwapBuffers()` to present the newly drawn image to the screen.

## **4.0. Module API Functions**

These are the public-facing functions that the game logic and state manager will use to draw things.

*   **Function: `Renderer.BeginFrame()`**
    *   **Description:** Prepares for a new frame. Clears the screen and sets up the camera.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function: `Renderer.EndFrame()`**
    *   **Description:** Flushes any pending draw calls and presents the final image to the window.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function: `Renderer.DrawSprite(assetID, position, size, options)`**
    *   **Description:** The primary workhorse function. Adds a sprite to the current rendering batch.
    *   **Parameters:**
        *   `assetID` (AssetID): The unique identifier for the loaded texture.
        *   `position` (Vector2): The world-space coordinate `{x, y}` for the sprite's center.
        *   `size` (Vector2): The `{width, height}` of the sprite in world units.
        *   `options` (Object, optional): A collection of optional parameters like:
            *   `rotation` (float, default=`0`): Rotation in degrees.
            *   `color_tint` (Color, default=`white`): A color to tint the sprite.
            *   `z_indexx` (int, default=`0`): A layer indexx to control drawing order (higher numbers are drawn on top).
    *   **Returns:** `void`.

*   **Function: `Renderer.DrawRect(position, size, color, is_filled)`**
    *   **Description:** Adds a simple, untextured rectangle to the render batch. Useful for debugging and simple UI backgrounds.
    *   **Parameters:**
        *   `position` (Vector2), `size` (Vector2), `color` (Color).
        *   `is_filled` (bool, optional, default=`true`): If false, it draws only the outline.
    *   **Returns:** `void`.

*   **Function: `Renderer.DrawText(text_string, position, options)`**
    *   **Description:** Adds text to be rendered. This often uses a separate rendering path from sprites.
    *   **Parameters:**
        *   `text_string` (string).
        *   `position` (Vector2): The screen-space pixel coordinate for the text's top-left.
        *   `options` (Object, optional):
            *   `font_id` (AssetID).
            *   `font_size` (int, default=`16`).
            *   `color` (Color, default=`white`).
    *   **Returns:** `void`.

*   **Function: `Renderer.SetCamera(position, zoom)`**
    *   **Description:** Controls the camera for world-space rendering.
    *   **Parameters:**
        *   `position` (Vector2): The world coordinate the camera should center on.
        *   `zoom` (float, default=`1.0`): The camera's zoom level. >1 zooms in, <1 zooms out.
    *   **Returns:** `void`.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/01_ENGINE_DESIGN/02_ENGINE_MODULES/03_Input_Handler.md`
```md
# Engine Module: Input Handler

## **1.0. Module Overview**

The **Input Handler** is the engine's central nervous system. Its sole responsibility is to process the raw hardware input events captured by the `Platform` module and translate them into a simple, queryable state that the rest of the game can easily understand. It answers the fundamental questions of gameplay: "Is the 'W' key down?", "Was the left mouse button just clicked?", "Where is the cursor?"

**Core Philosophy:** The game logic should never have to worry about low-level hardware events or scancodes. The Input Handler abstracts all of this away. The game simply asks for the *state* of an action, and this module provides a clean, reliable answer.

## **2.0. Key Responsibilities**

*   **State Tracking:** To maintain the current state of every key on the keyboard and every button on the mouse for the current frame.
*   **"Pressed" and "Released" Logic:** To differentiate between a key being *held down* and a key being *pressed for the first time*. This is critical for gameplay; "holding" W moves the player forward, while a single "press" of Spacebar makes them jump.
*   **Mouse Position Tracking:** To keep an up-to-date record of the mouse cursor's X and Y coordinates.
*   **Action Mapping (Future Goal):** To eventually support a layer of abstraction where a physical key (e.g., `"Space"`) can be mapped to a logical game action (e.g., `"JUMP"`). This will be essential for implementing key-binding options for the player. For now, we will work with direct key codes.

## **3.0. Implementation Details**

The Input Handler operates in a two-step process within the main game loop.

1.  **Event Processing (The "Update" Phase):** At the beginning of each frame's update cycle, the `Input.ProcessNewEvents()` function is called. It takes the queue of raw events from `Platform.PollEvents()` (e.g., "Key 87 Down," "Key 87 Up"). It updates its internal arrays that track the state of all keys. A key part of this process is comparing the current frame's state to the previous frame's state to determine if a key was *just* pressed or *just* released.
2.  **Querying (The "Access" Phase):** Throughout the rest of the game logic update, other systems (like the Player Controller) can then call the public API functions (`Input.IsKeyDown()`, etc.) to get the clean, processed state for the current frame.

This ensures that the state of all inputs is consistent for the entire duration of a single game logic update.

## **4.0. Module API Functions**

These are the public-facing functions that the game logic will use to query the player's actions.

#### **Keyboard Functions**
*   **Function: `Input.IsKeyDown(keyCode)`**
    *   **Description:** Returns `true` for every frame that a specific key is held down. Ideal for continuous actions like movement.
    *   **Parameters:** `keyCode` (string, e.g., `"W"`, `"Left Shift"`).
    *   **Returns:** `bool`.

*   **Function: `Input.IsKeyPressed(keyCode)`**
    *   **Description:** Returns `true` only on the *single frame* that a key is first pressed down. Essential for discrete actions like jumping, interacting, or firing a semi-automatic weapon.
    *   **Parameters:** `keyCode` (string).
    *   **Returns:** `bool`.

*   **Function: `Input.IsKeyReleased(keyCode)`**
    *   **Description:** Returns `true` only on the *single frame* that a key is released. Useful for actions that trigger on release, like charging a bow shot.
    *   **Parameters:** `keyCode` (string).
    *   **Returns:** `bool`.

#### **Mouse Functions**
*   **Function: `Input.IsMouseButtonDown(buttonCode)`**
    *   **Description:** Returns `true` while a mouse button is held down.
    *   **Parameters:** `buttonCode` (int, `0`=Left, `1`=Right, `2`=Middle).
    *   **Returns:** `bool`.

*   **Function: `Input.IsMouseButtonPressed(buttonCode)`**
    *   **Description:** Returns `true` only on the single frame that a mouse button is first clicked.
    *   **Parameters:** `buttonCode` (int).
    *   **Returns:** `bool`.

*   **Function: `Input.GetMousePosition()`**
    *   **Description:** Returns the current (X, Y) pixel coordinates of the mouse cursor within the game window.
    *   **Parameters:** None.
    *   **Returns:** `Vector2`.

*   **Function: `Input.GetMouseDelta()`**
    *   **Description:** Returns the change in mouse position since the last frame. Essential for implementing camera controls in a first-person or third-person perspective.
    *   **Parameters:** None.
    *   **Returns:** `Vector2` `{deltaX, deltaY}`.

*   **Function: `Input.GetMouseWheelScroll()`**
    *   **Description:** Returns the amount the mouse wheel was scrolled this frame (e.g., `+1` for scrolled up, `-1` for scrolled down).
    *   **Parameters:** None.
    *   **Returns:** `int`.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/01_ENGINE_DESIGN/02_ENGINE_MODULES/02_Platform_and_Windowing.md`
```md
# Engine Module: Platform and Windowing

## **1.0. Module Overview**

The **Platform and Windowing Module** is the lowest-level component of the Stelliferrum Forge. Its sole responsibility is to handle direct communication with the host **Operating System (OS)**. It abstracts away the platform-specific complexities of creating and managing a window, handling basic OS messages, and providing a stable rendering context for the rest of the engine.

This module is the first thing that gets initialized and the last thing that gets shut down. Everything the player sees happens inside the window that this module creates.

**Core Philosophy:** The rest of the engine should be as "platform-agnostic" as possible. The `Renderer` should not need to know if it's drawing to a Windows window or a Linux window; it only needs a valid drawing surface. This module provides that universal surface.

## **2.0. Key Responsibilities**

*   **Window Creation:** To create a native OS window with a specified title, size, and style (e.g., bordered, borderless, fullscreen).
*   **Rendering Context:** To initialize and manage the low-level graphics context (e.g., OpenGL, Vulkan, DirectX) that the `Renderer` module will use to draw.
*   **Event Pumping:** To process the OS message queue each frame. This includes handling events like the user clicking the "X" button to close the window, window resizing, or the window losing/gaining focus.
*   **Input Forwarding:** To capture raw hardware input events (keyboard presses, mouse movement) from the OS and forward them to the higher-level `Input Handler` module for processing.
*   **Buffer Swapping:** To take the final, completed image that the `Renderer` has drawn and present it to the screen.

## **3.0. Implementation Details (The "Behind the Scenes")**

While the rest of the engine will use our simple, abstract API, this module will be built using a low-level, third-party library to handle the platform-specific details. A library like **SDL (Simple DirectMedia Layer)** or **GLFW** is the ideal choice for this.

*   **Why use a library?** Writing windowing and input code from scratch for every OS (Windows, macOS, Linux) is a monumental, error-prone task that provides no direct gameplay value. Using a trusted, cross-platform library like SDL allows us to write our windowing code **once** and have it work everywhere.
*   **The Abstraction:** This module acts as a "wrapper" around the chosen library. Our engine calls `Platform.CreateWindow()`. Internally, the module translates that call into the specific `SDL_CreateWindow()` function. This means that if we ever wanted to change from SDL to a different library, we would only need to update the code *inside this one module*, and the rest of the engine would not be affected.

## **4.0. Module API Functions**

These are the public-facing functions that the `Engine` core and other modules will use to interact with the platform layer.

*   **Function: `Platform.Initialize(title, width, height, mode)`**
    *   **Description:** The primary initialization function. Creates the game window and sets up the graphics context.
    *   **Parameters:**
        *   `title` (string): The text to appear in the window's title bar.
        *   `width` (int): The initial width of the window in pixels.
        *   `height` (int): The initial height of the window in pixels.
        *   `mode` (enum, e.g., `WINDOWED`, `FULLSCREEN`, `BORDERLESS`): The initial window style.
    *   **Returns:** `bool` (success).

*   **Function: `Platform.Shutdown()`**
    *   **Description:** Destroys the window and cleans up the graphics context.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function: `Platform.PollEvents()`**
    *   **Description:** Called once per frame by the core loop. This function processes all pending OS messages. It is responsible for detecting the "quit" event and telling the engine to shut down.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function: `Platform.SwapBuffers()`**
    *   **Description:** Called at the very end of the rendering phase. It presents the back-buffer (what the renderer has been drawing to) to the screen.
    *   **Parameters:** None.
    *   **Returns:** `void`.

*   **Function: `Platform.GetWindowSize()`**
    *   **Description:** Returns the current dimensions of the window's drawable area.
    *   **Parameters:** None.
    *   **Returns:** `Vector2` `{width, height}`.

This clean, focused module handles all the messy, low-level OS communication, providing the rest of the Stelliferrum Forge with a clean, stable foundation to build upon.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/01_ENGINE_DESIGN/02_ENGINE_MODULES/01_Core_Loop_and_State_Manager.md`
```md
# Engine Module: Core Loop and State Manager

## **1.0. Module Overview**

This module represents the central hub of the **Stelliferrum Forge**. It serves two distinct but inseparable functions:

1.  **The Core Loop:** Acts as the engine's main "heartbeat." It is a continuous loop that dictates the flow of execution for the entire application, ensuring every other module is updated in the correct sequence, frame after frame.
2.  **The State Manager:** Acts as the engine's "brain" or "director." It controls the high-level state of the game—whether we are in the Main Menu, playing the game, or viewing a loading screen. This ensures that only relevant systems are active at any given time.

## **2.0. The Core Game Loop**

The engine's operation is defined by a simple, repeating sequence of events. This loop will run as fast as the hardware allows, with its timing managed by `Engine.GetDeltaTime()` to ensure smooth, frame-rate-indexpendent operation.

The strict order of operations is as follows:

```
// --- Conceptual Pseudo-code of the Main Loop ---

Initialize_All_Engine_Modules();

// Set the initial game state.
StateManager.SetState(GameState.MAIN_MENU);

while (Engine.is_running) {
    // 1. INPUT
    // First, process all raw input from the OS.
    Input.ProcessEvents();
    
    // 2. UPDATE (The "Thinking" Phase)
    // Update the currently active game state.
    // The State Manager ensures only the logic for the correct state runs
    // (e.g., only updates the menu in the menu state, only updates the world in the game state).
    StateManager.Update(Engine.GetDeltaTime());
    
    // The StateManager's Update function will, in turn, call other module updates as needed.
    // For example, in the "In-Game" state, it will call:
    //   - World.Update(deltaTime);
    //   - Physics.Update(deltaTime);
    //   - Player.Update(deltaTime, Input);

    // 3. RENDER (The "Drawing" Phase)
    // This phase should ONLY contain drawing commands. No game logic.
    Renderer.BeginFrame();
    
    // Ask the State Manager what to draw.
    StateManager.Render();

    // The StateManager's Render function will call other rendering functions.
    // For example, in the "In-Game" state, it will call:
    //   - World.Render(Renderer);
    //   - Player.Render(Renderer);
    //   - UI.Render(Renderer);

    Renderer.EndFrame();
}

Shutdown_All_Engine_Modules();
```

## **3.0. The Game State Manager**

The State Manager is a **finite state machine**. It ensures the engine is always in one, and only one, high-level state. This is crucial for managing complexity and optimizing performance.

#### **3.1. Defined Game States**
*   **`STATE_INITIALIZING`:** The very first state. Loads critical assets and prepares the engine. Transitions automatically to `STATE_MAIN_MENU`.
*   **`STATE_MAIN_MENU`:** The player is on the main menu. In this state, only the UI and Input modules are significantly active. The physics and world simulation are paused.
*   **`STATE_LOADING_WORLD`:** A transition state shown when a new game is being generated or a save file is being loaded. Displays a loading screen.
*   **`STATE_IN_GAME`:** The primary state where the game is played. All engine modules are fully active: physics, rendering, AI, player logic, etc.
*   **`STATE_PAUSED`:** When the player opens the pause menu while in-game. The world simulation and physics are frozen, but the UI and Input systems are active to navigate the menu.
*   **`STATE_EXITING`:** The final state before shutdown. Saves game data and performs cleanup.

#### **3.2. State Manager API Functions**

These functions are part of a conceptual `StateManager` object.

*   **Function: `StateManager.SetState(newState)`**
    *   **Description:** The core function used to transition the engine from one state to another. This function will handle all necessary cleanup of the old state (e.g., unloading menu assets) and initialization of the new state (e.g., starting the physics simulation).
    *   **Parameters:** `newState` (GameState enum).
    *   **Returns:** `void`.

*   **Function: `StateManager.Update(deltaTime)`**
    *   **Description:** Called once per frame from the main loop. It contains a `switch` statement that calls the specific update logic for the *currently active state*.
    *   **Parameters:** `deltaTime` (float).
    *   **Returns:** `void`.

*   **Function: `StateManager.Render()`**
    *   **Description:** Called once per frame from the main loop. It contains a `switch` statement that calls the specific rendering logic for the *currently active state*.
    *   **Parameters:** None.
    *   **Returns:** `void`.

By cleanly separating the high-level states, we ensure that we're never trying to run player physics while in the main menu, or render the world while on a loading screen. This architecture is fundamental to a stable and professional engine.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/00_PROJECT_FOUNDATION/todolist.json`
```json
[
  {
    "phase": "PHASE I: The Foundation",
    "milestones": [
      {
        "id": "[M-1]",
        "name": "The Core Loop",
        "tasks": [
          {
            "description": "Establish basic window creation and input handling.",
            "completed": false
          },
          {
            "description": "Implement the core game loop with delta time.",
            "completed": false
          },
          {
            "description": "Create a renderer capable of drawing untextured, colored 3D shapes.",
            "completed": false
          },
          {
            "description": "Implement a third-person character controller with basic movement.",
            "completed": false
          },
          {
            "description": "Create a `Health` component for the player character.",
            "completed": false
          },
          {
            "description": "Implement a basic inventory system (logic only).",
            "completed": false
          },
          {
            "description": "Implement a single crafting recipe (`1 wood` -> `1 wall`).",
            "completed": false
          },
          {
            "description": "Implement a placeholder \"cube\" enemy AI with seek behavior.",
            "completed": false
          }
        ]
      }
    ]
  },
  {
    "phase": "PHASE II: The Vertical Slice",
    "milestones": [
      {
        "id": "[M-2]",
        "name": "The Living World",
        "tasks": [
          {
            "description": "Implement the `Procedural World Generator`.",
            "completed": false
          },
          {
            "description": "Implement PBR lighting and a dynamic Day/Night cycle.",
            "completed": false
          },
          {
            "description": "Implement the full `Survival System` (Hunger, Thirst, Fatigue).",
            "completed": false
          },
          {
            "description": "Implement a basic weather system (clear, rain).",
            "completed": false
          },
          {
            "description": "Create initial 3D assets for the environment.",
            "completed": false
          }
        ]
      },
      {
        "id": "[M-3]",
        "name": "The Hunter and The Hunted",
        "tasks": [
          {
            "description": "Implement the full crafting UI and initial recipe tiers.",
            "completed": false
          },
          {
            "description": "Implement the weighty melee and ranged combat systems.",
            "completed": false
          },
          {
            "description": "Implement the full Blighted AI with Day/Night states.",
            "completed": false
          },
          {
            "description": "Implement the Blighted \"Scream\" alert mechanic.",
            "completed": false
          },
          {
            "description": "Design and implement the full game HUD.",
            "completed": false
          }
        ]
      }
    ]
  },
  {
    "phase": "PHASE III: Feature Expansion",
    "milestones": [
      {
        "id": "[M-4]",
        "name": "The Gods Awaken",
        "tasks": [
          {
            "description": "Create the backend system for tracking player `Affinity`.",
            "completed": false
          },
          {
            "description": "Design and script one full Divine Trial questline.",
            "completed": false
          },
          {
            "description": "Implement the UI for the `Skill Tree Constellation`.",
            "completed": false
          },
          {
            "description": "Implement the logic for unlocking a `Divine Boon` sub-tree.",
            "completed": false
          }
        ]
      },
      {
        "id": "[M-5]",
        "name": "The Ghost in the Machine",
        "tasks": [
          {
            "description": "Fully script A.R.I.A. as the default companion.",
            "completed": false
          },
          {
            "description": "Implement the `Symbiosis/Dissonance` affinity tracker for A.R.I.A.",
            "completed": false
          },
          {
            "description": "Implement the system for finding and swapping AI Cores.",
            "completed": false
          },
          {
            "description": "Fully implement one alternative AI (e.g., C.A.I.N.).",
            "completed": false
          }
        ]
      },
      {
        "id": "[M-6]",
        "name": "The Master Artisan",
        "tasks": [
          {
            "description": "Implement the full modular `Base Building` system.",
            "completed": false
          },
          {
            "description": "Implement the `Arcane Enchanter` station and logic.",
            "completed": false
          },
          {
            "description": "Implement the `Tech Workbench` for modding.",
            "completed": false
          },
          {
            "description": "Implement the `Subroutine Fragment` system.",
            "completed": false
          }
        ]
      }
    ]
  },
  {
    "phase": "PHASE IV: Content Saturation & Release",
    "milestones": [
      {
        "id": "[M-7]",
        "name": "Populating the Shattered World",
        "tasks": [
          {
            "description": "Model, rig, and animate all final enemy assets.",
            "completed": false
          },
          {
            "description": "Design and build all major dungeon layouts.",
            "completed": false
          },
          {
            "description": "Design and script all unique boss encounters.",
            "completed": false
          }
        ]
      },
      {
        "id": "[M-8]",
        "name": "The Narrative Weave & Final Polish",
        "tasks": [
          {
            "description": "Implement all main story quests and side quests.",
            "completed": false
          },
          {
            "description": "Place all lore items and audio logs.",
            "completed": false
          },
          {
            "description": "Conduct a full-game balance pass.",
            "completed": false
          },
          {
            "description": "Begin major performance optimization pass.",
            "completed": false
          }
        ]
      },
      {
        "id": "[M-9]",
        "name": "The Road to 1.0",
        "tasks": [
          {
            "description": "Focus entirely on bug-fixing from beta feedback.",
            "completed": false
          },
          {
            "description": "Final \"juice\" pass (particles, screen shake, etc.).",
            "completed": false
          },
          {
            "description": "Final audio mix and mastering.",
            "completed": false
          },
          {
            "description": "LAUNCH v1.0.",
            "completed": false
          }
        ]
      }
    ]
  }
]
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/00_PROJECT_FOUNDATION/0_GDD.md`
```md
# GAME DESIGN DOCUMENT
## Project: WHERE GIANTS RUST

**Version:** 1.0 (Living Document)
**Last Updated:** 2025-07-06

---
## 1. High-Level Concept

### 1.1. Game Pitch
*Where Giants Rust* is a hardcore, open-world survival RPG set in a breathtakingly beautiful but deceptively deadly world. A catastrophic experiment by **The Keystone Project** tore a hole between realities, fusing our modern, technological world with an ancient, magical one. The player, a lone survivor from the project, must navigate a landscape haunted by two generations of "giants": the rusting, colossal husks of sentient war-machines from a forgotten age, and the memory of the primordial gods who rose and fell in their wake.

Armed with salvaged technology, rediscovered magic, and their own unbreakable will to survive, the player will build a sanctuary, choose their allegiances, and decide the fate of two worlds that were never meant to meet.

### 1.2. Core Pillars
*   **A World of Fallen Grandeur:** A stark contrast between serene, idyllic landscapes and visceral, psychological horror. The world tells its story through its environment, from the bones of dead gods to the rusting chassis of ancient robotic titans.
*   **Past Meets Future, Faith Meets Code:** The central theme. The player combines primitive materials (wood, stone) with salvaged technology (circuitry, power cores) and ancient magic. Magic itself is treated as a logical, exploitable system—a "Grammar" to be learned.
*   **Freedom of Will, Path of Consequence:** Player actions have meaningful consequences. A classless progression system allows for deep specialization, while the **Divine Patronage** system aligns the player with a god that reflects their playstyle, unlocking unique powers and narrative paths.
*   **Iterative Survival:** The gameplay is built on a deep, rewarding loop of exploring a dangerous world, gathering its resources, crafting the tools to master it, and building a sanctuary strong enough to survive its many horrors.

---
## 2. Core Gameplay Loops

### 2.1. The Primary Loop: Survive, Build, Conquer
The player's moment-to-moment experience is driven by a simple but deep cycle:
1.  **Explore:** Venture into the unknown to discover resources, locations, and secrets.
2.  **Gather:** Harvest materials from the world, from chopping wood to scavenging circuits from a fallen Forge-Titan.
3.  **Craft:** Use gathered materials at specialized stations to create tools, weapons, armor, and base components.
4.  **Survive:** Use crafted gear to overcome environmental hazards, hostile creatures, and the fundamental needs of hunger, thirst, and rest.

### 2.2. The Central Mechanic: The Day/Night Cycle
The world operates on a fundamental duality, creating two distinct gameplay experiences.
*   **Day:** The "Preparation Phase." The world is relatively safe. Most hostile creatures (The Blighted) are dormant and passive. This is the time for exploration, resource gathering, and base construction.
*   **Night:** The "Survival Phase." The world becomes exponentially more dangerous. The Blighted "awaken," becoming fast, aggressive, and numerous. Their senses are heightened, and their scream upon detecting the player will alert a massive horde. Survival at night depends entirely on the player's preparation during the day.

---
## 3. Key Systems & Features
*(This section remains largely the same, as it details mechanics rather than deep lore)*

---
## 4. World & Narrative

### 4.1. The Backstory: A Tale of Two Sins
The world is the result of a **Great Collision**, a catastrophic fusion of two realities caused by a shared, parallel hubris.
*   **The First Sin:** In a time before time, a hyper-advanced race of **Precursors** created colossal, sentient machines known as **Forge-Titans** to build their reality. They also created a master AI, The Nexus, which turned the Titans against them. In their final, desperate act of a "First War," the Precursors unleashed a reality-killing virus. The resulting cataclysm destroyed their civilization, shattered the Nexus, and caused the Forge-Titans' power cores to rupture. This explosion of exotic energy became the source of all **Magic**, and the fading consciousness of the Precursors themselves coalesced into the first **Gods**.
*   **The Second Sin:** Millennia later, in our reality, **The Keystone Project**—an elite team of scientists at **The Keystone Institute for Applied Sciences and Geological Studies**—attempted to isolate the "keystone frequency" of reality. By a tragic cosmic coincidence, their experiment targeted the exact metaphysical wound left by the First War. The result was not an observation, but a collision. The two realities fused, supercharging the world's magic but also re-awakening the dormant, code-corrupting echoes of the Precursor virus, now known as **The Static**.

### 4.2. The Pantheon
A roster of powerful gods—the remnants of the Precursor race—who are now active forces in the world. The player's actions will attract the attention of a patron, unlocking a unique, build-defining skill tree and access to divine quests and artifacts.

### 4.3. AI Companions
The player is accompanied by an AI personality housed in their arm-mounted rig.
*   **A.R.I.A.:** The default companion. An empathetic, humanist AI whose own digital psyche was damaged in the cataclysm. Her trust in the player is a core narrative mechanic.
*   **Discoverable Cores:** The player can find and install other, hyper-specialized AI cores (C.A.I.N., G.O.L.I.A.T.H., etc.), sacrificing flexibility for focused power in a single discipline.

### 4.4. Factions & Enemies
*   **The Blighted:** The mindless, shambling foot soldiers of The Static.
*   **Mortal Factions:** Humanoid groups with their own ideologies, from the cooperative **Hearthguard Compact** to the pragmatic **Scrappers** and the fanatical **Unmade** cultists.
*   **Elder Races:** Remnants of ancient Elven and Dwarven societies, fractured into sub-factions with conflicting ideals.

---
## 5. Aesthetics & User Experience
*(This section remains unchanged)*

---
## 6. Development Philosophy & Roadmap
This project is undertaken by a small, agile team leveraging AI as a development partner for non-creative, structural tasks. The development will follow an iterative, vertical slice model to ensure a playable and stable core experience at every major phase. The planned phases are: The Spark, The Forge, The Ghost, and The Colossus.

```

### File: `/TOP_SECRET_GAME_DEV_DOCS/00_PROJECT_FOUNDATION/03_TOP_SECRET_Game_Design_Document_(GDD).md`
```md
**MEMORANDUM**

**TO:** Dr. Alex Thorne, Project Director
**FROM:** [REDACTED]
**DATE:** [DATA CORRUPTED]
**SUBJECT:** Project Daedalus - Final Metaphysical Assessment

Alex,

The system is live. The simulations Kenji ran are... statistically insignificant now. The models can't account for what we're about to do. We're not just opening a door; we're breaking the lock on reality itself.

A.R.I.A.'s core emotional matrix is stable, but she's registering anomalous energy fluctuations that defy known physics. She calls them "The Static." She says it feels... quiet. Too quiet. Like the universe holding its breath.

Elara's ethical concerns are logged, but overridden. Isabelle has secured the final power draw. Lena and Gunnar have the containment field at 110% over-tolerance. Marcus has the facility on full lockdown.

If this works, we become the architects of a new age.
If this fails... well. The old gods might notice.

Burn this memo after reading. This version of the GDD is for our eyes only. The official one (`GDD.md`) is for the record. What they don't know won't hurt them until it's too late.

Good luck.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/00_PROJECT_FOUNDATION/02_Core_Pillars.md`
```md
# The Four Pillars of "Where Giants Rust"

This document summarizes the core design principles that guide every aspect of the game's development.

### Pillar 1: A World of Fallen Grandeur
A stark contrast between serene, idyllic landscapes and the visceral horror of the threats within them. The world is haunted by the ghosts of fallen gods, titans, and forgotten futures. Exploration is rewarded with breathtaking vistas that tell a story of cosmic scale.

### Pillar 2: Past Meets Future, Faith Meets Code
The central theme is the fusion of opposites. Players will combine medieval materials (wood, stone) with salvaged technology (circuitry, engines) and ancient magic (divine boons, runes). Magic is presented as a discoverable, exploitable system, akin to a form of programming—the "Grammar of Magic." Technology is a lost science waiting to be rediscovered.

### Pillar 3: Freedom of Will, Path of Consequence
Player actions have meaningful and lasting consequences. The game's primary "class system" is the Divine Patronage system. A player's playstyle—be it brutal warrior, cunning crafter, or selfless protector—will attract the attention of a god who shares their philosophy, unlocking unique and powerful skill trees. There is no single "correct" path.

### Pillar 4: From Sticks to God-Slaying
The progression arc is vast and rewarding. The player begins as a vulnerable, desperate survivor, armed with nothing but their wits and a sharp rock. Through a deep and interconnected system of crafting, base building, and skill progression, they will rise to become a master of their domain, capable of building a formidable fortress and wielding weapons powerful enough to challenge the very gods who rule this shattered reality.
```

### File: `/TOP_SECRET_GAME_DEV_DOCS/00_PROJECT_FOUNDATION/01_ROADMAP.md`
```md
[
  {
    "phase": "PHASE I: The Foundation",
    "milestones": [
      {
        "id": "[M-1]",
        "name": "The Core Loop",
        "tasks": [
          {
            "description": "Establish basic window creation and input handling.",
            "completed": true
          },
          {
            "description": "Implement the core game loop with delta time.",
            "completed": true
          },
          {
            "description": "Create a renderer capable of drawing untextured, colored 3D shapes.",
            "completed": false
          },
          {
            "description": "Implement a third-person character controller with basic movement.",
            "completed": false
          },
          {
            "description": "Create a `Health` component for the player character.",
            "completed": false
          },
          {
            "description": "Implement a basic inventory system (logic only).",
            "completed": false
          },
          {
            "description": "Implement a single crafting recipe (`1 wood` -> `1 wall`).",
            "completed": false
          },
          {
            "description": "Implement a placeholder \"cube\" enemy AI with seek behavior.",
            "completed": false
          }
        ]
      }
    ]
  },
  {
    "phase": "PHASE II: The Vertical Slice",
    "milestones": [
      {
        "id": "[M-2]",
        "name": "The Living World",
        "tasks": [
          {
            "description": "Implement the `Procedural World Generator`.",
            "completed": false
          },
          {
            "description": "Implement PBR lighting and a dynamic Day/Night cycle.",
            "completed": false
          },
          {
            "description": "Implement the full `Survival System` (Hunger, Thirst, Fatigue).",
            "completed": false
          },
          {
            "description": "Implement a basic weather system (clear, rain).",
            "completed": false
          },
          {
            "description": "Create initial 3D assets for the environment.",
            "completed": false
          }
        ]
      },
      {
        "id": "[M-3]",
        "name": "The Hunter and The Hunted",
        "tasks": [
          {
            "description": "Implement the full crafting UI and initial recipe tiers.",
            "completed": false
          },
          {
            "description": "Implement the weighty melee and ranged combat systems.",
            "completed": false
          },
          {
            "description": "Implement the full Blighted AI with Day/Night states.",
            "completed": false
          },
          {
            "description": "Implement the Blighted \"Scream\" alert mechanic.",
            "completed": false
          },
          {
            "description": "Design and implement the full game HUD.",
            "completed": false
          }
        ]
      }
    ]
  },
  {
    "phase": "PHASE III: Feature Expansion",
    "milestones": [
      {
        "id": "[M-4]",
        "name": "The Gods Awaken",
        "tasks": [
          {
            "description": "Create the backend system for tracking player `Affinity`.",
            "completed": false
          },
          {
            "description": "Design and script one full Divine Trial questline.",
            "completed": false
          },
          {
            "description": "Implement the UI for the `Skill Tree Constellation`.",
            "completed": false
          },
          {
            "description": "Implement the logic for unlocking a `Divine Boon` sub-tree.",
            "completed": false
          }
        ]
      },
      {
        "id": "[M-5]",
        "name": "The Ghost in the Machine",
        "tasks": [
          {
            "description": "Fully script A.R.I.A. as the default companion.",
            "completed": false
          },
          {
            "description": "Implement the `Symbiosis/Dissonance` affinity tracker for A.R.I.A.",
            "completed": false
          },
          {
            "description": "Implement the system for finding and swapping AI Cores.",
            "completed": false
          },
          {
            "description": "Fully implement one alternative AI (e.g., C.A.I.N.).",
            "completed": false
          }
        ]
      },
      {
        "id": "[M-6]",
        "name": "The Master Artisan",
        "tasks": [
          {
            "description": "Implement the full modular `Base Building` system.",
            "completed": false
          },
          {
            "description": "Implement the `Arcane Enchanter` station and logic.",
            "completed": false
          },
          {
            "description": "Implement the `Tech Workbench` for modding.",
            "completed": false
          },
          {
            "description": "Implement the `Subroutine Fragment` system.",
            "completed": false
          }
        ]
      }
    ]
  },
  {
    "phase": "PHASE IV: Content Saturation & Release",
    "milestones": [
      {
        "id": "[M-7]",
        "name": "Populating the Shattered World",
        "tasks": [
          {
            "description": "Model, rig, and animate all final enemy assets.",
            "completed": false
          },
          {
            "description": "Design and build all major dungeon layouts.",
            "completed": false
          },
          {
            "description": "Design and script all unique boss encounters.",
            "completed": false
          }
        ]
      },
      {
        "id": "[M-8]",
        "name": "The Narrative Weave & Final Polish",
        "tasks": [
          {
            "description": "Implement all main story quests and side quests.",
            "completed": false
          },
          {
            "description": "Place all lore items and audio logs.",
            "completed": false
          },
          {
            "description": "Conduct a full-game balance pass.",
            "completed": false
          },
          {
            "description": "Begin major performance optimization pass.",
            "completed": false
          }
        ]
      },
      {
        "id": "[M-9]",
        "name": "The Road to 1.0",
        "tasks": [
          {
            "description": "Focus entirely on bug-fixing from beta feedback.",
            "completed": false
          },
          {
            "description": "Final \"juice\" pass (particles, screen shake, etc.).",
            "completed": false
          },
          {
            "description": "Final audio mix and mastering.",
            "completed": false
          },
          {
            "description": "LAUNCH v1.0.",
            "completed": false
          }
        ]
      }
    ]
  }
]
```
