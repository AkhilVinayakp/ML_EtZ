# test file
from fastapi.testclient import TestClient
from app import app
from mongo import getMongo

client = TestClient(app=app)


# test for mongo collection
def test_mongoConnection_status():
    """Test able to connect to the application.
    """
    try:
        db = await getMongo()

    except Exception:
        pass
