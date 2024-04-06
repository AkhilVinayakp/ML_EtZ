# sample application to handle
from fastapi import FastAPI
from hydra import compose, initialize
from mongo_connect import getMongo

# getting the config file
with initialize(config_path="config"):
    cfg = compose(config_name="api_conf")

app = FastAPI()


@app.get("/test")
async def test_app():
    """Testing purpose only
    """
    return {
        "message": "test ok",
        "code": 0
    }


@app.get("/test_db")
async def test_db():
    """Testing the connection to db"""
    collection = await getMongo(cfg.app.db)
    return await collection.find_one()  # Add proper connection obj.

