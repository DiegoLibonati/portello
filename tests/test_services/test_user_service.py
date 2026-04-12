from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.models.user_model import UserModel
from src.services.user_service import UserService
from src.utils.dialogs import ConflictDialogError


class TestUserService:
    def test_get_user_by_username_returns_none_when_not_found(self) -> None:
        with patch("src.services.user_service.UserDAO.find_one_by_username", return_value=None):
            result: dict[str, Any] | None = UserService.get_user_by_username("ghost")
        assert result is None

    def test_get_user_by_username_returns_user_dict(self) -> None:
        user_data: dict[str, str] = {"username": "alice", "password": "hash", "_id": "abc123"}
        with patch("src.services.user_service.UserDAO.find_one_by_username", return_value=user_data):
            result: dict[str, Any] | None = UserService.get_user_by_username("alice")
        assert result == user_data

    def test_get_user_by_username_passes_username_to_dao(self) -> None:
        with patch("src.services.user_service.UserDAO.find_one_by_username", return_value=None) as mock_find:
            UserService.get_user_by_username("alice")
        mock_find.assert_called_once_with(username="alice")

    def test_add_user_raises_conflict_when_user_exists(self) -> None:
        existing: dict[str, str] = {"username": "alice", "password": "hash", "_id": "abc"}
        user: UserModel = UserModel(username="alice", password="pass")
        with patch("src.services.user_service.UserDAO.find_one_by_username", return_value=existing):
            with pytest.raises(ConflictDialogError):
                UserService.add_user(user)

    def test_add_user_calls_insert_when_not_exists(self) -> None:
        user: UserModel = UserModel(username="newuser", password="pass")
        mock_result: MagicMock = MagicMock()
        with patch("src.services.user_service.UserDAO.find_one_by_username", return_value=None):
            with patch("src.services.user_service.UserDAO.insert_one", return_value=mock_result) as mock_insert:
                UserService.add_user(user)
        mock_insert.assert_called_once_with(user=user.model_dump())

    def test_add_user_returns_insert_result(self) -> None:
        user: UserModel = UserModel(username="newuser", password="pass")
        mock_result: MagicMock = MagicMock()
        with patch("src.services.user_service.UserDAO.find_one_by_username", return_value=None):
            with patch("src.services.user_service.UserDAO.insert_one", return_value=mock_result):
                result = UserService.add_user(user)
        assert result is mock_result
