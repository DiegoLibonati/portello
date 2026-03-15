from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import (
    MESSAGE_ALREADY_EXISTS_USER,
    MESSAGE_NOT_EXISTS_USER,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_NOT_VALID_MATCH_PASSWORD,
    MESSAGE_NOT_VALID_PASSWORD,
    MESSAGE_SUCCESS_LOGIN,
    MESSAGE_SUCCESS_REGISTER,
)
from src.models.user_model import UserModel
from src.services.auth_service import AuthService
from src.utils.dialogs import ConflictDialogError, NotFoundDialogError, ValidationDialogError


class TestAuthServiceLogin:
    def test_raises_validation_error_when_username_is_empty(self) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            AuthService.login(username="", password="pass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_password_is_empty(self) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            AuthService.login(username="user", password="")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_username_is_whitespace(self) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            AuthService.login(username="   ", password="pass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_password_is_whitespace(self) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            AuthService.login(username="user", password="   ")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_not_found_error_when_user_does_not_exist(self) -> None:
        with patch("src.services.auth_service.UserService.get_user_by_username", return_value=None):
            with pytest.raises(NotFoundDialogError) as exc_info:
                AuthService.login(username="unknown", password="pass")
        assert exc_info.value.message == MESSAGE_NOT_EXISTS_USER

    def test_raises_validation_error_when_password_is_wrong(self) -> None:
        user: dict[str, Any] = {"username": "alice", "password": "hashed", "_id": "123"}
        with (
            patch("src.services.auth_service.UserService.get_user_by_username", return_value=user),
            patch("src.services.auth_service.check_password_hash", return_value=False),
        ):
            with pytest.raises(ValidationDialogError) as exc_info:
                AuthService.login(username="alice", password="wrongpass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_PASSWORD

    def test_returns_user_model_on_success(self) -> None:
        user: dict[str, Any] = {"username": "alice", "password": "hashed", "_id": "123"}
        with (
            patch("src.services.auth_service.UserService.get_user_by_username", return_value=user),
            patch("src.services.auth_service.check_password_hash", return_value=True),
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class,
        ):
            mock_dialog_class.return_value = MagicMock()
            result: UserModel = AuthService.login(username="alice", password="testpass")
        assert isinstance(result, UserModel)
        assert result.username == "alice"

    def test_success_dialog_opened_on_login(self) -> None:
        user: dict[str, Any] = {"username": "alice", "password": "hashed", "_id": "123"}
        with (
            patch("src.services.auth_service.UserService.get_user_by_username", return_value=user),
            patch("src.services.auth_service.check_password_hash", return_value=True),
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class,
        ):
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            AuthService.login(username="alice", password="testpass")
        mock_dialog_class.assert_called_once_with(message=MESSAGE_SUCCESS_LOGIN)
        mock_dialog.open.assert_called_once()

    def test_get_user_by_username_called_with_correct_username(self) -> None:
        with (
            patch("src.services.auth_service.UserService.get_user_by_username", return_value=None) as mock_get,
            pytest.raises(NotFoundDialogError),
        ):
            AuthService.login(username="alice", password="pass")
        mock_get.assert_called_once_with(username="alice")


class TestAuthServiceRegister:
    def test_raises_validation_error_when_username_is_empty(self) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            AuthService.register(username="", password="pass", confirm_password="pass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_password_is_empty(self) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            AuthService.register(username="alice", password="", confirm_password="pass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_confirm_password_is_empty(self) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            AuthService.register(username="alice", password="pass", confirm_password="")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_username_is_whitespace(self) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            AuthService.register(username="   ", password="pass", confirm_password="pass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_password_is_whitespace(self) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            AuthService.register(username="alice", password="   ", confirm_password="   ")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_passwords_do_not_match(self) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            AuthService.register(username="alice", password="pass1", confirm_password="pass2")
        assert exc_info.value.message == MESSAGE_NOT_VALID_MATCH_PASSWORD

    def test_raises_conflict_error_when_user_already_exists(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserService.get_user_by_username", return_value={"username": "newuser"}),
            pytest.raises(ConflictDialogError) as exc_info,
        ):
            AuthService.register(**registration_data)
        assert exc_info.value.message == MESSAGE_ALREADY_EXISTS_USER

    def test_returns_true_on_success(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserService.get_user_by_username", return_value=None),
            patch("src.services.auth_service.UserService.add_user"),
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class,
        ):
            mock_dialog_class.return_value = MagicMock()
            result: bool = AuthService.register(**registration_data)
        assert result is True

    def test_add_user_called_on_success(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserService.get_user_by_username", return_value=None),
            patch("src.services.auth_service.UserService.add_user") as mock_add,
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class,
        ):
            mock_dialog_class.return_value = MagicMock()
            AuthService.register(**registration_data)
        mock_add.assert_called_once()

    def test_saved_user_has_correct_username(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserService.get_user_by_username", return_value=None),
            patch("src.services.auth_service.UserService.add_user") as mock_add,
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class,
        ):
            mock_dialog_class.return_value = MagicMock()
            AuthService.register(**registration_data)
        saved_user: UserModel = mock_add.call_args[1]["user"]
        assert saved_user.username == registration_data["username"]

    def test_saved_user_has_hashed_password(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserService.get_user_by_username", return_value=None),
            patch("src.services.auth_service.UserService.add_user") as mock_add,
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class,
        ):
            mock_dialog_class.return_value = MagicMock()
            AuthService.register(**registration_data)
        saved_user: UserModel = mock_add.call_args[1]["user"]
        assert saved_user.password != registration_data["password"]

    def test_success_dialog_opened_on_register(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserService.get_user_by_username", return_value=None),
            patch("src.services.auth_service.UserService.add_user"),
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class,
        ):
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            AuthService.register(**registration_data)
        mock_dialog_class.assert_called_once_with(message=MESSAGE_SUCCESS_REGISTER)
        mock_dialog.open.assert_called_once()
