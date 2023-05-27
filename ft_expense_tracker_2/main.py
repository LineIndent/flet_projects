import flet
from flet import *
from math import pi

CONTROLS = []


def store_control_sub_reference(function):
    def wrapper(*args, **kwargs):
        reference = function(*args, **kwargs)
        CONTROLS.append(reference)
        return reference

    return wrapper


class Main(UserControl):
    def __init__(self):
        super().__init__()

    def main_title(self):
        return Row(
            alignment=MainAxisAlignment.START,
            controls=[
                Text("Dashboard", size=21, weight="bold"),
            ],
        )

    def main_body(self):
        return Container(
            width=260,
            height=500,
            border=border.all(0.5, "white24"),
            border_radius=10,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.main_body_title(),
                    Divider(height=25, color="transparent"),
                    self.main_body_card(),
                    Divider(height=35, color="transparent"),
                    self.main_body_card_detail(),
                ],
            ),
        )

    def main_body_title(self):
        return Container(
            padding=15,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Text("1. Current Card", size=12, weight="bold"),
                    Container(
                        content=Row(
                            alignment=MainAxisAlignment.END,
                            spacing=-10,
                            controls=[
                                IconButton(icon=icons.ADD_CIRCLE_ROUNDED, icon_size=14),
                                IconButton(icon=icons.SETTINGS, icon_size=14),
                            ],
                        ),
                    ),
                ],
            ),
        )

    def card_text_control(self, name: str, size: int, bold: str):
        return Text(
            value=name,
            size=size,
            color="black",
            weight=bold,
        )

    def rotate_card(self, e):
        if e.data == "true":
            CONTROLS[0].rotate = transform.Rotate(0)
            CONTROLS[0].update()
        else:
            CONTROLS[0].rotate = transform.Rotate(-pi / 2)
            CONTROLS[0].update()

    @store_control_sub_reference
    def main_body_card(self):
        return Card(
            rotate=transform.Rotate(-pi / 2),
            animate_rotation=animation.Animation(500, "easeInOut"),
            elevation=15,
            content=Container(
                width=200,
                height=140,
                border_radius=8,
                on_hover=lambda e: self.rotate_card(e),
                content=Column(
                    spacing=0,
                    controls=[
                        Container(
                            expand=2,
                            bgcolor="#e5ece8",
                            border_radius=border_radius.only(top_left=10, top_right=10),
                            padding=12,
                            content=Column(
                                controls=[
                                    Row(
                                        controls=[
                                            self.card_text_control(
                                                "Shopping Card", 11, "bold"
                                            )
                                        ]
                                    ),
                                    Row(
                                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            self.card_text_control("Name", 11, None),
                                            Divider(height=50, color="transparent"),
                                            self.card_text_control(
                                                "Exp. 10/25", 11, None
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                        Container(
                            expand=1,
                            bgcolor="#85b899",
                            padding=12,
                            border_radius=border_radius.only(
                                bottom_left=10, bottom_right=10
                            ),
                            content=Row(
                                alignment=MainAxisAlignment.END,
                                controls=[
                                    self.card_text_control(
                                        "•••• •••• •••• 4123", 13, "bold"
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
        )

    def main_body_card_detail(self):
        row = Row(alignment=MainAxisAlignment.START)
        data = [
            ["EXPIRE DATA", "10/25"],
            ["CVV", "982"],
            ["LEVEL", "03"],
        ]
        for item in data:
            row.controls.append(
                Container(
                    padding=padding.only(left=12, right=12),
                    content=Column(
                        spacing=4,
                        controls=[
                            Text(item[0], size=8, color="white54", weight="bold"),
                            Text(item[1], size=12, weight="bold"),
                        ],
                    ),
                ),
            )

        return Container(
            content=Column(
                controls=[
                    Container(
                        padding=padding.only(left=12, right=12),
                        content=Text("2. Card Details", size=12, weight="bold"),
                    ),
                    Container(
                        padding=padding.only(left=12, right=12),
                        content=Row(
                            controls=[
                                Column(
                                    spacing=4,
                                    controls=[
                                        Text(
                                            "CARD NUMBER",
                                            size=8,
                                            color="white54",
                                            weight="bold",
                                        ),
                                        Text(
                                            "4123 1324 1233 4123",
                                            size=12,
                                            weight="bold",
                                        ),
                                    ],
                                )
                            ]
                        ),
                    ),
                    Container(
                        content=row,
                    ),
                ],
            )
        )

    def build(self):
        return Column(
            expand=True,
            alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.main_title(),
                Divider(height=25, color="transparent"),
                self.main_body(),
            ],
        )


def main(page: Page):
    # page.horizontal_alignment = "end"
    # page.vertical_alignment = "center"
    page.add(
        Container(
            width=1500,
            height=1000,
            gradient=RadialGradient(
                center=Alignment(0.8, 0.8),
                radius=2,
                colors=[
                    "#14b8a6",
                    "#0d9488",
                    "#0f766e",
                    "#115e59",
                    "#134e4a",
                    "#1e3e3b",
                    "#1a3734",
                    "#182726",
                ],
            ),
            alignment=alignment.center_right,
            padding=padding.only(right=60, bottom=50),
            content=Container(
                width=300,
                height=620,
                bgcolor="#1d2630",
                border_radius=10,
                padding=20,
                content=Main(),
            ),
        )
    )
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
