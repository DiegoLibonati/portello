from unittest.mock import MagicMock, patch

from src.configs.default_config import DefaultConfig
from src.configs.mongo_config import Mongo, mongo


class TestMongoInit:
    def test_client_initial_value_is_none(self) -> None:
        m: Mongo = Mongo()
        assert m.client is None

    def test_db_initial_value_is_none(self) -> None:
        m: Mongo = Mongo()
        assert m.db is None


class TestMongoConnect:
    def test_client_is_set_after_connect(self) -> None:
        m: Mongo = Mongo()
        config: DefaultConfig = DefaultConfig()
        with patch("src.configs.mongo_config.MongoClient") as mock_client_class:
            mock_client_class.return_value = MagicMock()
            m.connect(config=config)
        assert m.client is not None

    def test_db_is_set_after_connect(self) -> None:
        m: Mongo = Mongo()
        config: DefaultConfig = DefaultConfig()
        with patch("src.configs.mongo_config.MongoClient") as mock_client_class:
            mock_client: MagicMock = MagicMock()
            mock_client_class.return_value = mock_client
            m.connect(config=config)
        assert m.db is not None

    def test_mongo_client_called_with_uri(self) -> None:
        m: Mongo = Mongo()
        config: DefaultConfig = DefaultConfig()
        with patch("src.configs.mongo_config.MongoClient") as mock_client_class:
            mock_client_class.return_value = MagicMock()
            m.connect(config=config)
        mock_client_class.assert_called_once_with(config.MONGO_URI)

    def test_db_uses_correct_db_name(self) -> None:
        m: Mongo = Mongo()
        config: DefaultConfig = DefaultConfig()
        with patch("src.configs.mongo_config.MongoClient") as mock_client_class:
            mock_client: MagicMock = MagicMock()
            mock_client_class.return_value = mock_client
            m.connect(config=config)
        mock_client.__getitem__.assert_called_once_with(config.MONGO_DB_NAME)


class TestMongoDisconnect:
    def test_client_close_called_when_client_is_set(self) -> None:
        m: Mongo = Mongo()
        mock_client: MagicMock = MagicMock()
        m.client = mock_client
        m.disconnect()
        mock_client.close.assert_called_once()

    def test_disconnect_does_nothing_when_client_is_none(self) -> None:
        m: Mongo = Mongo()
        m.disconnect()

    def test_mongo_singleton_is_mongo_instance(self) -> None:
        assert isinstance(mongo, Mongo)

    def test_mongo_singleton_client_starts_none(self) -> None:
        fresh: Mongo = Mongo()
        assert fresh.client is None
