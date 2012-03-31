import cryptacular.bcrypt
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
from sqlalchemy.ext.hybrid import hybrid_property

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

bcrypt = cryptacular.bcrypt.BCRYPTPasswordManager()

class User(Base):
    """User model"""
    __tablename__ = 'users'
    id = Column(String(32), primary_key=True, unique=True)
    name = Column(Unicode(255), unique=True)
    email = Column(Unicode(255), unique=True)

    _password = Column(Unicode(255))

    def __init__(self, name, password, email):
        self.id = str(uuid.uuid1())
        self.password = password
        self.name = name
        self.email = email

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def set_password(self, value):
        hashed = bcrypt.encode(value)
        self._password = unicode(hashed)

    @classmethod
    def by_name(cls, name):
        return DBSession.query(cls).filter(cls.name == name).first()

    def check_password(self, password):
        return bcrypt.check(self.password, password)