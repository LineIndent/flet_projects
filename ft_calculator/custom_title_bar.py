from flet import (
    UserControl,
    Row,
    Container,
    border_radius,
    colors,
)


class CustomTitleBar(UserControl):
    def build(self):
        return Container(
            content=Row(
                spacing=7,
                controls=[
                    Container(
                        width=12,
                        height=12,
                        bgcolor=colors.RED_400,
                        border_radius=border_radius.all(20),
                        on_click=lambda e: e.page.window_close(),
                    ),
                    Container(
                        width=12,
                        height=12,
                        bgcolor=colors.YELLOW_500,
                        border_radius=border_radius.all(20),
                    ),
                    Container(
                        width=12,
                        height=12,
                        bgcolor=colors.GREEN_400,
                        border_radius=border_radius.all(20),
                    ),
                ],
            )
        )
