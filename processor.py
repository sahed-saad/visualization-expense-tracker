import pandas as pd
from openai import OpenAI

# Initialize the client for Gemini 2.5 (via OpenAI wrapper)
client = OpenAI(
    api_key="GEMINI_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def auto_categorize(description):
    """
    Uses the exact prompt and logic provided by the user.
    """
    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[{
                "role": "user", 
                "content": f"You are a financial assistant. Categorize this expense into one of: ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Shopping', 'Others']. Expense: {description}Just return the category name.Return ONLY the plain text word, no bolding, no asterisks, and no punctuation."
            }]
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "Other"