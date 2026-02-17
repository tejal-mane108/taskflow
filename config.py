import os

class Config:
    if os.environ.get("DATABASE_URL"):
        # Production (Render PostgreSQL)
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    else:
        # Local Development (SQLite)
        SQLALCHEMY_DATABASE_URI = "sqlite:///tasks.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False