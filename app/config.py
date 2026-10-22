import os
import warnings
from dotenv import load_dotenv

# Load variables from .env file if present
load_dotenv()

ENV: str = os.getenv("ENV", "development").lower()

# JWT Settings
JWT_SECRET_KEY: str | None = os.getenv("JWT_SECRET_KEY") or os.getenv("SECRET_KEY")

if not JWT_SECRET_KEY:
    if ENV == "production":
        raise RuntimeError("CRITICAL: JWT_SECRET_KEY environment variable is not set in production!")
    warnings.warn(
        "JWT_SECRET_KEY is not set. Using insecure default secret key for development.",
        UserWarning,
        stacklevel=2,
    )
    JWT_SECRET_KEY = "small-start-python"

JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# Database Settings
DB_USER: str = os.getenv("DB_USER") or os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD: str | None = os.getenv("DB_PASSWORD") or os.getenv("POSTGRES_PASSWORD")
DB_HOST: str = os.getenv("DB_HOST") or os.getenv("POSTGRES_HOST", "localhost")
DB_PORT: str = os.getenv("DB_PORT") or os.getenv("POSTGRES_PORT", "5432")
DB_NAME: str = os.getenv("DB_NAME") or os.getenv("POSTGRES_DB", "taskflow")

DATABASE_URL: str | None = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    if not DB_PASSWORD:
        if ENV == "production":
            raise RuntimeError("CRITICAL: DB_PASSWORD or DATABASE_URL environment variable is not set in production!")
        DB_PASSWORD = "postgres"

    DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
