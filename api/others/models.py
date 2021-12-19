import sys
sys.path.append("..")

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import backref, relationship
from db import Base 


user_item = Table(
    'association_user_item', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('item_id', Integer, ForeignKey('items.id'))
)

class User(Base):
    
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", secondary = user_item, backref = backref("users", lazy="dynamic"))



class Item(Base):

    __tablename__ = "items"


    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    # owner_id = Column(Integer, ForeignKey("users.id"))

    # owners = relationship("Association", back_populates="items", cascade="all, delete")







# class Association(Base):
#     __tablename__ = "association"

#     user_id = Column(ForeignKey('users.id'), primary_key=True)
#     item_id = Column(ForeignKey('items.id'), primary_key=True)

#     items = relationship("Item", back_populates="owners")
#     users = relationship("User", back_populates="items")



# class User(Base):

#     __tablename__ = "users"


#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Association", back_populates="users", cascade="all, delete")



# class Item(Base):

#     __tablename__ = "items"


#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     # owner_id = Column(Integer, ForeignKey("users.id"))

#     owners = relationship("Association", back_populates="items", cascade="all, delete")
