from pymongo import MongoClient
from pymongo.database import Database

from src.configs.default_config import DefaultConfig


class Mongo:
    def __init__(self):
        self.client: MongoClient | None = None
        self.db: Database | None = None

    def connect(self, config: DefaultConfig) -> None:
        mongo_uri = config.MONGO_URI
        db_name = config.MONGO_DB_NAME

        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]

    def disconnect(self) -> None:
        if self.client:
            self.client.close()


mongo = Mongo()
