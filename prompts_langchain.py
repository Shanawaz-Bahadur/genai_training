from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOllama(model="phi3:latest")

# model - phi3:latest

template = PromptTemplate.from_template("What is the capital of {country}?")

# prompt = template.invoke(input={"country": "France"})

chain = template | llm

# result= llm.invoke(prompt)

result = chain.invoke({"country": "France"} )

print(result.content)