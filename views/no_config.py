from flet import Container, Page

from components import Alert


class NoConfig(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.content = Alert(
            "manage_accounts_rounded",
            "First setup store and/or staff\nPlease go to settings",
        )
