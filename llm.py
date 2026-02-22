import os
import config
from dotenv import load_dotenv, find_dotenv
from google import genai

#load_dotenv()

#api_key = os.getenv("")

client = genai.Client(api_key=config.GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)