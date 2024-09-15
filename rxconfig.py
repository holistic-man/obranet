import reflex as rx
import dotenv
import os

dotenv.load_dotenv(),

DATABASE_URL = os.environ.get("DATABASE_URL")


config = rx.Config(
    app_name="obranet",
    db_url=DATABASE_URL,
    cors_allowed_origins=[
        "https://obranet.vercel.app",
        "http://localhost:3000",
        "http://localhost:3001"
    ]
)