import flet as ft
import asyncio


class CodeBlock(ft.UserControl):
    def __init__(self, title):
        #
        self.title = title

        #
        self._hovered: bool | None = None

        self.copy_box = ft.Container(
            width=28,
            height=28,
            border=ft.border.all(1, "transparent"),
            right=1,
            top=1,
            border_radius=7,
            scale=ft.Scale(1),
            animate=ft.Animation(400, "ease"),
            alignment=ft.alignment.center,
            content=ft.Icon(
                name=ft.icons.COPY,
                size=14,
                color="white12",
                opacity=0,
                animate_opacity=ft.Animation(420, "ease"),
            ),
            on_click=lambda e: asyncio.run(self.get_copy_box_content(e)),
        )

        super().__init__()

    async def get_copy_box_content(self, e):
        self.title = self.title.replace("`", "")
        self.title = self.title.replace("python", "")
        e.page.set_clipboard(self.title)

        while self._hovered:
            self.copy_box.disabled = True
            self.copy_box.update()

            self.copy_box.content.opacity = 0
            self.copy_box.content.name = ft.icons.CHECK
            self.copy_box.update()

            await asyncio.sleep(0.25)

            self.copy_box.content.opacity = 1
            self.copy_box.content.color = "teal"
            self.copy_box.update()

            await asyncio.sleep(1)

            self.copy_box.content.opacity = 0
            self.copy_box.content.name = ft.icons.COPY
            self.copy_box.content.color = "white12"
            self.copy_box.update()

            self.copy_box.disabled = False
            self.copy_box.update()

            break

        if self._hovered == True:
            self.copy_box.content.opacity = 1

        else:
            self.copy_box.content.opacity = 0

        self.copy_box.content.update()

    def show_copy_box(self, e):
        if e.data == "true":
            self.copy_box.border = ft.border.all(0.95, "white10")
            self.copy_box.content.opacity = 1
            self._hovered = True

        else:
            self.copy_box.content.opacity = 0
            self.copy_box.border = ft.border.all(0.95, "transparent")
            self._hovered = False

        self.copy_box.update()

    def build(self):
        return ft.Row(
            alignment="start",
            vertical_alignment="center",
            controls=[
                ft.Container(
                    expand=True,
                    padding=8,
                    border_radius=7,
                    bgcolor="#282b33",
                    on_hover=lambda e: self.show_copy_box(e),
                    content=ft.Stack(
                        controls=[
                            ft.Markdown(
                                value=self.title,
                                selectable=True,
                                extension_set="gitHubWeb",
                                code_theme="atom-one-dark-reasonable",
                                code_style=ft.TextStyle(size=12),
                            ),
                            self.copy_box,
                        ],
                    ),
                )
            ],
        )
