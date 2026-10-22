import os
from dotenv import load_dotenv

# Load variables from .env file if present
load_dotenv()

# JWT Settings
JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY") or os.getenv("SECRET_KEY", "small-start-python")
JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM") or os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# Database Settings
DB_USER: str = os.getenv("DB_USER") or os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD: str = os.getenv("DB_PASSWORD") or os.getenv("POSTGRES_PASSWORD", "postgres")
DB_HOST: str = os.getenv("DB_HOST") or os.getenv("POSTGRES_HOST", "localhost")
DB_PORT: str = os.getenv("DB_PORT") or os.getenv("POSTGRES_PORT", "5432")
DB_NAME: str = os.getenv("DB_NAME") or os.getenv("POSTGRES_DB", "taskflow")

DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
