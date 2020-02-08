from sqlalchemy import Column, Integer, String, Text, DateTime
from models.base import AlchemyBase
from database.connection import Connection


class Post(AlchemyBase, Connection):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(500))
    body = Column(Text)
    created_at = Column(DateTime)

    def __repr__(self):
        return "<Post(title='%s', body='%s', created_at='%s')>" % (
            self.title, self.body, self.created_at
        )