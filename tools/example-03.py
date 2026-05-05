import os
from dotenv import load_dotenv
from langchain.agents import Tool
from langchain_core.prompts import PromptTemplate
from langchain_experimental,utilities import PythonREPL
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-3.5-turbo")

python_repl = PythonREPL()
python_repl_tool = Tool(
    name="python_repl",
    description="A Python REPL. Use this to execute validate Python code.",
    func=python_repl.run
)

agent_executor = create_python_agent(
    llm=model,
    tools=python_repl_tool,
    verbose=True
)

# Prompt
prompt_template = PromptTemplate.from_template(
    "Resolve the calculation:\n\n{content}"
)

# Query
question = "20 x 25"

# Mount prompt
prompt = prompt_template.format({"content": question})

# Call LLM
response = agent_executor.invoke(prompt)
print(response.get("output"))