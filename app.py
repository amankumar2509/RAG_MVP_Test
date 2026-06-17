import os
import streamlit as st
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

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("houses")

# UI
st.title("🏠 RAG Test Assistant")

st.markdown("""
Ask questions about the houses stored in ChromaDB.

### Example Questions
- Which house has the most bedrooms?
- Describe House F
- How many bathrooms does House B have?
""")

st.success("App Loaded Successfully")

query = st.text_input("Ask a question")

if st.button("Search") and query:

    st.write("Generating embedding...")

    query_embedding = model.encode(query)

    st.write("Retrieving documents...")

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
    )

    retrieved_chunks = results["documents"][0]

    retrieved_text = "\n".join(retrieved_chunks)

    st.subheader("Retrieved Chunks")

    for chunk in retrieved_chunks:
        st.write(chunk)

    st.subheader("Sources")

    for metadata in results["metadatas"][0]:
        st.write(metadata["source"])

    prompt = f"""
Answer the question using ONLY the provided context.

Carefully analyze all retrieved information before answering.

If the question asks:
- highest
- lowest
- most
- least
- compare

then compare all relevant values before answering.

Context:
{retrieved_text}

Question:
{query}
"""

    st.write("Calling Gemini...")

    gemini_model = genai.GenerativeModel("gemini-2.5-flash")

    response = gemini_model.generate_content(prompt)

    st.subheader("Answer")

    st.write(response.text)