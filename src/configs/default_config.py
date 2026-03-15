import os


class DefaultConfig:
    def __init__(self) -> None:
        # General
        self.TZ = os.getenv("TZ", "America/Argentina/Buenos_Aires")
        self.DEBUG = False
        self.TESTING = False

        # Mongo
        self.MONGO_HOST = os.getenv("MONGO_HOST", "host.docker.internal")
        self.MONGO_PORT = os.getenv("MONGO_PORT", 27017)
        self.MONGO_USER = os.getenv("MONGO_USER", "admin")
        self.MONGO_PASS = os.getenv("MONGO_PASS", "secret123")
        self.MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "templates_db")
        self.MONGO_AUTH_SOURCE = os.getenv("MONGO_AUTH_SOURCE", "admin")
        self.MONGO_URI = (
            f"mongodb://{self.MONGO_USER}:{self.MONGO_PASS}@{self.MONGO_HOST}:{self.MONGO_PORT}/{self.MONGO_DB_NAME}?authSource={self.MONGO_AUTH_SOURCE}"
        )
        self.JSON_AS_ASCII = False
