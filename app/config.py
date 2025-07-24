

from tortoise import Tortoise
import os
async def init_db():
    await Tortoise.init(
        db_url = os.getenv("DB_URL", "sqlite://library.db"),
        modules={"models": ["app.models.models"]}
    )
    await Tortoise.generate_schemas()
