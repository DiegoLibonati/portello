from src.configs.default_config import DefaultConfig
from src.configs.production_config import ProductionConfig


class TestProductionConfig:
    def test_inherits_default_config(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert isinstance(config, DefaultConfig)

    def test_debug_is_false(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert config.DEBUG is False

    def test_env_is_production(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert config.ENV == "production"

    def test_testing_is_false(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert config.TESTING is False

    def test_mongo_uri_is_string(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert isinstance(config.MONGO_URI, str)

    def test_mongo_uri_starts_with_mongodb_scheme(self) -> None:
        config: ProductionConfig = ProductionConfig()
        assert config.MONGO_URI.startswith("mongodb://")
