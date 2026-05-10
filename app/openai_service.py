import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_openai(instructions: str, user_input: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=instructions,
        input=user_input
    )

    return response.output_text


def summarize_text(text: str, style: str = "simple") -> str:
    instructions = f"""
You are a professional text summarizer.
Summarize the user's text in a {style} style.
Keep the summary clear, useful, and not too long.
"""

    return ask_openai(
        instructions=instructions,
        user_input=text
    )


def translate_text(text: str, target_language: str) -> str:
    instructions = f"""
You are a professional translator.
Translate the user's text into {target_language}.
Only return the translated text.
Do not add explanations.
"""

    return ask_openai(
        instructions=instructions,
        user_input=text
    )


def generate_titles(text: str, count: int = 5) -> str:
    instructions = f"""
You are a professional copywriter.
Generate {count} clear and attractive title ideas from the user's text.
Return the result as a numbered list.
"""

    return ask_openai(
        instructions=instructions,
        user_input=text
    )


def explain_code(code: str, language: str = "auto-detect") -> str:
    instructions = f"""
You are a senior software developer.
Explain this {language} code in simple words.

Include:
1. What the code does
2. Important parts
3. Any possible improvement
"""

    return ask_openai(
        instructions=instructions,
        user_input=code
    )