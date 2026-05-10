import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(message: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=message
    )

    return response.output_text