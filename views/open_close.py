from flet import Container, Page, Text


class OpenClose(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.content = Text("OpenClose")
