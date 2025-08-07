import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def is_password_weak(password: str) -> bool:
    prompt = f"Is the following password weak or strong? Answer with only 'weak' or 'strong': {password}"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        result = response['choices'][0]['message']['content'].strip().lower()
        return "weak" in result
    except Exception as e:
        print(f"GPT Error: {e}")
        return False
