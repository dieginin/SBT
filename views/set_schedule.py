from flet import Container, Page, Text, alignment


class SetSchedule(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.alignment = alignment.center
        self.content = Text("SetSchedule")
