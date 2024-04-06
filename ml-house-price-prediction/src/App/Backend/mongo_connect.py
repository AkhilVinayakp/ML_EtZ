# functions related to mongo
from motor.motor_asyncio import AsyncIOMotorClient
from utils.logger import logger


async def getMongo(db) -> AsyncIOMotorClient:
    """ Create a mongodb connection and return the client obj.
    """
    mongoClient = AsyncIOMotorClient(db.url)
    logger.info("Requesting MongoDB connection.")
    return mongoClient[db.database][db.collection_name]

