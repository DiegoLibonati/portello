import os

from src.configs.default_config import DefaultConfig


class TestingConfig(DefaultConfig):
    def __init__(self) -> None:
        super().__init__()
        self.TESTING = True
        self.DEBUG = True
        self.ENV = "testing"

        self.MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "templates_db")
        self.MONGO_URI = os.getenv(
            "MONGO_URI",
            f"mongodb://admin:secret123@host.docker.internal:27017/{self.MONGO_DB_NAME}?authSource=admin",
        )
