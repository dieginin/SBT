from typing import List

from flet import Column, Control, CrossAxisAlignment, Icon, MainAxisAlignment, Row

from .uix import Title


class Mrow(Row):
    def __init__(
        self,
        controls: List[Control] | None = None,
        alignment: MainAxisAlignment = MainAxisAlignment.SPACE_EVENLY,
        vertical_alignment: CrossAxisAlignment = CrossAxisAlignment.CENTER,
    ):
        super().__init__()

        self.controls = controls
        self.alignment = alignment
        self.vertical_alignment = vertical_alignment


class Mcol(Column):
    def __init__(
        self,
        controls: List[Control] | None = None,
        alignment: MainAxisAlignment = MainAxisAlignment.CENTER,
        horizontal_alignment: CrossAxisAlignment = CrossAxisAlignment.CENTER,
    ):
        super().__init__()

        self.controls = controls
        self.alignment = alignment
        self.horizontal_alignment = horizontal_alignment


class Alert(Mcol):
    def __init__(self, icon: str, text: str):
        super().__init__()

        self.controls = [
            Icon(icon, size=125, color="outline"),
            Title(text),
        ]
