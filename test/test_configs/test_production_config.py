from src.configs.default_config import DefaultConfig
from src.configs.development_config import DevelopmentConfig
from src.configs.production_config import ProductionConfig


class TestProductionConfig:
    def test_inherits_from_default_config(self) -> None:
        assert isinstance(ProductionConfig(), DefaultConfig)

    def test_debug_is_false(self) -> None:
        assert ProductionConfig().DEBUG is False

    def test_debug_is_bool(self) -> None:
        assert isinstance(ProductionConfig().DEBUG, bool)

    def test_env_is_production(self) -> None:
        assert ProductionConfig().ENV == "production"

    def test_env_is_string(self) -> None:
        assert isinstance(ProductionConfig().ENV, str)

    def test_env_differs_from_development(self) -> None:
        assert ProductionConfig().ENV != DevelopmentConfig().ENV
