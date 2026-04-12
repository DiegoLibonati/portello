import pytest

from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    def test_debug_is_false(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.DEBUG is False

    def test_testing_is_false(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.TESTING is False

    def test_json_as_ascii_is_false(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.JSON_AS_ASCII is False

    def test_mongo_uri_starts_with_mongodb_scheme(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.MONGO_URI.startswith("mongodb://")

    def test_mongo_uri_contains_auth_source(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert "authSource=" in config.MONGO_URI

    def test_mongo_uri_includes_db_name(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.MONGO_DB_NAME in config.MONGO_URI

    def test_mongo_uri_includes_user(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.MONGO_USER in config.MONGO_URI

    def test_mongo_uri_includes_host(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.MONGO_HOST in config.MONGO_URI

    def test_mongo_host_override_via_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("MONGO_HOST", "my-custom-host")
        config: DefaultConfig = DefaultConfig()
        assert config.MONGO_HOST == "my-custom-host"
        assert "my-custom-host" in config.MONGO_URI

    def test_mongo_user_override_via_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("MONGO_USER", "custom-user")
        config: DefaultConfig = DefaultConfig()
        assert config.MONGO_USER == "custom-user"

    def test_tz_default_when_not_set(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("TZ", raising=False)
        config: DefaultConfig = DefaultConfig()
        assert config.TZ == "America/Argentina/Buenos_Aires"

    def test_tz_override_via_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("TZ", "UTC")
        config: DefaultConfig = DefaultConfig()
        assert config.TZ == "UTC"

    def test_mongo_db_name_override_via_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("MONGO_DB_NAME", "custom_db")
        config: DefaultConfig = DefaultConfig()
        assert config.MONGO_DB_NAME == "custom_db"
        assert "custom_db" in config.MONGO_URI
