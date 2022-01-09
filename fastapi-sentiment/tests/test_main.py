from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_positive_sentiment():
    response = client.post("/sentiment?sentence=Beatuiful bright and sunny day")
    assert response.status_code == 200
    assert response.json() == {"sentiment": "positive"}

def test_negative_sentiment():
    response = client.post("/sentiment?sentence=Worst moment in my life")
    assert response.status_code == 200
    assert response.json() == {"sentiment": "negative"}

def test_neutral_sentiment():
    response = client.post("/sentiment?sentence=There is a book on the desk")
    assert response.status_code == 200
    assert response.json() == {"sentiment": "neutral"}