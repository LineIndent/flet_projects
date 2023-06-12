import flet as ft


class Header(ft.UserControl):
    def __init__(self):
        self.header = ft.Container(
            height=90,
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
                controls=[
                    # Title section ...
                    ft.Row(controls=[ft.Text("Name Or Title", size=21)]),
                    # Navigation section ...
                    ft.Row(
                        controls=[
                            ft.Text("Home", size=9),
                            ft.Text("About", size=9),
                            ft.Text("Contact", size=9),
                        ]
                    ),
                ]
            ),
        )
        super().__init__()

    def build(self):
        return self.header


def main(page: ft.Page):
    #
    header = Header()

    page.add(
        ft.Stack(
            controls=[
                header,
            ]
        )
    )

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
