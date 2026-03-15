from tkinter import CENTER

from src.ui.styles import Styles


class TestStyles:
    def test_primary_color(self) -> None:
        assert Styles.PRIMARY_COLOR == "#141B41"

    def test_secondary_color(self) -> None:
        assert Styles.SECONDARY_COLOR == "#306BAC"

    def test_white_color(self) -> None:
        assert Styles.WHITE_COLOR == "#FFFFFF"

    def test_font_roboto_base(self) -> None:
        assert Styles.FONT_ROBOTO == "Roboto"

    def test_font_roboto_12(self) -> None:
        assert Styles.FONT_ROBOTO_12 == "Roboto 12"

    def test_font_roboto_13(self) -> None:
        assert Styles.FONT_ROBOTO_13 == "Roboto 13"

    def test_font_roboto_15(self) -> None:
        assert Styles.FONT_ROBOTO_15 == "Roboto 15"

    def test_anchor_center(self) -> None:
        assert Styles.ANCHOR_CENTER == CENTER

    def test_instantiation(self) -> None:
        assert isinstance(Styles(), Styles)
