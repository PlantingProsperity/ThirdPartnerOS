-- =============================================================================
-- Partner OS — SQLite Database Schema
-- =============================================================================
-- This file is the authoritative definition of all tables in partner_os.db.
-- It is executed once on first run by src/database/db.py to initialize the
-- database. All schema changes must be made here and applied via migration.
--
-- Conventions:
--   - All primary keys are INTEGER (SQLite rowid alias) unless noted.
--   - All timestamps are TEXT in ISO 8601 format: YYYY-MM-DD HH:MM:SS
--   - All status fields use the string constants defined in config.py.
--   - All file paths are stored as absolute path strings.
--   - Foreign key constraints are enforced (PRAGMA foreign_keys = ON).
-- =============================================================================

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
-- WAL (Write-Ahead Logging) allows concurrent reads while writing.
-- Appropriate for a local single-machine system with multiple agent writes.


-- =============================================================================
-- DEALS — Master deal registry
-- =============================================================================
CREATE TABLE IF NOT EXISTS deals (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    deal_code       TEXT NOT NULL UNIQUE,
    -- Format: {4-digit-id}_{address_slug} e.g. 0042_1234_main_st_vancouver
    -- This matches the Deal Jacket directory name exactly.

    address         TEXT NOT NULL,
    -- Full human-readable property address.

    city            TEXT,
    state           TEXT DEFAULT 'WA',
    parcel_number   TEXT,

    status          TEXT NOT NULL DEFAULT 'INTAKE',
    -- One of DealStatus constants from config.py.

    assigned_to     TEXT DEFAULT 'BOTH',
    -- Which principal is lead: 'PRINCIPAL_1', 'PRINCIPAL_2', or 'BOTH'

    jacket_path     TEXT NOT NULL,
    -- Absolute path to the Deal Jacket directory on disk.

    created_at      TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at      TEXT NOT NULL DEFAULT (datetime('now')),
    notes           TEXT
);

CREATE INDEX IF NOT EXISTS idx_deals_status ON deals(status);
CREATE INDEX IF NOT EXISTS idx_deals_deal_code ON deals(deal_code);


-- =============================================================================
-- FILES — Librarian's index of all ingested files
-- =============================================================================
CREATE TABLE IF NOT EXISTS files (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    deal_id         INTEGER REFERENCES deals(id) ON DELETE CASCADE,
    -- NULL if file is in staging/inbox/unresolved (not yet assigned)

    file_path       TEXT NOT NULL UNIQUE,
    -- Absolute path to the file's current location on disk.

    original_path   TEXT,
    -- Path where the file was first discovered (staging or Drive sync).

    filename        TEXT NOT NULL,
    file_type       TEXT NOT NULL,
    -- MIME type or extension: 'audio', 'pdf', 'spreadsheet', 'text', 'image'

    content_class   TEXT,
    -- One of ContentClass constants from config.py.

    content_hash    TEXT NOT NULL,
    -- SHA-256 hash of file content. Used for duplicate detection.
    -- A file is re-processed only if this hash changes.

    status          TEXT NOT NULL DEFAULT 'PENDING',
    -- One of FileStatus constants from config.py.

    error_detail    TEXT,
    -- If status is FAILED, the exception message and traceback go here.

    discovered_at   TEXT NOT NULL DEFAULT (datetime('now')),
    processed_at    TEXT,
    last_modified   TEXT
);

CREATE INDEX IF NOT EXISTS idx_files_deal_id ON files(deal_id);
CREATE INDEX IF NOT EXISTS idx_files_status ON files(status);
CREATE INDEX IF NOT EXISTS idx_files_content_hash ON files(content_hash);


-- =============================================================================
-- DRAFT_FINANCIALS — CFO Phase 1 extraction output (AI-generated, UNVERIFIED)
-- =============================================================================
CREATE TABLE IF NOT EXISTS draft_financials (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    deal_id         INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,
    source_file_id  INTEGER REFERENCES files(id),
    -- The file the CFO read to extract these numbers.

    status          TEXT NOT NULL DEFAULT 'UNVERIFIED',
    -- UNVERIFIED → VERIFIED (when principal approves) → LOCKED (after calc)

    -- Extracted financial variables (all nullable — AI may not find all values)
    asking_price            REAL,
    gross_potential_income  REAL,
    vacancy_rate            REAL,
    effective_gross_income  REAL,
    operating_expenses      REAL,
    net_operating_income    REAL,
    annual_debt_service     REAL,
    loan_amount             REAL,
    purchase_price          REAL,
    square_footage          REAL,
    year_built              TEXT,
    num_units               INTEGER,

    -- Source citations: JSON array of {field, value, source_file, page, verbatim_text}
    -- The UI renders this so the principal can verify each number against its source.
    extraction_citations    TEXT,

    extracted_at    TEXT NOT NULL DEFAULT (datetime('now')),
    extracted_by    TEXT DEFAULT 'cfo_agent'
);

CREATE INDEX IF NOT EXISTS idx_draft_financials_deal_id ON draft_financials(deal_id);


-- =============================================================================
-- VERIFIED_FINANCIALS — Principal-approved financial inputs for CFO Phase 3
-- =============================================================================
CREATE TABLE IF NOT EXISTS verified_financials (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    deal_id         INTEGER NOT NULL UNIQUE REFERENCES deals(id) ON DELETE CASCADE,
    -- UNIQUE: only one verified record per deal at a time.

    draft_id        INTEGER NOT NULL REFERENCES draft_financials(id),
    -- Links back to the draft this was verified from.

    -- Principal-confirmed values (corrected from draft if needed)
    asking_price            REAL,
    gross_potential_income  REAL,
    vacancy_rate            REAL,
    effective_gross_income  REAL,
    operating_expenses      REAL,
    net_operating_income    REAL,
    annual_debt_service     REAL,
    loan_amount             REAL,
    purchase_price          REAL,
    square_footage          REAL,
    year_built              TEXT,
    num_units               INTEGER,

    verified_by     TEXT NOT NULL,
    -- Which principal approved: 'PRINCIPAL_1' or 'PRINCIPAL_2'

    verified_at     TEXT NOT NULL DEFAULT (datetime('now'))
);


-- =============================================================================
-- FINANCIAL_ANALYSES — CFO Phase 3 deterministic calculation results
-- =============================================================================
CREATE TABLE IF NOT EXISTS financial_analyses (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    deal_id         INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,
    verified_id     INTEGER NOT NULL REFERENCES verified_financials(id),

    -- Calculated metrics (pure Python math, no AI)
    cap_rate                REAL,   -- NOI / Purchase Price
    dscr                    REAL,   -- NOI / Annual Debt Service
    ltv_ratio               REAL,   -- Loan Amount / Purchase Price
    cash_on_cash_return     REAL,   -- Year 1 Cash Flow / Initial Equity
    irr_before_tax          REAL,   -- Before-tax Internal Rate of Return
    irr_after_tax           REAL,   -- After-tax Internal Rate of Return (if applicable)
    price_per_sqft          REAL,
    price_per_unit          REAL,   -- For multi-family deals

    -- Red line flags (set to 1 if threshold breached)
    flag_dscr_below_minimum         INTEGER DEFAULT 0,  -- DSCR < 1.2
    flag_ltv_above_maximum          INTEGER DEFAULT 0,  -- LTV > 75%
    flag_negative_cash_flow         INTEGER DEFAULT 0,

    -- AI interpretation and creative structuring recommendations
    -- (generated after deterministic math, grounded in Pinneo Brain)
    ai_interpretation       TEXT,
    structuring_options     TEXT,   -- JSON array of recommended structures
    pinneo_citations        TEXT,   -- JSON array of cited Pinneo heuristics

    calculated_at   TEXT NOT NULL DEFAULT (datetime('now'))
);


-- =============================================================================
-- PROPERTY_RECORDS — Scout agent public records output
-- =============================================================================
CREATE TABLE IF NOT EXISTS property_records (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    deal_id         INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,

    parcel_number   TEXT,
    owner_name      TEXT,
    owner_mailing_address TEXT,
    assessed_value  REAL,
    land_value      REAL,
    improvement_value REAL,
    tax_status      TEXT,       -- 'CURRENT', 'DELINQUENT', 'EXEMPT'
    tax_year        TEXT,
    zoning_code     TEXT,
    zoning_description TEXT,
    year_built      TEXT,
    square_footage  REAL,
    lot_size        REAL,
    ownership_tenure_years INTEGER,
    -- Years the current owner has held the property.
    -- >= 10 years triggers the Pinneo Equity Screen Rule.

    last_sale_date  TEXT,
    last_sale_price REAL,

    data_source     TEXT,       -- URL or 'CSV_UPLOAD'
    data_retrieved_at TEXT NOT NULL DEFAULT (datetime('now'))
);


-- =============================================================================
-- SCOUT_REPORTS — Scout agent synthesized signal report
-- =============================================================================
CREATE TABLE IF NOT EXISTS scout_reports (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    deal_id         INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,

    motivated_seller_score  INTEGER,
    -- 0-100. Higher = stronger motivated seller signal.

    -- Signal flags (1 = signal detected)
    flag_long_hold_period       INTEGER DEFAULT 0,  -- Ownership >= 10 years
    flag_tax_delinquency        INTEGER DEFAULT 0,
    flag_expired_listing        INTEGER DEFAULT 0,
    flag_probate_indicator      INTEGER DEFAULT 0,
    flag_suspicious_rent_data   INTEGER DEFAULT 0,

    signal_narrative    TEXT,
    -- Plain English description of all detected signals, Pinneo-cited.

    data_quality_notes  TEXT,
    -- Flags any data that appears unreliable (e.g. inflated rent estimates).

    pinneo_citations    TEXT,   -- JSON array
    generated_at        TEXT NOT NULL DEFAULT (datetime('now'))
);


-- =============================================================================
-- SELLER_PROFILES — Profiler agent psychological archetype output
-- =============================================================================
CREATE TABLE IF NOT EXISTS seller_profiles (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    deal_id         INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,

    seller_name     TEXT,
    archetype       TEXT,
    -- e.g. 'OLD_SCHOOL', 'MOTIVATED_DELEGATOR', 'ESTATE_HEIR',
    --      'ADVERSARIAL', 'CREATIVE_PARTNER', 'DISTRESSED'

    pain_hierarchy  TEXT,
    -- JSON ordered list of the seller's pain points from most to least acute.

    leverage_triggers TEXT,
    -- JSON list of what motivates this seller to act.

    recommended_approach TEXT,
    -- Plain English negotiation strategy for this specific seller.

    pinneo_scripts  TEXT,
    -- JSON list of relevant Pinneo verbatim scripts from the Master Rulebook.

    risk_flags      TEXT,
    -- Warnings: adversarial posture, attorney involvement, partnership disputes.

    pinneo_citations TEXT,   -- JSON array
    generated_at    TEXT NOT NULL DEFAULT (datetime('now'))
);


-- =============================================================================
-- SELLER_HISTORY — Cross-deal seller tracking (longitudinal)
-- =============================================================================
CREATE TABLE IF NOT EXISTS seller_history (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    seller_name     TEXT NOT NULL,
    entity_name     TEXT,       -- LLC, trust, or corporate name if applicable
    parcel_numbers  TEXT,       -- JSON list of all known parcel numbers
    deal_ids        TEXT,       -- JSON list of deal IDs this seller appears in
    first_seen_at   TEXT NOT NULL DEFAULT (datetime('now')),
    last_seen_at    TEXT NOT NULL DEFAULT (datetime('now')),
    notes           TEXT
);

CREATE INDEX IF NOT EXISTS idx_seller_history_name ON seller_history(seller_name);


-- =============================================================================
-- VERDICTS — Manager agent final APPROVE/KILL output
-- =============================================================================
CREATE TABLE IF NOT EXISTS verdicts (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    deal_id         INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,

    verdict         TEXT NOT NULL,
    -- 'APPROVE' or 'KILL'. No other values permitted.

    confidence_score INTEGER NOT NULL,
    -- 0-100. The Manager's confidence in this verdict.

    reasoning       TEXT NOT NULL,
    -- Plain English argument for the verdict. Must cite Pinneo Brain.

    conditions_to_flip TEXT,
    -- Required for KILL verdicts. JSON list of precise conditions that
    -- would flip this verdict to APPROVE. Null for APPROVE verdicts.

    pinneo_citations TEXT,   -- JSON array of cited heuristics
    low_confidence_flag INTEGER DEFAULT 0,
    -- Set to 1 if verdict was generated without sufficient Pinneo context.

    issued_at       TEXT NOT NULL DEFAULT (datetime('now'))
);


-- =============================================================================
-- LOI_DRAFTS — Manager agent Letter of Intent drafts
-- =============================================================================
CREATE TABLE IF NOT EXISTS loi_drafts (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    deal_id         INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,
    verdict_id      INTEGER NOT NULL REFERENCES verdicts(id),

    draft_version   INTEGER NOT NULL DEFAULT 1,
    file_path       TEXT NOT NULL,
    -- Absolute path to the .docx file in deals/{deal_code}/drafts/

    status          TEXT NOT NULL DEFAULT 'DRAFT',
    -- 'DRAFT' only — firewall prevents anything beyond draft status.

    generated_at    TEXT NOT NULL DEFAULT (datetime('now'))
);


-- =============================================================================
-- DEAL_OUTCOMES — Outcome tracking for the Continuous Learning Loop
-- =============================================================================
CREATE TABLE IF NOT EXISTS deal_outcomes (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    deal_id         INTEGER NOT NULL UNIQUE REFERENCES deals(id),

    final_status    TEXT NOT NULL,
    -- 'CLOSED' or 'DEAD'

    verdict_issued  TEXT,
    -- The APPROVE or KILL verdict that was active at resolution.

    verdict_correct INTEGER,
    -- 1 if verdict matched outcome, 0 if not. Used for accuracy tracking.

    confidence_score_at_verdict INTEGER,

    -- Closed deal details
    final_purchase_price    REAL,
    terms_achieved          TEXT,   -- JSON description of deal terms
    close_date              TEXT,
    days_to_close           INTEGER,

    -- Dead deal details
    failure_reason          TEXT,
    failure_flags           TEXT,   -- JSON list of specific failure causes

    -- Learning Loop data
    pinneo_heuristics_cited TEXT,   -- JSON list — what the system recommended
    seller_archetype_assigned TEXT, -- What the Profiler called it
    seller_archetype_confirmed TEXT, -- What it actually was in hindsight
    archetype_correct       INTEGER, -- 1 if archetype matched

    knowledge_doc_generated INTEGER DEFAULT 0,
    -- 1 if a knowledge/outcomes/ .md file was generated for this deal.

    knowledge_doc_approved  INTEGER DEFAULT 0,
    -- 1 if principals approved the doc for embedding into ChromaDB.

    knowledge_doc_path      TEXT,
    -- Absolute path to the .md file in knowledge/outcomes/

    recorded_at     TEXT NOT NULL DEFAULT (datetime('now')),
    recorded_by     TEXT
    -- Which principal recorded this outcome.
);


-- =============================================================================
-- ARCHETYPE_PERFORMANCE — Longitudinal archetype success tracking
-- =============================================================================
CREATE TABLE IF NOT EXISTS archetype_performance (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    archetype       TEXT NOT NULL UNIQUE,
    total_deals     INTEGER DEFAULT 0,
    closed_deals    INTEGER DEFAULT 0,
    dead_deals      INTEGER DEFAULT 0,
    close_rate      REAL,
    -- Recalculated by the Learning Loop: closed_deals / total_deals
    last_updated    TEXT NOT NULL DEFAULT (datetime('now'))
);
