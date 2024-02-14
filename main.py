from flet import Page, Theme, app

from router import Router


class Main:
    def __init__(self, page: Page):
        super().__init__()

        page.title = "Scrubs Boutique Tools"
        page.window_min_height = 600
        page.window_min_width = 800
        page.theme = Theme(color_scheme_seed="lightgreen")

        Router(page)


app(Main)
