from flet import (
    flet,
    Page,
    UserControl,
    Container,
    animation,
    border,
    alignment,
    Text,
    Column,
    Row,
    colors,
    Card,
    transform,
)


class AnimatedCard(UserControl):
    def __int__(self):
        super().__int__()

    def build(self):
        self._icon_container_ = Container(
            width=120,
            height=35,
            bgcolor=colors.BLUE_800,
            border_radius=25,
            animate_opacity=200,
            offset=transform.Offset(0, 0.25),
            animate_offset=animation.Animation(duration=900, curve="ease"),
            visible=False,
            content=Row(
                alignment="center",
                vertical_alignment="center",
                controls=[
                    Text(
                        "More Info",
                        size=12,
                        weight="w600",
                    ),
                ],
            ),
        )

        self._container = Container(
            width=280,
            height=380,
            bgcolor=colors.WHITE,
            border_radius=12,
            on_hover=lambda e: self.AnimatedCardHover(e),
            animate=animation.Animation(600, "ease"),
            border=border.all(2, colors.WHITE24),
            content=Column(
                alignment="center",
                horizontal_alignment="start",
                spacing=0,
                controls=[
                    Container(
                        padding=20,
                        alignment=alignment.bottom_center,
                        content=Text(
                            "Card Title",
                            color=colors.BLACK,
                            size=28,
                            weight="w800",
                        ),
                    ),
                    Container(
                        padding=20,
                        alignment=alignment.top_center,
                        content=Text(
                            "Insert card details here...",
                            color=colors.BLACK,
                            size=14,
                            weight="w500",
                        ),
                    ),
                ],
            ),
        )

        self.__card = Card(
            elevation=0,
            content=Container(
                content=Column(
                    spacing=0,
                    horizontal_alignment="center",
                    controls=[
                        self._container,
                    ],
                ),
            ),
        )

        self._card = Column(
            horizontal_alignment="center",
            spacing=0,
            controls=[
                self.__card,
                self._icon_container_,
            ],
        )

        self._main = self._card

        return self._main

    def AnimatedCardHover(self, e):
        self._icon_container_.visible = True
        self._icon_container_.update()

        if e.data == "true":

            for __ in range(20):
                self.__card.elevation += 1
                self.__card.update()

            self._container.border = border.all(4, colors.BLUE_800)
            self._container.update()

            self._icon_container_.offset = transform.Offset(0, -0.75)
            self._icon_container_.opacity = 1
            self._icon_container_.update()

        else:
            for __ in range(20):
                self.__card.elevation -= 1
                self.__card.update()

            self._container.border = border.all(4, colors.WHITE24)
            self._container.update()

            self._icon_container_.offset = transform.Offset(0, 0.5)
            self._icon_container_.opacity = 0
            self._icon_container_.update()


def main(page: Page):
    page.bgcolor = colors.WHITE60
    app = AnimatedCard()
    page.add(app)
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
