from tkinter import Button, Frame, Label, StringVar, Tk

from src.ui.components.labeled_entry import LabeledEntry
from src.ui.styles import Styles


class LoginView(Frame):
    def __init__(self, root: Tk, styles: Styles, on_login: callable, on_register: callable) -> None:
        super().__init__(root, bg=styles.PRIMARY_COLOR)
        self._styles = styles
        self._on_login = on_login
        self._on_register = on_register

        self.text_confirm = StringVar(value="Welcome")
        self.text_username = StringVar()
        self.text_password = StringVar()

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.columnconfigure(0, weight=1)

        LabeledEntry(
            parent=self,
            label_text="Username",
            styles=self._styles,
            variable=self.text_username,
        ).grid(row=0, column=0, pady=(20, 5), sticky="ew")

        LabeledEntry(
            parent=self,
            label_text="Password",
            styles=self._styles,
            variable=self.text_password,
            show="*",
        ).grid(row=1, column=0, pady=5, sticky="ew")

        Label(
            self,
            textvariable=self.text_confirm,
            font=self._styles.FONT_ROBOTO_13,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
        ).grid(row=2, column=0, pady=(20, 10))

        Button(
            self,
            text="Login",
            width=15,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
            command=self._on_login,
        ).grid(row=3, column=0, pady=5)

        Button(
            self,
            text="Register",
            width=15,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
            command=self._on_register,
        ).grid(row=4, column=0, pady=5)
