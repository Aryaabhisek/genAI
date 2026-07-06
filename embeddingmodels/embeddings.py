from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model = 'text-embedding-3-large',
    dimensions = 64 
)

texts = [
    "Hi This is Arya",
    "Hello This is Sam",
    "Hello This is Jon Snow"
]

vector = embeddings.embed_documents(texts)

print(vector)

