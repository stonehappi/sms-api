import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base

from core.setting import Settings

settings = Settings()
engine = sa.create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
