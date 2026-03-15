import os
from unittest.mock import patch

from src.configs.default_config import DefaultConfig
from src.configs.production_config import ProductionConfig
from src.configs.testing_config import TestingConfig


class TestTestingConfig:
    def test_inherits_from_default_config(self) -> None:
        assert isinstance(TestingConfig(), DefaultConfig)

    def test_testing_is_true(self) -> None:
        assert TestingConfig().TESTING is True

    def test_debug_is_true(self) -> None:
        assert TestingConfig().DEBUG is True

    def test_env_is_testing(self) -> None:
        assert TestingConfig().ENV == "testing"

    def test_mongo_db_name_from_env(self) -> None:
        with patch.dict(os.environ, {"MONGO_DB_NAME": "custom_test_db"}):
            assert TestingConfig().MONGO_DB_NAME == "custom_test_db"

    def test_mongo_uri_from_env(self) -> None:
        with patch.dict(os.environ, {"MONGO_URI": "mongodb://custom_uri"}):
            assert TestingConfig().MONGO_URI == "mongodb://custom_uri"

    def test_env_differs_from_production(self) -> None:
        assert TestingConfig().ENV != ProductionConfig().ENV
