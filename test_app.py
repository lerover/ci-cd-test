from app import app

def test_app():
    assert app(1, 2) == 3