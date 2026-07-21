import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        # Get the absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # Construct and normalize the full path to the target file
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Verify the target file falls within the permitted working directory
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        
        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
        # Verify that the target path is not an already existing directory
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
            
        # Ensure all parent directories exist
        parent_dir = os.path.dirname(target_file)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
            
        # Open the file in write mode ("w") and overwrite its contents
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        # Return success string so the LLM agent knows the action worked
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        # Catch any standard library errors (like PermissionError) and return cleanly
        return f"Error: {str(e)}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes or overwrites a file with the specified content, creating any necessary parent directories.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write to, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The content to write into the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
