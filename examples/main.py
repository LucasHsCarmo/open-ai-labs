from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("API_KEY"),
)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me more about Chevrolet Cobalt!"}
    ],
    stream=True, # view the response as a stream of events
    temperature=0.2, # control the randomness and lower values make the output more deterministic | between 0 and 2
)

for chunk in stream: # iterate through the stream of events
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")