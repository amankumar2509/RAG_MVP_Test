import os
import chromadb
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader


#chunking function
def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Create/Get collection


collection = client.get_or_create_collection(
    name="houses"
)

# data_folder = "data"

# for filename in os.listdir(data_folder):

#     filepath = os.path.join(data_folder, filename)

#     with open(filepath, "r") as file:
#         text = file.read()

data_folder = "data"

for filename in os.listdir(data_folder):

    filepath = os.path.join(data_folder, filename)

    text = ""

    if filename.endswith(".txt"):

        with open(filepath, "r") as file:
            text = file.read()

    elif filename.endswith(".pdf"):

        reader = PdfReader(filepath)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    else:
        print(f"Skipping unsupported file: {filename}")
        continue

    # Skip empty files
    if not text.strip():
        print(f"Skipping empty file: {filename}")
        continue


    # Chunk text
    chunks = chunk_text(text)


    # Create embedding
    # embedding = model.encode(text)

    # Store in ChromaDB


    # collection.upsert(
    #     ids=[filename],
    #     embeddings=[embedding.tolist()],
    #     documents=[text],
    #     metadatas=[{"source": filename}]
    # )

    for i, chunk in enumerate(chunks):

        embedding = model.encode(chunk)

        collection.upsert(
            ids=[f"{filename}_{i}"],
            embeddings=[embedding.tolist()],
            documents=[chunk],
            metadatas=[
                {
                    "source": filename,
                    "chunk": i
                }
            ]
        )

    print("FILE:", filename)
    # print("CONTENT:", text)
    print(f"Stored {len(chunks)} chunks from {filename}")
    print("EMBEDDING LENGTH:", len(embedding))
    print("-" * 50)

print("Documents stored successfully!")