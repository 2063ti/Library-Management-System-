

from tortoise import Tortoise
import os

# DB_URL = os.getenv("DB_URL", "sqlite://library.db")

TORTOISE_ORM = {
    "connections": {"default": "sqlite://library.db"},  # or your DB URL
    "apps": {
        "models": {
            "models": ["app.models.models", "aerich.models"],  # include your models + aerich
            "default_connection": "default",
        },
    },
}

async def init_db():
    await Tortoise.init(
        db_url = os.getenv("DB_URL", "sqlite://library.db"),
        modules={"models": ["app.models.models","aerich.models"]}
    )
