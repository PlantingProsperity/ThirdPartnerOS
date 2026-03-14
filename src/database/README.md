# The Shared Notebook (Database Layer)

This directory contains the relational core of Partner OS. It acts as the "Shared Notebook" where all agents record their work, ensuring the entire system stays coordinated.

## 1. High-Level Summary (For Principals)
Think of this as the master ledger for your business.
*   **Centralization:** Every deal you are working on, every file you upload, and every decision the AI makes is recorded here in one place.
*   **Coordination:** Agents don't need to "talk" to each other directly. They write their notes in this ledger so that the next agent knows exactly where the deal stands.
*   **Permanence:** This data stays on your local machine. It creates a permanent, searchable history of every deal you've ever analyzed with the system.

## 2. Components

### [Database Helper](./db.py)
*   **What it does:** The system's "Secretary." It provides simple Python functions for agents to read and write to the ledger.
*   **Key Feature:** It handles complex data (like negotiation scripts or financial citations) automatically, so the agents can focus on strategy.

### [Master Schema](../../schema.sql)
*   **What it does:** The "Blueprint." It defines exactly what information we track for every deal, from parcel numbers to seller archetypes.

## 3. System Integration
The Database Layer is the **Communication Bus** of Partner OS. 
1. The **Librarian** indexes a file here.
2. The **CFO** sees that file and records a financial draft.
3. The **Principal** verifies the numbers via the UI (which updates the database).
4. The **Manager** reads all the final records to issue a verdict.

Without this layer, the agents would be "blind" to each other's work.
