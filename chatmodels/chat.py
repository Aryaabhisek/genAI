from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import ChatOpenAI

model = ChatOpenAI(model = "gpt-4.1")

response = model.invoke("What is Cricket?")
print(response.content)