from flet import Container, Page, Text


class SetSchedule(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.content = Text("SetSchedule")
