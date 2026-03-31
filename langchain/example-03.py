from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-3.5-turbo")

template = """
Translate the text to {language1} to {language2}:
{text}
"""

prompt_template = PromptTemplate.from_template(
    template=template
)

prompt = prompt_template.format(
    language1="English",
    language2="Portuguese",
    text="What's the beautiful places around world?"
)

response = model.invoke(prompt)

print(response.content)