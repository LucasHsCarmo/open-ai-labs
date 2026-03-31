from openai import OpenAI
import os

client = OpenAI(
    api_key = os.getenv("API_KEY"),
)

response = client.audio.speech.create(
    model='tts-1',
    voice='onyx',
    input='Hello, my name is Lucas, and I am a SRE with 30 years age.'
)
response.write_to_file('output.mp3')