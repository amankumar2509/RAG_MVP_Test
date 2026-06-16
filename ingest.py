import os
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Create/Get collection
collection = client.get_or_create_collection(
    name="houses"
)

data_folder = "data"

for filename in os.listdir(data_folder):

    filepath = os.path.join(data_folder, filename)

    with open(filepath, "r") as file:
        text = file.read()

    # Skip empty files
    if not text.strip():
        print(f"Skipping empty file: {filename}")
        continue

    # Create embedding
    embedding = model.encode(text)

    # Store in ChromaDB
    collection.upsert(
        ids=[filename],
        embeddings=[embedding.tolist()],
        documents=[text],
        metadatas=[{"source": filename}]
    )

    print("FILE:", filename)
    print("CONTENT:", text)
    print("EMBEDDING LENGTH:", len(embedding))
    print("-" * 50)

print("Documents stored successfully!")