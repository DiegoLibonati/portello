import pytest
from pydantic import ValidationError

from src.models.user_model import UserModel


class TestUserModel:
    def test_valid_user_model(self) -> None:
        user: UserModel = UserModel(username="alice", password="secret")
        assert user.username == "alice"
        assert user.password == "secret"

    def test_username_cannot_be_empty(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="", password="secret")

    def test_password_cannot_be_empty(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="alice", password="")

    def test_username_whitespace_only_raises(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="   ", password="secret")

    def test_password_whitespace_only_raises(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="alice", password="   ")

    def test_username_strips_surrounding_whitespace(self) -> None:
        user: UserModel = UserModel(username="  alice  ", password="secret")
        assert user.username == "alice"

    def test_password_strips_surrounding_whitespace(self) -> None:
        user: UserModel = UserModel(username="alice", password="  secret  ")
        assert user.password == "secret"

    def test_model_dump_returns_correct_keys(self) -> None:
        user: UserModel = UserModel(username="alice", password="secret")
        dumped: dict[str, str] = user.model_dump()
        assert set(dumped.keys()) == {"username", "password"}

    def test_model_dump_returns_correct_values(self) -> None:
        user: UserModel = UserModel(username="alice", password="secret")
        dumped: dict[str, str] = user.model_dump()
        assert dumped["username"] == "alice"
        assert dumped["password"] == "secret"

    def test_missing_username_raises(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(password="secret")

    def test_missing_password_raises(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="alice")

    def test_single_char_username_is_valid(self) -> None:
        user: UserModel = UserModel(username="a", password="secret")
        assert user.username == "a"

    def test_single_char_password_is_valid(self) -> None:
        user: UserModel = UserModel(username="alice", password="x")
        assert user.password == "x"
