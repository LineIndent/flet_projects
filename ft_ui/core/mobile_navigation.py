import flet as ft


class MobileNavigation(ft.IconButton):
    def __init__(
        self,
        icon=ft.icons.MENU_SHARP,
        visible=False,
        icon_size=14,
        icon_color="white",
        on_click=callable,
    ):
        super().__init__(
            icon=icon,
            visible=visible,
            icon_size=icon_size,
            icon_color=icon_color,
            on_click=on_click,
        )
