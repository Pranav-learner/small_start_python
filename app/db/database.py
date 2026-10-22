from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
HTTP request
     ↓
get_db()
     ↓
SessionLocal()
     ↓
database session
     ↓
endpoint/repository uses it
     ↓
finally
     ↓
db.close()

The yield is important.

It means:

"Give this session to whoever depends on me, then execute the cleanup code after that work finishes."
'''
