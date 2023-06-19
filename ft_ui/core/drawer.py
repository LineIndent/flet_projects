import flet as ft
from core.repo_data import RepoData


class Drawer(ft.Container):
    def __init__(
        self,
        docs: dict,
        page: ft.Page,
        expand=True,
        width=0,
        bgcolor="#23262d",
        shadow=None,
        animate=ft.Animation(550, "ease"),
        content=ft.Column(
            expand=True,
            opacity=0,
            spacing=0,
            animate_opacity=ft.Animation(100, "ease"),
        ),
    ):
        self.page = page
        self.docs = docs
        self.repo = RepoData(self.docs)

        url = self.docs["repo-url"]
        background_color = self.docs["theme"][0]["bgcolor"]
        primary = self.docs["theme"][1]["primary"]

        super().__init__(
            expand=expand,
            width=width,
            bgcolor=bgcolor,
            shadow=shadow,
            animate=animate,
            content=content,
        )

        self.content.controls = [
            ft.Container(
                bgcolor=background_color,
                height=60,
                padding=ft.padding.only(left=14),
                content=ft.Row(
                    alignment="start",
                    controls=[
                        ft.Text(
                            # start #
'Flet Material UI',# end #
                            size=19,
                            weight="w700",
                        )
                    ],
                ),
            ),
            ft.Container(
                padding=ft.padding.only(left=14),
                bgcolor=primary,
                height=45,
                on_click=lambda __: self.page.launch_url(url=url),
                content=ft.Tooltip(
                    padding=10,
                    vertical_offset=30,
                    message="Go to repository",
                    bgcolor="#20222c",
                    text_style=ft.TextStyle(color="white", size=9),
                    content=self.repo,
                ),
            ),
        ]
