from tkinter import Button, Label, StringVar, Toplevel

from src.ui.components.labeled_entry import LabeledEntry
from src.ui.styles import Styles


class RegisterView(Toplevel):
    def __init__(self, root, styles: Styles, on_register: callable) -> None:
        super().__init__(root)
        self._styles = styles
        self._on_register = on_register

        self.title("Register")
        self.geometry("400x400")
        self.resizable(False, False)
        self.config(bg=self._styles.PRIMARY_COLOR)

        self.text_confirm = StringVar()
        self.text_username = StringVar()
        self.text_password = StringVar()
        self.text_confirm_password = StringVar()

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

        LabeledEntry(
            parent=self,
            label_text="Confirm password",
            styles=self._styles,
            variable=self.text_confirm_password,
            show="*",
        ).grid(row=2, column=0, pady=5, sticky="ew")

        Label(
            self,
            textvariable=self.text_confirm,
            font=self._styles.FONT_ROBOTO_13,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
        ).grid(row=3, column=0, pady=(20, 10))

        Button(
            self,
            text="Register",
            width=15,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
            command=self._on_register,
        ).grid(row=4, column=0, pady=5)
