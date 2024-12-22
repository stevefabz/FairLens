import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_recommendations(prompt: str) -> str:
    """Generate actionable recommendations using OpenAI API."""
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("OpenAI API Key not found in environment variables.")
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error fetching recommendations: {e}"
