from typing import Any

import pytest
from bson import ObjectId
from pymongo.database import Database
from pymongo.results import InsertOneResult

from src.configs.mongo_config import mongo
from src.data_access.user_dao import UserDAO
from src.utils.dialogs import InternalDialogError


class TestUserDAOParseUser:
    def test_parse_user_with_none_returns_none(self) -> None:
        result: dict[str, Any] | None = UserDAO.parse_user(None)
        assert result is None

    def test_parse_user_converts_object_id_to_str(self) -> None:
        oid: ObjectId = ObjectId()
        user: dict[str, Any] = {"_id": oid, "username": "alice"}
        result: dict[str, Any] = UserDAO.parse_user(user)
        assert isinstance(result["_id"], str)
        assert result["_id"] == str(oid)

    def test_parse_user_preserves_username(self) -> None:
        oid: ObjectId = ObjectId()
        user: dict[str, Any] = {"_id": oid, "username": "alice"}
        result: dict[str, Any] = UserDAO.parse_user(user)
        assert result["username"] == "alice"

    def test_parse_user_preserves_all_extra_fields(self) -> None:
        oid: ObjectId = ObjectId()
        user: dict[str, Any] = {"_id": oid, "username": "alice", "password": "hash", "role": "admin"}
        result: dict[str, Any] = UserDAO.parse_user(user)
        assert result["username"] == "alice"
        assert result["password"] == "hash"
        assert result["role"] == "admin"

    def test_parse_users_empty_list(self) -> None:
        result: list[dict[str, Any]] = UserDAO.parse_users([])
        assert result == []

    def test_parse_users_multiple_converts_all_ids(self) -> None:
        oid1: ObjectId = ObjectId()
        oid2: ObjectId = ObjectId()
        users: list[dict[str, Any]] = [
            {"_id": oid1, "username": "alice"},
            {"_id": oid2, "username": "bob"},
        ]
        result: list[dict[str, Any]] = UserDAO.parse_users(users)
        assert len(result) == 2
        assert isinstance(result[0]["_id"], str)
        assert isinstance(result[1]["_id"], str)

    def test_parse_users_preserves_order(self) -> None:
        oid1: ObjectId = ObjectId()
        oid2: ObjectId = ObjectId()
        users: list[dict[str, Any]] = [
            {"_id": oid1, "username": "alice"},
            {"_id": oid2, "username": "bob"},
        ]
        result: list[dict[str, Any]] = UserDAO.parse_users(users)
        assert result[0]["username"] == "alice"
        assert result[1]["username"] == "bob"


class TestUserDAOGetCollection:
    def test_raises_internal_error_when_db_not_connected(self) -> None:
        original_db = mongo.db
        try:
            mongo.db = None
            with pytest.raises(InternalDialogError):
                UserDAO._get_collection()
        finally:
            mongo.db = original_db


class TestUserDAOIntegration:
    @pytest.mark.integration
    def test_find_one_by_username_returns_none_when_not_found(self, connected_mongo: Database) -> None:
        result: dict[str, Any] | None = UserDAO.find_one_by_username("nonexistent_user_xyz")
        assert result is None

    @pytest.mark.integration
    def test_insert_one_and_find_by_username(self, connected_mongo: Database) -> None:
        user: dict[str, Any] = {"username": "testuser", "password": "hashed_pw"}
        UserDAO.insert_one(user)
        result: dict[str, Any] | None = UserDAO.find_one_by_username("testuser")
        assert result is not None
        assert result["username"] == "testuser"

    @pytest.mark.integration
    def test_find_one_by_username_case_insensitive(self, connected_mongo: Database) -> None:
        user: dict[str, Any] = {"username": "CasedUser", "password": "hash"}
        UserDAO.insert_one(user)
        result: dict[str, Any] | None = UserDAO.find_one_by_username("caseduser")
        assert result is not None
        assert result["username"] == "CasedUser"

    @pytest.mark.integration
    def test_insert_one_returns_insert_result(self, connected_mongo: Database) -> None:
        user: dict[str, Any] = {"username": "inserttest", "password": "hash"}
        result: InsertOneResult = UserDAO.insert_one(user)
        assert result.inserted_id is not None

    @pytest.mark.integration
    def test_parsed_user_has_string_id(self, connected_mongo: Database) -> None:
        user: dict[str, Any] = {"username": "idcheck", "password": "hash"}
        UserDAO.insert_one(user)
        result: dict[str, Any] | None = UserDAO.find_one_by_username("idcheck")
        assert result is not None
        assert isinstance(result["_id"], str)
