from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from pymongo.database import Database

from src.configs.mongo_config import mongo
from src.constants.messages import MESSAGE_ALREADY_EXISTS_USER
from src.models.user_model import UserModel
from src.services.user_service import UserService
from src.utils.dialogs import ConflictDialogError


class TestUserServiceAddUser:
    def test_raises_conflict_error_when_user_already_exists(self) -> None:
        user: UserModel = UserModel(username="alice", password="hashed")
        with patch("src.services.user_service.UserDAO.find_one_by_username", return_value={"username": "alice"}):
            with pytest.raises(ConflictDialogError) as exc_info:
                UserService.add_user(user=user)
        assert exc_info.value.message == MESSAGE_ALREADY_EXISTS_USER

    def test_insert_one_called_when_user_does_not_exist(self) -> None:
        user: UserModel = UserModel(username="alice", password="hashed")
        with (
            patch("src.services.user_service.UserDAO.find_one_by_username", return_value=None),
            patch("src.services.user_service.UserDAO.insert_one") as mock_insert,
        ):
            UserService.add_user(user=user)
        mock_insert.assert_called_once_with(user=user.model_dump())

    def test_insert_one_not_called_when_user_already_exists(self) -> None:
        user: UserModel = UserModel(username="alice", password="hashed")
        with (
            patch("src.services.user_service.UserDAO.find_one_by_username", return_value={"username": "alice"}),
            patch("src.services.user_service.UserDAO.insert_one") as mock_insert,
            pytest.raises(ConflictDialogError),
        ):
            UserService.add_user(user=user)
        mock_insert.assert_not_called()

    def test_returns_insert_result(self) -> None:
        user: UserModel = UserModel(username="alice", password="hashed")
        mock_result: MagicMock = MagicMock()
        with (
            patch("src.services.user_service.UserDAO.find_one_by_username", return_value=None),
            patch("src.services.user_service.UserDAO.insert_one", return_value=mock_result),
        ):
            result = UserService.add_user(user=user)
        assert result is mock_result

    def test_find_one_called_with_username(self) -> None:
        user: UserModel = UserModel(username="alice", password="hashed")
        with (
            patch("src.services.user_service.UserDAO.find_one_by_username", return_value=None) as mock_find,
            patch("src.services.user_service.UserDAO.insert_one"),
        ):
            UserService.add_user(user=user)
        mock_find.assert_called_once_with(username="alice")


class TestUserServiceGetUserByUsername:
    def test_returns_user_dict_when_found(self) -> None:
        expected: dict[str, Any] = {"username": "alice", "password": "hashed", "_id": "123"}
        with patch("src.services.user_service.UserDAO.find_one_by_username", return_value=expected):
            result: dict[str, Any] = UserService.get_user_by_username(username="alice")
        assert result is expected

    def test_returns_none_when_not_found(self) -> None:
        with patch("src.services.user_service.UserDAO.find_one_by_username", return_value=None):
            result = UserService.get_user_by_username(username="unknown")
        assert result is None

    def test_delegates_to_user_dao(self) -> None:
        with patch("src.services.user_service.UserDAO.find_one_by_username", return_value=None) as mock_find:
            UserService.get_user_by_username(username="alice")
        mock_find.assert_called_once_with(username="alice")


class TestUserServiceIntegration:
    def test_add_user_persisted_to_real_db(self, clean_db: Database) -> None:
        mongo.db = clean_db

        user: UserModel = UserModel(username="integrationuser", password="hashed_pass")
        UserService.add_user(user=user)

        stored = clean_db.users.find_one({"username": "integrationuser"})
        assert stored is not None

    def test_add_user_raises_conflict_when_duplicate_in_real_db(self, clean_db: Database) -> None:
        mongo.db = clean_db

        user: UserModel = UserModel(username="duplicateuser", password="hashed")
        UserService.add_user(user=user)

        with pytest.raises(ConflictDialogError):
            UserService.add_user(user=user)

    def test_get_user_by_username_from_real_db(self, clean_db: Database) -> None:
        mongo.db = clean_db

        clean_db.users.insert_one({"username": "dbuser", "password": "hashed"})
        result: dict[str, Any] = UserService.get_user_by_username(username="dbuser")

        assert result is not None
        assert result["username"] == "dbuser"

    def test_get_user_returns_none_when_not_in_real_db(self, clean_db: Database) -> None:
        mongo.db = clean_db

        result = UserService.get_user_by_username(username="nobody")
        assert result is None
