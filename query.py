import chromadb 
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(name="houses")

query = "How many bathroom does house 2 have?"

#user question -> embedding
query_embedding = model.encode(query)

#similarity search -> relevant document
results= collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=1
)

print(results)