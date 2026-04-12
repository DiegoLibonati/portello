from src.constants import messages


class TestMessages:
    def test_message_success_login_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_SUCCESS_LOGIN, str)

    def test_message_success_login_not_empty(self) -> None:
        assert len(messages.MESSAGE_SUCCESS_LOGIN) > 0

    def test_message_success_register_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_SUCCESS_REGISTER, str)

    def test_message_success_register_not_empty(self) -> None:
        assert len(messages.MESSAGE_SUCCESS_REGISTER) > 0

    def test_message_error_app_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_ERROR_APP, str)

    def test_message_error_pydantic_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_ERROR_PYDANTIC, str)

    def test_message_error_database_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_ERROR_DATABASE, str)

    def test_message_not_valid_password_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_PASSWORD, str)

    def test_message_not_valid_match_password_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_MATCH_PASSWORD, str)

    def test_message_not_valid_fields_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_FIELDS, str)

    def test_message_not_exists_user_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_EXISTS_USER, str)

    def test_message_already_exists_user_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_ALREADY_EXISTS_USER, str)

    def test_message_not_found_dialog_type_is_str(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_FOUND_DIALOG_TYPE, str)

    def test_all_messages_are_unique(self) -> None:
        all_messages: list[str] = [
            messages.MESSAGE_SUCCESS_LOGIN,
            messages.MESSAGE_SUCCESS_REGISTER,
            messages.MESSAGE_ERROR_APP,
            messages.MESSAGE_ERROR_PYDANTIC,
            messages.MESSAGE_ERROR_DATABASE,
            messages.MESSAGE_NOT_VALID_PASSWORD,
            messages.MESSAGE_NOT_VALID_MATCH_PASSWORD,
            messages.MESSAGE_NOT_VALID_FIELDS,
            messages.MESSAGE_NOT_EXISTS_USER,
            messages.MESSAGE_ALREADY_EXISTS_USER,
            messages.MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ]
        assert len(all_messages) == len(set(all_messages))
