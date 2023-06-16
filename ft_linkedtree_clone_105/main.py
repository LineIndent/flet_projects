import flet as ft


def main(page: ft.Page):
    page.padding = 0
    app = AppView()

    page.add(app)
    page.update()


class AppView(ft.Stack):
    def __init__(
        self,
        expand=True,
    ):
        super().__init__(expand=expand)

        socials = SocialDashboard()
        main = FakeContent()

        control_list: list = [main, socials]

        self.controls = control_list


class SocialDashboard(ft.UserControl):
    def __init__(self):
        self.header = ft.Container(
            height=70,
            bottom=0,
            left=0,
            right=0,
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
                controls=[],
            ),
        )
        super().__init__()

    def build(self):
        return self.header


class FakeContent(ft.Container):
    def __init__(
        self,
        # header,
        bgcolor="#23262d",
        expand=True,
        padding=ft.padding.only(top=10, right=15, left=15),
        # alignment=ft.alignment.top_center,
        content=ft.Column(
            expand=True,
            alignment="center",
            horizontal_alignment="center",
            scroll="auto",
        ),
    ):
        super().__init__(
            bgcolor=bgcolor,
            expand=expand,
            padding=padding,
            # alignment=alignment,
            content=content,
        )

        # self.header = header
        # self.content.on_scroll = lambda e: self.header.dynamic_navigation(e)

        for i in range(50):
            self.content.controls.append(
                ft.Row(alignment="center", controls=[ft.Text(i, size=11)])
            )


if __name__ == "__main__":
    ft.flet.app(target=main)
