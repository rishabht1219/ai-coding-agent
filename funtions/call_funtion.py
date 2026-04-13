from google.genai import types

from funtions.get_files_info import get_files_info, schema_get_files_info
from funtions.get_file_content import get_file_content, schema_get_file_content
from funtions.run_python_file import run_python_file, schema_run_python_file
from funtions.write_file import write_file, schema_write_file


available_functions = types.Tool(function_declarations=[
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
])


function_map = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}


def call_function(function_call, verbose=False):
    if function_call is None:
        raise ValueError("function_call is None")

    function_name = function_call.name or ""

    # Logging
    if verbose:
        print(f"Calling function: {function_name}({function_call.args})")
    else:
        print(f" - Calling function: {function_name}")

    # Validate function exists
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    # Copy args safely
    args = dict(function_call.args) if function_call.args else {}

    # Force working directory
    args["working_directory"] = "./calculator"

    if verbose:
        print(f"Resolved args: {args}")

    # Call function
    try:
        function_result = function_map[function_name](**args)

        if not isinstance(function_result, str):
            function_result = str(function_result)

        response = {"result": function_result}

    except Exception as e:
        response = {"error": str(e)}

    # Wrap result
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response=response,
            )
        ],
    )