import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        # Get the absolute path of the working directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # Construct and normalize the full path to the target directory
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        # Verify the target directory falls within the permitted working directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            
        # Verify that the target path is actually a directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
            
        # Iterate over items in the target directory and collect their data
        directory_contents = []
        for item_name in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item_name)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            
            directory_contents.append(f"- {item_name}: file_size={file_size} bytes, is_dir={is_dir}")
            
        # Return the items joined by newlines
        return "\n".join(directory_contents)
        
    except Exception as e:
        # Catch any standard library errors and return them cleanly
        return f"Error: {str(e)}"
