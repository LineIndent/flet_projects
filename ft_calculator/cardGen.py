from flet import (
    Container,
    UserControl,
    RadialGradient,
    Alignment,
    alignment,
    Row,
    border_radius,
    padding,
    Column,
    Text,
    Card,
    animation,
    transform,
)


class CardGenerator(UserControl):
    def __init__(
        self,
        colors: list,
        title: str,
        subtitle: str,
        price: str,
        icon: str,
        card_icon: str,
        card_type: str,
        card_number: str,
    ):
        self.colors = colors
        self.title = title
        self.subtitle = subtitle
        self.price = price
        self.icon = icon
        self.card_icon = card_icon
        self.card_type = card_type
        self.card_number = card_number

        super().__init__()

    def show_price(self, e):
        if e.data == "true":

            self.animated_text.offset = transform.Offset(0, 0)
            self.animated_text.opacity = 1
            self.animated_text.update()
        else:
            self.animated_text.offset = transform.Offset(0.35, 0)
            self.animated_text.opacity = 0
            self.animated_text.update()

    def build(self):
        self.animated_card = Container(
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(900),
            content=Card(
                width=64,
                height=64,
                elevation=20,
                content=Container(
                    width=56,
                    height=56,
                    border_radius=20,
                    image_src=self.icon,
                ),
            ),
        )

        self.animated_text = Text(
            self.price,
            size=18,
            weight="bold",
            offset=transform.Offset(0.35, 0),
            animate_offset=animation.Animation(duration=900, curve="decelerate"),
            animate_opacity=300,
            opacity=0,
        )

        self.main_card = Container(
            gradient=RadialGradient(
                center=Alignment(0.8, 0.8),
                radius=1.4,
                colors=self.colors,
            ),
            width=210,
            height=260,
            border_radius=35,
            alignment=alignment.bottom_center,
            content=(
                Column(
                    alignment="end",
                    horizontal_alignment="end",
                    controls=[
                        Column(
                            expand=True,
                            alignment="start",
                            controls=[
                                Row(
                                    controls=[
                                        Container(
                                            width=210,
                                            height=100,
                                            content=Row(
                                                spacing=5,
                                                controls=[
                                                    Column(
                                                        alignment="center",
                                                        controls=[
                                                            Container(
                                                                width=80,
                                                                height=64,
                                                                padding=padding.only(
                                                                    left=10,
                                                                ),
                                                                alignment=alignment.center,
                                                                content=self.animated_card,
                                                            ),
                                                        ],
                                                    ),
                                                    Column(
                                                        horizontal_alignment="start",
                                                        alignment="start",
                                                        controls=[
                                                            Container(
                                                                width=120,
                                                                height=100,
                                                                content=Column(
                                                                    spacing=5,
                                                                    alignment="center",
                                                                    controls=[
                                                                        Text(
                                                                            self.title,
                                                                            size=16,
                                                                        ),
                                                                        Text(
                                                                            self.subtitle,
                                                                            size=12,
                                                                            color="white54",
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        )
                                    ]
                                )
                            ],
                        ),
                        Row(
                            vertical_alignment="end",
                            alignment="end",
                            spacing=0,
                            controls=[
                                Container(
                                    width=100,
                                    height=150,
                                    content=Column(
                                        alignment="end",
                                        controls=[
                                            Container(
                                                padding=padding.only(
                                                    bottom=35,
                                                    left=10,
                                                ),
                                                content=self.animated_text,
                                            )
                                        ],
                                    ),
                                ),
                                Container(
                                    on_hover=lambda e: self.show_price(e),
                                    width=100,
                                    height=120,
                                    bgcolor="white10",
                                    border_radius=border_radius.only(
                                        topLeft=25,
                                        bottomRight=35,
                                    ),
                                    content=Column(
                                        spacing=1,
                                        controls=[
                                            Row(
                                                alignment="start",
                                                controls=[
                                                    Container(
                                                        width=100,
                                                        height=40,
                                                        padding=15,
                                                        content=Column(
                                                            spacing=5,
                                                            controls=[
                                                                Container(
                                                                    width=21,
                                                                    height=21,
                                                                    image_src=self.card_icon,
                                                                ),
                                                                Text(
                                                                    self.card_type,
                                                                    size=12,
                                                                    color="white70",
                                                                ),
                                                            ],
                                                        ),
                                                    )
                                                ],
                                            ),
                                            Container(
                                                padding=padding.only(bottom=35),
                                            ),
                                            Row(
                                                controls=[
                                                    Container(
                                                        padding=15,
                                                        width=100,
                                                        height=60,
                                                        content=Text(
                                                            self.card_number,
                                                            size=12,
                                                            color="white70",
                                                        ),
                                                    )
                                                ]
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                )
            ),
        )

        return self.main_card
