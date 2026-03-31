from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#where the database is located
DATABASE_URL = "sqlite:///./app.db"

#engine is SQLAlchemy's connection layer to database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
#session is what app uses to talk to database, create rows, query rows, update rows, delete rows
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
