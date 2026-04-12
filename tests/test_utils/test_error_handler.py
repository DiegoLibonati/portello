from unittest.mock import MagicMock, patch

from src.utils.dialogs import InternalDialogError, ValidationDialogError
from src.utils.error_handler import error_handler


class TestErrorHandler:
    def test_base_dialog_exception_calls_open(self) -> None:
        dialog: ValidationDialogError = ValidationDialogError(message="test")
        with patch.object(dialog, "open") as mock_open:
            error_handler(type(dialog), dialog, None)
        mock_open.assert_called_once()

    def test_internal_dialog_error_calls_open(self) -> None:
        dialog: InternalDialogError = InternalDialogError(message="internal")
        with patch.object(dialog, "open") as mock_open:
            error_handler(type(dialog), dialog, None)
        mock_open.assert_called_once()

    def test_non_dialog_exception_creates_internal_error(self) -> None:
        exc: ValueError = ValueError("unexpected failure")
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(type(exc), exc, None)
        mock_internal.assert_called_once_with(message=str(exc))

    def test_non_dialog_exception_opens_internal_error(self) -> None:
        exc: RuntimeError = RuntimeError("runtime failure")
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(type(exc), exc, None)
        mock_instance.open.assert_called_once()

    def test_non_dialog_exception_message_is_str_of_exception(self) -> None:
        exc: TypeError = TypeError("type mismatch")
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(type(exc), exc, None)
        mock_internal.assert_called_once_with(message="type mismatch")
