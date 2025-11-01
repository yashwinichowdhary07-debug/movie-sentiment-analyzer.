from app.routes import app

def test_predict_api():
    client = app.test_client()
    resp = client.post('/api/predict', json={'text': 'I loved this movie'})
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'label' in data and 'score' in data
