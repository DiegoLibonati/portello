import tkinter as tk
from unittest.mock import patch

from src.configs.default_config import DefaultConfig
from src.models.user_model import UserModel
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


class TestInterfaceApp:
    def test_instantiation(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app is not None

    def test_user_initial_value_is_none(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app.user is None

    def test_username_property_when_no_user_returns_na(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app.username == "N/A"

    def test_username_property_with_user_returns_username(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app.user = UserModel(username="alice", password="pass")
        assert app.username == "alice"

    def test_login_view_is_created(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app._login_view is not None

    def test_config_is_stored(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app._config is config

    def test_styles_default_instance_used_when_not_provided(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert isinstance(app._styles, Styles)

    def test_custom_styles_stored(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        styles: Styles = Styles()
        app: InterfaceApp = InterfaceApp(root=root, config=config, styles=styles)
        assert app._styles is styles

    def test_register_view_initial_is_none(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app._register_view is None

    def test_login_sets_user_on_success(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        user_model: UserModel = UserModel(username="alice", password="pass")
        app._login_view.text_username.set("alice")
        app._login_view.text_password.set("pass")
        with patch("src.ui.interface_app.AuthService.login", return_value=user_model):
            with patch("src.ui.interface_app.MainView"):
                app._login()
        assert app.user == user_model

    def test_login_creates_main_view_on_success(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        user_model: UserModel = UserModel(username="alice", password="pass")
        app._login_view.text_username.set("alice")
        app._login_view.text_password.set("pass")
        with patch("src.ui.interface_app.AuthService.login", return_value=user_model):
            with patch("src.ui.interface_app.MainView") as mock_main_view:
                app._login()
        mock_main_view.assert_called_once()

    def test_open_register_creates_register_view(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._open_register()
        assert app._register_view is not None
        app._register_view.destroy()
        app._register_view = None

    def test_register_does_nothing_when_register_view_is_none(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._register_view = None
        app._register()

    def test_register_destroys_view_and_resets_on_success(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._open_register()
        app._register_view.text_username.set("alice")
        app._register_view.text_password.set("pass")
        app._register_view.text_confirm_password.set("pass")
        with patch("src.ui.interface_app.AuthService.register", return_value=True):
            app._register()
        assert app._register_view is None

    def test_register_preserves_view_when_register_returns_false(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._open_register()
        app._register_view.text_username.set("alice")
        app._register_view.text_password.set("pass")
        app._register_view.text_confirm_password.set("pass")
        with patch("src.ui.interface_app.AuthService.register", return_value=False):
            app._register()
        assert app._register_view is not None
        app._register_view.destroy()
        app._register_view = None
