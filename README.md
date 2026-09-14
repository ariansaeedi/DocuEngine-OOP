# 🚀 DocuEngine: Object-Oriented Document Processing & Search Pipeline

A lightweight, pure Python framework demonstrating advanced **Object-Oriented Programming (OOP)** patterns applied to Document Processing, Chunking, and Retrieval (the foundational layer of RAG systems).

## ✨ Key OOP Concepts Implemented:
- **Encapsulation & Validation:** Managed attributes using `@property` and `@setter` with defensive data validation.
- **Alternative Constructors:** Implemented `@classmethod from_file()` for seamless file ingestion.
- **Abstract Base Classes (ABC):** Designed `BaseSearchEngine(ABC)` enforcing modular polymorphic search implementations.
- **Inheritance & Polymorphism:** Subclassed `SimpleKeywordSearch` overriding core retrieval behaviors with `super()`.
- **Dunder (Magic) Methods:**
  - `__len__`: Document & search index size evaluation.
  - `__repr__`: Human-readable object inspection.
  - `__contains__`: Intuitive keyword lookup (`if "keyword" in search_engine:`).
- **Custom Exceptions:** Clean error management via `EmptyQueryError`.

## 🛠️ Project Structure
```text
DocuEngine/
├── models.py       # Document class with property and classmethod
├── chunker.py      # TextChunker with overlapping logic
├── search.py       # BaseSearchEngine (ABC) & SimpleKeywordSearch
├── demo.py         # End-to-end pipeline execution
└── sample.txt      # Sample file for testing from_file()
💻 Quick Start
from models import Document
from chunker import TextChunker
from search import SimpleKeywordSearch

# 1. Ingest via classmethod
doc = Document.from_file("sample.txt", doc_id=1)

# 2. Chunk with overlap
chunker = TextChunker(chunk_size=10, overlap=2)
chunks = chunker.split(doc)

# 3. Index and Search
engine = SimpleKeywordSearch()
engine.add_documents(chunks)

# 4. Search and verify
results = engine.search("AI")
print("AI" in engine)  # Returns True