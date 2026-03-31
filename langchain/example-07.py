from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-3.5-turbo")

loader = TextLoader("base_conhecimento.txt")
document = loader.load()

prompt_base_conhecimento = PromptTemplate(
    input_variables=["context","question"],
    template="""Use the following context to answer the question.
    Answer only with the information provided in the context.
    Don't use any information that is not in the context.
    Context: {context}
    Question: {question}
    """
)

chain = prompt_base_conhecimento | model | StrOutputParser()

response = chain.invoke(
    {
        "context": "\n".join(doc.page_content for doc in document),
        "question": "What's the capital of France?"
    }
)

print(response)