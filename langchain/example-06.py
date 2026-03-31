from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-3.5-turbo")

classification_chain = (
    PromptTemplate.from_template(
        """
        Classify the question the user of the following categories:
        - Finance
        - Technical Support
        - Others informations

        Question: {question}
        """
    )
    | model
    | StrOutputParser()
)

financial_chain = (
    PromptTemplate.from_template(
        """        
        You are a specialized financial. 
        Always answer the question inicializing with: "Welcome to the Financial Department".
        Answer the question to the user:
        Question: {question}
        """    )
    | model
    | StrOutputParser()
)

technical_support_chain = (
    PromptTemplate.from_template(
        """       
        You are a specialized technical support. 
        Always answer the question inicializing with: "Welcome to the Technical Support Department".
        Answer the question to the user:
        Question: {question}
        """
        )
    | model
    | StrOutputParser()
)

other_informations_chain = (
    PromptTemplate.from_template(
        """        
        You are a specialized in other informations. 
        Always answer the question inicializing with: "Welcome to the Other Informations Department".
        Answer the question to the user:
        Question: {question}
        """    
    )
    | model
    | StrOutputParser()
)

def route(answer: str):
    answer = answer.lower()
    if "finance" in answer:
        return financial_chain
    elif "technical support" in answer:
        return technical_support_chain
    else:
        return other_informations_chain

question = input("What is your question? \n")

classification = classification_chain.invoke(
    { "question": question }
)

response_chain = route(answer=classification)

response = response_chain.invoke(
    { "question": question }
)

print(response)