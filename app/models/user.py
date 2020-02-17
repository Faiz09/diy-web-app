from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime
from app.models.base import AlchemyBase
from app.core.database.connection import Connection
from app.core.helpers.time import Time

class User(Connection, AlchemyBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    email = Column(String(200))
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
    posts = relationship('Post')

    def __init__(self, id=None, first_name='', last_name='', email='', created_at = '', updated_at = ''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        if created_at == '':
            self.created_at = Time().now()
        else:
            self.created_at = created_at

        if updated_at == '':
            self.updated_at = Time().now()
        else:
            self.updated_at = created_at

        super().__init__()

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', email='%s')>" % (
            self.first_name, self.last_name, self.email
        )

    def create(self):
        self.session.add(self)
        self.session.commit()
        return self


