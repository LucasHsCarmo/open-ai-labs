import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.prompts import PromptTemplate

from langchain_community.tools import DuckDuckGoSearchResults

load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-3.5-turbo")


@tool
def calculator(expression: str) -> str:
    """Execute simple financial calculations."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

# Define the search tool - DuckDuckGO
search_tool = DuckDuckGoSearchResults()

# Define o template do prompt
prompt_template = PromptTemplate.from_template("""
You are a financial assistant.

Use:
- internet search for updated financial advice
- calculations when needed

Always answer in English.

User question:
{query}
""")

# Example question that requires both search and calculation tools
question = """
My income is R$10,000 per month, my total expenses are R$8,500 plus 1,000 reais in rent.
What investment tips do you give me?
"""

# Search for relevant financial advice based on the user's question
search_results = search_tool.invoke("financial tips budgeting investing Brazil")

# Prepare the prompt with the user's question and the search results
prompt = prompt_template.invoke({
    "query": question + "\n\nRelevant info:\n" + str(search_results)
})

# Call the model
response = model.invoke(prompt)

print(response.content)