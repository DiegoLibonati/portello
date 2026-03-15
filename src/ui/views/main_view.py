from tkinter import Label, Toplevel

from src.ui.styles import Styles


class MainView(Toplevel):
    def __init__(self, root, styles: Styles, username: str) -> None:
        super().__init__(root)
        self._styles = styles

        self.title("Template Tkinter Program")
        self.geometry("200x200")
        self.resizable(False, False)
        self.config(bg=self._styles.PRIMARY_COLOR)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        Label(
            self,
            text=f"Welcome {username}",
            font=self._styles.FONT_ROBOTO_13,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
        ).grid(row=0, column=0, padx=20, pady=20)
