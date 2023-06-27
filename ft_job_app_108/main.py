import flet as ft
import requests


class JobEntry(ft.Container):
    def __init__(
        self, col={"xs": 12, "sm": 12, "md": 12, "lg": 6, "xl": 5}, expand=True
    ):
        super().__init__(col=col, expand=expand)

        self.input_query = ft.TextField(
            border_color="transparent", on_submit=lambda e: self.get_data(e)
        )

        self.column = ft.Column(
            horizontal_alignment="center",
            spacing=0,
            controls=[
                ft.Divider(height=20, color="transparent"),
                ft.Container(
                    padding=15,
                    content=ft.Text(
                        "Python Job Search".upper(),
                        weight="bold",
                        style=ft.TextThemeStyle("titleLarge"),
                    ),
                ),
                ft.Divider(height=10, color="transparent"),
                ft.Container(
                    shadow=ft.BoxShadow(
                        spread_radius=7,
                        blur_radius=14,
                        color=ft.colors.with_opacity(0.1, "teal900"),
                        offset=ft.Offset(4, 4),
                    ),
                    content=self.input_query,
                    border=ft.border.all(2, "#64b687"),
                    border_radius=6,
                ),
                ft.Divider(height=20, color="transparent"),
            ],
        )

        self.content = self.column

    def get_data(self, e):
        res = requests.get("https://api-pourhakimi.vercel.app/")
        res = res.json()

        for index, __ in enumerate(res["data"]):
            print(res["data"][index]["job_apply_link"])
            print()


class JobSearchResult(ft.Container):
    def __init__(
        self,
        # border_radius=6,
        # border=ft.border.all(1, "#64b687"),
        col={"xs": 12, "sm": 12, "md": 12, "lg": 6, "xl": 7},
        content=ft.Column(expand=True),
    ):
        super().__init__(
            col=col,
            content=content,
            # border=border,
            # border_radius=border_radius,
        )


class App(ft.UserControl):
    def __init__(self):
        self.job_entry = JobEntry()
        self.job_result = JobSearchResult()
        self.row = ft.ResponsiveRow(
            alignment="center",
            vertical_alignment="center",
            offset=ft.transform.Offset(0, 0),
            animate_size=ft.Animation(500, "ease"),
            animate_offset=ft.Animation(900, "ease"),
        )

        super().__init__()

    def build(self):
        self.row.controls.append(self.job_entry)
        self.row.controls.append(self.job_result)

        return self.row


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#1a1a1a"
    page.padding = 30

    app = App()
    page.add(app)

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
