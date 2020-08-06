from typing import Optional
from pydantic import BaseModel

class Player(BaseModel):
    name: str
    birth_year: Optional[int] = None
    death_year: Optional[int] = None

class Film(BaseModel):
    title: str
    start_year: Optional[int] = None
    end_year: Optional[int] = None
    genres: Optional[str] = None

def as_player(_dict):
    return Player(
        name=_dict.get("primaryName", ""),
        birth_year=_dict.get("birthYear", None),
        death_year=_dict.get("deathYear", None)
    )

def as_film(_dict):
    return Film(
        title=_dict.get("primaryTitle", ""),
        start_year=_dict.get("startYear", None),
        end_year=_dict.get("endYear", None),
        genres=_dict.get("genres", None)
    )