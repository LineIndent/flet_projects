""" Flet Animated Icons """

# modules
import flet
from flet import *
import time


def main(page: Page):
    # title
    page.title = "Flet Animated Icons"

    # alignment
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # main row
    _main_row = Container(
        content=Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[],
        ),
    )

    # icon list
    _icon_list = [
        icons.DISCORD_ROUNDED,
        icons.PERSON_ADD,
        icons.SEARCH_ROUNDED,
        icons.FAVORITE_ROUNDED,
        icons.NOTIFICATION_ADD_ROUNDED,
    ]

    def _animate_icon(e):
        e.control.scale = transform.Scale(0.65)
        e.control.update()
        time.sleep(0.15)
        e.control.scale = transform.Scale(1)
        e.control.update()

        for control in _main_row.content.controls[:]:
            control.content.selected = False
            control.content.icon_color = "white54"
            control.content.update()

            if e.control.content.selected != True:
                e.control.content.selected = True
                e.control.content.icon_color = "white"
                e.control.content.update()

    for icon in _icon_list:
        __ = Container(
            on_click=lambda e: _animate_icon(e),
            animate_scale=animation.Animation(duration=500, curve="bounceOut"),
            scale=transform.Scale(1),
            content=IconButton(
                icon=icon,
                icon_size=32,
                icon_color="white54",
                selected=False,
            ),
        )
        _main_row.content.controls.append(__)

        if icon == icons.DISCORD_ROUNDED:
            __.content.icon_color, __.content.selected = "white", True

    def _rotate_phone(e):
        _main_container.rotate = transform.Rotate(1.57, alignment=alignment.center)
        _main_container.update()

    _rotator = Container(
        width=32,
        height=32,
        border_radius=32,
        bgcolor="teal900",
        on_click=lambda e: _rotate_phone(e),
        content=IconButton(
            icon=icons.PHISHING_ROUNDED,
            icon_size=18,
        ),
    )
    # main container
    _main_container = Container(
        width=580,
        height=260,
        rotate=transform.Rotate(0, alignment=alignment.center),
        animate_rotation=animation.Animation(duration=500, curve="decelerate"),
        border_radius=35,
        bgcolor="black",
        alignment=alignment.bottom_center,
        padding=20,
        content=Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                _main_row,
            ],
        ),
    )

    page.add(
        Container(
            width=1400,
            height=800,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["blue800", "blue100"],
            ),
            padding=50,
            content=Column(
                alignment="end",
                horizontal_alignment="center",
                controls=[_main_container],
            ),
        )
    )
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
