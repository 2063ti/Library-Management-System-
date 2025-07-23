# TORTOISE_ORM = {
#     "connections": {
#         "default": 'postgresql://neondb_owner:npg_3cMKgkzbvs0T@ep-wild-feather-a1mf903w-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require',
#     },
#     "apps": {
#         "models": {
#             "models": ["app.models"],  # Where your Tortoise models are
#             "default_connection": "default",
#         }
#     }
# }


from tortoise import Tortoise
import os
async def init_db():
    await Tortoise.init(
        db_url = os.getenv("DB_URL", "sqlite://library.db"),
        modules={"models": ["app.models.models"]}
    )
    await Tortoise.generate_schemas()
