import tkinter as tk
from unittest.mock import MagicMock

from src.ui.styles import Styles
from src.ui.views.login_view import LoginView


class TestLoginView:
    def test_instantiation(self, root: tk.Tk) -> None:
        view: LoginView = LoginView(
            root=root,
            styles=Styles(),
            on_login=MagicMock(),
            on_register=MagicMock(),
        )
        assert view is not None
        view.destroy()

    def test_text_confirm_initial_value(self, root: tk.Tk) -> None:
        view: LoginView = LoginView(
            root=root,
            styles=Styles(),
            on_login=MagicMock(),
            on_register=MagicMock(),
        )
        assert view.text_confirm.get() == "Welcome"
        view.destroy()

    def test_text_username_initial_empty(self, root: tk.Tk) -> None:
        view: LoginView = LoginView(
            root=root,
            styles=Styles(),
            on_login=MagicMock(),
            on_register=MagicMock(),
        )
        assert view.text_username.get() == ""
        view.destroy()

    def test_text_password_initial_empty(self, root: tk.Tk) -> None:
        view: LoginView = LoginView(
            root=root,
            styles=Styles(),
            on_login=MagicMock(),
            on_register=MagicMock(),
        )
        assert view.text_password.get() == ""
        view.destroy()

    def test_text_username_set_and_get(self, root: tk.Tk) -> None:
        view: LoginView = LoginView(
            root=root,
            styles=Styles(),
            on_login=MagicMock(),
            on_register=MagicMock(),
        )
        view.text_username.set("alice")
        assert view.text_username.get() == "alice"
        view.destroy()

    def test_text_password_set_and_get(self, root: tk.Tk) -> None:
        view: LoginView = LoginView(
            root=root,
            styles=Styles(),
            on_login=MagicMock(),
            on_register=MagicMock(),
        )
        view.text_password.set("secret")
        assert view.text_password.get() == "secret"
        view.destroy()

    def test_on_login_callback_is_invoked(self, root: tk.Tk) -> None:
        mock_login: MagicMock = MagicMock()
        view: LoginView = LoginView(
            root=root,
            styles=Styles(),
            on_login=mock_login,
            on_register=MagicMock(),
        )
        view._on_login()
        mock_login.assert_called_once()
        view.destroy()

    def test_on_register_callback_is_invoked(self, root: tk.Tk) -> None:
        mock_register: MagicMock = MagicMock()
        view: LoginView = LoginView(
            root=root,
            styles=Styles(),
            on_login=MagicMock(),
            on_register=mock_register,
        )
        view._on_register()
        mock_register.assert_called_once()
        view.destroy()

    def test_background_color_matches_styles(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: LoginView = LoginView(
            root=root,
            styles=styles,
            on_login=MagicMock(),
            on_register=MagicMock(),
        )
        assert view.cget("bg") == styles.PRIMARY_COLOR
        view.destroy()
