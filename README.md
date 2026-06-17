# RAG MVP

Small reproduction for a retrieval-augmented generation (RAG) MVP.

## Overview

This repository demonstrates a minimal RAG pipeline using local text files, a Chroma vector store, and Python utilities for ingestion and querying.

## Contents
- `app.py` — main application entry point for the MVP.
- `ingest.py` — script that ingests `data/*.txt` into a local Chroma DB.
- `query.py` — script to query the vector DB.
- `data/` — sample text files used for ingestion.
- `chroma_db/` — local SQLite DB (ignored by git).
- `requirements.txt` — Python dependencies.

## Quick start

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

4. Run the example query script:

```bash
python query.py
```

5. Optionally run the main app:

```bash
python app.py
```

## Notes
- The local Chroma SQLite database is stored in `chroma_db/chroma.sqlite3`.
- `chroma_db/` is intentionally ignored by git to avoid committing the database file.
- Add a LICENSE file and environment variable documentation before publishing.

## Contact
- Repository owner: amankumar2509

