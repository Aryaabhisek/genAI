from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(model = "mistral-small-2506",temperature = 0.9)

print("Choose your AI Mode")
print("Press 1 for Angry Mode")
print("Press 2 for Funny Mode")
print("Press 3 for Sad Mode")

choice = int(input("Tell me your response : "))

if choice == 1:
    mode = "You are an angry AI Agent , you respond aggressively and impatiently."
elif choice == 2:
    mode = "You are very funny AI Agent, you respond with humor and jokes."
elif choice == 3:
    mode = "You are an angry AI Agent, you respond aggressively."


messsages = [
    SystemMessage(content= mode)
]

print("---------------Welcome, type 0 to exit application---------------")

while True:
    prompt = input("You:")
    messsages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messsages)
    messsages.append(AIMessage(response.content))
    print("Bot:", response.content)
    
print(messsages)