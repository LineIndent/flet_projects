import flet
from flet import *
from math import pi


class Toggle_1(UserControl):
    def __init__(self, on_color, animation):
        self.on_color = on_color
        self.animation = animation
        super().__init__()

    def toggle_switch(self, e):
        if self.toggle.offset == transform.Offset(-0.25, 0):
            self.toggle.offset = transform.Offset(0.25, 0)
            self.controls[0].bgcolor = self.on_color
            self.update()
        elif self.toggle.offset == transform.Offset(0.25, 0):
            self.toggle.offset = transform.Offset(-0.25, 0)
            self.controls[0].bgcolor = "white10"
            self.update()
        else:
            pass

    def build(self):
        self.toggle = Container(
            bgcolor="white",
            shape=BoxShape("circle"),
            offset=transform.Offset(-0.25, 0),
            animate_offset=animation.Animation(600, self.animation),
            on_click=lambda e: self.toggle_switch(e),
        )
        return Container(
            width=54,
            height=30,
            border_radius=25,
            bgcolor="white10",
            padding=4,
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=self.toggle,
            animate=400,
            on_click=lambda e: self.toggle_switch(e),
        )


class Toggle_2(UserControl):
    def __init__(self, animation):
        self.animation = animation
        super().__init__()

    def toggle_switch(self, e):
        if self.line_1.rotate == transform.Rotate(0):
            self.line_1.rotate = transform.Rotate(-pi / 4)
            self.line_2.rotate = transform.Rotate(pi / 4)
            self.update()
        elif self.line_1.rotate == transform.Rotate(-pi / 4):
            self.line_1.rotate = transform.Rotate(0)
            self.line_2.rotate = transform.Rotate(0)
            self.update()

        pass

    def build(self):
        self.line_1 = Container(
            height=2,
            width=28,
            border_radius=15,
            bgcolor="white",
            rotate=transform.Rotate(0),
            animate_rotation=animation.Animation(600, self.animation),
        )
        self.line_2 = Container(
            height=2,
            width=28,
            border_radius=15,
            bgcolor="white",
            rotate=transform.Rotate(0),
            animate_rotation=animation.Animation(600, self.animation),
        )

        return Container(
            width=32,
            height=32,
            border_radius=4,
            gradient=RadialGradient(
                center=Alignment(-0.9, -0.9),
                radius=4,
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
            shape=BoxShape("rectangle"),
            padding=2,
            on_click=lambda e: self.toggle_switch(e),
            alignment=alignment.center,
            content=Stack(controls=[self.line_1, self.line_2]),
        )


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    toggle_color = ["blue700", "green700", "red700", "yellow700", "purple700"]
    toggle_animation = [
        "easeInOutBack",
        "decelerate",
        "bounceOut",
        "linear",
        "easeOutBack",
    ]
    toggle_column_1 = Column()
    for color in toggle_color:
        row = Row(alignment=MainAxisAlignment.CENTER, spacing=20)
        for animation in toggle_animation:
            row.controls.append(
                Toggle_1(color, animation),
            )
        toggle_column_1.controls.append(row)

    toggle_column_2 = Column()
    for __ in range(5):
        row = Row(alignment=MainAxisAlignment.CENTER, spacing=20)
        for animation in toggle_animation:
            row.controls.append(
                Toggle_2(animation),
            )
        toggle_column_2.controls.append(row)

    page.add(toggle_column_1)
    page.add(Divider(height=20, color="transparent"))
    page.add(toggle_column_2)
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
