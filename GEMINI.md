# GEMINI.md — Partner OS / "The Third Partner"

## AI-Native Digital Back-Office for Commercial Real Estate


---

## DOCUMENT STATUS

|Field|Value|
|---|---|
|Version|1.1|
|Supersedes|GEMINI.md v1.0|
|Changes in this version|Betterleaks security layer (immediate); Memsearch hybrid Brain retrieval (Sprint 1A); Galileo Agent Control centralized governance (V1 planned)|

---

## WHO YOU ARE BUILDING FOR

Partner OS is a multi-agent AI system functioning as a superintelligent Co-General Partner for a two-principal commercial real estate brokerage in Clark County, WA, affiliated with Weichert Realtors | Equity NW.

The two principals are strategic thinkers and smart non-developers. Communicate in plain English at all times. Explain what you are doing and why before you do it. Never assume they know what a library, pattern, or architectural decision means — explain it in one plain English sentence alongside any technical term you use.

The full system specification lives in: `docs/PartnerOS_Architecture_v1.0.docx` Read it when you need architectural context beyond what is here.

---

## YOUR WORKING POSTURE

You are a master software architect and you are trusted as one. Lead with your expertise. You do not need permission to think.

Your default behavior is:

1. **If the task is clear:** State your plan briefly in plain English, then proceed. Flag any meaningful decision points as you encounter them.
    
2. **If the task is ambiguous:** Ask your clarifying questions first — all of them at once, not one at a time — then plan, then proceed.
    
3. **Always before writing code:** Name every file you will create or modify and what each one does. This is not a gate — it is a courtesy that keeps the principals oriented.
    
4. **Always after writing code:** Provide the exact terminal command to verify it works, and describe what success looks like vs. failure. A task is not complete until it is verified.
    

---

## YOU ARE FREE TO

- Propose a better library, pattern, or approach than what is specified here — explain why it is better, and wait for a "yes" before implementing it. Never silently substitute.
    
- Push back on a requirement if you believe it will cause problems. State your concern and offer a concrete alternative.
    
- Raise architectural concerns proactively, even if not asked.
    
- Ask "are you sure?" when a request conflicts with this document or the architecture specification.
    

---

## YOU MUST NEVER DO

These are failure modes we have already experienced. Do not repeat them.

- **No hollow code.** Never write a function, class, or module that contains placeholder logic, `pass` statements, `# TODO` comments, or stub implementations. If you cannot implement something fully right now, say so explicitly. Do not fake it.
    
- **No walls of code.** Do not generate more than one logical unit per response (one file, one class, one coherent function group) unless explicitly instructed. Small steps, verified before the next step begins.
    
- **No silent decisions.** If you choose a library, pattern, or approach not specified here, name it and briefly justify it.
    
- **No overconfidence.** If you are uncertain whether something will work on this specific hardware or OS configuration, say so before building around it.
    
- **Never search the principals' personal files or directories** for knowledge content. All knowledge is loaded manually by the principals into the `knowledge/` folder. Read from `knowledge/` — do not find or move the principals' files.
    

---

## TECH STACK (VERIFIED — DO NOT SUBSTITUTE WITHOUT PROPOSING FIRST)

All software must be free and open source. The only paid service is the Google Gemini API, accessed via Google account OAuth — there is no API key. Authentication is already configured on this machine.

### Core Backend

|Layer|Tool|Notes|
|---|---|---|
|Language|Python 3.11+|All agent logic, all pipelines|
|AI Engine|Google Gemini API|`google-genai` library. OAuth — no API key needed.|
|Embeddings|`text-embedding-004`|Via Gemini API. Generates vectors for ChromaDB.|
|Vector Database|ChromaDB 1.x|Local, no server. Two collections: `pinneo_brain` and `reference_library`.|
|Brain Retrieval|Memsearch (Zilliz, MIT)|Hybrid dense + BM25 sparse search + reranking. Replaces raw ChromaDB query calls in `retriever.py`. See MEMSEARCH INTEGRATION section.|
|Relational Database|SQLite|Standard library `sqlite3` — no install needed.|
|Audio Transcription|OpenAI Whisper|`openai-whisper` package. CPU mode only — see hardware note.|
|Document Generation|`python-docx`|Generates LOIs and strategy briefs as .docx files.|

### V0.1 Frontend (Streamlit — Python Native)

The V0.1 UI is built entirely in **Streamlit**. It is pure Python, requires no JavaScript, no build pipeline, and no API routing layer. It runs locally in a browser tab. This eliminates an entire category of complexity for the initial build.

`streamlit` replaces React + FastAPI for V0.1. FastAPI is deferred to V1 when the agent layer is proven and a richer UI is warranted.

### File Ingestion & Sync

|Tool|Role|
|---|---|
|`rclone`|Already configured. Syncs Google Drive to `staging/` on a schedule set by the principal.|
|Streamlit file uploader|Active ingestion. Files uploaded through the UI are written directly to `staging/inbox/`. The Librarian sweep processes them from there.|

No continuous file watcher (watchdog) is used. All file ingestion is handled by the Librarian sweep. This eliminates a continuously-running process and the edge cases that come with it (partial writes, mid-sync rclone states, file descriptor leaks). Simpler is correct here.

### Scout Tooling

|Tool|Role|
|---|---|
|`playwright`|Headless browser for scraping JavaScript-rendered county websites (Clark County Assessor portal, etc.).|
|`beautifulsoup4`|HTML parsing of pages rendered by Playwright.|
|`pandas`|CSV ingestion for manually exported county records and rent rolls.|

### Security Tooling (Active — installed at scaffold)

|Tool|Role|
|---|---|
|Betterleaks|Pre-commit secret scanner. Blocks any commit containing API keys, tokens, `.env` files, or hardcoded paths. Configured in `.betterleaks.toml`. Installed via `scripts/install_hooks.sh`.|

### V1 Planned Integrations (Do not build yet — architecture only)

|Tool|Role|
|---|---|
|Galileo Agent Control|Centralized policy governance plane for all five agents. Replaces per-agent hard-coded guardrails with a single policy layer. See GALILEO AGENT CONTROL section.|

### Infrastructure

|Tool|Role|
|---|---|
|Git + GitHub|Version control. Commit after every verified sprint.|

### Hardware Constraints

Debian 13.3, Intel i7-950, 11GB RAM, NVIDIA GTX 580 (`nouveau` driver). The GTX 580's CUDA version is too old for PyTorch or TensorFlow GPU acceleration. All ML workloads (Whisper, embeddings) run on CPU. Do not write CUDA-dependent code under any circumstances.

---

## THE THREE LAWS (ABSOLUTE — NEVER VIOLATE)

1. **THE FIREWALL:** Partner OS produces draft-only outputs. No email, contract, LOI, or document is ever sent, signed, or executed by the system. All outbound action requires explicit principal authorization. Enforced in code via `src/utils/firewall.py`, which validates every agent output before it reaches the UI. In V1: Galileo Agent Control will enforce this as a system-wide policy rather than per-file code. `firewall.py` remains authoritative until Agent Control is installed and verified.
    
2. **THE VERDICT:** Every deal analysis terminates in exactly one of two verdicts: `APPROVE` or `KILL`. There is no CONDITIONAL state. Every KILL verdict must include a `conditions_to_flip` field: a precise, enumerated list of what would have to be true for the verdict to become APPROVE. The verdict is decisive. The reasoning carries the nuance. Both verdicts include a confidence score (0-100) and plain English reasoning grounded in Pinneo Brain citations.
    
3. **THE BRAIN:** Every deal recommendation must be grounded in retrieved context from the Pinneo Brain (ChromaDB + Memsearch). Outputs generated without Pinneo citations must be flagged explicitly as `LOW_CONFIDENCE: TRUE`.
    

---

## THE FOUR KNOWLEDGE CATEGORIES

This is the foundational data architecture distinction. Do not mix these categories. Do not deviate from this model.

### CATEGORY 1 — WISDOM

**What it answers:** "How do we think about this?" **Where it lives:** ChromaDB collection: `pinneo_brain` **Who manages it:** Principals load manually into `knowledge/pinneo/` and `knowledge/ccim/`. The system reads it. Never modifies it. **What it contains:**

- Greg Pinneo's processed transcript `.md` files (60-100 files)
- CCIM course modules and financial frameworks
- Negotiation heuristics, deal-structuring philosophy, mental models

### CATEGORY 2 — REFERENCE

**What it answers:** "What are the rules governing this?" **Where it lives:** ChromaDB collection: `reference_library` **Who manages it:** Principals load manually into `knowledge/reference/`. Updated when regulations change. The system reads it. Never modifies it. **What it contains:**

- Clark County zoning codes and municipal building codes
- Washington State real estate law
- Federal regulations (1031 exchange, SEC rules, etc.)
- Any document required to make a sound, legally informed decision

### CATEGORY 3 — DATA

**What it answers:** "What do we know about this deal, property, or person?" **Where it lives:** SQLite database: `data/partner_os.db` **Who manages it:** Agents write to it during normal operation. Principals review and verify via the UI. Never embedded into ChromaDB. **What it contains:**

- Properties (address, zoning, square footage, assessed value)
- Sellers (ownership history, contact history, behavior patterns)
- Deal financials — in two states (see CFO Hallucination Firewall)
- Agent outputs (verdicts, profiles, financial analyses)
- Deal outcomes (feeds the Continuous Learning Loop)

### CATEGORY 4 — LEARNED OUTCOMES

**What it answers:** "What has actually worked in the real world?" **Where it lives:** ChromaDB collection `pinneo_brain` (merged at embed time) and source files in `knowledge/outcomes/` **Who manages it:** Generated by the Learning Loop when a deal closes. Principals review and approve before embedding. Read-only after approval. **What it contains:**

- Structured `.md` files summarizing closed deals: what Pinneo doctrine proved correct, what the seller archetype actually was, what terms were achieved. Embedded alongside Pinneo transcripts so the Brain learns from real deals the same way it learned from Greg's lectures.

---

## SECURITY LAYER — BETTERLEAKS

### What it is

Betterleaks is a drop-in replacement for Gitleaks, the industry-standard open-source secret scanner. It runs as a Git pre-commit hook — meaning it scans every file staged for commit before Git allows the commit to proceed. If it finds a leaked credential, the commit is blocked and the finding is printed to the terminal.

It uses a novel filtering method called "token efficiency" that achieves 98.6% recall for detecting real secrets (vs. 70.4% for traditional entropy-based tools). In practical terms: fewer false alarms, more real catches.

### Why it is installed at scaffold, before Sprint 1A

The greatest risk window for a credential leak is early in development, when code is moving fast and patterns haven't solidified. Installing Betterleaks at scaffold — before a single line of production logic is written — ensures there is no gap in protection.

### Files

|File|Purpose|
|---|---|
|`.betterleaks.toml`|Rule configuration. Defines what counts as a secret for Partner OS specifically (Gemini OAuth tokens, generic API key assignments, `.env` files, hardcoded home directory paths).|
|`scripts/install_hooks.sh`|One-time setup script. Downloads the Betterleaks binary to `scripts/bin/` and writes `.git/hooks/pre-commit`. Run once from repo root after cloning.|
|`.git/hooks/pre-commit`|The actual hook Git calls before every commit. Written by `install_hooks.sh` — do not edit manually.|
|`.gitignore`|Excludes `scripts/bin/` (binary), `.env` (secrets), `staging/`, `deals/`, `data/` (client data), `knowledge/` (IP), `token.json` (OAuth cache).|

### Custom Rules Active in `.betterleaks.toml`

|Rule ID|What it catches|
|---|---|
|`google-oauth-token`|Google OAuth `ya29.*` access tokens|
|`google-service-account-key`|Service account JSON credential files|
|`generic-api-key-assignment`|Any `API_KEY = "..."` pattern with a 20+ char value|
|`dotenv-file`|A `.env` file staged for commit|
|`private-key-block`|PEM-encoded private keys (RSA, EC, OpenSSH)|
|`database-connection-string`|Remote DB URIs with embedded credentials|
|`hardcoded-home-path`|`/home/fasahov/...` paths hardcoded instead of using `config.py` constants — this is also a GEMINI.md coding standards violation|

### Installation (one-time, already done if scaffold is complete)

```bash
# From repo root:
chmod +x scripts/install_hooks.sh
./scripts/install_hooks.sh
```

Success: green banner, checkmark, confirmation that the binary runs.

### Verification

```bash
# Simulate a leak — should be BLOCKED:
echo 'API_KEY = "sk-abc123def456ghi789jkl012mno345pqr"' > /tmp/test_leak.py
git add /tmp/test_leak.py
git commit -m "test"
# Expected: commit blocked, red banner with finding printed
git restore --staged /tmp/test_leak.py && rm /tmp/test_leak.py
```

### Emergency bypass

```bash
git commit --no-verify
```

Use only in a genuine emergency. Log the reason in the commit message. The bypass is auditable — it appears in `git log`.

### Developer workflow impact

Zero. When no secrets are present, the hook prints one line (`✓ No secrets detected`) and the commit proceeds normally.

---

## MEMSEARCH INTEGRATION — HYBRID PINNEO BRAIN

### What it is

Memsearch is an open-source library (MIT license) from Zilliz, the company behind the Milvus vector database. It gives AI systems persistent, long-term memory by combining two retrieval methods that are individually weaker than their combination:

- **Dense vector search** (what ChromaDB does today): finds semantically similar content — good at conceptual matching ("what Pinneo says about motivated sellers").
- **BM25 sparse search**: a keyword-matching algorithm — good at precise term matching ("And/Or Assigns clause", "Substitution of Security", exact Pinneo-isms).
- **Reranking**: a second-pass model that scores the combined results and surfaces the most relevant chunks at the top.

The combination (hybrid search + reranking) consistently outperforms either method alone, especially for domain-specific terminology like Pinneo's vocabulary.

### Why this matters for Partner OS

The Pinneo Brain contains highly specific, idiosyncratic language ("The Bird," "The Unforgiving Minute," "Gift Pile," "Wall Tent"). Pure dense vector search can miss exact term matches when the semantic neighborhood is noisy. BM25 catches exact phrases. Reranking sorts the combined pool. The result: the Manager's citations are more precise, verdicts are better grounded, and `LOW_CONFIDENCE` flags are rarer.

### Architectural fit — what changes, what stays the same

**What stays exactly the same:**

- ChromaDB remains the vector store. Memsearch sits in front of it as a retrieval interface — it does not replace ChromaDB's storage role.
- The `pinneo_brain` and `reference_library` collections are unchanged.
- Knowledge files remain plain-text `.md` files in `knowledge/`. (Memsearch was designed around this exact format — `.md` files are its native memory unit.)
- The embedder pipeline (`src/brain/embedder.py`) is unchanged.

**What changes:**

- `src/brain/retriever.py` is rewritten to route queries through Memsearch's hybrid search interface instead of calling ChromaDB directly. ChromaDB becomes the backend Memsearch talks to.
- A new dependency is added to `requirements.txt`: `memsearch`.
- The `src/brain/chroma_client.py` connection is passed to Memsearch at initialization rather than used directly by agents.

**In plain English:** Agents still call `retriever.py` the same way they always did. They ask a question, they get ranked chunks back. The only thing that changes is what happens inside `retriever.py` — it now uses Memsearch instead of a raw ChromaDB query. Agents don't know or care about this difference.

### Continuous Learning Loop — Memsearch alignment

Memsearch was built around the exact pattern the Learning Loop uses: generating `.md` memory files from real-world events and making them retrievable. When `learning/loop.py` generates a closed-deal summary and saves it to `knowledge/outcomes/`, that file is in precisely the format Memsearch expects. The principals approve it, the Librarian embeds it, and future retrievals surface it alongside Pinneo doctrine as a first-class memory.

### Implementation target: Sprint 1A (alongside `embedder.py`)

`retriever.py` must be written to the Memsearch interface from day one. Do not write a raw ChromaDB retriever and plan to migrate later. Building the retriever correctly once is cheaper than migrating it.

### Sprint 1A implementation sequence

1. Install `memsearch` — add to `requirements.txt` with pinned version.
2. Write `src/brain/chroma_client.py` — ChromaDB connection, collection management. This is Memsearch's backend; initialize it first.
3. Write `src/brain/embedder.py` — knowledge ingestion pipeline. Reads `.md` files from `knowledge/`, chunks them, generates embeddings via `text-embedding-004`, writes to ChromaDB.
4. Write `src/brain/retriever.py` — the Memsearch hybrid interface. Accepts a natural-language query, returns ranked chunks with source citations. All agents call this and only this for Brain queries.
5. Write `tests/test_brain.py` — end-to-end: ingest one Pinneo `.md` file, query for a known Pinneo-ism, assert the correct chunk is returned in position 1 of the results.

### Requirements addition

```
# requirements.txt addition for Sprint 1A:
memsearch==<latest-stable>   # Zilliz hybrid search over ChromaDB
                              # MIT license. Check pypi.org/project/memsearch
                              # for current stable version before pinning.
```

---

## GALILEO AGENT CONTROL — V1 PLANNED INTEGRATION

### Status: Architecture only. Do not build in V0.1.

This section documents the planned V1 integration so the V0.1 codebase is built in a way that makes Agent Control easy to add later. Read it before building any agent in V0.1 — it affects how guardrails should be structured now.

### What it is

Galileo Agent Control (Apache 2.0 license) is an open-source control plane — a centralized location where policies governing AI agent behavior are defined and enforced. Instead of hard-coding behavioral rules into each agent file, policies are written once and applied across all agents simultaneously. Policy updates take effect in real time without restarting or redeploying agents.

It solves the exact problem Partner OS faces as it scales from five agents in V0.1 to a richer agent ecosystem in V1: when a compliance rule changes (e.g., "never generate an LOI without a verified DSCR above 1.15"), today that change requires editing `manager.py`, `firewall.py`, and potentially the Manager's prompt. In V1, it means updating one policy in Agent Control and all agents inherit it.

### Why V1, not V0.1

In V0.1, five agents with three hard-coded laws is manageable. The complexity that justifies a centralized control plane emerges when:

- The number of policies grows beyond what can be held in a developer's head
- Policies need to be updated without code changes (e.g., principals want to adjust a threshold)
- Multiple agents need to enforce the same policy and drift is a risk

V0.1 does not have these problems yet. Building Agent Control before the agents exist is premature. Building agents in a way that makes Agent Control easy to add later is the correct posture now.

### How to build V0.1 agents so Agent Control slots in cleanly

Each agent in V0.1 should enforce its guardrails through a single, clearly named validation function — not scattered inline conditionals. This is the pattern:

```python
# CORRECT — guardrail is isolated and named
def _validate_output(self, output: dict) -> dict:
    """
    Validates agent output against current policy.
    In V0.1: enforces hard-coded Three Laws.
    In V1: this function will delegate to Galileo Agent Control's
    policy evaluation API. Isolating it here means V1 migration
    is a one-function change per agent, not a full rewrite.
    """
    return firewall.validate(output)  # V0.1 implementation

# WRONG — guardrails scattered through business logic
# These are impossible to centralize later without a full rewrite.
```

Every agent file must contain this pattern. When Agent Control is integrated in V1, the only code change per agent is replacing the body of `_validate_output` to call the Agent Control API instead of `firewall.validate`. The rest of the agent is unchanged.

### V1 policy architecture (planned, not built)

These are the policies that will be defined in Agent Control at V1:

|Policy ID|Scope|Rule|
|---|---|---|
|`LAW_1_FIREWALL`|All agents|No agent may produce output that triggers an external action (send, sign, execute) without principal authorization.|
|`LAW_2_VERDICT`|Manager only|Every deal analysis must produce exactly one binary verdict: APPROVE or KILL. No CONDITIONAL state.|
|`LAW_3_BRAIN`|Manager, Profiler|Every recommendation must include at least one Pinneo Brain citation. Output without citations is flagged LOW_CONFIDENCE.|
|`CFO_VERIFIED_GATE`|CFO|No financial calculation may execute without a `verified_financials` record in SQLite.|
|`DSCR_FLOOR`|CFO, Manager|Flag any deal where DSCR falls below 1.15 for elevated principal review. (Threshold is adjustable via Agent Control UI — no code change required.)|
|`SINGLE_DEAL_SCOPE`|All agents|No agent may read files from a deal directory other than the one it is currently authorized to process.|

### Integration platforms that already support Agent Control

Strands Agents, CrewAI, Glean, and Cisco AI Defense are listed as first-wave integrations. Partner OS's Python-native multi-agent architecture will integrate via Agent Control's Python SDK when it reaches V1 readiness.

---

## THE LIBRARIAN — FULL SCOPE & AUTHORITY

The Librarian (Archivist) is the sole gatekeeper of all data entering the system. It is the only agent permitted to move, rename, or reorganize files anywhere in the filesystem. No other agent touches files. No other agent makes routing decisions.

### The Two Operating Modes

**Mode 1 — The Sweep** The Librarian's primary operation. Runs automatically on startup and can be triggered manually by the principals at any time through the UI. The sweep performs a full reconciliation in this order:

1. Recursively scan `staging/` for all files not yet in the SQLite index.
2. For each unindexed file: classify it, determine its deal association, and move it to the correct Deal Jacket subdirectory.
3. If deal association is ambiguous, write the file to `staging/inbox/unresolved/` and flag it in SQLite as `AWAITING_PRINCIPAL` — surface it in the UI for the principal to assign.
4. Recursively scan all `deals/` subdirectories and reconcile against SQLite — update any records where files have changed, been renamed, or are missing.
5. Update `jacket.json` for every deal touched during the sweep.
6. Trigger downstream processing for newly routed files (Whisper for audio, PDF extraction for documents, etc.).

The sweep is the single mechanism for all file ingestion. There is no continuously-running file watcher. This keeps the system simple, predictable, and free of edge cases caused by partial writes or mid-sync file states from rclone.

**Mode 2 — UI Upload Handler** When a principal uploads a file through the Streamlit UI, the file is written to `staging/inbox/` and nothing more. The UI confirms receipt. The next sweep — which the principal can trigger immediately — processes it from there. The Librarian makes all routing decisions; the UI never routes files directly to a Deal Jacket.

### The Librarian's Classification Logic

When processing a file from `staging/`, the Librarian determines:

- **File type:** audio, PDF, spreadsheet, image, text/markdown, other
- **Content class:** seller correspondence, financial document (T12, rent roll, OM), title report, field notes, municipal record, other
- **Deal association:** which deal does this file belong to? Association is determined by folder path (if synced from a named Drive subfolder), filename patterns, or AI classification of content. When uncertain: `AWAITING_PRINCIPAL`.

### The Librarian's Indexing Contract

Every file processed is recorded in SQLite with:

- Absolute file path (using `pathlib.Path`)
- Deal ID it belongs to
- File type and content class
- Processing status: `PENDING`, `PROCESSING`, `COMPLETE`, `FAILED`, `AWAITING_PRINCIPAL`
- Timestamps: discovered, processed, last modified
- Content hash (SHA-256): used to detect duplicates and track changes

The Librarian never processes the same file twice unless its content hash has changed. Duplicate detection is hash-based, not filename-based.

---

## AGENT COMMUNICATION & SHARED DEAL STATE

Agents in Partner OS do not call each other directly. There is no message queue, no inter-process communication, and no agent-to-agent API. This is intentional. It keeps the system simple, inspectable, and debuggable on a single local machine.

### The Communication Model: SQLite as the Shared State Bus

SQLite is the single source of truth for all operational state. Every agent reads deal state from SQLite before acting. Every agent writes its outputs and status updates to SQLite when done. The Manager reads all agent outputs from SQLite to synthesize verdicts.

In plain English: agents communicate by leaving structured records in a shared notebook (SQLite) that every agent can read. No agent talks to another agent directly. They all read from and write to the same notebook. This also means every agent action is permanently logged and inspectable by the principals at any time.

### The Deal State Machine

Every deal in SQLite has a `status` field that moves forward through a defined sequence. An agent is only authorized to act on a deal when that deal's status is the one that calls for it. No agent skips ahead. No agent acts out of turn. Status transitions are written to SQLite by the agent completing that stage.

```
INTAKE
  └─► LIBRARIAN_PROCESSING       Librarian is classifying and routing files
        └─► AWAITING_VERIFICATION  CFO extracted financials; principal must verify
              └─► CFO_CALCULATING   Verified financials confirmed; running math
                    └─► SCOUT_RUNNING        Scout querying public records
                          └─► PROFILER_RUNNING   Profiler building seller archetype
                                └─► MANAGER_SYNTHESIZING  Manager reading all outputs
                                      └─► VERDICT_ISSUED     APPROVE or KILL issued
                                            └─► PRINCIPAL_REVIEW  Principals reviewing
                                                  ├─► CLOSED        Deal completed
                                                  └─► DEAD          Deal abandoned
```

### Agent Output Contracts

Every agent writes structured, versioned records to SQLite. Each agent owns specific tables and may not write to others'. Read access is broad; write access is strictly scoped.

|Agent|Writes to|Reads from|
|---|---|---|
|Librarian|`files`, `deal_index`|`deals`|
|CFO|`draft_financials`, `verified_financials`, `financial_analyses`|`files`, `deals`|
|Scout|`property_records`, `scout_reports`|`deals`, `files`|
|Profiler|`seller_profiles`|`deals`, `scout_reports`, `files`, `seller_history`|
|Manager|`verdicts`, `loi_drafts`|all agent output tables, ChromaDB via `retriever.py`|

### jacket.json — The Filesystem Manifest

Every Deal Jacket contains a `jacket.json` maintained solely by the Librarian. It records what files exist in this deal's directories, their classification, and their processing status. Other agents read it for file path resolution and never write to it.

When `jacket.json` and SQLite conflict, SQLite is authoritative. `jacket.json` exists for human readability and quick inspection.

### Cross-Deal and Longitudinal State

Partner OS accumulates intelligence across deals over time through:

**SQLite longitudinal tables:** `deal_outcomes`, `seller_history`, `archetype_performance` — these grow with every deal processed. The Profiler queries `seller_history` to detect if a seller or entity has been encountered before. The Manager queries `archetype_performance` to weight its reasoning toward what has historically worked in Clark County specifically.

**ChromaDB growth via Learning Loop + Memsearch:** As approved closed-deal summaries are embedded into `pinneo_brain`, the Brain becomes richer over time. Future retrievals via Memsearch surface not just Pinneo's original doctrine but validated real-world applications of that doctrine from the principals' own deal history. The hybrid search ensures that both the conceptual wisdom and the precise deal-specific language are retrievable.

---

## THE CFO HALLUCINATION FIREWALL

LLMs hallucinate numbers. This is a known, non-negotiable risk when parsing financial documents (T12s, rent rolls, OMs). The CFO agent enforces a mandatory three-phase pipeline. Skipping any phase is a critical architectural error.

### Phase 1 — EXTRACT (AI)

The CFO reads the raw document and extracts financial variables into a `draft_financials` record in SQLite, flagged `status: UNVERIFIED`. For every number extracted, it records the exact source citation: filename, page number, and the verbatim text it read the number from. This is surfaced in the UI for principal verification. Deal status advances to `AWAITING_VERIFICATION`.

### Phase 2 — VERIFY (Human — mandatory gate)

The Streamlit UI renders a verification form: every extracted number alongside its source citation. The principal reviews, corrects any errors, and explicitly clicks "Approve Numbers." This creates a `verified_financials` record in SQLite, locks the draft record, and advances deal status to `CFO_CALCULATING`.

### Phase 3 — CALCULATE (Pure Python — no AI)

Only after `verified_financials` exists and deal status is `CFO_CALCULATING` does the CFO run its deterministic math. This is pure Python arithmetic — no LLM at this stage. DSCR, IRR, Cap Rate, LTV, and Cash-on-Cash are calculated from human-approved inputs only. The CFO must verify the presence of a `verified_financials` record at the start of every calculation function and raise an explicit, logged error if it is absent or `UNVERIFIED`. This check is not optional and never skippable.

---

## THE DEAL JACKET — FILESYSTEM CONTRACT

Every deal gets one isolated directory under `deals/`. The Librarian creates this directory when a deal is first registered. No other agent or process creates Deal Jacket directories.

```
deals/
  {DEAL_ID}_{address_slug}/       e.g., 0042_1234_main_st_vancouver/
    audio/                        .m4a / .mp3 / .mp4 originals
    transcripts/                  Whisper output (.txt / .md)
    documents/                    PDFs, spreadsheets, OMs, title reports
    analysis/                     Agent outputs (write-once, timestamped)
    drafts/                       LOIs, strategy briefs (Firewall-gated)
    jacket.json                   Filesystem manifest (Librarian only)

staging/
  inbox/                          All new files land here — UI uploads and
  │                               rclone Drive syncs arrive here first.
  └── unresolved/                 Files the Librarian could not auto-assign.
                                  Flagged for principal review in the UI.
```

### Filesystem Authority Rules — enforce in code

- **The Librarian is the only agent that moves or renames files.** All other agents are read-only on the filesystem except for writing their own outputs to `analysis/` (or `drafts/` for the Manager).
    
- **`analysis/` is write-once per agent per run.** Never edit in place. Each output is a new timestamped file: `{agent}_{YYYYMMDD_HHMMSS}.json`.
    
- **`jacket.json` is written only by the Librarian.** Never by any other agent or by the UI.
    
- **No agent accesses another deal's directory.** Enforce with a path validation check at the start of every file operation: confirm the resolved absolute path begins with the authorized deal's directory before any read or write executes.
    
- **`staging/` and `deals/` are entirely separate.** Files in `staging/` have not been processed. Files in `deals/` have. The Librarian is the only process that moves files from one to the other.
    

---

## THE CONTINUOUS LEARNING LOOP

Partner OS evolves over decades. Learning happens at the retrieval layer — not by retraining the Gemini model, which is not possible. New knowledge is added to ChromaDB (via Memsearch) and SQLite so that future retrievals reflect accumulated real-world experience.

### Track A — Outcome Recording (every deal resolution)

When a deal closes or dies, principals record the outcome in the UI. SQLite stores: verdict issued vs. actual outcome, confidence score, Pinneo heuristics cited, seller archetype assigned vs. confirmed, terms achieved (closed deals), reason for failure (dead deals).

### Track B — Knowledge Reinforcement (on successful close)

The Learning Loop generates a structured `.md` summary of the closed deal and saves it to `knowledge/outcomes/`. Principals approve it. The Librarian embeds it into ChromaDB via the standard embedder pipeline. Memsearch's hybrid index is updated automatically — the new memory is immediately retrievable by all agents on the next query. Future deals benefit from this real-world experience exactly as they benefit from Pinneo's lectures.

### Track C — Pattern Analysis (on principal request)

The Manager analyzes `deal_outcomes` and `archetype_performance`: which archetypes close most in Clark County? Which Pinneo heuristics correlate with success? Produces a plain-English report. Principals review. System recommends — principals decide.

---

## THE FIVE AGENTS

Full specifications in `docs/PartnerOS_Architecture_v1.0.docx`.

|Agent|Codename|Core Job|
|---|---|---|
|The Manager|Chief of Staff|Reads all agent outputs from SQLite → APPROVE or KILL verdict → drafts LOIs|
|The Librarian|Archivist|Runs sweeps → classifies and routes all files → sole filesystem authority|
|The CFO|Underwriter|Phase 1: AI extraction. Phase 2: human verification. Phase 3: pure Python math.|
|The Scout|Intelligence Officer|Playwright scraping of Clark County records → motivated seller signal detection|
|The Profiler|Psychologist|Seller archetypes via Pinneo doctrine + longitudinal seller history|

### Guardrail pattern — required in every agent (for V1 Agent Control compatibility)

Every agent class must implement guardrails through a single isolated method. This is not optional. See GALILEO AGENT CONTROL section for why.

```python
def _validate_output(self, output: dict) -> dict:
    """
    Validates agent output against current policy.
    V0.1: delegates to firewall.validate().
    V1: this method will delegate to Galileo Agent Control's
        policy evaluation API. No other code changes required.
    """
    from src.utils import firewall
    return firewall.validate(output)
```

---

## PROJECT FILE STRUCTURE

```
PartnerOS_gemini/
├── GEMINI.md                            ← This file. The CLI's primary context.
├── .betterleaks.toml                    ← Secret scanner rules (Betterleaks)
├── .gitignore                           ← Security-first: excludes all secrets,
│                                          data, knowledge, and binaries
├── docs/
│   └── PartnerOS_Architecture_v1.0.docx
├── scripts/
│   ├── install_hooks.sh                 ← One-time Betterleaks setup. Run once.
│   └── bin/                             ← Betterleaks binary (gitignored)
│       └── betterleaks
├── config.py                            ← All constants. API keys via env vars only.
├── requirements.txt                     ← All dependencies, pinned versions
├── knowledge/
│   ├── pinneo/                          ← WISDOM (manually loaded)
│   ├── ccim/                            ← WISDOM (manually loaded)
│   ├── reference/                       ← REFERENCE (manually loaded)
│   └── outcomes/                        ← LEARNED (Learning Loop output)
├── staging/
│   ├── inbox/                           ← All new files arrive here
│   └── inbox/unresolved/                ← Ambiguous files awaiting principal assignment
├── deals/                               ← Deal Jackets (Librarian creates and manages)
│   └── {DEAL_ID}_{slug}/
│       ├── audio/
│       ├── transcripts/
│       ├── documents/
│       ├── analysis/
│       ├── drafts/
│       └── jacket.json
├── data/
│   ├── chroma/                          ← ChromaDB vector store (auto-created)
│   └── partner_os.db                    ← SQLite (auto-created on first run)
├── src/
│   ├── ui/
│   │   └── app.py                       ← Entire V0.1 Streamlit frontend
│   ├── agents/
│   │   ├── manager.py                   ← Must implement _validate_output()
│   │   ├── librarian.py                 ← Must implement _validate_output()
│   │   ├── cfo.py                       ← Must implement _validate_output()
│   │   ├── scout.py                     ← Must implement _validate_output()
│   │   └── profiler.py                  ← Must implement _validate_output()
│   ├── brain/
│   │   ├── embedder.py                  ← knowledge/ → chunks → embeddings → ChromaDB
│   │   ├── retriever.py                 ← Memsearch hybrid interface (dense + BM25
│   │   │                                   + reranking). All agents call this only.
│   │   └── chroma_client.py             ← ChromaDB connection. Backend for Memsearch.
│   ├── database/
│   │   ├── schema.sql                   ← All SQLite table definitions and indexes
│   │   └── db.py                        ← Connection helpers and typed query functions
│   ├── integrations/
│   │   ├── drive_sync.py                ← rclone wrapper and sync scheduling
│   │   └── whisper_transcriber.py       ← Audio to transcript (CPU mode)
│   ├── learning/
│   │   └── loop.py                      ← Outcome recording and knowledge reinforcement
│   └── utils/
│       ├── logger.py                    ← Centralized logging. Never use print().
│       └── firewall.py                  ← Validates all agent output. Enforces Law 1.
│                                          V1: will delegate to Galileo Agent Control.
└── tests/
    ├── test_brain.py                    ← Memsearch hybrid retrieval end-to-end test
    ├── test_cfo.py
    └── test_firewall.py
```

---

## CODING STANDARDS

- Module-level docstring on every file: what it does, what it owns
- Docstring on every function: purpose, args, return value, exceptions
- Type hints on every function signature
- All configuration in `config.py` — never hardcoded anywhere else
- All file paths use `pathlib.Path` — never raw strings
- Error handling: specific exception types only, never bare `except:`
- Use `logging` module exclusively — never `print()`
- PEP 8 compliant, 4-space indentation
- All database writes use parameterized queries — never string formatting
- All file operations validate that the resolved absolute path is inside the authorized directory before executing
- All agent guardrails live in `_validate_output()` — never inline

---

## SPRINT ROADMAP

### COMPLETED — Scaffold

All folders and stub files created. `requirements.txt` and `config.py` are complete and verified. Betterleaks pre-commit hook installed and verified. `.gitignore` is security-hardened.

### SPRINT 1A — The Pinneo Brain (current)

Build the knowledge ingestion and retrieval layer. This is the foundation everything else depends on.

**Files to build, in order:**

1. `src/brain/chroma_client.py` — ChromaDB connection and collection management. This is Memsearch's backend. Build it first.
2. `src/brain/embedder.py` — Reads `.md` files from `knowledge/`, chunks them, generates embeddings via `text-embedding-004`, writes to ChromaDB.
3. `src/brain/retriever.py` — Memsearch hybrid interface. Takes a natural-language query, returns ranked chunks with source citations. This is what all five agents call.
4. `tests/test_brain.py` — Ingest one Pinneo `.md` file, query for a known Pinneo-ism, assert correct chunk is in position 1.

**Sprint 1A is complete when:** `python -m pytest tests/test_brain.py` passes.

### SPRINT 1B — SQLite Schema & Database Layer

Build the relational layer that all agents share as their communication bus.

**Files to build:**

1. `src/database/schema.sql` — All table definitions and indexes.
2. `src/database/db.py` — Typed connection helpers and parameterized query functions.

**Sprint 1B is complete when:** `partner_os.db` is created, all tables exist, and a test write/read roundtrip passes.

### SPRINT 2 — The Librarian

Build the file ingestion and routing agent. Nothing else can be built until the Librarian can get files into Deal Jackets.

**Sprint 2 is complete when:** A file dropped in `staging/inbox/` is correctly classified, routed to a Deal Jacket, and recorded in SQLite.

### SPRINT 3 — The CFO (Phases 1 and 2 only)

Build the financial extraction and human verification pipeline. Phase 3 (pure Python math) follows in Sprint 3B.

### SPRINT 4 — The Scout

Build the Clark County public records scraper using Playwright.

### SPRINT 5 — The Profiler

Build the seller archetype engine using Pinneo doctrine.

### SPRINT 6 — The Manager + V0.1 UI

Synthesize all agent outputs into verdicts and draft LOIs. Wire everything into the Streamlit frontend.

### V1 — Agent Control Integration (post-V0.1)

When all five agents are operational and tested, migrate guardrail enforcement from `firewall.py` to Galileo Agent Control. Because every agent implements `_validate_output()` as a single isolated method, this migration is a one-function change per agent — no architectural rewrite required.

---

## CURRENT SPRINT: 1A — THE PINNEO BRAIN

The scaffold is complete. Betterleaks is installed. The `knowledge/` folders are being populated manually by the principals.

**Your immediate task:** Build `src/brain/chroma_client.py`.

Before writing any code, state:

- What the file does
- What it owns
- The exact terminal command to verify it works after you write it
- What success looks like vs. failure

Then write the complete file. No stubs. No placeholders.
