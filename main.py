import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
  raise RuntimeError("GEMINI_API_KEY environment variable not found.")
       
client = genai.Client(api_key=api_key)

def main():
    parser = argparse.ArgumentParser(description="A simple CLI AI Agent powered by Gemini")
    parser.add_argument("user_prompt", type=str, help="The prompt you want to send to the AI")
    args = parser.parse_args()    
    
    prompt_text = args.user_prompt
    print(f"User prompt: {prompt_text}")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_text
    )
    print(response.text)

    if response.usage_metadata is None:
        raise RuntimeError("API request failed to return usage metadata. The request may have failed.")

    # 2. Print the token counts
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
