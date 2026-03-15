from typing import Any

from pymongo.results import InsertOneResult

from src.configs.mongo_config import mongo
from src.constants.messages import MESSAGE_ERROR_DATABASE
from src.utils.dialogs import InternalDialogError


class UserDAO:
    @staticmethod
    def _get_collection():
        if mongo.db is None:
            raise InternalDialogError(message=MESSAGE_ERROR_DATABASE)
        return mongo.db.users

    @staticmethod
    def find_one_by_username(username: str) -> dict[str, Any] | None:
        return UserDAO.parse_user(UserDAO._get_collection().find_one({"username": {"$regex": f"^{username}$", "$options": "i"}}))

    @staticmethod
    def insert_one(user: dict[str, Any]) -> InsertOneResult:
        return UserDAO._get_collection().insert_one(user)

    @staticmethod
    def parse_users(users: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [UserDAO.parse_user(user) for user in users]

    @staticmethod
    def parse_user(user: dict[str, Any]) -> dict[str, Any]:
        if not user:
            return None

        return {
            **{k: v for k, v in user.items() if k != "_id"},
            "_id": str(user["_id"]),
        }
