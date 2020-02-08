from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import AlchemyBase
from app.core.database.connection import Connection

class User(Connection, AlchemyBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    fullname = Column(String(200))
    nickname = Column(String(200))
    posts = relationship('Post')

    def __init__(self, id = None, name = '', fullname = '', nickname = ''):
        self.id = id
        self.name = name
        self.fullname = fullname
        self.nickname = nickname
        super().__init__()

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname
        )

    def create(self):
        self.session.add(self)
        self.session.commit()
        return self

    def migrate(self):
        self.metadata.create_all(self.engine)

    def drop(self):
        self.metadata.drop_all(self.engine)

