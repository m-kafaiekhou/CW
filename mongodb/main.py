from functools import lru_cache
from fastapi import FastAPI

from config.settings import settings


app = FastAPI()


@lru_cache
def get_settings():
    return settings
