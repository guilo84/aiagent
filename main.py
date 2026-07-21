import argparse
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    # Set up argparse to get the user's prompt from the command line
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to the AI")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not found. Please set it in your .env file.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    # The Iteration Loop (Max 20 attempts)
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free", # Or whichever model you are using
            messages=messages,
            tools=available_functions,
        )

        message = response.choices[0].message
        
        # 1. Append the assistant's response to the history immediately.
        # If it made tool calls, this ensures the API knows about them.
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                # Execute the function
                result_message = call_function(tool_call, verbose=args.verbose)
                
                if not result_message.get("content"):
                    raise ValueError(f"Function {tool_call.function.name} returned empty content.")
                
                if args.verbose:
                    print(f"-> {result_message['content']}")
                
                # 2. Append the function's result as a "tool" role message
                messages.append(result_message)
        else:
            # 3. No tool calls were made. The model has given its final answer!
            print(message.content)
            return # Exit the function successfully

    # 4. If the loop exhausts all 20 iterations without returning, it got stuck.
    print("\nError: Agent reached maximum iterations (20) without providing a final response.")
    sys.exit(1)

if __name__ == "__main__":
    main()
