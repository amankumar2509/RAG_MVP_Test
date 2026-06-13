# RAG MVP

Small reproduction for a retrieval-augmented generation (RAG) MVP.

Contents
- `ingest.py` — script that ingests `data/*.txt` into a local Chroma DB.
- `query.py` — (placeholder) script to query the vector DB.
- `data/` — sample text files used for ingestion.
- `chroma_db/` — local SQLite DB (ignored by git).

Quick start

1. Create a Python virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ingest sample data:

```bash
python ingest.py
```

4. Query the database (example):

```bash
python query.py
```

Notes
- The local Chroma SQLite database is stored in `chroma_db/chroma.sqlite3`. That file is intentionally listed in `.gitignore` and will not be pushed to the repository.
- If you publish this repository, consider adding a LICENSE and more detailed README sections describing architecture and environment variables.

Contact
- Repository owner: amankumar2509
# RAG_MVP_Test
RAG model 
