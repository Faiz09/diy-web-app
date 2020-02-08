from sqlalchemy import create_engine
from config.config import Config

class Connection:
    def engine(self):

        db_config = Config().database()
        url = "mysql://{}:{}@{}/{}".format(db_config['user'], db_config['password'], db_config['host'], db_config['database'])
        return create_engine(url, echo=False)