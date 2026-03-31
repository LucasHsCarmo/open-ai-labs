from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = OpenAI()

# response = model.invoke(
#     input="What is Allan Turing?",
#     temperature=1,
#     max_tokens=250,
# )

# print(response)

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=1,
    max_tokens=250,
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Allan Turing?"},
]

response = model.invoke(messages)
print(response)
print(response.content)