from app.database.base import *
from app.database.session import Base, engine


def create_database():
    Base.metadata.create_all(bind=engine)