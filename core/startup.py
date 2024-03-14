from fastapi import FastAPI

from core.cors import add_cors
from core.database import Base, engine


def startup() -> FastAPI:
    app = FastAPI()
    add_cors(app)
    return app


def reset_factory():
    # Base.metadata.create_all(bind=engine)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
