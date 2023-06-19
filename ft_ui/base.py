from core.mobile_drop_down import MobileDropDownNavigation
from core.mobile_navigation import MobileNavigation
from core.middle_panel import MiddlePanel
from core.right_panel import RightPanel
from core.navigation import Navigation
from core.left_panel import LeftPanel
from core.header import Header
from core.drawer import Drawer

import flet as ft


class FxControls(ft.UserControl):
    def __init__(self, page: ft.Page, docs: dict, fx_controls: list, fx_rail: list):
        self.page = page
        self.docs = docs

        self.fx_controls = fx_controls
        self.fx_rail = fx_rail

        self.fx_stack = ft.Stack(expand=True)
        self.fx_row = ft.Row(expand=True, spacing=2)

        self.fx_drawer = Drawer(docs=self.docs, page=self.page)

        self.fx_max_nav = Navigation(
            page=self.page, docs=self.docs, function=lambda e: self.set_app_router(e)
        )
        self.fx_min_nav = MobileNavigation(on_click=lambda e: self.set_fx_drawer(e))

        self.fx_header = Header(
            docs=self.docs, full_nav=self.fx_max_nav, mobile_nav=self.fx_min_nav
        )

        self.fx_left = LeftPanel()
        self.fx_middle = MiddlePanel(
            controls=self.fx_controls,
            function=[
                self.set_fx_header,
                self.set_header_navigation_row,
                self.fx_header.set_header_name,
            ],
            page=self.page,
            header_name=self.fx_header,
        )
        self.fx_right = RightPanel(middle_panel=self.fx_middle, fx_rail=self.fx_rail)

        self.fx_drop_down = MobileDropDownNavigation(
            "On this page ...", len(self.fx_rail), self.fx_rail, self.fx_middle
        )
        self.fx_middle.controls.insert(1, self.fx_drop_down)

        super().__init__()

    # Method: Responsive method to set the UI for 'mobile/tablet' screens ...
    def set_application_to_mobile(self):
        self.set_fx_max_nav(0, False)
        self.set_fx_left(False)
        self.set_fx_right(False)

        self.set_fx_min_nav(True)

        if self.fx_drop_down.max_height != 0:
            self.set_fx_drop_down(True)
        else:
            self.set_fx_drop_down(False)

        self.set_fx_header(60)
        self.set_header_repo_opacity(0, False)
        self.set_header_navigation_row(0, False)

        self.update()

    # Method: Responsive method to set the UI for 'desktop' screens ...
    def set_application_to_desktop(self):
        self.set_fx_left(True)
        self.set_fx_right(True)
        self.set_fx_max_nav(1, True)

        self.set_fx_min_nav(False)
        self.set_fx_drop_down(False)

        self.set_fx_header(90)
        self.set_header_repo_opacity(1, True)
        self.set_header_navigation_row(1, True)

        self.update()

    # Method: sets the state of the header with animations ...
    def set_header_navigation_row(self, value: int, state: bool):
        self.fx_header.navigation.opacity = value
        self.fx_header.navigation.visible = state
        self.fx_header.navigation.update()

    def set_header_repo_opacity(self, value: int, state: bool):
        self.fx_header.repo.controls[1].opacity = value
        self.fx_header.repo.controls[1].visible = state
        self.fx_header.repo.update()

    def set_fx_header(self, height: int):
        self.fx_header.height = height
        self.fx_header.update()

    def set_fx_drop_down(self, state: bool):
        self.fx_drop_down.visible = state

    def set_fx_max_nav(self, value: int, state: bool):
        self.fx_max_nav.opacity = value
        self.fx_max_nav.update()

        self.fx_max_nav.visible = state
        self.fx_max_nav.update()

    def set_fx_min_nav(self, state: bool):
        self.fx_min_nav.visible = state
        self.fx_min_nav.update()

    def set_fx_left(self, state: bool):
        self.fx_left.visible = state
        self.fx_left.update()

    def set_fx_right(self, state: bool):
        self.fx_right.visible = state
        self.fx_right.update()

    def set_fx_drawer(self, e):
        if self.fx_drawer.width != 220:
            self.show_fx_drawer()
        else:
            self.hide_fx_drawer()

    def show_fx_drawer(self):
        self.fx_drawer.width = 220
        self.fx_drawer.shadow = ft.BoxShadow(
            blur_radius=15,
            spread_radius=8,
            color=ft.colors.with_opacity(0.25, "black"),
            offset=(4, 4),
        )
        self.fx_drawer.update()

        self.fx_drawer.content.opacity = 1
        self.fx_drawer.update()

    def hide_fx_drawer(self):
        self.fx_drawer.content.opacity = 0
        self.fx_drawer.update()

        self.fx_drawer.width = 0
        self.fx_drawer.shadow = None
        self.fx_drawer.update()

    def build(self):
        self.fx_row.controls = [self.fx_left, self.fx_middle, self.fx_right]
        self.fx_stack.controls = [self.fx_row, self.fx_header, self.fx_drawer]

        return self.fx_stack
