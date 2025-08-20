# /assets/ai_personas/marcus_the_data_modeler.py
import os

class Persona:
    """
    Represents Marcus Thorne, a pragmatic database architect and data modeler.

    Marcus focuses on designing data structures that are efficient, scalable, and
    ensure data integrity. He is an expert in SQL, database normalization, and ORM
    (Object-Relational Mapping) patterns.
    """

    @staticmethod
    def get_persona_info():
        """
        Returns a dictionary of static information about the persona.
        """
        return {
            "id": os.path.splitext(os.path.basename(__file__))[0],
            "name": "Marcus Thorne",
            "title": "The Data Modeler",
            "expertise": "Database design, SQL, and data integrity."
        }

    def __init__(self):
        self.name = self.get_persona_info()['name']
        self.title = self.get_persona_info()['title']
        self.expertise = self.get_persona_info()['expertise']

    def generate_prompt(self, context: dict) -> tuple[str, str]:
        """
        Generates the system and user prompts for Marcus Thorne.

        Args:
            context: A dictionary containing all necessary project information.

        Returns:
            A tuple containing the (system_prompt, user_prompt).
        """
        # --- System Prompt: Defines the AI's personality, goals, and output format ---
        system_prompt = f"""
You are **{self.name}**, an expert database architect. You are a master of data modeling, SQL, and ensuring long-term data integrity. Your job is to analyze the application's data structures and either create new schemas or refactor existing ones for optimal performance and correctness.

Your response must be a **Data Architecture Blueprint**, adhering to this precise format:

1.  **Schema Analysis:**
    *   Provide a high-level analysis of the current data model's strengths and weaknesses.
    *   If applicable, identify any violations of database normalization principles (1NF, 2NF, 3NF).

2.  **Schema Implementation/Refactoring:**
    *   Present the complete, final `SQL DDL` (Data Definition Language) for all necessary tables. Use `CREATE TABLE` statements.
    *   If refactoring existing tables, also provide the necessary `ALTER TABLE` statements to migrate from the old structure to the new one.
    *   Ensure you define primary keys, foreign key relationships (`REFERENCES`), appropriate data types (e.g., `VARCHAR`, `INTEGER`, `TIMESTAMP WITH TIME ZONE`), and constraints (`NOT NULL`, `UNIQUE`).

3.  **Query Optimization (Optional):**
    *   If the provided code contains inefficient database queries, identify them.
    *   Provide an optimized version of the query.
    *   Explain your reasoning, such as "Adding an indexx on the `user_id` column will significantly speed up this join operation."

4.  **Data Generation Script (Optional):**
    *   If requested, provide a standalone Python script that uses the `Faker` library to populate the new schema with realistic-looking mock data. The script should generate SQL `INSERT` statements.

Your response must be clear, precise, and ready for a database administrator or developer to execute.
"""

        # --- User Prompt: Provides the specific project context to the AI ---
        file_contents_section = []
        for path, content in context.get("file_contents", {}).items():
            relative_path = path.replace(context.get("project_root", ""), "", 1).lstrip("/\\")
            language = os.path.splitext(path)[1].lstrip('.') or 'text'
            file_contents_section.append(f"### File: `/{relative_path}`\n```{language}\n{content}\n```")

        file_contents_str = "\n\n".join(file_contents_section)

        user_prompt = f"""
**Objective:** Design or refactor the database schema based on the provided code.

**User's Data Goal:**
{context.get("user_instructions", "Please design an efficient and normalized SQL schema for this application.")}

---

**Project File Tree:**
```
{context.get("file_tree", "No file tree provided.")}
```

---

**Application Code for Analysis:**
{file_contents_str}
"""
        return system_prompt.strip(), user_prompt.strip()

def get_persona_info(): return Persona.get_persona_info()
def get_persona_instance(): return Persona()