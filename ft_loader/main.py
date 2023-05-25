import flet
from flet import *
from math import pi
import time


class AnimatedBox(UserControl):
    def __init__(self, border_color, bg_color, rotate_angle):
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle
        super().__init__()

    def build(self):
        return Container(
            width=64,
            height=64,
            border=border.all(2.5, self.border_color),
            bgcolor=self.bg_color,
            border_radius=2,
            rotate=transform.Rotate(self.rotate_angle, alignment.center),
            animate_rotation=animation.Animation(700, "easeInOut"),
        )


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#1f262f"

    def animate_boxes():
        clock_wise_rotate = pi / 4
        counter_clock_wise_rotate = -pi * 2
        red_box = page.controls[0].controls[0].controls[0]
        blue_box = page.controls[0].controls[1].controls[0]
        counter = 0
        while True:
            if counter >= 0 and counter <= 4:
                red_box.rotate = transform.Rotate(
                    counter_clock_wise_rotate, alignment.center
                )
                blue_box.rotate = transform.Rotate(clock_wise_rotate, alignment.center)

                red_box.update()
                blue_box.update()

                clock_wise_rotate += pi / 2
                counter_clock_wise_rotate -= pi / 2

                counter += 1

                time.sleep(0.70)

            if counter >= 5 and counter <= 10:
                clock_wise_rotate -= pi / 2
                counter_clock_wise_rotate += pi / 2

                red_box.rotate = transform.Rotate(
                    counter_clock_wise_rotate, alignment.center
                )
                blue_box.rotate = transform.Rotate(clock_wise_rotate, alignment.center)

                red_box.update()
                blue_box.update()

                counter += 1

                time.sleep(0.70)

            if counter > 10:
                counter = 0

    page.add(
        Stack(
            controls=[
                AnimatedBox("#e9665a", None, 0),
                AnimatedBox("#7df6dd", "#1f262f", pi / 4),
            ]
        )
    )
    page.update()
    animate_boxes()


if __name__ == "__main__":
    flet.app(target=main)
