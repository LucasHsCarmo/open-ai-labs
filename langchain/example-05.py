from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-3.5-turbo")

# prompt_template = PromptTemplate.from_template("Tell me about the car {car_name}.")
# runnable_sequence = prompt_template | model | StrOutputParser()
# response = runnable_sequence.invoke({ "car_name": "Marea 20v 1999" })
# print(response)

runnable_sequence = (
    PromptTemplate.from_template("Tell me about the car {car_name}.")
    | model
    | StrOutputParser()
)

response = runnable_sequence.invoke({ "car_name": "Marea 20v 1999" })
print(response)