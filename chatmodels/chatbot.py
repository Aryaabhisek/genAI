from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2506",temperature = 0.9)


messsages = [
    
]

print("---------------Welcome, type 0 to exit application---------------")

while True:
    prompt = input("You:")
    messsages.append(prompt)
    if prompt == "0":
        break
    response = model.invoke(messsages)
    messsages.append(response.content)
    print("Bot:", response.content)