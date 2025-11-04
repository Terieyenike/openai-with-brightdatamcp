import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from rich.console import Console
from rich.markdown import Markdown

load_dotenv(find_dotenv(), override=True)

api_token = os.getenv("OPENAI_API_KEY")
brightdata_api_token = os.getenv("BRIGHT_DATA_API_TOKEN")

client = OpenAI(api_key=api_token)

# Get user input
user_question = input("What would you like to know? ")

resp = client.responses.create(
  model="gpt-4o",
  tools=[
    {
      "type": "mcp",
      "server_label": "BrightData",
      "server_url": "https://mcp.brightdata.com/sse?token=" + brightdata_api_token,
      "require_approval": "never",
    },
  ],
  input=user_question,
)

Console().print(Markdown(resp.output_text))

# if __name__ == "__main__":
    # main()
