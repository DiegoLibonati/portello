import os
import subprocess
import time
from collections.abc import Generator
from tkinter import StringVar
from unittest.mock import MagicMock

import pytest
from pymongo import MongoClient
from pymongo.database import Database
from werkzeug.security import generate_password_hash

TEST_MONGO_HOST = os.getenv("TEST_MONGO_HOST", "localhost")
TEST_MONGO_PORT = int(os.getenv("TEST_MONGO_PORT", "27018"))
TEST_MONGO_USER = os.getenv("TEST_MONGO_USER", "admin")
TEST_MONGO_PASS = os.getenv("TEST_MONGO_PASS", "secret123")
TEST_MONGO_DB = os.getenv("TEST_MONGO_DB", "test_db")
TEST_MONGO_URI = f"mongodb://{TEST_MONGO_USER}:{TEST_MONGO_PASS}@{TEST_MONGO_HOST}:{TEST_MONGO_PORT}/{TEST_MONGO_DB}?authSource=admin"


# ============================================================================
# Docker / MongoDB infrastructure fixtures
# ============================================================================


def is_mongo_ready(uri: str, timeout: int = 30) -> bool:
    start_time: float = time.time()
    while time.time() - start_time < timeout:
        try:
            client: MongoClient = MongoClient(uri, serverSelectionTimeoutMS=1000)
            client.admin.command("ping")
            client.close()
            return True
        except Exception:
            time.sleep(1)
    return False


def start_docker_compose() -> None:
    compose_file: str = os.path.join(os.path.dirname(__file__), "..", "test.docker-compose.yml")
    if not os.path.exists(compose_file):
        raise FileNotFoundError(f"The docker-compose file was not found: {compose_file}")
    subprocess.run(
        ["docker", "compose", "-f", compose_file, "up", "-d", "--wait"],
        check=True,
        capture_output=True,
    )


def stop_docker_compose() -> None:
    compose_file: str = os.path.join(os.path.dirname(__file__), "..", "test.docker-compose.yml")
    subprocess.run(
        ["docker", "compose", "-f", compose_file, "down", "-v"],
        check=False,
        capture_output=True,
    )


def clean_all_collections(db: Database) -> None:
    for collection_name in db.list_collection_names():
        db[collection_name].delete_many({})


@pytest.fixture(scope="session")
def docker_compose_up() -> Generator[None, None, None]:
    skip_docker: bool = os.getenv("SKIP_DOCKER_COMPOSE", "").lower() in ("true", "1", "yes")
    if not skip_docker:
        try:
            start_docker_compose()
        except subprocess.CalledProcessError:
            raise
    if not is_mongo_ready(TEST_MONGO_URI):
        raise RuntimeError("MongoDB is unavailable after the timeout.")
    yield
    if not skip_docker:
        stop_docker_compose()


@pytest.fixture(scope="session")
def mongo_client(docker_compose_up: None) -> Generator[MongoClient, None, None]:
    client: MongoClient = MongoClient(TEST_MONGO_URI)
    yield client
    client.close()


@pytest.fixture(scope="session")
def mongo_db(mongo_client: MongoClient) -> Database:
    return mongo_client[TEST_MONGO_DB]


@pytest.fixture(scope="function")
def clean_db(mongo_db: Database) -> Generator[Database, None, None]:
    clean_all_collections(mongo_db)
    yield mongo_db
    clean_all_collections(mongo_db)


# ============================================================================
# Model / test data fixtures
# ============================================================================


@pytest.fixture
def sample_user_data() -> dict[str, str]:
    return {"username": "testuser", "password": "testpass"}


@pytest.fixture
def valid_credentials() -> dict[str, str]:
    return {"username": "testuser", "password": "testpass"}


@pytest.fixture
def invalid_credentials() -> dict[str, str]:
    return {"username": "nonexistent", "password": "wrongpass"}


@pytest.fixture
def registration_data() -> dict[str, str]:
    return {
        "username": "newuser",
        "password": "newpass123",
        "confirm_password": "newpass123",
    }


@pytest.fixture(scope="function")
def inserted_user(mongo_db: Database, sample_user_data: dict[str, str]) -> Generator[dict[str, str], None, None]:
    user: dict[str, str] = {
        "username": sample_user_data["username"],
        "password": generate_password_hash(sample_user_data["password"]),
    }
    result = mongo_db.users.insert_one(user.copy())
    yield {**user, "_id": str(result.inserted_id)}
    mongo_db.users.delete_many({})


# ============================================================================
# UI fixtures
# ============================================================================


@pytest.fixture
def mock_root() -> MagicMock:
    root: MagicMock = MagicMock()
    root.title = MagicMock()
    root.geometry = MagicMock()
    root.resizable = MagicMock()
    root.config = MagicMock()
    return root


@pytest.fixture
def mock_styles() -> MagicMock:
    styles: MagicMock = MagicMock()
    styles.PRIMARY_COLOR = "#141B41"
    styles.SECONDARY_COLOR = "#306BAC"
    styles.WHITE_COLOR = "#FFFFFF"
    styles.FONT_ROBOTO_12 = "Roboto 12"
    styles.FONT_ROBOTO_13 = "Roboto 13"
    styles.FONT_ROBOTO_15 = "Roboto 15"
    return styles


@pytest.fixture
def on_register() -> MagicMock:
    return MagicMock()


@pytest.fixture
def variable() -> MagicMock:
    return MagicMock(spec=StringVar)
