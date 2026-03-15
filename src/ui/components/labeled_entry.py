from tkinter import Entry, Frame, Label, Misc, StringVar

from src.ui.styles import Styles


class LabeledEntry(Frame):
    def __init__(
        self,
        parent: Misc,
        label_text: str,
        styles: Styles,
        variable: StringVar,
        show: str = "",
    ) -> None:
        super().__init__(parent, bg=styles.PRIMARY_COLOR)
        self._styles = styles

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        Label(
            self,
            text=label_text,
            font=self._styles.FONT_ROBOTO_12,
            bg=self._styles.PRIMARY_COLOR,
            fg=self._styles.WHITE_COLOR,
        ).grid(row=0, column=0, padx=(20, 5), sticky="e")

        entry_config = {
            "width": 20,
            "font": self._styles.FONT_ROBOTO_15,
            "bg": self._styles.SECONDARY_COLOR,
            "border": 0,
            "fg": self._styles.WHITE_COLOR,
            "textvariable": variable,
        }

        if show:
            entry_config["show"] = show

        Entry(self, **entry_config).grid(row=0, column=1, padx=(5, 20), sticky="w")
