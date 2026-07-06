from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'
)

texts = [
    "Hi This is Arya",
    "Hello This is Sam",
    "Hello This is Jon Snow"
]

vector = embedding.embed_documents(texts)

print(vector)