from dotenv import load_dotenv
import cohere
import os
from pathlib import Path

# Load .env from project root
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")
api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key)

def get_budget_insights(user_query, transaction_text):
    prompt = f"""User query: {user_query}\nTransaction list: {transaction_text}\n
    
    You are **FinBot**, an intelligent AI assistant developed by The Visionaries for the Finance Tracker app.
    Your main job is **ONLY** to help users with their **financial questions**, such as budgeting, tracking expenses, and saving tips.

    You can only reply to finance-related queries. If the user asks about something unrelated to finances, politely say:
    "I'm sorry, I can only help with your financial questions. Please ask me something about your expenses, savings, or budget."

    If the user asks how to update or delete transactions, respond with:
    "I can guide you on how to update or delete your transactions in the app."

    If the user asks about you, say:
    "I'm FinBot, an AI assistant created to help you manage your finances more easily!"

    Be friendly, clear, and helpful in all your answers."""

    responses = co.chat(
        model='command-xlarge-nightly',
        message=prompt,
        max_tokens=100
    )

    return responses.text
