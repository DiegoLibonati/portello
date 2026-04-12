import pytest
from pymongo.errors import PyMongoError

from src.models.user_model import UserModel
from src.utils.dialogs import InternalDialogError, ValidationDialogError
from src.utils.exceptions_handler import exceptions_handler


class TestExceptionsHandler:
    def test_passthrough_on_success(self) -> None:
        @exceptions_handler
        def fn() -> str:
            return "ok"

        result: str = fn()
        assert result == "ok"

    def test_passes_arguments_to_wrapped_function(self) -> None:
        @exceptions_handler
        def fn(a: int, b: int) -> int:
            return a + b

        result: int = fn(2, 3)
        assert result == 5

    def test_catches_pydantic_validation_error_raises_validation_dialog(self) -> None:
        @exceptions_handler
        def fn() -> None:
            UserModel(username="", password="")

        with pytest.raises(ValidationDialogError):
            fn()

    def test_catches_pymongo_error_raises_internal_dialog(self) -> None:
        @exceptions_handler
        def fn() -> None:
            raise PyMongoError("connection failed")

        with pytest.raises(InternalDialogError):
            fn()

    def test_dialog_errors_propagate_unchanged(self) -> None:
        @exceptions_handler
        def fn() -> None:
            raise ValidationDialogError(message="from dialog")

        with pytest.raises(ValidationDialogError) as exc_info:
            fn()
        assert exc_info.value.message == "from dialog"

    def test_internal_dialog_error_propagates_unchanged(self) -> None:
        @exceptions_handler
        def fn() -> None:
            raise InternalDialogError(message="internal msg")

        with pytest.raises(InternalDialogError) as exc_info:
            fn()
        assert exc_info.value.message == "internal msg"

    def test_preserves_function_name(self) -> None:
        @exceptions_handler
        def my_named_function() -> None:
            pass

        assert my_named_function.__name__ == "my_named_function"

    def test_preserves_function_return_value_none(self) -> None:
        @exceptions_handler
        def fn() -> None:
            return None

        result = fn()
        assert result is None
