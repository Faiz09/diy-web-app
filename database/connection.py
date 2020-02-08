from sqlalchemy import create_engine
from config.config import Config
from sqlalchemy.orm import sessionmaker

class Connection:
    session = None
    engine = None

    def __init__(self):
        self.engine = self.connect()
        self.session = sessionmaker(bind=self.engine)()
        super().__init__()

    def connect(self):
        db_config = Config().database()
        url = "mysql://{}:{}@{}/{}".format(db_config['user'], db_config['password'], db_config['host'], db_config['database'])
        return create_engine(url, echo=True)