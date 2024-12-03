import os
import logging
from pathlib import Path
from typing import List, Tuple
import jsonschema


# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


# Schema for validating the directory structure (explained below)
STRUCTURE_SCHEMA = {
    "type": "array",
    "items": {
        "type": "array",  # Each item is a tuple (represented as a list in JSON)
        "items": {"type": "string"},  # Each element in the tuple is a string
        "minItems": 1,  # At least one string (the file/directory name)
    },
}

DIRECTORY_STRUCTURE = [
    ("README.md",),
    ("requirements.txt",),
    ("configs/config.yaml",),
    ("data/knowledge_base/",),
    ("data/experimental_data/",),
    ("data/experiments/",),
    ("data/experiment_runs/",),
    ("data/latex/template.tex",),
    ("data/latex/references.bib",),
    ("data/papers/",),
    ("data/fewshot_examples/132_automated_relational.pdf",),
    ("data/fewshot_examples/attention.pdf",),
    ("data/fewshot_examples/2_carpe_diem.pdf",),
    ("data/fewshot_examples/132_automated_relational.json",),
    ("data/fewshot_examples/attention.json",),
    ("data/fewshot_examples/2_carpe_diem.json",),
    ("data/fewshot_examples/paper1.pdf",),
    ("data/fewshot_examples/paper1_review.json",),
    ("src/__init__.py",),
    ("src/main.py",),
    ("src/agents/__init__.py",),
    ("src/agents/constants.py",),
    ("src/agents/adaptive_orchestration_agent.py",),
    ("src/agents/user_interaction_agent.py",),
    ("src/agents/idea_generation_agent.py",),
    ("src/agents/idea_reflection_agent.py",),
    ("src/agents/knowledge_management_agent.py",),
    ("src/agents/novelty_evaluation_agent.py",),
    ("src/agents/experiment_planning_agent.py",),
    ("src/agents/experiment_design_agent.py",),
    ("src/agents/experiment_execution_agent.py",),
    ("src/agents/data_analysis_agent.py",),
    ("src/agents/plotting_agent.py",),
    ("src/agents/documentation_agent.py",),
    ("src/agents/reporting_agent.py",),
    ("src/agents/citation_management_agent.py",),
    ("src/agents/error_checking_agent.py",),
    ("src/agents/document_compilation_agent.py",),
    ("src/agents/peer_review_simulation_agent.py",),
    ("src/agents/review_generation_agent.py",),
    ("src/agents/review_reflection_agent.py",),
    ("src/agents/meta_review_agent.py",),
    ("src/agents/improvement_agent.py",),
    ("src/agents/resource_management_agent.py",),
    ("src/models/__init__.py",),
    ("src/models/llm_provider.py",),
    ("src/prompts/__init__.py",),
    ("src/prompts/idea_generation/generation_prompt.txt",),
    ("src/prompts/idea_generation/reflection_prompt.txt",),
    ("src/prompts/novelty_evaluation/prompt.txt",),
    ("src/prompts/novelty_evaluation/system_message.txt",),
    ("src/prompts/experiment_design/design_prompt.txt",),
    ("src/prompts/experiment_design/coder_prompt.txt",),
    ("src/prompts/experiment_execution/failure_prompt.txt",),
    ("src/prompts/experiment_execution/completion_prompt.txt",),
    ("src/prompts/experiment_execution/timeout_prompt.txt",),
    ("src/prompts/experiment_execution/plotting_prompt.txt",),
    ("src/prompts/experiment_execution/notes_prompt.txt",),
    ("src/prompts/data_analysis/data_analysis_prompt.txt",),
    ("src/prompts/reporting/abstract_prompt.txt",),
    ("src/prompts/reporting/section_prompt.txt",),
    ("src/prompts/reporting/refinement_prompt.txt",),
    ("src/prompts/reporting/second_refinement_prompt.txt",),
    ("src/prompts/reporting/second_refinement_loop_prompt.txt",),
    ("src/prompts/reporting/per_section_tips.txt",),
    ("src/prompts/reporting/common_errors.txt",),
    ("src/prompts/review_generation/generation_prompt.txt",),
    ("src/prompts/review_generation/system_prompt_base.txt",),
    ("src/prompts/review_generation/system_prompt_neg.txt",),
    ("src/prompts/review_generation/system_prompt_pos.txt",),
    ("src/prompts/review_generation/reflection_prompt.txt",),
    ("src/prompts/review_generation/meta_system_prompt.txt",),
    ("src/prompts/review_generation/improvement_prompt.txt",),
    ("src/prompts/citation_management/system_message.txt",),
    ("src/prompts/citation_management/first_prompt.txt",),
    ("src/prompts/citation_management/second_prompt.txt",),
    ("src/prompts/citation_management/aider_prompt_format.txt",),
    ("src/prompts/misc/template_instructions.txt",),
    ("src/utils/__init__.py",),
    ("src/utils/helpers.py",),
    ("src/utils/api_clients.py",),
    ("src/utils/latex_utils.py",),
    ("src/utils/paper_loader.py",),
    ("src/utils/other_utils.py",),
    ("src/memory/__init__.py",),
    ("src/memory/memory_manager.py",),
    ("src/tests/__init__.py",),
    ("src/tests/test_agents.py",),
    ("src/tests/test_workflow.py",),
    ("Dockerfile",),
    (".gitignore",),
]


def create_file_structure(base_path: str, structure: List[Tuple[str, ...]] = DIRECTORY_STRUCTURE) -> None:
    """Creates a predefined directory and file structure.

    This function takes a base path and a list of tuples, each representing a file or directory
    path relative to the base path. It creates the specified files and directories, handling
    existing files and directories gracefully.  A trailing slash in a path component indicates a directory.

    Args:
        base_path (str): The base path where the structure will be created.  Must be a non-empty string.
        structure (List[Tuple[str,...]]): A list of tuples defining the file/directory structure.
            Defaults to `DIRECTORY_STRUCTURE`. Each tuple represents a path relative to `base_path`.
            Each element within a tuple is a string representing a directory or file name.
            For directories, the last element in the tuple should end with a forward slash ("/").

    Raises:
        TypeError: If `base_path` is not a string or `structure` is not a list of tuples.
        ValueError: If `base_path` is empty or `structure` is invalid according to the schema.
        jsonschema.ValidationError: If the `structure` does not conform to `STRUCTURE_SCHEMA`.

    Example:
        >>> create_file_structure("my_project", [("data/",), ("data/file1.txt",), ("src/utils/",), ("src/utils/helper.py",)])
    """

    if not isinstance(base_path, str):
        raise TypeError("base_path must be a string")
    if not base_path:
        raise ValueError("base_path cannot be empty")
    if not isinstance(structure, list):
        raise TypeError("structure must be a list")

    try:
        jsonschema.validate(structure, STRUCTURE_SCHEMA)  # Validate against the schema
    except jsonschema.ValidationError as e:
        raise ValueError(f"Invalid structure: {e}")


    base_path = Path(base_path)

    for path_parts in structure:
        current_path = base_path
        for part in path_parts:
            current_path /= part
            if part.endswith("/"): # Directory
                create_directory(current_path)
            else: # File
                create_file(current_path)


def create_directory(dir_path: Path) -> None:
    """Creates a directory if it doesn't exist.

    Args:
        dir_path (Path): The path to the directory to be created.

    Side Effects:
        Creates a directory at the specified path if it doesn't already exist.  Logs informational
        messages indicating whether the directory was created or already existed.  Logs error messages
        if any exceptions occur during directory creation.
    """
    if dir_path.exists() and dir_path.is_dir():
        logger.info(f"Directory already exists: {dir_path}")
    else:
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {dir_path}")
        except Exception as e:
            logger.error(f"Error creating directory {dir_path}: {e}")

def create_file(file_path: Path) -> None:
    """Creates a file if it doesn't exist. If the file already exists, it is not modified.

    Args:
        file_path (Path): The path to the file to be created.

    Side Effects:
        Creates an empty file at the specified path if it doesn't already exist. Logs informational
        messages indicating whether the file was created or already existed. Logs error messages
        if any exceptions occur during file creation.
    """
    if file_path.exists() and file_path.is_file():
        logger.info(f"File already exists: {file_path}")
    else:
        try:
            file_path.touch(exist_ok=True)  # or file_path.write_text("") to overwrite
            logger.info(f"Created file: {file_path}")
        except Exception as e:
            logger.error(f"Error creating file {file_path}: {e}")


# Example usage (outside the function for testability)
BASE_PATH = "C:/Projects/researcher"  # Or make this configurable


if __name__ == "__main__":
    try:
        create_file_structure(BASE_PATH)
        logger.info("Directory structure created successfully!")
    except Exception as e:
        logger.error(f"Failed to create directory structure: {e}")


# Explanation of STRUCTURE_SCHEMA:
# This JSON Schema ensures that the `structure` argument to `create_file_structure` is a list of tuples (represented as lists in JSON).
# Each tuple must contain at least one string, representing the path components of a file or directory.
# This schema helps prevent common errors like providing a single string instead of a list of tuples or forgetting to include file/directory names.
