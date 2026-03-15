from src.constants.messages import (
    MESSAGE_ALREADY_EXISTS_USER,
    MESSAGE_ERROR_APP,
    MESSAGE_ERROR_DATABASE,
    MESSAGE_ERROR_PYDANTIC,
    MESSAGE_NOT_EXISTS_USER,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_NOT_VALID_MATCH_PASSWORD,
    MESSAGE_NOT_VALID_PASSWORD,
    MESSAGE_SUCCESS_LOGIN,
    MESSAGE_SUCCESS_REGISTER,
)


class TestMessages:
    def test_success_login_is_string(self) -> None:
        assert isinstance(MESSAGE_SUCCESS_LOGIN, str)

    def test_success_login_is_not_empty(self) -> None:
        assert MESSAGE_SUCCESS_LOGIN

    def test_success_register_is_string(self) -> None:
        assert isinstance(MESSAGE_SUCCESS_REGISTER, str)

    def test_success_register_is_not_empty(self) -> None:
        assert MESSAGE_SUCCESS_REGISTER

    def test_error_app_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_APP, str)

    def test_error_app_is_not_empty(self) -> None:
        assert MESSAGE_ERROR_APP

    def test_error_pydantic_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_PYDANTIC, str)

    def test_error_pydantic_is_not_empty(self) -> None:
        assert MESSAGE_ERROR_PYDANTIC

    def test_error_database_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_DATABASE, str)

    def test_error_database_is_not_empty(self) -> None:
        assert MESSAGE_ERROR_DATABASE

    def test_not_valid_password_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_PASSWORD, str)

    def test_not_valid_password_is_not_empty(self) -> None:
        assert MESSAGE_NOT_VALID_PASSWORD

    def test_not_valid_match_password_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_MATCH_PASSWORD, str)

    def test_not_valid_match_password_is_not_empty(self) -> None:
        assert MESSAGE_NOT_VALID_MATCH_PASSWORD

    def test_not_valid_fields_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_FIELDS, str)

    def test_not_valid_fields_is_not_empty(self) -> None:
        assert MESSAGE_NOT_VALID_FIELDS

    def test_not_exists_user_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_EXISTS_USER, str)

    def test_not_exists_user_is_not_empty(self) -> None:
        assert MESSAGE_NOT_EXISTS_USER

    def test_already_exists_user_is_string(self) -> None:
        assert isinstance(MESSAGE_ALREADY_EXISTS_USER, str)

    def test_already_exists_user_is_not_empty(self) -> None:
        assert MESSAGE_ALREADY_EXISTS_USER

    def test_not_found_dialog_type_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_DIALOG_TYPE, str)

    def test_not_found_dialog_type_is_not_empty(self) -> None:
        assert MESSAGE_NOT_FOUND_DIALOG_TYPE

    def test_all_messages_are_unique(self) -> None:
        all_messages: list[str] = [
            MESSAGE_SUCCESS_LOGIN,
            MESSAGE_SUCCESS_REGISTER,
            MESSAGE_ERROR_APP,
            MESSAGE_ERROR_PYDANTIC,
            MESSAGE_ERROR_DATABASE,
            MESSAGE_NOT_VALID_PASSWORD,
            MESSAGE_NOT_VALID_MATCH_PASSWORD,
            MESSAGE_NOT_VALID_FIELDS,
            MESSAGE_NOT_EXISTS_USER,
            MESSAGE_ALREADY_EXISTS_USER,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ]
        assert len(all_messages) == len(set(all_messages))
