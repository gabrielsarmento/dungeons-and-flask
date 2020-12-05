from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from settings import base

Base = declarative_base()


def get_engine():
    return create_engine(
        base.DATABASE['connection_creation'].format(**base.DATABASE)
    )


def get_db_session():
    engine = get_engine()
    return scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=True,
            expire_on_commit=False
        )
    )
