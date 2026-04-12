from unittest.mock import MagicMock, patch

import pytest
from werkzeug.security import generate_password_hash

from src.models.user_model import UserModel
from src.services.auth_service import AuthService
from src.utils.dialogs import ConflictDialogError, NotFoundDialogError, ValidationDialogError


class TestAuthServiceLogin:
    def test_empty_username_raises_validation_error(self) -> None:
        with pytest.raises(ValidationDialogError):
            AuthService.login(username="", password="pass")

    def test_empty_password_raises_validation_error(self) -> None:
        with pytest.raises(ValidationDialogError):
            AuthService.login(username="user", password="")

    def test_whitespace_username_raises_validation_error(self) -> None:
        with pytest.raises(ValidationDialogError):
            AuthService.login(username="   ", password="pass")

    def test_whitespace_password_raises_validation_error(self) -> None:
        with pytest.raises(ValidationDialogError):
            AuthService.login(username="user", password="   ")

    def test_user_not_found_raises_not_found_error(self) -> None:
        with patch("src.services.auth_service.UserService.get_user_by_username", return_value=None):
            with pytest.raises(NotFoundDialogError):
                AuthService.login(username="ghost", password="pass")

    def test_wrong_password_raises_validation_error(self) -> None:
        hashed: str = generate_password_hash("correct")
        user_data: dict[str, str] = {"username": "alice", "password": hashed}
        with patch("src.services.auth_service.UserService.get_user_by_username", return_value=user_data):
            with pytest.raises(ValidationDialogError):
                AuthService.login(username="alice", password="wrong")

    def test_login_success_returns_user_model(self) -> None:
        hashed: str = generate_password_hash("correct")
        user_data: dict[str, str] = {"username": "alice", "password": hashed}
        with patch("src.services.auth_service.UserService.get_user_by_username", return_value=user_data):
            with patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog:
                mock_dialog.return_value.open = MagicMock()
                result: UserModel = AuthService.login(username="alice", password="correct")
        assert isinstance(result, UserModel)
        assert result.username == "alice"

    def test_login_success_calls_dialog_open(self) -> None:
        hashed: str = generate_password_hash("correct")
        user_data: dict[str, str] = {"username": "alice", "password": hashed}
        with patch("src.services.auth_service.UserService.get_user_by_username", return_value=user_data):
            with patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog:
                mock_instance: MagicMock = MagicMock()
                mock_dialog.return_value = mock_instance
                AuthService.login(username="alice", password="correct")
        mock_instance.open.assert_called_once()


class TestAuthServiceRegister:
    def test_empty_username_raises_validation_error(self) -> None:
        with pytest.raises(ValidationDialogError):
            AuthService.register(username="", password="pass", confirm_password="pass")

    def test_empty_password_raises_validation_error(self) -> None:
        with pytest.raises(ValidationDialogError):
            AuthService.register(username="alice", password="", confirm_password="")

    def test_whitespace_username_raises_validation_error(self) -> None:
        with pytest.raises(ValidationDialogError):
            AuthService.register(username="   ", password="pass", confirm_password="pass")

    def test_whitespace_password_raises_validation_error(self) -> None:
        with pytest.raises(ValidationDialogError):
            AuthService.register(username="alice", password="   ", confirm_password="   ")

    def test_password_mismatch_raises_validation_error(self) -> None:
        with pytest.raises(ValidationDialogError):
            AuthService.register(username="alice", password="pass1", confirm_password="pass2")

    def test_existing_user_raises_conflict_error(self) -> None:
        existing: dict[str, str] = {"username": "alice", "password": "hash", "_id": "abc"}
        with patch("src.services.auth_service.UserService.get_user_by_username", return_value=existing):
            with pytest.raises(ConflictDialogError):
                AuthService.register(username="alice", password="pass", confirm_password="pass")

    def test_register_success_returns_true(self) -> None:
        with patch("src.services.auth_service.UserService.get_user_by_username", return_value=None):
            with patch("src.services.auth_service.UserService.add_user"):
                with patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog:
                    mock_dialog.return_value.open = MagicMock()
                    result: bool = AuthService.register(username="alice", password="pass", confirm_password="pass")
        assert result is True

    def test_register_success_calls_dialog_open(self) -> None:
        with patch("src.services.auth_service.UserService.get_user_by_username", return_value=None):
            with patch("src.services.auth_service.UserService.add_user"):
                with patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog:
                    mock_instance: MagicMock = MagicMock()
                    mock_dialog.return_value = mock_instance
                    AuthService.register(username="alice", password="pass", confirm_password="pass")
        mock_instance.open.assert_called_once()
