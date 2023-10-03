import flet as ft
import flet_fastapi


columns = [
    ft.DataColumn(ft.Text("First name")),
    ft.DataColumn(ft.Text("Last name")),
    ft.DataColumn(ft.Text("Age"), numeric=True),
]


form_css: dict = {
    "height": 230,
    "border": ft.border.all(1, "white10"),
    "border_radius": 8,
    "padding": ft.padding.only(top=10),
}

input_css: dict = {
    "height": 45,
}

input_column: dict = {
    "spacing": 5,
    "alignment": "center",
    "horizontal_alignment": "start",
    "expand": True,
    "scale": ft.transform.Scale(0.85),
}


class Form(ft.Container):
    def __init__(self) -> ft.Container:
        super().__init__(**form_css)
        self.content = ft.Column(
            controls=[
                ft.Row(
                    alignment="center",
                    controls=[
                        ft.Text("Data Form Field", size=28, weight="bold"),
                    ],
                ),
                ft.Row(
                    controls=[
                        self.input_("First Name"),
                        self.input_("Last Name"),
                    ],
                ),
                ft.Row(
                    controls=[
                        self.input_("Age"),
                    ],
                ),
            ]
        )

    def input_(self, text: str):
        return ft.Column(
            **input_column,
            controls=[
                ft.Text(text),
                ft.TextField(**input_css),
            ],
        )


class DataTable(ft.DataTable):
    def __init__(self) -> ft.DataTable:
        super().__init__(columns=columns)


async def main(page: ft.Page) -> ft.Page:
    # page.theme_mode = ft.ThemeMode.LIGHT

    form: ft.Container = Form()
    dt: ft.DataTable = DataTable()

    await page.add_async(form)
    await page.add_async(dt)
    await page.update_async()


app = flet_fastapi.app(main)
