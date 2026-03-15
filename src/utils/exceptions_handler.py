from collections.abc import Callable
from functools import wraps
from typing import TypeVar

from pydantic import ValidationError
from pymongo.errors import PyMongoError
from typing_extensions import ParamSpec

from src.configs.logger_config import setup_logger
from src.constants.messages import MESSAGE_ERROR_DATABASE, MESSAGE_ERROR_PYDANTIC
from src.utils.dialogs import InternalDialogError, ValidationDialogError

logger = setup_logger(__name__)

P = ParamSpec("P")
R = TypeVar("R")


def exceptions_handler(fn: Callable[P, R]) -> Callable[P, R]:
    @wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return fn(*args, **kwargs)

        except ValidationError as _e:
            # logger.error("Validation error: %s", e)
            raise ValidationDialogError(message=MESSAGE_ERROR_PYDANTIC)

        except PyMongoError:
            raise InternalDialogError(
                message=MESSAGE_ERROR_DATABASE,
            )

    return wrapper
