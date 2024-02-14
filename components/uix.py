from flet import FontWeight, Text, TextAlign


class Title(Text):
    def __init__(
        self,
        value: str | None = None,
        size: int = 42,
        color: str = "outline",
    ):
        super().__init__()

        self.value = value
        self.color = color
        self.size = size
        self.text_align = TextAlign.CENTER
        self.weight = FontWeight.W_100
