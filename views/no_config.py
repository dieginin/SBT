from flet import Container, Page

from components import Alert
from databases import Location, Staff


class NoConfig(Container):
    def __init__(self, page: Page):
        super().__init__()
        location = not Location().name
        staff = not Staff().members
        
        string = f"{"store" if location else ""}{" and " if location & staff else ""}{"staff" if staff else ""}"
        self.content = Alert(
            "manage_accounts_rounded",
            f"First setup {string}\nPlease go to settings",
        )
