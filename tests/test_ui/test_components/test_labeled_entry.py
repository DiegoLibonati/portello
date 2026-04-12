import tkinter as tk
from tkinter import StringVar

from src.ui.components.labeled_entry import LabeledEntry
from src.ui.styles import Styles


class TestLabeledEntry:
    def test_instantiation(self, root: tk.Tk) -> None:
        var: StringVar = StringVar(root)
        widget: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Test Label",
            styles=Styles(),
            variable=var,
        )
        assert widget is not None
        widget.destroy()

    def test_variable_initial_empty(self, root: tk.Tk) -> None:
        var: StringVar = StringVar(root)
        widget: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Label",
            styles=Styles(),
            variable=var,
        )
        assert var.get() == ""
        widget.destroy()

    def test_variable_with_initial_value_is_preserved(self, root: tk.Tk) -> None:
        var: StringVar = StringVar(root, value="hello")
        widget: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Label",
            styles=Styles(),
            variable=var,
        )
        assert var.get() == "hello"
        widget.destroy()

    def test_variable_set_updates_value(self, root: tk.Tk) -> None:
        var: StringVar = StringVar(root)
        widget: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Label",
            styles=Styles(),
            variable=var,
        )
        var.set("updated")
        assert var.get() == "updated"
        widget.destroy()

    def test_instantiation_with_show_parameter(self, root: tk.Tk) -> None:
        var: StringVar = StringVar(root)
        widget: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Password",
            styles=Styles(),
            variable=var,
            show="*",
        )
        assert widget is not None
        widget.destroy()

    def test_background_color_matches_styles(self, root: tk.Tk) -> None:
        var: StringVar = StringVar(root)
        styles: Styles = Styles()
        widget: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Label",
            styles=styles,
            variable=var,
        )
        assert widget.cget("bg") == styles.PRIMARY_COLOR
        widget.destroy()

    def test_instantiation_without_show_does_not_raise(self, root: tk.Tk) -> None:
        var: StringVar = StringVar(root)
        widget: LabeledEntry = LabeledEntry(
            parent=root,
            label_text="Username",
            styles=Styles(),
            variable=var,
            show="",
        )
        assert widget is not None
        widget.destroy()
