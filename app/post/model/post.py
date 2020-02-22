from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.core.helpers.time import Time
from app.core.models.base import AlchemyBase, Base


class Post(Base, AlchemyBase):
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
        self.created_at = created_at if created_at != '' else Time().now()
        self.updated_at = updated_at if updated_at != '' else Time().now()
        super().__init__()

    def __repr__(self):
        return "{}".format({
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M"),
            'updated_at': self.updated_at.strftime("%Y-%m-%d %H:%M"),
        })