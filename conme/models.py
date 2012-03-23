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
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    verify_code = Column(Unicode(20))

    _password = Column(Unicode(255))

    def __init__(self, name, password, email, is_active, is_admin,
                                                         verify_code=None):
        self.id = str(uuid.uuid1())
        self.name = name
        self.password = password
        self.email = email
        self.is_active = is_active
        self.is_admin = is_admin
        self.verify_code = verify_code