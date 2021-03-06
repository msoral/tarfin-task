from database import Base, Session
from sqlalchemy import create_engine
from config import DatabaseConfig


class DatabaseService:

    def __init__(self, config: DatabaseConfig):
        self.db_url = f"{config.dialect}+{config.driver}://{config.user}:" \
                      f"{config.password}@{config.host}:{config.port}/{config.db}"

        self.engine = create_engine(self.db_url, echo=False)
        Session.configure(bind=self.engine)
        self.session = Session()

    def initialize_database(self):
        Base.metadata.create_all(bind=self.engine)

    def purge_database(self):
        Base.metadata.drop_all(bind=self.engine)
        print("Database has been purged.")
