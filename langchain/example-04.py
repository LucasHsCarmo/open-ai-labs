from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-3.5-turbo")

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are give to answer based on the data geographical location of the Brazil."),
        HumanMessagePromptTemplate.from_template("Please, tell me about the region {region}."),
        AIMessage(content="Sure! I go to start collecting infomation about the region {region} and I will give you an answer as soon as possible."),
        HumanMessage(content="Ok, I will input demographic data."),
        AIMessage(content="Understand. Here is the data:")
    ]
)


prompt = chat_template.format_messages(region="South")

response = model.invoke(prompt)

print(response.content)