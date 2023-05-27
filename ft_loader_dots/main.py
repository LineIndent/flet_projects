import flet
from flet import *
import time
import math


class LoadingAnimation(UserControl):
    def __init__(self):
        self.loading_row = Row(alignment="center", spacing=10)
        super().__init__()

    def animate_loader(self, load=True):
        t = 0
        while load:
            for i, circle in enumerate(self.loading_row.controls):
                y_offset = math.sin(t + i * math.pi / 2)
                circle.offset = transform.Offset(0, y_offset)
                circle.update()
            t += 0.20
            time.sleep(0.05)

    def build(self):
        items: list = [
            Container(
                width=21,
                height=21,
                bgcolor="bluegrey600",
                shape=BoxShape("circle"),
                offset=transform.Offset(0, 0),
                animate_offset=300,
            )
            for i in range(3)
        ]

        self.loading_row.controls = items

        return Container(
            content=self.loading_row,
        )


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    loading = LoadingAnimation()
    page.add(loading)

    loading.animate_loader()
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
