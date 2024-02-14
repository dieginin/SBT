from flet import (
    Image,
    NavigationRail,
    NavigationRailDestination,
    NavigationRailLabelType,
    Page,
)

btns = [
    {
        "icon": "dashboard_outlined",
        "selected_icon": "dashboard_rounded",
        "label": "Dashboard",
    },
    {
        "icon": "countertops_outlined",
        "selected_icon": "countertops_rounded",
        "label": "DSR",
    },
    {
        "icon": "access_time",
        "selected_icon": "access_time_filled_outlined",
        "label": "Schedule",
    },
    {
        "icon": "settings_outlined",
        "selected_icon": "settings_rounded",
        "label": "Settings",
    },
]


class NavRail(NavigationRail):
    def __init__(self, page: Page):
        super().__init__()
        dst = ["/", "/dsr", "/schedule", "/settings"]

        self.selected_index = 0
        self.label_type = NavigationRailLabelType.SELECTED
        self.width = 85
        self.leading = Image(f"/SBM_logo.png")
        self.group_alignment = -0.9
        self.destinations = self._destinations()
        self.on_change = lambda e: page.go(dst[e.control.selected_index])

    _destinations = lambda self: [self._btn(**b) for b in btns]
    _btn = lambda _, **b: NavigationRailDestination(**b)
