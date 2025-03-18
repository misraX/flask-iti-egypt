import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def get_session(db_url: str = os.getenv('SQLALCHEMY_DATABASE_URI')) -> Session:
    engine = create_engine(db_url)
    return Session(engine)
