import os
import chromadb
from sentence_transformers import SentenceTransformer

# print("STEP 1")

model = SentenceTransformer("all-MiniLM-L6-v2")

# print("STEP 2")

client = chromadb.PersistentClient(path="./chroma_db")

# print("STEP 3")

collection = client.get_or_create_collection(
    name="houses"
)

# print("STEP 4")

data_folder = "data"

for filename in os.listdir(data_folder):
    filepath = os.path.join(data_folder, filename)
    
    with open(filepath,"r") as file:
        text = file.read()
    embedding = model.encode(text)
    collection.add(
        ids=[filename],
        embeddings=[embedding.tolist()],
        documents=[text],
        metadatas=[{"source": filename}],
    )

    print("FILE:", filename)
    print("CONTENT:", text)
    print("EMBEDDING LENGTH:", len(embedding))
    print("-"*50)
print("Documents stored successfully!")