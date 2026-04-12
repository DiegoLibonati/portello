import tkinter as tk

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
