import pytest

from src.configs.mongo_config import Mongo, mongo
from src.configs.testing_config import TestingConfig


class TestMongo:
    def test_initial_client_is_none(self) -> None:
        m: Mongo = Mongo()
        assert m.client is None

    def test_initial_db_is_none(self) -> None:
        m: Mongo = Mongo()
        assert m.db is None

    def test_disconnect_when_no_client_does_not_raise(self) -> None:
        m: Mongo = Mongo()
        m.disconnect()

    def test_module_level_mongo_is_mongo_instance(self) -> None:
        assert isinstance(mongo, Mongo)

    @pytest.mark.integration
    def test_connect_sets_client(self, docker_db: None) -> None:
        m: Mongo = Mongo()
        config: TestingConfig = TestingConfig()
        m.connect(config)
        assert m.client is not None
        m.disconnect()

    @pytest.mark.integration
    def test_connect_sets_db(self, docker_db: None) -> None:
        m: Mongo = Mongo()
        config: TestingConfig = TestingConfig()
        m.connect(config)
        assert m.db is not None
        m.disconnect()

    @pytest.mark.integration
    def test_connect_db_name_matches_config(self, docker_db: None) -> None:
        m: Mongo = Mongo()
        config: TestingConfig = TestingConfig()
        m.connect(config)
        assert m.db.name == config.MONGO_DB_NAME
        m.disconnect()

    @pytest.mark.integration
    def test_disconnect_after_connect_does_not_raise(self, docker_db: None) -> None:
        m: Mongo = Mongo()
        config: TestingConfig = TestingConfig()
        m.connect(config)
        m.disconnect()
