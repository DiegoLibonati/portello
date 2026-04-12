import os
import subprocess
import time
import tkinter as tk

import pymongo
import pytest
from pymongo.database import Database
from pymongo.mongo_client import MongoClient

from src.configs.mongo_config import mongo
from src.configs.testing_config import TestingConfig


@pytest.fixture(scope="session")
def root() -> tk.Tk:
    instance: tk.Tk = tk.Tk()
    instance.withdraw()
    yield instance
    instance.destroy()


@pytest.fixture(scope="session")
def docker_db() -> None:
    subprocess.run(
        ["docker", "compose", "-f", "test.docker-compose.yml", "up", "-d", "--wait"],
        check=True,
    )
    time.sleep(2)
    yield
    subprocess.run(
        ["docker", "compose", "-f", "test.docker-compose.yml", "down", "-v"],
        check=True,
    )


@pytest.fixture(scope="session")
def mongo_client(docker_db: None) -> MongoClient:
    client: MongoClient = pymongo.MongoClient(os.environ["MONGO_URI"])
    yield client
    client.close()


@pytest.fixture(scope="function")
def mongo_db(mongo_client: MongoClient) -> Database:
    db: Database = mongo_client[os.environ["MONGO_DB_NAME"]]
    yield db
    for name in db.list_collection_names():
        db.drop_collection(name)


@pytest.fixture(scope="function")
def connected_mongo(mongo_db: Database) -> Database:
    config: TestingConfig = TestingConfig()
    mongo.connect(config)
    yield mongo_db
    mongo.disconnect()
