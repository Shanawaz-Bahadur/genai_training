from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

model = ChatOllama(model="qwen2.5:0.5b")

template1 = PromptTemplate(template="Expalin me this topic: {topic}", input_variables=["topic"])

# prompt1 = template1.invoke({'topic': "Cricket"})

# result = model.invoke(prompt1)

template2 = PromptTemplate(template="Summaries this :${context} in 5 Bullet points", input_variables=["context"])

# prompt2 = template2.invoke({"context": result.content})

chain = template1 | model | template2 | model 

chain_result = chain.invoke({'topic': "Cricket"})

# final_result = model.invoke(prompt2)

print("First result ",chain_result)
# print("Second Result",final_result.content)
