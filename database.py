from motor.motor_asyncio import AsyncIOMotorClient
from model import as_film, as_player
from logger import CustomLogger
from typing import Optional

class Database:
    def __init__(self, uri: str = "mongodb://localhost:27017", timeout: int = 5):
        self.logger = CustomLogger("db_logger", "logs/db.log")

        conn = AsyncIOMotorClient(uri, socketTimeoutMS=timeout * 1000)
        self.crew_coll = conn.get_database("imdb").get_collection("crew")
        self.film_coll = conn.get_database("imdb").get_collection("films")

    async def get_random_film(self):
        step = { "$sample": { "size": 1 } }
        cursor = self.film_coll.aggregate([step])
        result = await cursor.to_list(length=1)

        if result:
            return as_film(result[0])
        else:
            self.logger.error("Couldn't get a random film")
            return None

    async def get_random_player(self):
        step = { "$sample": { "size": 1 } }
        cursor = self.crew_coll.aggregate([step])
        result = await cursor.to_list(length=1)

        if result:
            return as_player(result[0])
        else:
            self.logger.error("Couldn't get a random player")
            return None

    async def get_player(self, name: str):
        _filter = { "primaryName": { "$regex": name, "$options": "i" } }
        result = await self.crew_coll.find_one(_filter)

        if result:
            return as_player(result)
        else:
            self.logger.error(f"Couldn't get a player by name {name}")
            return None

    async def get_film(self, title: str):
        _filter = { "primaryTitle": { "$regex": title, "$options": "i" } }
        result = await self.film_coll.find_one(_filter)

        if result:
            return as_film(result)
        else:
            self.logger.error(f"Couldn't get a film by title {title}")
            return None