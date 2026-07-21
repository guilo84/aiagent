import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        # Get the absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # Construct and normalize the full path to the target file
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Verify the target file falls within the permitted working directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            
        # Verify that the target path is actually a regular file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
            
        # Read the file up to MAX_CHARS
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read(MAX_CHARS)
            
            # Try reading one more character to see if we reached the end
            if f.read(1):
                content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                
        return content
        
    except Exception as e:
        # Catch any standard library errors (like PermissionError) and return cleanly
        return f"Error: {str(e)}"

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the contents of a specified file relative to the working directory up to a maximum character limit.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}
