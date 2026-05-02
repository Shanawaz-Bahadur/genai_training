from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOllama(model="phi3:latest")

chat_history = [
    SystemMessage(content="You are an Helpful Assistant.")
]

while True:
    user_input = input(("User: "))
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"Chatbot: {response.content}")

print("Chat history:", chat_history)