import os

from src.configs.default_config import DefaultConfig
from src.configs.testing_config import TestingConfig


class TestTestingConfig:
    def test_inherits_default_config(self) -> None:
        config: TestingConfig = TestingConfig()
        assert isinstance(config, DefaultConfig)

    def test_testing_is_true(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.TESTING is True

    def test_debug_is_true(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.DEBUG is True

    def test_env_is_testing(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.ENV == "testing"

    def test_mongo_db_name_from_env(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.MONGO_DB_NAME == os.environ.get("MONGO_DB_NAME")

    def test_mongo_uri_is_string(self) -> None:
        config: TestingConfig = TestingConfig()
        assert isinstance(config.MONGO_URI, str)

    def test_mongo_uri_starts_with_mongodb_scheme(self) -> None:
        config: TestingConfig = TestingConfig()
        assert config.MONGO_URI.startswith("mongodb://")

    def test_mongo_uri_contains_test_db(self) -> None:
        config: TestingConfig = TestingConfig()
        assert os.environ.get("MONGO_DB_NAME") in config.MONGO_URI
