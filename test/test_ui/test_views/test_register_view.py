from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.register_view import RegisterView


@pytest.fixture
def register_view(mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> RegisterView:
    with (
        patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
        patch("src.ui.views.register_view.LabeledEntry"),
        patch("src.ui.views.register_view.Label"),
        patch("src.ui.views.register_view.Button"),
        patch("src.ui.views.register_view.StringVar"),
        patch.object(RegisterView, "title"),
        patch.object(RegisterView, "geometry"),
        patch.object(RegisterView, "resizable"),
        patch.object(RegisterView, "config"),
        patch.object(RegisterView, "columnconfigure"),
    ):
        instance: RegisterView = RegisterView.__new__(RegisterView)
        instance._styles = mock_styles
        instance._on_register = on_register
        instance.text_confirm = MagicMock(spec=StringVar)
        instance.text_username = MagicMock(spec=StringVar)
        instance.text_password = MagicMock(spec=StringVar)
        instance.text_confirm_password = MagicMock(spec=StringVar)
        return instance


class TestRegisterViewInit:
    def test_stores_styles(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        with (
            patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.register_view.LabeledEntry") as mock_le,
            patch("src.ui.views.register_view.Label"),
            patch("src.ui.views.register_view.Button"),
            patch("src.ui.views.register_view.StringVar"),
            patch.object(RegisterView, "title"),
            patch.object(RegisterView, "geometry"),
            patch.object(RegisterView, "resizable"),
            patch.object(RegisterView, "config"),
            patch.object(RegisterView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            instance: RegisterView = RegisterView.__new__(RegisterView)
            RegisterView.__init__(instance, root=mock_root, styles=mock_styles, on_register=on_register)
        assert instance._styles is mock_styles

    def test_stores_on_register(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        with (
            patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.register_view.LabeledEntry") as mock_le,
            patch("src.ui.views.register_view.Label"),
            patch("src.ui.views.register_view.Button"),
            patch("src.ui.views.register_view.StringVar"),
            patch.object(RegisterView, "title"),
            patch.object(RegisterView, "geometry"),
            patch.object(RegisterView, "resizable"),
            patch.object(RegisterView, "config"),
            patch.object(RegisterView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            instance: RegisterView = RegisterView.__new__(RegisterView)
            RegisterView.__init__(instance, root=mock_root, styles=mock_styles, on_register=on_register)
        assert instance._on_register is on_register

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        with (
            patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.register_view.LabeledEntry") as mock_le,
            patch("src.ui.views.register_view.Label"),
            patch("src.ui.views.register_view.Button"),
            patch("src.ui.views.register_view.StringVar"),
            patch.object(RegisterView, "title") as mock_title,
            patch.object(RegisterView, "geometry"),
            patch.object(RegisterView, "resizable"),
            patch.object(RegisterView, "config"),
            patch.object(RegisterView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            instance: RegisterView = RegisterView.__new__(RegisterView)
            RegisterView.__init__(instance, root=mock_root, styles=mock_styles, on_register=on_register)
        mock_title.assert_called_once_with("Register")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        with (
            patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.register_view.LabeledEntry") as mock_le,
            patch("src.ui.views.register_view.Label"),
            patch("src.ui.views.register_view.Button"),
            patch("src.ui.views.register_view.StringVar"),
            patch.object(RegisterView, "title"),
            patch.object(RegisterView, "geometry") as mock_geometry,
            patch.object(RegisterView, "resizable"),
            patch.object(RegisterView, "config"),
            patch.object(RegisterView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            instance: RegisterView = RegisterView.__new__(RegisterView)
            RegisterView.__init__(instance, root=mock_root, styles=mock_styles, on_register=on_register)
        mock_geometry.assert_called_once_with("400x400")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        with (
            patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.register_view.LabeledEntry") as mock_le,
            patch("src.ui.views.register_view.Label"),
            patch("src.ui.views.register_view.Button"),
            patch("src.ui.views.register_view.StringVar"),
            patch.object(RegisterView, "title"),
            patch.object(RegisterView, "geometry"),
            patch.object(RegisterView, "resizable") as mock_resizable,
            patch.object(RegisterView, "config"),
            patch.object(RegisterView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            instance: RegisterView = RegisterView.__new__(RegisterView)
            RegisterView.__init__(instance, root=mock_root, styles=mock_styles, on_register=on_register)
        mock_resizable.assert_called_once_with(False, False)

    def test_three_labeled_entries_are_created(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        with (
            patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.register_view.LabeledEntry") as mock_le,
            patch("src.ui.views.register_view.Label"),
            patch("src.ui.views.register_view.Button"),
            patch("src.ui.views.register_view.StringVar"),
            patch.object(RegisterView, "title"),
            patch.object(RegisterView, "geometry"),
            patch.object(RegisterView, "resizable"),
            patch.object(RegisterView, "config"),
            patch.object(RegisterView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            instance: RegisterView = RegisterView.__new__(RegisterView)
            RegisterView.__init__(instance, root=mock_root, styles=mock_styles, on_register=on_register)
        assert mock_le.call_count == 3

    def test_password_entries_have_show(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        with (
            patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.register_view.LabeledEntry") as mock_le,
            patch("src.ui.views.register_view.Label"),
            patch("src.ui.views.register_view.Button"),
            patch("src.ui.views.register_view.StringVar"),
            patch.object(RegisterView, "title"),
            patch.object(RegisterView, "geometry"),
            patch.object(RegisterView, "resizable"),
            patch.object(RegisterView, "config"),
            patch.object(RegisterView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            instance: RegisterView = RegisterView.__new__(RegisterView)
            RegisterView.__init__(instance, root=mock_root, styles=mock_styles, on_register=on_register)
        password_calls = [c for c in mock_le.call_args_list if c[1].get("show") == "*"]
        assert len(password_calls) == 2

    def test_register_button_command_is_on_register(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        with (
            patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.register_view.LabeledEntry") as mock_le,
            patch("src.ui.views.register_view.Label"),
            patch("src.ui.views.register_view.Button") as mock_button,
            patch("src.ui.views.register_view.StringVar"),
            patch.object(RegisterView, "title"),
            patch.object(RegisterView, "geometry"),
            patch.object(RegisterView, "resizable"),
            patch.object(RegisterView, "config"),
            patch.object(RegisterView, "columnconfigure"),
        ):
            mock_le.return_value.grid = MagicMock()
            mock_button.return_value.grid = MagicMock()
            instance: RegisterView = RegisterView.__new__(RegisterView)
            RegisterView.__init__(instance, root=mock_root, styles=mock_styles, on_register=on_register)
        _, kwargs = mock_button.call_args
        assert kwargs.get("command") is on_register
