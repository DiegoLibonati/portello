from tkinter import CENTER

from src.ui.styles import Styles


class TestStyles:
    def test_primary_color(self) -> None:
        assert Styles.PRIMARY_COLOR == "#141B41"

    def test_secondary_color(self) -> None:
        assert Styles.SECONDARY_COLOR == "#306BAC"

    def test_white_color(self) -> None:
        assert Styles.WHITE_COLOR == "#FFFFFF"

    def test_font_roboto(self) -> None:
        assert Styles.FONT_ROBOTO == "Roboto"

    def test_font_roboto_12_contains_size(self) -> None:
        assert "12" in Styles.FONT_ROBOTO_12

    def test_font_roboto_13_contains_size(self) -> None:
        assert "13" in Styles.FONT_ROBOTO_13

    def test_font_roboto_15_contains_size(self) -> None:
        assert "15" in Styles.FONT_ROBOTO_15

    def test_font_roboto_12_contains_font_name(self) -> None:
        assert Styles.FONT_ROBOTO in Styles.FONT_ROBOTO_12

    def test_font_roboto_13_contains_font_name(self) -> None:
        assert Styles.FONT_ROBOTO in Styles.FONT_ROBOTO_13

    def test_font_roboto_15_contains_font_name(self) -> None:
        assert Styles.FONT_ROBOTO in Styles.FONT_ROBOTO_15

    def test_anchor_center_equals_tkinter_center(self) -> None:
        assert Styles.ANCHOR_CENTER == CENTER

    def test_colors_are_hex_strings(self) -> None:
        for color in [Styles.PRIMARY_COLOR, Styles.SECONDARY_COLOR, Styles.WHITE_COLOR]:
            assert color.startswith("#")
            assert len(color) == 7
