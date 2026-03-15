import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger_instance(self) -> None:
        assert isinstance(setup_logger("test"), logging.Logger)

    def test_logger_has_correct_name(self) -> None:
        assert setup_logger("my-logger").name == "my-logger"

    def test_logger_default_name(self) -> None:
        assert setup_logger().name == "tkinter-app"

    def test_logger_level_is_debug(self) -> None:
        assert setup_logger("level-test").level == logging.DEBUG

    def test_logger_has_handlers(self) -> None:
        assert len(setup_logger("handler-test").handlers) > 0

    def test_logger_handler_is_stream_handler(self) -> None:
        logger: logging.Logger = setup_logger("stream-test")
        assert isinstance(logger.handlers[0], logging.StreamHandler)

    def test_calling_twice_does_not_duplicate_handlers(self) -> None:
        setup_logger("duplicate-test")
        logger: logging.Logger = setup_logger("duplicate-test")
        assert len(logger.handlers) == 1
