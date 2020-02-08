from sqlalchemy import Column, Integer, String
from models.base import AlchemyBase
from database.connection import Connection


class User(AlchemyBase, Connection):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    fullname = Column(String(200))
    nickname = Column(String(200))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname
        )

