from unittest.mock import MagicMock, patch

import pytest

from src.models.user_model import UserModel
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock) -> InterfaceApp:
    with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
        mock_login_view: MagicMock = MagicMock()
        mock_login_view.pack = MagicMock()
        mock_login_view_class.return_value = mock_login_view
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance.user = None
        instance._styles = mock_styles
        instance._root = mock_root
        instance._config = MagicMock()
        instance._login_view = mock_login_view
        return instance


class TestInterfaceAppInit:
    def test_user_initial_value_is_none(self, interface_app: InterfaceApp) -> None:
        assert interface_app.user is None

    def test_stores_styles(self, interface_app: InterfaceApp, mock_styles: MagicMock) -> None:
        assert interface_app._styles is mock_styles

    def test_stores_root(self, interface_app: InterfaceApp, mock_root: MagicMock) -> None:
        assert interface_app._root is mock_root

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
            mock_login_view_class.return_value.pack = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.title.assert_called_once_with("Template Tkinter")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
            mock_login_view_class.return_value.pack = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.geometry.assert_called_once_with("400x400")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
            mock_login_view_class.return_value.pack = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.resizable.assert_called_once_with(False, False)

    def test_background_uses_primary_color(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
            mock_login_view_class.return_value.pack = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_root.config.assert_called_once_with(background=mock_styles.PRIMARY_COLOR)

    def test_default_styles_is_styles_instance(self, mock_root: MagicMock) -> None:
        with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
            mock_login_view_class.return_value.pack = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock())
        assert isinstance(app._styles, Styles)

    def test_login_view_receives_callbacks(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
            mock_login_view_class.return_value.pack = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        _, kwargs = mock_login_view_class.call_args
        assert callable(kwargs.get("on_login"))
        assert callable(kwargs.get("on_register"))

    def test_login_view_pack_called(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
            mock_login_view: MagicMock = MagicMock()
            mock_login_view_class.return_value = mock_login_view
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)
        mock_login_view.pack.assert_called_once_with(fill="both", expand=True)


class TestInterfaceAppUsernameProperty:
    def test_returns_username_when_user_is_set(self, interface_app: InterfaceApp) -> None:
        interface_app.user = UserModel(username="alice", password="hashed")
        assert interface_app.username == "alice"

    def test_returns_na_when_user_is_none(self, interface_app: InterfaceApp) -> None:
        interface_app.user = None
        assert interface_app.username == "N/A"


class TestInterfaceAppLogin:
    def test_user_is_set_on_successful_login(self, interface_app: InterfaceApp) -> None:
        interface_app._login_view.text_username.get.return_value = "alice"
        interface_app._login_view.text_password.get.return_value = "pass"
        mock_user: UserModel = UserModel(username="alice", password="hashed")

        with (
            patch("src.ui.interface_app.AuthService.login", return_value=mock_user),
            patch("src.ui.interface_app.MainView"),
        ):
            interface_app._login()

        assert interface_app.user is mock_user

    def test_main_view_created_on_successful_login(self, interface_app: InterfaceApp) -> None:
        interface_app._login_view.text_username.get.return_value = "alice"
        interface_app._login_view.text_password.get.return_value = "pass"
        mock_user: UserModel = UserModel(username="alice", password="hashed")

        with (
            patch("src.ui.interface_app.AuthService.login", return_value=mock_user),
            patch("src.ui.interface_app.MainView") as mock_main_view,
        ):
            interface_app._login()

        mock_main_view.assert_called_once()

    def test_main_view_receives_username(self, interface_app: InterfaceApp) -> None:
        interface_app._login_view.text_username.get.return_value = "alice"
        interface_app._login_view.text_password.get.return_value = "pass"
        mock_user: UserModel = UserModel(username="alice", password="hashed")

        with (
            patch("src.ui.interface_app.AuthService.login", return_value=mock_user),
            patch("src.ui.interface_app.MainView") as mock_main_view,
        ):
            interface_app._login()

        _, kwargs = mock_main_view.call_args
        assert kwargs.get("username") == "alice"

    def test_auth_service_called_with_credentials(self, interface_app: InterfaceApp) -> None:
        interface_app._login_view.text_username.get.return_value = "alice"
        interface_app._login_view.text_password.get.return_value = "pass"
        mock_user: UserModel = UserModel(username="alice", password="hashed")

        with (
            patch("src.ui.interface_app.AuthService.login", return_value=mock_user) as mock_login,
            patch("src.ui.interface_app.MainView"),
        ):
            interface_app._login()

        mock_login.assert_called_once_with(username="alice", password="pass")

    def test_raises_when_auth_service_raises(self, interface_app: InterfaceApp) -> None:
        interface_app._login_view.text_username.get.return_value = ""
        interface_app._login_view.text_password.get.return_value = ""

        with (
            patch("src.ui.interface_app.AuthService.login", side_effect=ValidationDialogError(message="err")),
            pytest.raises(ValidationDialogError),
        ):
            interface_app._login()


class TestInterfaceAppOpenRegister:
    def test_register_view_is_created(self, interface_app: InterfaceApp) -> None:
        with patch("src.ui.interface_app.RegisterView") as mock_register_view:
            interface_app._open_register()
        mock_register_view.assert_called_once()

    def test_register_view_receives_on_register(self, interface_app: InterfaceApp) -> None:
        with patch("src.ui.interface_app.RegisterView") as mock_register_view:
            interface_app._open_register()
        _, kwargs = mock_register_view.call_args
        assert callable(kwargs.get("on_register"))

    def test_register_view_receives_root(self, interface_app: InterfaceApp, mock_root: MagicMock) -> None:
        with patch("src.ui.interface_app.RegisterView") as mock_register_view:
            interface_app._open_register()
        _, kwargs = mock_register_view.call_args
        assert kwargs.get("root") is mock_root


class TestInterfaceAppRegister:
    def test_register_view_destroyed_on_success(self, interface_app: InterfaceApp) -> None:
        mock_register_view: MagicMock = MagicMock()
        interface_app._register_view = mock_register_view
        mock_register_view.text_username.get.return_value = "newuser"
        mock_register_view.text_password.get.return_value = "pass123"
        mock_register_view.text_confirm_password.get.return_value = "pass123"

        with patch("src.ui.interface_app.AuthService.register", return_value=True):
            interface_app._register()

        mock_register_view.destroy.assert_called_once()

    def test_register_view_not_destroyed_when_register_returns_false(self, interface_app: InterfaceApp) -> None:
        mock_register_view: MagicMock = MagicMock()
        interface_app._register_view = mock_register_view
        mock_register_view.text_username.get.return_value = "newuser"
        mock_register_view.text_password.get.return_value = "pass123"
        mock_register_view.text_confirm_password.get.return_value = "pass123"

        with patch("src.ui.interface_app.AuthService.register", return_value=False):
            interface_app._register()

        mock_register_view.destroy.assert_not_called()

    def test_auth_service_called_with_register_view_fields(self, interface_app: InterfaceApp) -> None:
        mock_register_view: MagicMock = MagicMock()
        interface_app._register_view = mock_register_view
        mock_register_view.text_username.get.return_value = "newuser"
        mock_register_view.text_password.get.return_value = "pass123"
        mock_register_view.text_confirm_password.get.return_value = "pass123"

        with patch("src.ui.interface_app.AuthService.register", return_value=True) as mock_register:
            interface_app._register()

        mock_register.assert_called_once_with(
            username="newuser",
            password="pass123",
            confirm_password="pass123",
        )

    def test_raises_when_auth_service_raises(self, interface_app: InterfaceApp) -> None:
        mock_register_view: MagicMock = MagicMock()
        interface_app._register_view = mock_register_view
        mock_register_view.text_username.get.return_value = ""
        mock_register_view.text_password.get.return_value = ""
        mock_register_view.text_confirm_password.get.return_value = ""

        with (
            patch("src.ui.interface_app.AuthService.register", side_effect=ValidationDialogError(message="err")),
            pytest.raises(ValidationDialogError),
        ):
            interface_app._register()
