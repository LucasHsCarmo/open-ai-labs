from langchain_openai import OpenAI
from langchain_community.cache import InMemoryCache, SQLiteCache
from langchain_core.globals import set_llm_cache
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = OpenAI()

# set_llm_cache(InMemoryCache())

set_llm_cache(
    SQLiteCache(database_path="openai_cache.db")
)

prompt = "What's the beautiful places around world?"

response1 = model.invoke(prompt)
print(f"Call 1: {response1}")

response2 = model.invoke(prompt)
print(f"Call 2: {response2}")