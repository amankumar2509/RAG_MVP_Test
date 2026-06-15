import os
import chromadb
import google.generativeai as genai

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("houses")

# User Question
query = input("Ask a question: ")
# Query Embedding
query_embedding = model.encode(query)

# Retrieval
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=1
)

retrieved_text = results["documents"][0][0]

print("Retrieved Context:")
print(retrieved_text)

print("-" * 50)

# Prompt Augmentation
prompt = f"""
Answer the question using ONLY the provided context.

Give only the information requested.
Do not add extra details.


Context:
{retrieved_text}

Question:
{query}
"""

# Gemini
gemini_model = genai.GenerativeModel("gemini-2.5-flash")

response = gemini_model.generate_content(prompt)

print("Answer:")
print(response.text)