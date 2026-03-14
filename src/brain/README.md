# The Pinneo Brain (Retrieval Layer)

This directory contains the "Brain" of Partner OS. It is responsible for storing, searching, and retrieving the wisdom of Greg Pinneo and the legal rules governing commercial real estate.

## 1. High-Level Summary (For Principals)
Think of this as a super-intelligent filing cabinet. 
*   It **reads** all the transcripts, books, and laws you provide.
*   It **remembers** every detail by converting text into numerical "vectors" (mathematical finger-prints).
*   It **finds** the exact right advice when an agent asks a question, like "How do I handle an emotional seller?"
*   It **cites** its sources, so you always know exactly which transcript or law the advice came from.

## 2. Components

### [Chroma Client](./chroma_client.py)
*   **What it does:** Manages the actual database files where the "fingerprints" are stored.
*   **How it works:** It sets up two separate "collections": one for Wisdom (Pinneo/CCIM) and one for Reference (Laws/Zoning).

### [Embedder](./embedder.py)
*   **What it does:** The ingestion engine. It reads your files and turns them into data the computer can search.
*   **Key Feature:** It uses "Incremental Ingestion." It calculates a unique code (hash) for every file. If the file hasn't changed, it skips it, saving time and money.

### [Retriever](./retriever.py)
*   **What it does:** The search interface used by all other agents.
*   **Key Feature:** "Hybrid Search." It doesn't just look for keywords; it understands the *meaning* of your question. It then double-checks the results to make sure they are high-quality before showing them to you.

## 3. System Integration
The Brain is the foundation of every decision. When the **Manager** needs to issue a verdict or the **Profiler** needs to understand a seller, they "ask the Brain" for relevant context. No agent is allowed to make a recommendation without first checking the Brain for Greg Pinneo's doctrine.
