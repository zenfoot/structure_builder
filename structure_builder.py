import logging
from pathlib import Path
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

DIRECTORY_STRUCTURE = [
    "README.md",
    "requirements.txt",
    "configs/config.yaml",
    "data/knowledge_base/",
    "data/experimental_data/",
    "data/experiments/",
    "data/experiment_runs/",
    "data/latex/README.md",
    "data/latex/template.tex",
    "data/latex/references.bib",
    "data/papers/",
    "data/fewshot_examples/132_automated_relational.pdf",
    "data/fewshot_examples/attention.pdf",
    "data/fewshot_examples/2_carpe_diem.pdf",
    "data/fewshot_examples/132_automated_relational.json",
    "data/fewshot_examples/attention.json",
    "data/fewshot_examples/2_carpe_diem.json",
    "data/fewshot_examples/paper1.pdf",
    "data/fewshot_examples/paper1_review.json",
    "src/__init__.py",
    "src/main.py",
    "src/agents/__init__.py",
    "src/agents/constants.py",
    "src/agents/adaptive_orchestration_agent.py",
    "src/agents/user_interaction_agent.py",
    "src/agents/idea_generation_agent.py",
    "src/agents/idea_reflection_agent.py",
    "src/agents/knowledge_management_agent.py",
    "src/agents/novelty_evaluation_agent.py",
    "src/agents/experiment_planning_agent.py",
    "src/agents/experiment_design_agent.py",
    "src/agents/experiment_execution_agent.py",
    "src/agents/data_analysis_agent.py",
    "src/agents/plotting_agent.py",
    "src/agents/documentation_agent.py",
    "src/agents/reporting_agent.py",
    "src/agents/citation_management_agent.py",
    "src/agents/error_checking_agent.py",
    "src/agents/document_compilation_agent.py",
    "src/agents/peer_review_simulation_agent.py",
    "src/agents/review_generation_agent.py",
    "src/agents/review_reflection_agent.py",
    "src/agents/meta_review_agent.py",
    "src/agents/improvement_agent.py",
    "src/agents/resource_management_agent.py",
    "src/models/__init__.py",
    "src/models/llm_provider.py",
    "src/prompts/README.md",
    "src/prompts/__init__.py",
    "src/prompts/idea_generation/generation_prompt.txt",
    "src/prompts/idea_generation/reflection_prompt.txt",
    "src/prompts/novelty_evaluation/prompt.txt",
    "src/prompts/novelty_evaluation/system_message.txt",
    "src/prompts/experiment_design/design_prompt.txt",
    "src/prompts/experiment_design/coder_prompt.txt",
    "src/prompts/experiment_execution/failure_prompt.txt",
    "src/prompts/experiment_execution/completion_prompt.txt",
    "src/prompts/experiment_execution/timeout_prompt.txt",
    "src/prompts/experiment_execution/plotting_prompt.txt",
    "src/prompts/experiment_execution/notes_prompt.txt",
    "src/prompts/data_analysis/data_analysis_prompt.txt",
    "src/prompts/reporting/abstract_prompt.txt",
    "src/prompts/reporting/section_prompt.txt",
    "src/prompts/reporting/refinement_prompt.txt",
    "src/prompts/reporting/second_refinement_prompt.txt",
    "src/prompts/reporting/second_refinement_loop_prompt.txt",
    "src/prompts/reporting/per_section_tips.txt",
    "src/prompts/reporting/common_errors.txt",
    "src/prompts/review_generation/generation_prompt.txt",
    "src/prompts/review_generation/system_prompt_base.txt",
    "src/prompts/review_generation/system_prompt_neg.txt",
    "src/prompts/review_generation/system_prompt_pos.txt",
    "src/prompts/review_generation/reflection_prompt.txt",
    "src/prompts/review_generation/meta_system_prompt.txt",
    "src/prompts/review_generation/improvement_prompt.txt",
    "src/prompts/citation_management/system_message.txt",
    "src/prompts/citation_management/first_prompt.txt",
    "src/prompts/citation_management/second_prompt.txt",
    "src/prompts/citation_management/aider_prompt_format.txt",
    "src/prompts/misc/template_instructions.txt",
    "src/utils/__init__.py",
    "src/utils/helpers.py",
    "src/utils/api_clients.py",
    "src/utils/latex_utils.py",
    "src/utils/paper_loader.py",
    "src/utils/other_utils.py",
    "src/memory/__init__.py",
    "src/memory/memory_manager.py",
    "src/tests/__init__.py",
    "src/tests/test_agents.py",
    "src/tests/test_workflow.py",
    "Dockerfile",
    ".gitignore",
]

def create_file_structure(base_path: str, structure: List[str]) -> None:
    """Creates the directory and file structure based on the provided list."""
    base_path = Path(base_path)
    for path_string in structure:
        current_path = base_path / path_string
        logger.info(f"Processing: {current_path}")
        if current_path.suffix == "":
            create_directory(current_path)
        else:
            create_file(current_path)

def create_directory(dir_path: Path) -> None:
    """Creates a directory if it doesn't exist."""
    try:
        dir_path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Directory created: {dir_path}")
    except Exception as e:
        logger.error(f"Error creating directory {dir_path}: {e}")

def create_file(file_path: Path) -> None:
    """Creates a file, ensuring parent directories exist."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if not file_path.exists():
            file_path.touch()
            logger.info(f"File created: {file_path}")
        else:
            logger.info(f"File already exists: {file_path}")
    except Exception as e:
        logger.error(f"Error creating file {file_path}: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Create project directory structure.")
    parser.add_argument('base_path', type=str, help='Base path for the project structure.')
    args = parser.parse_args()

    try:
        create_file_structure(args.base_path, DIRECTORY_STRUCTURE)
        logger.info("Directory structure created successfully!")
    except Exception as e:
        logger.error(f"Failed to create directory structure: {e}")