from langchain_ollama import ChatOllama

model = ChatOllama(model="phi3:latest")

while True:
    user_input = input(("User: "))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(user_input)
    print(f"Chatbot: {response.content}")