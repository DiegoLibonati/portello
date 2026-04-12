from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP
from src.utils.dialogs import (
    AuthenticationDialogError,
    BaseDialog,
    BaseDialogError,
    BaseDialogNotification,
    BusinessDialogError,
    ConflictDialogError,
    DeprecatedDialogWarning,
    InternalDialogError,
    NotFoundDialogError,
    SuccessDialogInformation,
    ValidationDialogError,
)


class TestBaseDialog:
    def test_default_dialog_type_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.dialog_type == BaseDialog.ERROR

    def test_default_message(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.message == MESSAGE_ERROR_APP

    def test_custom_message_is_stored(self) -> None:
        dialog: BaseDialog = BaseDialog(message="Custom message")
        assert dialog.message == "Custom message"

    def test_title_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.title == "Error"

    def test_to_dict_contains_expected_keys(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, Any] = dialog.to_dict()
        assert "dialog_type" in result
        assert "title" in result
        assert "message" in result

    def test_to_dict_dialog_type_value(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, Any] = dialog.to_dict()
        assert result["dialog_type"] == BaseDialog.ERROR

    def test_to_dict_message_value(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test msg")
        result: dict[str, Any] = dialog.to_dict()
        assert result["message"] == "test msg"

    def test_open_error_calls_showerror(self) -> None:
        dialog: BaseDialog = BaseDialog(message="err")
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            dialog.open()
        mock_handler.assert_called_once_with("Error", "err")

    def test_open_info_calls_showinfo(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation(message="done")
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_handler}):
            dialog.open()
        mock_handler.assert_called_once_with("Information", "done")

    def test_open_warning_calls_showwarning(self) -> None:
        dialog: DeprecatedDialogWarning = DeprecatedDialogWarning(message="deprecated")
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_handler}):
            dialog.open()
        mock_handler.assert_called_once_with("Warning", "deprecated")

    def test_error_constant_value(self) -> None:
        assert BaseDialog.ERROR == "Error"

    def test_warning_constant_value(self) -> None:
        assert BaseDialog.WARNING == "Warning"

    def test_info_constant_value(self) -> None:
        assert BaseDialog.INFO == "Info"


class TestBaseDialogError:
    def test_is_exception(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert isinstance(error, Exception)

    def test_is_base_dialog(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert isinstance(error, BaseDialog)

    def test_dialog_type_is_error(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert error.dialog_type == BaseDialog.ERROR

    def test_can_be_raised_and_caught_as_exception(self) -> None:
        with pytest.raises(Exception):
            raise BaseDialogError()

    def test_can_be_raised_and_caught_as_base_dialog_error(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError(message="caught")


class TestDialogErrorSubclasses:
    def test_validation_dialog_error_is_base_dialog_error(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="invalid")
        assert isinstance(error, BaseDialogError)

    def test_validation_dialog_error_stores_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="invalid input")
        assert error.message == "invalid input"

    def test_authentication_dialog_error_is_base_dialog_error(self) -> None:
        assert isinstance(AuthenticationDialogError(), BaseDialogError)

    def test_not_found_dialog_error_stores_message(self) -> None:
        error: NotFoundDialogError = NotFoundDialogError(message="not found")
        assert error.message == "not found"

    def test_conflict_dialog_error_stores_message(self) -> None:
        error: ConflictDialogError = ConflictDialogError(message="conflict")
        assert error.message == "conflict"

    def test_business_dialog_error_is_base_dialog_error(self) -> None:
        assert isinstance(BusinessDialogError(), BaseDialogError)

    def test_internal_dialog_error_stores_message(self) -> None:
        error: InternalDialogError = InternalDialogError(message="internal")
        assert error.message == "internal"

    def test_validation_dialog_error_can_be_raised_and_caught(self) -> None:
        with pytest.raises(ValidationDialogError):
            raise ValidationDialogError(message="caught")

    def test_conflict_dialog_error_can_be_raised_and_caught(self) -> None:
        with pytest.raises(ConflictDialogError):
            raise ConflictDialogError(message="caught")


class TestDialogNotifications:
    def test_deprecated_dialog_warning_type(self) -> None:
        dialog: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert dialog.dialog_type == BaseDialog.WARNING

    def test_success_dialog_information_type(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation()
        assert dialog.dialog_type == BaseDialog.INFO

    def test_success_dialog_custom_message(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation(message="success")
        assert dialog.message == "success"

    def test_deprecated_dialog_is_base_dialog_notification(self) -> None:
        assert isinstance(DeprecatedDialogWarning(), BaseDialogNotification)

    def test_success_dialog_is_base_dialog_notification(self) -> None:
        assert isinstance(SuccessDialogInformation(), BaseDialogNotification)

    def test_success_dialog_title(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation()
        assert dialog.title == "Information"

    def test_deprecated_dialog_title(self) -> None:
        dialog: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert dialog.title == "Warning"
