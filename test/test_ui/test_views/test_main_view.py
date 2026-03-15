from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.main_view import MainView


@pytest.fixture
def main_view(mock_root: MagicMock, mock_styles: MagicMock) -> MainView:
    with (
        patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
        patch("src.ui.views.main_view.Label"),
        patch.object(MainView, "title"),
        patch.object(MainView, "geometry"),
        patch.object(MainView, "resizable"),
        patch.object(MainView, "config"),
        patch.object(MainView, "columnconfigure"),
        patch.object(MainView, "rowconfigure"),
    ):
        instance: MainView = MainView.__new__(MainView)
        instance._styles = mock_styles
        return instance


class TestMainViewInit:
    def test_stores_styles(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label") as mock_label,
            patch.object(MainView, "title"),
            patch.object(MainView, "geometry"),
            patch.object(MainView, "resizable"),
            patch.object(MainView, "config"),
            patch.object(MainView, "columnconfigure"),
            patch.object(MainView, "rowconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="alice")
        assert instance._styles is mock_styles

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label") as mock_label,
            patch.object(MainView, "title") as mock_title,
            patch.object(MainView, "geometry"),
            patch.object(MainView, "resizable"),
            patch.object(MainView, "config"),
            patch.object(MainView, "columnconfigure"),
            patch.object(MainView, "rowconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="alice")
        mock_title.assert_called_once_with("Template Tkinter Program")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label") as mock_label,
            patch.object(MainView, "title"),
            patch.object(MainView, "geometry") as mock_geometry,
            patch.object(MainView, "resizable"),
            patch.object(MainView, "config"),
            patch.object(MainView, "columnconfigure"),
            patch.object(MainView, "rowconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="alice")
        mock_geometry.assert_called_once_with("200x200")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label") as mock_label,
            patch.object(MainView, "title"),
            patch.object(MainView, "geometry"),
            patch.object(MainView, "resizable") as mock_resizable,
            patch.object(MainView, "config"),
            patch.object(MainView, "columnconfigure"),
            patch.object(MainView, "rowconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="alice")
        mock_resizable.assert_called_once_with(False, False)

    def test_background_uses_primary_color(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label") as mock_label,
            patch.object(MainView, "title"),
            patch.object(MainView, "geometry"),
            patch.object(MainView, "resizable"),
            patch.object(MainView, "config") as mock_config,
            patch.object(MainView, "columnconfigure"),
            patch.object(MainView, "rowconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="alice")
        mock_config.assert_called_once_with(bg=mock_styles.PRIMARY_COLOR)

    def test_welcome_label_contains_username(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label") as mock_label,
            patch.object(MainView, "title"),
            patch.object(MainView, "geometry"),
            patch.object(MainView, "resizable"),
            patch.object(MainView, "config"),
            patch.object(MainView, "columnconfigure"),
            patch.object(MainView, "rowconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="alice")
        _, kwargs = mock_label.call_args
        assert "alice" in kwargs.get("text", "")

    def test_columnconfigure_called(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label") as mock_label,
            patch.object(MainView, "title"),
            patch.object(MainView, "geometry"),
            patch.object(MainView, "resizable"),
            patch.object(MainView, "config"),
            patch.object(MainView, "columnconfigure") as mock_col,
            patch.object(MainView, "rowconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="alice")
        mock_col.assert_called_once_with(0, weight=1)

    def test_rowconfigure_called(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label") as mock_label,
            patch.object(MainView, "title"),
            patch.object(MainView, "geometry"),
            patch.object(MainView, "resizable"),
            patch.object(MainView, "config"),
            patch.object(MainView, "columnconfigure"),
            patch.object(MainView, "rowconfigure") as mock_row,
        ):
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="alice")
        mock_row.assert_called_once_with(0, weight=1)
