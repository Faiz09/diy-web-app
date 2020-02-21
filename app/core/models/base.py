from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from config.config import CONFIG
from sqlalchemy.orm import sessionmaker

AlchemyBase = declarative_base()


class Base:
    session = None
    engine = None
    rows = None

    def __init__(self):
        self.engine = self.connect()
        self.session = sessionmaker(bind=self.engine)()
        super().__init__()

    def connect(self):
        db_config = CONFIG['database']
        url = "mysql://{}:{}@{}/{}".format(db_config['user'], db_config['password'], db_config['host'], db_config['database'])
        return create_engine(url, echo=False)

    def all(self):
        self.rows = self.session.query(self.__class__).all()
        return self

    def get(self):
        return self.rows

    def to_json(self):
        items = []
        for item in self.rows:
            items.append(item.json_rep())

        return items

    def create(self):
        self.session.add(self)
        self.session.commit()
        return self

    def where(self, field, value):
        return self.session.query(self.__class__).filter(field == value)

    def update(self, field, value, data):
        self.session.query(self.__class__).filter(field == value).update(data)
        self.session.commit()
        return self.session.query(self.__class__).filter(field == value).first()

    def find(self, id):
        return self.session.query(self.__class__).get(id)

    def delete(self, id):
        self.session.query(self.__class__).filter_by(id=id).delete()
        self.session.commit()
        return 1
