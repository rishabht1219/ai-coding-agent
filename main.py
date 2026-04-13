import os
from google import genai
import argparse
from dotenv import load_dotenv
from google.genai import types
from prompt import system_prompt
from funtions.call_funtion import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
]

config = types.GenerateContentConfig(
    tools=[available_functions],
    system_instruction=system_prompt
)

MAX_STEPS = 20

for step in range(MAX_STEPS):

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=messages,
        config=config
    )

    # ✅ Step 1: Add model response to conversation
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    function_responses = []

    # ✅ Step 2: Handle function calls
    if response.function_calls:
        for function_call in response.function_calls:

            function_call_result = call_function(function_call, verbose=args.verbose)

            if not function_call_result.parts:
                raise Exception("Function call result has no parts")

            part = function_call_result.parts[0]

            if part.function_response is None:
                raise Exception("Missing function_response")

            result = part.function_response.response

            if result is None:
                raise Exception("Function response is None")

            function_responses.append(part)

            if args.verbose:
                print(f"-> {result}")

        # ✅ Step 3: Append ALL tool results as USER (CRITICAL FIX)
        messages.append(
        types.Content(role="tool", parts=function_responses)
    )

    else:
        # ✅ Step 4: Final response
        print("Final response:")
        print(response.text)
        break

else:
    # ❌ If loop never finishes
    print("Agent did not finish within max steps.")
    exit(1)