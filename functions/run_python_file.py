import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        # Normalize the paths to ensure reliable security checking
        abs_working_dir = os.path.abspath(working_directory)
        # Assuming the provided file_path is relative to the working_directory
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if the target file is inside the working directory
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check if it exists and is a regular file
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # Check if it is a python file
        if not abs_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        # Build the command
        command = ["python", abs_file_path]
        if args:
            command.extend(args)

        # Run the subprocess
        result = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )

        # Build the output string
        output_parts = []
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not result.stdout and not result.stderr:
            output_parts.append("No output produced")
        else:
            if result.stdout:
                output_parts.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                output_parts.append(f"STDERR:\n{result.stderr}")

        return "\n".join(output_parts).strip()

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file and returns the output (stdout and stderr) or error code.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of command-line arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}
