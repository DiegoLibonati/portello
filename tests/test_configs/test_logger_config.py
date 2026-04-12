import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger_instance(self) -> None:
        logger: logging.Logger = setup_logger()
        assert isinstance(logger, logging.Logger)

    def test_default_name(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.name == "tkinter-app"

    def test_custom_name(self) -> None:
        logger: logging.Logger = setup_logger("custom-logger-test")
        assert logger.name == "custom-logger-test"

    def test_has_at_least_one_handler(self) -> None:
        logger: logging.Logger = setup_logger("handler-check-logger")
        assert len(logger.handlers) > 0

    def test_same_name_returns_same_instance(self) -> None:
        logger1: logging.Logger = setup_logger("shared-logger-test")
        logger2: logging.Logger = setup_logger("shared-logger-test")
        assert logger1 is logger2

    def test_handlers_not_duplicated_on_repeated_call(self) -> None:
        logger: logging.Logger = setup_logger("no-dup-logger-test")
        count_before: int = len(logger.handlers)
        setup_logger("no-dup-logger-test")
        assert len(logger.handlers) == count_before

    def test_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger("level-check-logger-test")
        assert logger.level == logging.DEBUG

    def test_handler_is_stream_handler(self) -> None:
        logger: logging.Logger = setup_logger("stream-handler-check-test")
        stream_handlers: list[logging.Handler] = [h for h in logger.handlers if isinstance(h, logging.StreamHandler)]
        assert len(stream_handlers) > 0
