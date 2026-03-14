import pytest
import os
import shutil
from pathlib import Path
from src.database.db import get_db_connection, init_db
from config import DATABASE_PATH

@pytest.fixture(autouse=True)
def setup_teardown():
    """Ensure a clean database for initialization tests."""
    if DATABASE_PATH.exists():
        os.remove(DATABASE_PATH)
    yield
    if DATABASE_PATH.exists():
        os.remove(DATABASE_PATH)

def test_init_db():
    # 1. Initialize database
    init_db()
    assert DATABASE_PATH.exists()
    
    # 2. Get singleton connection
    conn = get_db_connection()
    assert conn is not None
    
    # 3. Verify tables were created correctly
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='deals'")
    assert cursor.fetchone() is not None
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='files'")
    assert cursor.fetchone() is not None
    
def test_singleton_connection():
    conn1 = get_db_connection()
    conn2 = get_db_connection()
    assert conn1 is conn2

def test_deal_lifecycle():
    from src.database.db import register_deal, update_deal_status, get_deal
    init_db()
    
    # 1. Register a new deal
    deal_id = register_deal("1234 Main St", "0001_1234_main_st", "/home/fasahov/PartnerOS/deals/0001_1234_main_st")
    assert deal_id is not None
    
    # 2. Retrieve the deal
    deal = get_deal(deal_id)
    assert deal['address'] == "1234 Main St"
    assert deal['deal_code'] == "0001_1234_main_st"
    assert deal['status'] == "INTAKE" # Default from schema
    
    # 3. Update status
    update_deal_status(deal_id, "LIBRARIAN_PROCESSING")
    
    # 4. Verify update
    updated_deal = get_deal(deal_id)
    assert updated_deal['status'] == "LIBRARIAN_PROCESSING"
    assert updated_deal['updated_at'] >= deal['created_at']

def test_file_indexing():
    from src.database.db import register_deal, index_file, get_file_by_hash, init_db
    init_db()
    
    deal_id = register_deal("Test Deal", "T001", "/tmp")
    
    # 1. Index a file
    file_path = "/tmp/test.pdf"
    file_hash = "abc123hash"
    file_id = index_file(deal_id, file_path, "test.pdf", "pdf", file_hash)
    assert file_id is not None
    
    # 2. Retrieve by hash
    file_record = get_file_by_hash(file_hash)
    assert file_record is not None
    assert file_record['filename'] == "test.pdf"
    assert file_record['deal_id'] == deal_id
    
    # 3. Handle non-existent hash
    assert get_file_by_hash("nonexistent") is None

def test_json_verdict_serialization():
    from src.database.db import init_db, register_deal, save_verdict, get_latest_verdict
    init_db()
    deal_id = register_deal("Verdict Test", "V001", "/tmp")
    
    # 1. Save verdict with complex JSON data (citations)
    citations = [
        {"source": "Pinneo 1", "heading": "Ethics", "score": 0.95},
        {"source": "Zoning Code", "heading": "R-1", "score": 0.88}
    ]
    save_verdict(deal_id, "APPROVE", 95, "Strong doctrine grounding.", citations)
    
    # 2. Retrieve and verify deserialization
    verdict = get_latest_verdict(deal_id)
    assert verdict['verdict'] == "APPROVE"
    assert verdict['confidence_score'] == 95
    
    # Verify citations are a LIST, not a string (auto-deserialized)
    assert isinstance(verdict['pinneo_citations'], list)
    assert len(verdict['pinneo_citations']) == 2
    assert verdict['pinneo_citations'][0]['source'] == "Pinneo 1"
    assert verdict['pinneo_citations'][1]['heading'] == "R-1"
