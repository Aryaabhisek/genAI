from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(model = "mistral-small-2506",temperature = 0.9)


messsages = [
    SystemMessage(content= "You are a Funny AI Agent")
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