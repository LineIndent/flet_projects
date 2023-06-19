import flet as ft


class LeftPanel(ft.Container):
    def __init__(
        self,
        expand=1,
        padding=ft.padding.only(top=65),
        content=ft.Column(expand=True, alignment="start"),
    ):
        super().__init__(expand=expand, padding=padding, content=content)

        self.content.controls = []
