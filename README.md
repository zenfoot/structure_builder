# Project Directory Structure Creator

This project contains a Python script that programmatically creates a predefined directory and file structure for your project.

## Prerequisites

- **Python 3**: Ensure you have Python 3 installed on your system. You can verify your installation by running:

  ```bash
  python --version
  ```

- **Conda**: This project assumes you will be using Conda for environment management. Make sure you have Conda installed. You can find installation instructions on the [Anaconda website](https://www.anaconda.com/products/distribution).

## Setting Up the Environment

1. **Create a New Conda Environment**:

   Open your command line interface (CLI) and create a new Conda environment:

   ```bash
   conda create --name project_env python=3.9
   ```

   Replace `project_env` with your desired environment name.

2. **Activate the Environment**:

   Activate your Conda environment with:

   ```bash
   conda activate project_env
   ```

3. **~~Install Required Packages~~**:

   ~~Install the required packages using the `requirements.txt` file provided in the project:~~

   ```bash
   pip install -r requirements.txt
   ```

## Running the Script

**IMPORTANT:** Change `DIRECTORY_STRUCTURE = [ ]` for your needs.

1. **Save the Script**:

   Ensure the script `structure_builder.py` is saved in your working directory.

2. **Open the Command Line Interface**:

   - **Windows**: Open Command Prompt or PowerShell.
   - **macOS/Linux**: Open Terminal.

3. **Navigate to the Script's Directory**:

   Use the `cd` command to navigate to the directory containing `structure_builder.py`:

   ```bash
   cd path/to/your/script_directory
   ```

4. **Run the Script**:

   Execute the script by providing the base path where you want the directory structure to be created:

   ```bash
   python structure_builder.py [base_path]
   ```

   Replace `[base_path]` with the path where you want the project structure created.

   **Example**:

   ```bash
   python structure_builder.py .
   ```

## Verifying the Created Structure

After running the script, navigate to the base path you specified. You should see the following directory and file structure created:

```
project_directory/
├── README.md
├── requirements.txt
├── configs/
│   └── config.yaml
├── data/
│   ├── knowledge_base/
│   ├── experimental_data/
│   ├── experiments/
│   ├── experiment_runs/
│   ├── latex/
│   │   ├── template.tex
│   │   └── references.bib
│   ├── papers/
│   └── fewshot_examples/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── ... (other directories and files)
├── Dockerfile
└── .gitignore
```

## Additional Notes

- Ensure you have the necessary permissions to create files and directories in the specified base path.
- If you encounter any errors, check the logged messages for troubleshooting.
- If you need to deactivate the Conda environment, run:

  ```bash
  conda deactivate
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
