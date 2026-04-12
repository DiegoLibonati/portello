import tkinter as tk
from unittest.mock import MagicMock

from src.ui.styles import Styles
from src.ui.views.register_view import RegisterView


class TestRegisterView:
    def test_instantiation(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(
            root=root,
            styles=Styles(),
            on_register=MagicMock(),
        )
        assert view is not None
        view.destroy()

    def test_title(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(
            root=root,
            styles=Styles(),
            on_register=MagicMock(),
        )
        assert view.title() == "Register"
        view.destroy()

    def test_resizable_is_false(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(
            root=root,
            styles=Styles(),
            on_register=MagicMock(),
        )
        assert view.resizable() == (False, False)
        view.destroy()

    def test_text_confirm_initial_empty(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(
            root=root,
            styles=Styles(),
            on_register=MagicMock(),
        )
        assert view.text_confirm.get() == ""
        view.destroy()

    def test_text_username_initial_empty(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(
            root=root,
            styles=Styles(),
            on_register=MagicMock(),
        )
        assert view.text_username.get() == ""
        view.destroy()

    def test_text_password_initial_empty(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(
            root=root,
            styles=Styles(),
            on_register=MagicMock(),
        )
        assert view.text_password.get() == ""
        view.destroy()

    def test_text_confirm_password_initial_empty(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(
            root=root,
            styles=Styles(),
            on_register=MagicMock(),
        )
        assert view.text_confirm_password.get() == ""
        view.destroy()

    def test_text_username_set_and_get(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(
            root=root,
            styles=Styles(),
            on_register=MagicMock(),
        )
        view.text_username.set("bob")
        assert view.text_username.get() == "bob"
        view.destroy()

    def test_text_password_set_and_get(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(
            root=root,
            styles=Styles(),
            on_register=MagicMock(),
        )
        view.text_password.set("pass123")
        assert view.text_password.get() == "pass123"
        view.destroy()

    def test_text_confirm_password_set_and_get(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(
            root=root,
            styles=Styles(),
            on_register=MagicMock(),
        )
        view.text_confirm_password.set("pass123")
        assert view.text_confirm_password.get() == "pass123"
        view.destroy()

    def test_on_register_callback_is_invoked(self, root: tk.Tk) -> None:
        mock_register: MagicMock = MagicMock()
        view: RegisterView = RegisterView(
            root=root,
            styles=Styles(),
            on_register=mock_register,
        )
        view._on_register()
        mock_register.assert_called_once()
        view.destroy()

    def test_background_color_matches_styles(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: RegisterView = RegisterView(
            root=root,
            styles=styles,
            on_register=MagicMock(),
        )
        assert view.cget("bg") == styles.PRIMARY_COLOR
        view.destroy()
