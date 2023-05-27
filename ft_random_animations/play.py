import flet
from flet import *
import random
import time


def main(page: Page) -> None:
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    main_column = Column()
    color = ["blue", "green", "purple", "yellow", "orange", "black", "white"]

    def flashy_light(e):
        if e.data == "true":
            e.control.bgcolor = random.choice(color)
            e.control.update()
            time.sleep(0.4)
        else:
            e.control.bgcolor = None
            e.control.update()

    def get_red(e):
        if e.control.bgcolor != "red":
            e.control.bgcolor = "red700"
            e.control.on_hover = None
            e.control.update()
        else:
            pass

    for _ in range(15):
        row = Row(alignment=MainAxisAlignment.CENTER)
        for __ in range(15):
            row.controls.append(
                Container(
                    width=16,
                    height=16,
                    border=border.all(0.5, "white24"),
                    animate=animation.Animation(600, "easeOutBack"),
                    on_hover=lambda e: flashy_light(e),
                    on_click=lambda e: get_red(e),
                )
            )
        main_column.controls.append(row)

    page.add(main_column)
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
