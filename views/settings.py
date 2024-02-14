from flet import Container, Page, Text


class Settings(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.content = Text("Settings")
