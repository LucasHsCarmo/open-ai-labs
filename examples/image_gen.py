from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("API_KEY"),
)

response = client.images.generate(
    model="dall-e-3",
    prompt="The SRE with your laptop, in the style of a futuristic environment",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)