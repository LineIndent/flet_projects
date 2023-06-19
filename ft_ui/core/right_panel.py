import flet as ft
from utilities.rail import create_rail


class RightPanel(ft.Container):
    def __init__(
        self,
        middle_panel: ft.Container,
        fx_rail: list,
        expand=1,
        padding=ft.padding.only(top=65),
        content=ft.Column(expand=True, alignment="start"),
    ):
        super().__init__(
            expand=expand,
            padding=padding,
            content=content,
        )

        self.middle_panel = middle_panel
        self.fx_rail = fx_rail

        self.content.controls = create_rail(
            number=len(self.fx_rail),
            title=self.fx_rail,
            funcOne=[
                (
                    lambda i: lambda __: self.middle_panel.content.scroll_to(
                        key=str(i), duration=500
                    )
                )(i)
                for i in range(1, (len(self.fx_rail) + 1))
            ],
            funcTwo=[
                lambda e: self.rail_hover_color(e) for __ in range(len(self.fx_rail))
            ],
        )

    def rail_hover_color(self, e):
        if e.data == "true":
            e.control.content.color = "white"

        else:
            e.control.content.color = ft.colors.with_opacity(0.55, "white10")

        e.control.content.update()
