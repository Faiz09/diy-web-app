from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.core.models.base import AlchemyBase
from app.core.database.connection import Connection


class Post(Connection, AlchemyBase):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    body = Column(Text())
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, id = None, title = '', body = '', created_at = '', updated_at = ''):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at
        super().__init__()

    def __repr__(self):
        return "<Post(title='%s', body='%s', created_at='%s')>" % (
            self.title, self.body, self.created_at
        )

    def create(self):
        self.session.add(self)
        self.session.commit()