import reflex as rx

config = rx.Config(
    app_name="obranet",
    cors_allowed_origins=[
        "https://obranet.vercel.app",
        "http://localhost:3000"
    ]
)