from logger import CustomLogger
from model import Film, Player
from database import Database
from typing import Optional
from fastapi import FastAPI

import uvicorn
import logging

# create a logging session, a local DB session and a FastAPI session
logger = CustomLogger("api_logger", "logs/api.log")
db_session = Database("mongodb://localhost:27017", timeout=5)
app = FastAPI(debug=False)

@app.get("/")
async def root():
    return "Error 404: Route not found"

@app.get("/player/random", response_model=Player)
async def get_random_player():
    player = await db_session.get_random_player()

    if player:
        return player
    else:
        logger.warning("Database Random Player error")
        return None

@app.get("/film/random", response_model=Film)
async def get_random_film():
    film = await db_session.get_random_film()

    if film:
        return film
    else:
        logger.warning("Database Random Film error")
        return None

@app.get("/player", response_model=Player)
async def get_player(name: Optional[str] = None):
    if name:
        player = await db_session.get_player(name)
        if player:
            return player
        else:
            logger.warning("Database Player error")
            return None
    else:
        logger.error("Request Player error: didn't receive a player name")
        return None

@app.get("/film", response_model=Film)
async def get_film(title: Optional[str] = None):
    if title:
        film = await db_session.get_film(title)
        if film:
            return film
        else:
            logger.warning("Database Film error")
            return None
    else:
        logger.error("Request Film error: didn't receive a film name")
        return None


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        log_level="info",
        reload=True
    )