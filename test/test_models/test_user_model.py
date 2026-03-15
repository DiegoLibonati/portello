import pytest
from pydantic import ValidationError

from src.models.user_model import UserModel


class TestUserModelInit:
    def test_stores_username(self) -> None:
        user: UserModel = UserModel(username="alice", password="hashed")
        assert user.username == "alice"

    def test_stores_password(self) -> None:
        user: UserModel = UserModel(username="alice", password="hashed")
        assert user.password == "hashed"

    def test_strips_whitespace_from_username(self) -> None:
        user: UserModel = UserModel(username="  alice  ", password="hashed")
        assert user.username == "alice"

    def test_strips_whitespace_from_password(self) -> None:
        user: UserModel = UserModel(username="alice", password="  hashed  ")
        assert user.password == "hashed"


class TestUserModelValidation:
    def test_raises_validation_error_when_username_is_empty(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="", password="hashed")

    def test_raises_validation_error_when_password_is_empty(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="alice", password="")

    def test_raises_validation_error_when_username_is_whitespace_only(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="   ", password="hashed")

    def test_raises_validation_error_when_password_is_whitespace_only(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="alice", password="   ")

    def test_raises_validation_error_when_username_is_missing(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(password="hashed")

    def test_raises_validation_error_when_password_is_missing(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="alice")


class TestUserModelDump:
    def test_model_dump_contains_username(self) -> None:
        user: UserModel = UserModel(username="alice", password="hashed")
        assert user.model_dump()["username"] == "alice"

    def test_model_dump_contains_password(self) -> None:
        user: UserModel = UserModel(username="alice", password="hashed")
        assert user.model_dump()["password"] == "hashed"

    def test_model_dump_returns_dict(self) -> None:
        user: UserModel = UserModel(username="alice", password="hashed")
        assert isinstance(user.model_dump(), dict)
