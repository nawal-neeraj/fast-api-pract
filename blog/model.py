from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(20), index=True)
    body = Column(String(20), index=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blog")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), index=True)
    email = Column(String(20), index=True)
    password = Column(String(2000), index=True)

    blog = relationship("Blog", back_populates="creator")
