from flet import Container, Page, RouteChangeEvent, Row, VerticalDivider, alignment

from components import NavRail
from databases import Location, Staff
from views import *

app = Row(expand=True)
body = Container(expand=True, alignment=alignment.center)
routes = {
    "/": Dashboard,
    "/dsr": DSR,
    "/noconfig": NoConfig,
    "/openclose": OpenClose,
    "/schedule": Schedule,
    "/setschedule": SetSchedule,
    "/settings": Settings,
}


class Router:
    def __init__(self, page: Page):
        self.page = page
        self.page.on_route_change = self.route_change
        self.rail = NavRail(self.page)
        app.controls = [self.rail, VerticalDivider(width=1), body]

        self.initial_route()
        self.page.add(app)

    @property
    def config(self) -> bool:
        return Location().name and Staff().members

    def initial_route(self):
        if not self.config:
            self.rail.selected_index = None
            body.content = routes["/noconfig"](self.page)

    def route_change(self, event: RouteChangeEvent):
        if not self.config and event.route != "/settings":
            self.rail.selected_index = None
            r = "/noconfig"
        else:
            r = event.route
        body.content = routes[r](self.page)
        self.page.update()
