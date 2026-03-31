from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.session import SessionLocal

#get_db gives each request a database session and makes sure it closes after
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() #close db after request is done, even if there was an error
