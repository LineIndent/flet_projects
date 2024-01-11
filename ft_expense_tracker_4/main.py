import flet as ft
from datetime import datetime


# controller class to handle data between pages ...
class Controller:
    ledger: dict = {}

    @staticmethod
    def get_ledger():
        return Controller.ledger

    @staticmethod
    def add_to_ledger(value: str):
        Controller.ledger[datetime.now()] = int(value)

    @staticmethod
    def subtract_from_ledger(value: str):
        Controller.ledger[datetime.now()] = int(value) * -1


money_button_style: dict = {
    "border_radius": 5,
    "border": ft.border.all(1.25, "white54"),
    "padding": ft.padding.only(left=25, right=25, top=10, bottom=10),
    "animate": ft.Animation(350, "ease"),
}


# re-usable button control ...
class MoneyButton(ft.Container):
    def __init__(self, name: str, transaction_row: object, info: str):
        super(MoneyButton, self).__init__(**money_button_style, on_click=self.selected)
        self.info = info
        self.data = self.info
        self.transaction_row = transaction_row
        self.content = ft.Text(name)

    # method to highlight selected container
    def selected(self, e: ft.TapEvent):
        for item in self.transaction_row.controls:
            item.border = (
                ft.border.all(1.25, "teal")
                if item == e.control
                else ft.border.all(1.25, "white54")
            )
            item.data = self.info if item == e.control else None
            item.update()


# view for input page ...
class InputView(ft.View):
    def __init__(self, page: ft.page):
        super(InputView, self).__init__(
            route="/input", horizontal_alignment="start", padding=0, bgcolor="#131721"
        )

        self.page = page

        self.text = ft.TextField(
            text_align="center",
            border_color="white70",
            cursor_color="white70",
            height=50,
            focused_border_color="teal",
            width=320,
        )

        self.transaction_row = ft.Row(alignment="center")
        self.transaction_row.controls = [
            # buttons ...
            MoneyButton("Money In", self.transaction_row, "in"),
            MoneyButton("Money Out", self.transaction_row, "out"),
        ]

        self.records = ft.Text(
            spans=[
                ft.TextSpan(
                    "Ledger",
                    on_click=lambda _: self.page.go("/output"),
                ),
            ]
        )

        self.controls = [
            ft.Container(
                height=50,
                bgcolor="#1d212b",
                padding=ft.padding.only(left=20, right=20),
                content=ft.Row(
                    alignment="spaceBetween",
                    controls=[
                        ft.Text("My Ledger"),
                        self.records,
                    ],
                ),
            ),
            ft.Divider(height=30, color="transparent"),
            ft.Column(
                spacing=20,
                horizontal_alignment="center",
                controls=[
                    ft.Text("Transaction Type", weight="w700"),
                    self.transaction_row,
                ],
            ),
            ft.Divider(height=30, color="transparent"),
            ft.Column(
                horizontal_alignment="center",
                spacing=20,
                controls=[
                    ft.Text("Amount", weight="w700"),
                    ft.Row(
                        alignment="center",
                        controls=[
                            ft.Container(
                                border_radius=5,
                                border=ft.border.all(1.25, "white24"),
                                content=self.text,
                            )
                        ],
                    ),
                ],
            ),
            ft.Column(
                alignment="end",
                expand=True,
                controls=[
                    ft.Container(
                        bgcolor="#1d212b",
                        height=50,
                        on_click=self.submit,
                        content=ft.Row(
                            alignment="center", controls=[ft.Text("Submit")]
                        ),
                    )
                ],
            ),
        ]

    # handles the submit event ...
    def submit(self, e: ft.TapEvent):
        for item in self.transaction_row.controls:
            if item.data == "in":
                self.add_value()

            elif item.data == "out":
                self.subtract_value()

    def restart_button_border(self):
        for item in self.transaction_row.controls:
            item.border = ft.border.all(1.25, "white54")
            item.update()

    def add_value(self):
        if self.text.value:  # check to see if text field has a string,,,
            Controller.add_to_ledger(self.text.value)
            self.restart_button_border()
            self.text.value = None

        self.text.update()

    def subtract_value(self):
        if self.text.value:  # check to see if text field has a string,,,
            Controller.subtract_from_ledger(self.text.value)
            self.restart_button_border()
            self.text.value = None

        self.text.update()


# view for output page ...
class OutputView(ft.View):
    def __init__(self, page: ft.page):
        super(OutputView, self).__init__(route="/output", bgcolor="#131721")

        self.page = page
        self.ledger: dict = Controller.get_ledger()

        self.input_page = ft.Text(
            size=16,
            spans=[ft.TextSpan("Back", on_click=lambda _: self.page.go("/input"))],
        )

        self.balance = ft.Text(f"Total balance: {sum(self.ledger.values())}", size=11)

        self.number = ft.Text(f"No. of records: {len(self.ledger)}", size=11)

        self.controls = [
            ft.Row(
                controls=[
                    ft.Text("Records", size=16),
                    self.input_page,
                ],
                alignment="spaceBetween",
            ),
            ft.Row(controls=[self.number, self.balance], alignment="spaceBetween"),
            # hadnles the data from the ledger dictionary ...
            *[
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(key.strftime("%b %d, %Y")),
                                ft.Text(value),
                            ],
                            alignment="spaceBetween",
                        ),
                        ft.Divider(height=2, color="white10"),
                    ]
                )
                for key, value in self.ledger.items()
            ],
        ]


def main(page: ft.Page):
    def router(route):
        page.views.clear()

        if page.route == "/input":
            input_view = InputView(page)
            page.views.append(input_view)

        elif page.route == "/output":
            output_view = OutputView(page)
            page.views.append(output_view)

        page.update()

    page.on_route_change = router
    page.go("/input")

    page.update()


ft.app(main)
