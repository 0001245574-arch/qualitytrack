import os
os.environ["DATABASE_URL"]="sqlite:///./test_qualitytrack.db";os.environ["SECRET_KEY"]="test-secret-key"
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database.session import Base,engine
@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(bind=engine);Base.metadata.create_all(bind=engine);yield;Base.metadata.drop_all(bind=engine)
@pytest.fixture
def client(): return TestClient(app)
@pytest.fixture
def auth_headers(client):
    r=client.post("/api/auth/login",json={"username":"admin","password":"Quality@123"});return {"Authorization":f"Bearer {r.json()['access_token']}"}
@pytest.fixture
def sample_payload(): return {"title":"Solda fria no conector","product":"Placa CTRL-100","production_line":"Linha SMT-02","defect_type":"Solda fria","severity":"Alta","status":"Aberta","quantity":8,"description":"Inspeção visual identificou solda sem molhabilidade adequada.","containment_action":"Segregar lote e bloquear expedição.","responsible":"Ana Souza"}
