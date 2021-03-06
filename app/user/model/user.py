from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime
from app.core.models.base import AlchemyBase, Base
from app.core.helpers.time import Time
from app.post.model.post import Post


class User(Base, AlchemyBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    email = Column(String(200))
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
    posts = relationship(Post)

    def __init__(self, id=None, first_name='', last_name='', email='', created_at='', updated_at=''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = Time().now() if created_at == '' else created_at
        self.updated_at = Time().now() if updated_at == '' else updated_at
        super().__init__()

    def __repr__(self):
        return "{}".format({
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'posts': self.posts,
        })

