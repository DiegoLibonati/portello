import os
from unittest.mock import patch

from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    def test_debug_is_false(self) -> None:
        assert DefaultConfig().DEBUG is False

    def test_testing_is_false(self) -> None:
        assert DefaultConfig().TESTING is False

    def test_tz_default_value(self) -> None:
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("TZ", None)
            assert DefaultConfig().TZ == "America/Argentina/Buenos_Aires"

    def test_tz_from_env(self) -> None:
        with patch.dict(os.environ, {"TZ": "UTC"}):
            assert DefaultConfig().TZ == "UTC"

    def test_tz_is_string(self) -> None:
        assert isinstance(DefaultConfig().TZ, str)

    def test_debug_is_bool(self) -> None:
        assert isinstance(DefaultConfig().DEBUG, bool)

    def test_testing_is_bool(self) -> None:
        assert isinstance(DefaultConfig().TESTING, bool)

    def test_mongo_host_default(self) -> None:
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("MONGO_HOST", None)
            assert DefaultConfig().MONGO_HOST == "host.docker.internal"

    def test_mongo_host_from_env(self) -> None:
        with patch.dict(os.environ, {"MONGO_HOST": "myhost"}):
            assert DefaultConfig().MONGO_HOST == "myhost"

    def test_mongo_db_name_default(self) -> None:
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("MONGO_DB_NAME", None)
            assert DefaultConfig().MONGO_DB_NAME == "templates_db"

    def test_mongo_db_name_from_env(self) -> None:
        with patch.dict(os.environ, {"MONGO_DB_NAME": "my_db"}):
            assert DefaultConfig().MONGO_DB_NAME == "my_db"

    def test_mongo_uri_contains_host(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.MONGO_HOST in config.MONGO_URI

    def test_mongo_uri_contains_db_name(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.MONGO_DB_NAME in config.MONGO_URI

    def test_mongo_uri_is_string(self) -> None:
        assert isinstance(DefaultConfig().MONGO_URI, str)

    def test_json_as_ascii_is_false(self) -> None:
        assert DefaultConfig().JSON_AS_ASCII is False
