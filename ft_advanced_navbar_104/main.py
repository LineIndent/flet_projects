import flet as ft


class Header(ft.UserControl):
    def __init__(self):
        #
        self.nav = ft.Container(
            opacity=1,
            animate_opacity=ft.Animation(300, "ease"),
            content=ft.Row(
                controls=[
                    ft.Text("Home", size=9),
                    ft.Text("About", size=9),
                    ft.Text("Contact", size=9),
                ]
            ),
        )
        #
        self.header = ft.Container(
            height=80,
            bgcolor="teal",
            padding=ft.padding.only(left=60, right=60),
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=4,
                color=ft.colors.with_opacity(0.25, "black"),
                offset=ft.Offset(2, 2),
            ),
            animate=ft.Animation(500, "ease"),
            content=ft.Column(
                alignment="center",
                spacing=15,
                controls=[
                    # Title section ...
                    ft.Row(controls=[ft.Text("My Title", size=21)]),
                    # Navigation section ...
                    self.nav,
                ],
            ),
        )
        super().__init__()

    def dynamic_navigation(self, e):
        if e.pixels >= float(2.0):
            self.nav.opacity = 0
            self.nav.update()
            self.nav.visible = False

            self.header.height = 60

        else:
            self.header.height = 80

            self.nav.visible = True
            self.nav.update()
            self.nav.opacity = 1

        self.update()

    def build(self):
        return self.header


class FakeContent(ft.Container):
    def __init__(
        self,
        header,
        bgcolor="#23262d",
        expand=True,
        padding=ft.padding.only(top=55, right=15, left=15),
        alignment=ft.alignment.top_center,
        content=ft.Column(
            expand=True,
            alignment="start",
            scroll="auto",
        ),
    ):
        super().__init__(
            bgcolor=bgcolor,
            expand=expand,
            padding=padding,
            alignment=alignment,
            content=content,
        )

        self.header = header
        self.content.on_scroll = lambda e: self.header.dynamic_navigation(e)

        for i in range(50):
            self.content.controls.append(
                ft.Row(
                    controls=[ft.Text(i, size=11)],
                )
            )

        self.content.controls.insert(0, ft.Divider(height=25, color="transparent"))


def main(page: ft.Page):
    page.padding = 0

    header = Header()
    content = FakeContent(header)

    page.add(
        ft.Stack(
            expand=True,
            controls=[
                ft.Row(expand=True, controls=[content]),
                header,
            ],
        )
    )

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
