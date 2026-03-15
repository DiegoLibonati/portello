from unittest.mock import MagicMock, patch

import pytest

from src.ui.components.labeled_entry import LabeledEntry


@pytest.fixture
def labeled_entry(mock_styles: MagicMock, variable: MagicMock) -> LabeledEntry:
    with (
        patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
        patch("src.ui.components.labeled_entry.Label"),
        patch("src.ui.components.labeled_entry.Entry"),
        patch.object(LabeledEntry, "columnconfigure"),
    ):
        instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
        instance._styles = mock_styles
        return instance


@pytest.fixture
def labeled_entry_with_show(mock_styles: MagicMock, variable: MagicMock) -> LabeledEntry:
    with (
        patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
        patch("src.ui.components.labeled_entry.Label"),
        patch("src.ui.components.labeled_entry.Entry"),
        patch.object(LabeledEntry, "columnconfigure"),
    ):
        instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
        instance._styles = mock_styles
        return instance


class TestLabeledEntryInit:
    def test_stores_styles(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label"),
            patch("src.ui.components.labeled_entry.Entry"),
            patch.object(LabeledEntry, "columnconfigure"),
        ):
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            instance.__init__ = MagicMock()
            with patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None):
                LabeledEntry.__init__(instance, parent=MagicMock(), label_text="Name", styles=mock_styles, variable=variable)
        assert instance._styles is mock_styles

    def test_columnconfigure_called_twice(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label"),
            patch("src.ui.components.labeled_entry.Entry"),
            patch.object(LabeledEntry, "columnconfigure") as mock_col,
        ):
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            LabeledEntry.__init__(instance, parent=MagicMock(), label_text="Name", styles=mock_styles, variable=variable)
        assert mock_col.call_count == 2

    def test_label_created_with_label_text(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label") as mock_label,
            patch("src.ui.components.labeled_entry.Entry"),
            patch.object(LabeledEntry, "columnconfigure"),
        ):
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            LabeledEntry.__init__(instance, parent=MagicMock(), label_text="Username", styles=mock_styles, variable=variable)
        _, kwargs = mock_label.call_args
        assert kwargs.get("text") == "Username"

    def test_entry_created_with_textvariable(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label"),
            patch("src.ui.components.labeled_entry.Entry") as mock_entry,
            patch.object(LabeledEntry, "columnconfigure"),
        ):
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            LabeledEntry.__init__(instance, parent=MagicMock(), label_text="Name", styles=mock_styles, variable=variable)
        _, kwargs = mock_entry.call_args
        assert kwargs.get("textvariable") is variable

    def test_entry_created_without_show_by_default(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label"),
            patch("src.ui.components.labeled_entry.Entry") as mock_entry,
            patch.object(LabeledEntry, "columnconfigure"),
        ):
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            LabeledEntry.__init__(instance, parent=MagicMock(), label_text="Name", styles=mock_styles, variable=variable)
        _, kwargs = mock_entry.call_args
        assert "show" not in kwargs

    def test_entry_created_with_show_when_provided(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label"),
            patch("src.ui.components.labeled_entry.Entry") as mock_entry,
            patch.object(LabeledEntry, "columnconfigure"),
        ):
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            LabeledEntry.__init__(instance, parent=MagicMock(), label_text="Password", styles=mock_styles, variable=variable, show="*")
        _, kwargs = mock_entry.call_args
        assert kwargs.get("show") == "*"

    def test_label_uses_primary_color_bg(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label") as mock_label,
            patch("src.ui.components.labeled_entry.Entry"),
            patch.object(LabeledEntry, "columnconfigure"),
        ):
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            LabeledEntry.__init__(instance, parent=MagicMock(), label_text="Name", styles=mock_styles, variable=variable)
        _, kwargs = mock_label.call_args
        assert kwargs.get("bg") == mock_styles.PRIMARY_COLOR

    def test_entry_uses_secondary_color_bg(self, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label"),
            patch("src.ui.components.labeled_entry.Entry") as mock_entry,
            patch.object(LabeledEntry, "columnconfigure"),
        ):
            instance: LabeledEntry = LabeledEntry.__new__(LabeledEntry)
            LabeledEntry.__init__(instance, parent=MagicMock(), label_text="Name", styles=mock_styles, variable=variable)
        _, kwargs = mock_entry.call_args
        assert kwargs.get("bg") == mock_styles.SECONDARY_COLOR
