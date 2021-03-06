from flask import current_app

from sqlalchemy import create_engine
from sqlalchemy.exc import DisconnectionError
from sqlalchemy.orm import scoped_session, sessionmaker

from app.config import SQLALCHEMY_DATABASE_URI


def checkout_listener(dbapi_con, con_record, con_proxy):
    try:
        try:
            dbapi_con.ping(False)
        except TypeError:
            dbapi_con.ping()
    except dbapi_con.OperationalError as exc:
        if exc.args[0] in (2006, 2013, 2014, 2045, 2055):
            raise DisconnectionError()
        else:
            raise


def get_db():
    if not hasattr(current_app, 'db'):
        engine = create_engine(SQLALCHEMY_DATABASE_URI,
            pool_size=5,
            pool_timeout=60,
            pool_recycle=3500,
            echo=False
        )
        db_session = scoped_session(sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine))

        current_app.db = db_session
    return current_app.db
