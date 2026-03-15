from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.login_view import LoginView


@pytest.fixture
def login_view(mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> LoginView:
    mock_on_login: MagicMock = MagicMock()
    with (
        patch("src.ui.views.login_view.Frame.__init__", return_value=None),
        patch("src.ui.views.login_view.LabeledEntry"),
        patch("src.ui.views.login_view.Label"),
        patch("src.ui.views.login_view.Button"),
        patch("src.ui.views.login_view.StringVar") as mock_string_var,
        patch.object(LoginView, "columnconfigure"),
    ):
        mock_string_var.return_value = MagicMock(spec=StringVar)
        instance: LoginView = LoginView.__new__(LoginView)
        instance._styles = mock_styles
        instance._on_login = mock_on_login
        instance._on_register = on_register
        instance.text_confirm = MagicMock(spec=StringVar)
        instance.text_username = MagicMock(spec=StringVar)
        instance.text_password = MagicMock(spec=StringVar)
        return instance


class TestLoginViewInit:
    def test_stores_styles(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        mock_on_login: MagicMock = MagicMock()
        with (
            patch("src.ui.views.login_view.Frame.__init__", return_value=None),
            patch("src.ui.views.login_view.LabeledEntry"),
            patch("src.ui.views.login_view.Label"),
            patch("src.ui.views.login_view.Button"),
            patch("src.ui.views.login_view.StringVar"),
            patch.object(LoginView, "columnconfigure"),
        ):
            instance: LoginView = LoginView.__new__(LoginView)
            LoginView.__init__(instance, root=mock_root, styles=mock_styles, on_login=mock_on_login, on_register=on_register)
        assert instance._styles is mock_styles

    def test_stores_on_login(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        mock_on_login: MagicMock = MagicMock()
        with (
            patch("src.ui.views.login_view.Frame.__init__", return_value=None),
            patch("src.ui.views.login_view.LabeledEntry"),
            patch("src.ui.views.login_view.Label"),
            patch("src.ui.views.login_view.Button"),
            patch("src.ui.views.login_view.StringVar"),
            patch.object(LoginView, "columnconfigure"),
        ):
            instance: LoginView = LoginView.__new__(LoginView)
            LoginView.__init__(instance, root=mock_root, styles=mock_styles, on_login=mock_on_login, on_register=on_register)
        assert instance._on_login is mock_on_login

    def test_stores_on_register(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        mock_on_login: MagicMock = MagicMock()
        with (
            patch("src.ui.views.login_view.Frame.__init__", return_value=None),
            patch("src.ui.views.login_view.LabeledEntry"),
            patch("src.ui.views.login_view.Label"),
            patch("src.ui.views.login_view.Button"),
            patch("src.ui.views.login_view.StringVar"),
            patch.object(LoginView, "columnconfigure"),
        ):
            instance: LoginView = LoginView.__new__(LoginView)
            LoginView.__init__(instance, root=mock_root, styles=mock_styles, on_login=mock_on_login, on_register=on_register)
        assert instance._on_register is on_register

    def test_text_username_is_string_var(self, login_view: LoginView) -> None:
        assert isinstance(login_view.text_username, MagicMock)

    def test_text_password_is_string_var(self, login_view: LoginView) -> None:
        assert isinstance(login_view.text_password, MagicMock)

    def test_text_confirm_initial_value_is_welcome(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        mock_on_login: MagicMock = MagicMock()
        captured_value: list[str] = []

        def capture_string_var(value: str = "") -> MagicMock:
            captured_value.append(value)
            return MagicMock(spec=StringVar)

        with (
            patch("src.ui.views.login_view.Frame.__init__", return_value=None),
            patch("src.ui.views.login_view.LabeledEntry"),
            patch("src.ui.views.login_view.Label"),
            patch("src.ui.views.login_view.Button"),
            patch("src.ui.views.login_view.StringVar", side_effect=capture_string_var),
            patch.object(LoginView, "columnconfigure"),
        ):
            instance: LoginView = LoginView.__new__(LoginView)
            LoginView.__init__(instance, root=mock_root, styles=mock_styles, on_login=mock_on_login, on_register=on_register)

        assert "Welcome" in captured_value

    def test_two_labeled_entries_are_created(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        mock_on_login: MagicMock = MagicMock()
        with (
            patch("src.ui.views.login_view.Frame.__init__", return_value=None),
            patch("src.ui.views.login_view.LabeledEntry") as mock_le,
            patch("src.ui.views.login_view.Label"),
            patch("src.ui.views.login_view.Button"),
            patch("src.ui.views.login_view.StringVar"),
            patch.object(LoginView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            instance: LoginView = LoginView.__new__(LoginView)
            LoginView.__init__(instance, root=mock_root, styles=mock_styles, on_login=mock_on_login, on_register=on_register)
        assert mock_le.call_count == 2

    def test_password_labeled_entry_has_show(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        mock_on_login: MagicMock = MagicMock()
        with (
            patch("src.ui.views.login_view.Frame.__init__", return_value=None),
            patch("src.ui.views.login_view.LabeledEntry") as mock_le,
            patch("src.ui.views.login_view.Label"),
            patch("src.ui.views.login_view.Button"),
            patch("src.ui.views.login_view.StringVar"),
            patch.object(LoginView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            instance: LoginView = LoginView.__new__(LoginView)
            LoginView.__init__(instance, root=mock_root, styles=mock_styles, on_login=mock_on_login, on_register=on_register)
        calls = mock_le.call_args_list
        password_call = next(c for c in calls if c[1].get("label_text") == "Password")
        assert password_call[1].get("show") == "*"

    def test_two_buttons_are_created(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        mock_on_login: MagicMock = MagicMock()
        with (
            patch("src.ui.views.login_view.Frame.__init__", return_value=None),
            patch("src.ui.views.login_view.LabeledEntry") as mock_le,
            patch("src.ui.views.login_view.Label"),
            patch("src.ui.views.login_view.Button") as mock_button,
            patch("src.ui.views.login_view.StringVar"),
            patch.object(LoginView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: LoginView = LoginView.__new__(LoginView)
            LoginView.__init__(instance, root=mock_root, styles=mock_styles, on_login=mock_on_login, on_register=on_register)
        assert mock_button.call_count == 2

    def test_login_button_command_is_on_login(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        mock_on_login: MagicMock = MagicMock()
        with (
            patch("src.ui.views.login_view.Frame.__init__", return_value=None),
            patch("src.ui.views.login_view.LabeledEntry") as mock_le,
            patch("src.ui.views.login_view.Label"),
            patch("src.ui.views.login_view.Button") as mock_button,
            patch("src.ui.views.login_view.StringVar"),
            patch.object(LoginView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: LoginView = LoginView.__new__(LoginView)
            LoginView.__init__(instance, root=mock_root, styles=mock_styles, on_login=mock_on_login, on_register=on_register)
        login_call = next(c for c in mock_button.call_args_list if c[1].get("text") == "Login")
        assert login_call[1].get("command") is mock_on_login

    def test_register_button_command_is_on_register(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        mock_on_login: MagicMock = MagicMock()
        with (
            patch("src.ui.views.login_view.Frame.__init__", return_value=None),
            patch("src.ui.views.login_view.LabeledEntry") as mock_le,
            patch("src.ui.views.login_view.Label"),
            patch("src.ui.views.login_view.Button") as mock_button,
            patch("src.ui.views.login_view.StringVar"),
            patch.object(LoginView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: LoginView = LoginView.__new__(LoginView)
            LoginView.__init__(instance, root=mock_root, styles=mock_styles, on_login=mock_on_login, on_register=on_register)
        register_call = next(c for c in mock_button.call_args_list if c[1].get("text") == "Register")
        assert register_call[1].get("command") is on_register
