import tkinter as tk

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class TestMainView:
    def test_instantiation(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), username="alice")
        assert view is not None
        view.destroy()

    def test_title(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), username="alice")
        assert view.title() == "Template Tkinter Program"
        view.destroy()

    def test_resizable_is_false(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), username="alice")
        assert view.resizable() == (False, False)
        view.destroy()

    def test_background_color_matches_styles(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, username="alice")
        assert view.cget("bg") == styles.PRIMARY_COLOR
        view.destroy()

    def test_instantiation_with_different_username(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), username="bob")
        assert view is not None
        view.destroy()
