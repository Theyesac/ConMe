import uuid

from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Text,
    Unicode,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class User(Base):
    """User model"""
    __tablename__ = 'users'
    id = Column(String(32), primary_key=True, unique=True)
    name = Column(Unicode(255), unique=True)
    email = Column(Unicode(255), unique=True)

    def __init__(self, name, email):
        self.id = str(uuid.uuid1())
        self.name = name
        self.email = email