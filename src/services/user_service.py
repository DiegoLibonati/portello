from typing import Any

from pymongo.results import InsertOneResult

from src.constants.messages import MESSAGE_ALREADY_EXISTS_USER
from src.data_access.user_dao import UserDAO
from src.models.user_model import UserModel
from src.utils.dialogs import ConflictDialogError


class UserService:
    @staticmethod
    def add_user(user: UserModel) -> InsertOneResult:
        existing = UserDAO.find_one_by_username(username=user.username)
        if existing:
            raise ConflictDialogError(
                message=MESSAGE_ALREADY_EXISTS_USER,
            )
        return UserDAO.insert_one(user=user.model_dump())

    @staticmethod
    def get_user_by_username(username: str) -> dict[str, Any] | None:
        return UserDAO.find_one_by_username(username=username)
