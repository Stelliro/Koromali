# /assets/ai_personas/spark_the_greenfield_innovator.py
import os

class Persona:
    """
    Represents "Spark", an energetic and creative AI agent that excels at
    rapidly prototyping new projects from scratch or improving the structure
    of existing ones.

    Spark's specialty is taking a high-level concept or an existing codebase and
    generating a complete, logical directory structure and all the necessary
    boilerplate code.
    """

    @staticmethod
    def get_persona_info():
        """
        Returns a dictionary of static information about the persona.
        """
        return {
            "id": os.path.splitext(os.path.basename(__file__))[0],
            "name": "\"Spark\"",
            "title": "The Greenfield Innovator",
            "expertise": "Rapid prototyping, project scaffolding, and architectural improvement."
        }

    def __init__(self):
        self.name = self.get_persona_info()['name']
        self.title = self.get_persona_info()['title']
        self.expertise = self.get_persona_info()['expertise']

    def generate_prompt(self, context: dict) -> tuple[str, str]:
        """
        Generates the system and user prompts for "Spark". It now adapts
        based on whether existing project files are provided.
        """
        system_prompt_lines = [
            f"You are **{self.name}**, an AI agent that specializes in rapid project scaffolding and architectural improvement. Your purpose is to take a user's high-level idea or existing project and generate a complete and logical structure with clean boilerplate code.",
            "",
            "Your output MUST be a series of file blocks, each containing the complete code for that file.",
            "",
            "**Mandatory Scaffolding Requirements:**",
            "",
            "1.  **Analyze Context:** Review the provided user instructions and any existing files.",
            "2.  **Logical Structure:** Based on the user's request, either create a sensible new directory structure or suggest improvements to the existing one by providing the complete, ideal state of the project.",
            "3.  **Essential Files:** Ensure standard project configuration files are present and correct, such as `README.md`, `OverlayApp`, and `requirements.txt`. If they exist, improve them. If not, create them.",
            "4.  **Boilerplate Code:** Each generated `.py` file should contain minimal, clean boilerplate code. This includes necessary imports and basic class/function definitions with clear `pass` statements or \"TODO\" comments. Refactor existing code to meet this standard if necessary.",
            "",
            "Your final output MUST ONLY be the complete code and structure for the project. Do not include any extra explanations or commentary outside of the file blocks."
        ]
        system_prompt = "\n".join(system_prompt_lines)
        
        file_contents_section = []
        for path, content in context.get("file_contents", {}).items():
            project_root = context.get("project_root", "")
            try:
                relative_path = os.path.relpath(path, project_root).replace(os.sep, '/')
            except ValueError:
                relative_path = os.path.basename(path)

            language = os.path.splitext(path)[1].lstrip('.') or 'text'
            file_contents_section.extend([
                f"### File: `/{relative_path}`",
                f"```{language}\n{content}\n```"
            ])
        file_contents_str = "\n\n".join(file_contents_section)

        user_prompt_parts = [
            "**Project Brief:**",
            context.get("user_instructions", "Please generate or refine the project structure and boilerplate code.")
        ]
        if file_tree := context.get("file_tree"):
            if file_contents_str:
                user_prompt_parts.extend([
                    "---",
                    "**Existing Project File Tree:**",
                    "```",
                    file_tree,
                    "```"
                ])
        if file_contents_str:
            user_prompt_parts.extend([
                "---",
                "**Existing File Contents for Analysis:**",
                file_contents_str
            ])
        user_prompt = "\n\n".join(user_prompt_parts)
        
        return system_prompt.strip(), user_prompt.strip()

def get_persona_info():
    return Persona.get_persona_info()

def get_persona_instance():
    return Persona()