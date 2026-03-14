# Shared Utilities

This directory contains specialized tools used by all agents in Partner OS. These are the "power tools" that handle complex technical tasks so the agents can focus on real estate strategy.

## 1. Components

### [GenAI Client](./genai_client.py)
*   **For Laymen:** The secure "phone line" to Google's AI models. It handles the identification (keys and tokens) required to talk to the AI.
*   **For Programmers:** A factory function that initializes the `google-genai` SDK. It robustly handles both OAuth (for CLI/production) and API Keys (for testing/development).

### [PDF Utils](./pdf_utils.py)
*   **For Laymen:** The "translator" for documents. It opens PDFs (like zoning codes or municipal plans) and extracts the text so the AI can read it.
*   **For Programmers:** A wrapper around `pdfplumber` that safely extracts text page-by-page.

### [Text Utils](./text_utils.py)
*   **For Laymen:** The "chopper." AI can't read a 500-page book all at once. This tool chops the text into bite-sized "chunks" based on chapters and headings.
*   **For Programmers:** Implements Markdown-aware recursive splitting. It preserves header hierarchy so that chunks remain semantically grounded.

### [Logger](./logger.py)
*   **For Laymen:** The "black box recorder." It keeps a permanent record of every action the system takes, stored in `logs/partner_os.log`.
*   **For Programmers:** A standardized `logging` wrapper that ensures consistent formatting and log levels across all modules.

## 2. System Integration
Utilities are used by every other layer of the system. For example, the **Librarian** uses PDF Utils to process new files, while the **Embedder** uses GenAI Client to generate the data for the Brain.
