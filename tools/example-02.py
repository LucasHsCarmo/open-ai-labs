import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-3.5-turbo")

# Tool Wikipedia
wikipedia_tool = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(lang="en")
)

# Prompt
prompt_template = PromptTemplate.from_template(
    "Summarize the following content:\n\n{content}"
)

# Query
question = "Alan Turing"

# Find on Wikipedia
wiki_result = wikipedia_tool.invoke(question)

# Mount prompt
prompt = prompt_template.invoke({"content": wiki_result})

# Call LLM
response = model.invoke(prompt)

print(response.content)