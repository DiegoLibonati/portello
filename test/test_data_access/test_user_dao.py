from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from bson import ObjectId
from pymongo.database import Database
from werkzeug.security import generate_password_hash

from src.configs.mongo_config import mongo
from src.constants.messages import MESSAGE_ERROR_DATABASE
from src.data_access.user_dao import UserDAO
from src.utils.dialogs import InternalDialogError


class TestUserDAOGetCollection:
    def test_raises_internal_error_when_db_is_none(self) -> None:
        with patch("src.data_access.user_dao.mongo") as mock_mongo:
            mock_mongo.db = None
            with pytest.raises(InternalDialogError) as exc_info:
                UserDAO._get_collection()
        assert exc_info.value.message == MESSAGE_ERROR_DATABASE

    def test_returns_collection_when_db_is_set(self) -> None:
        with patch("src.data_access.user_dao.mongo") as mock_mongo:
            mock_mongo.db = MagicMock()
            mock_mongo.db.users = MagicMock()
            result = UserDAO._get_collection()
        assert result is mock_mongo.db.users


class TestUserDAOParseUser:
    def test_returns_none_when_user_is_none(self) -> None:
        assert UserDAO.parse_user(None) is None

    def test_returns_none_when_user_is_empty_dict(self) -> None:
        assert UserDAO.parse_user({}) is None

    def test_converts_id_to_string(self) -> None:
        oid: ObjectId = ObjectId()
        user: dict[str, Any] = {"_id": oid, "username": "alice"}
        result: dict[str, Any] = UserDAO.parse_user(user)
        assert result["_id"] == str(oid)

    def test_id_is_string_type(self) -> None:
        user: dict[str, Any] = {"_id": ObjectId(), "username": "alice"}
        result: dict[str, Any] = UserDAO.parse_user(user)
        assert isinstance(result["_id"], str)

    def test_preserves_other_fields(self) -> None:
        oid: ObjectId = ObjectId()
        user: dict[str, Any] = {"_id": oid, "username": "alice", "password": "hashed"}
        result: dict[str, Any] = UserDAO.parse_user(user)
        assert result["username"] == "alice"
        assert result["password"] == "hashed"

    def test_result_does_not_contain_original_id_object(self) -> None:
        oid: ObjectId = ObjectId()
        user: dict[str, Any] = {"_id": oid, "username": "alice"}
        result: dict[str, Any] = UserDAO.parse_user(user)
        assert not isinstance(result["_id"], ObjectId)


class TestUserDAOParseUsers:
    def test_returns_empty_list_for_empty_input(self) -> None:
        assert UserDAO.parse_users([]) == []

    def test_returns_list_of_parsed_users(self) -> None:
        users: list[dict[str, Any]] = [
            {"_id": ObjectId(), "username": "user1"},
            {"_id": ObjectId(), "username": "user2"},
        ]
        result: list[dict[str, Any]] = UserDAO.parse_users(users)
        assert len(result) == 2
        assert all(isinstance(u["_id"], str) for u in result)


class TestUserDAOFindOneByUsername:
    def test_calls_find_one_with_regex(self) -> None:
        with patch("src.data_access.user_dao.mongo") as mock_mongo:
            mock_collection: MagicMock = MagicMock()
            mock_mongo.db = MagicMock()
            mock_mongo.db.users = mock_collection
            mock_collection.find_one.return_value = None
            UserDAO.find_one_by_username("alice")
        mock_collection.find_one.assert_called_once_with({"username": {"$regex": "^alice$", "$options": "i"}})

    def test_returns_none_when_user_not_found(self) -> None:
        with patch("src.data_access.user_dao.mongo") as mock_mongo:
            mock_mongo.db = MagicMock()
            mock_mongo.db.users.find_one.return_value = None
            result = UserDAO.find_one_by_username("unknown")
        assert result is None

    def test_returns_parsed_user_when_found(self) -> None:
        oid: ObjectId = ObjectId()
        raw: dict[str, Any] = {"_id": oid, "username": "alice", "password": "hashed"}
        with patch("src.data_access.user_dao.mongo") as mock_mongo:
            mock_mongo.db = MagicMock()
            mock_mongo.db.users.find_one.return_value = raw
            result: dict[str, Any] = UserDAO.find_one_by_username("alice")
        assert result["_id"] == str(oid)
        assert result["username"] == "alice"

    def test_search_is_case_insensitive(self) -> None:
        with patch("src.data_access.user_dao.mongo") as mock_mongo:
            mock_collection: MagicMock = MagicMock()
            mock_mongo.db = MagicMock()
            mock_mongo.db.users = mock_collection
            mock_collection.find_one.return_value = None
            UserDAO.find_one_by_username("ALICE")
        call_kwargs = mock_collection.find_one.call_args[0][0]
        assert call_kwargs["username"]["$options"] == "i"


class TestUserDAOInsertOne:
    def test_insert_one_called_with_user(self) -> None:
        user: dict[str, Any] = {"username": "alice", "password": "hashed"}
        with patch("src.data_access.user_dao.mongo") as mock_mongo:
            mock_collection: MagicMock = MagicMock()
            mock_mongo.db = MagicMock()
            mock_mongo.db.users = mock_collection
            UserDAO.insert_one(user)
        mock_collection.insert_one.assert_called_once_with(user)

    def test_returns_insert_result(self) -> None:
        user: dict[str, Any] = {"username": "alice", "password": "hashed"}
        with patch("src.data_access.user_dao.mongo") as mock_mongo:
            mock_collection: MagicMock = MagicMock()
            mock_insert_result: MagicMock = MagicMock()
            mock_mongo.db = MagicMock()
            mock_mongo.db.users = mock_collection
            mock_collection.insert_one.return_value = mock_insert_result
            result = UserDAO.insert_one(user)
        assert result is mock_insert_result


class TestUserDAOIntegration:
    def test_find_one_by_username_with_real_db(self, clean_db: Database) -> None:
        mongo.db = clean_db

        clean_db.users.insert_one({"username": "realuser", "password": generate_password_hash("pass")})
        result: dict[str, Any] = UserDAO.find_one_by_username("realuser")

        assert result is not None
        assert result["username"] == "realuser"

    def test_find_one_by_username_case_insensitive_with_real_db(self, clean_db: Database) -> None:
        mongo.db = clean_db

        clean_db.users.insert_one({"username": "RealUser", "password": "hashed"})
        result: dict[str, Any] = UserDAO.find_one_by_username("realuser")

        assert result is not None
        assert result["username"] == "RealUser"

    def test_find_one_returns_none_when_not_found_with_real_db(self, clean_db: Database) -> None:
        mongo.db = clean_db

        result = UserDAO.find_one_by_username("nobody")
        assert result is None

    def test_insert_one_with_real_db(self, clean_db: Database) -> None:
        mongo.db = clean_db

        user: dict[str, Any] = {"username": "newuser", "password": "hashed"}
        result = UserDAO.insert_one(user)

        assert result.inserted_id is not None
        stored = clean_db.users.find_one({"username": "newuser"})
        assert stored is not None
