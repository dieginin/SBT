from flet import Container, Page, Text, alignment


class Settings(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.alignment = alignment.center
        self.content = Text("Settings")
