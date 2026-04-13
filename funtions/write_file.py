import os
from google.genai import types


def write_file(working_directory, file_path, content):
    try:
        # Get absolute working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Build normalized target path
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Ensure the target path is inside the working directory
        valid_target = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not valid_target:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Prevent writing to a directory
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Ensure parent directories exist
        parent_dir = os.path.dirname(target_path)
        os.makedirs(parent_dir, exist_ok=True)

        # Write the file
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {str(e)}"
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites content to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the file",
            ),
        },
        required=["file_path", "content"],
    ),
)