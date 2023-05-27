import flet
from flet import *


def main(page: Page):
    def DeleteAnimation(e):
        if e.data == "true":
            e.control.content.controls[0].offset = transform.Offset(-0.6, 0)
            e.control.content.controls[0].update()

            e.control.content.controls[0].opacity = 1
            e.control.content.controls[0].update()
        else:
            e.control.content.controls[0].offset = transform.Offset(0, 0)
            e.control.content.controls[0].update()

            e.control.content.controls[0].opacity = 0
            e.control.content.controls[0].update()

    def _max(e):
        _b.controls[0].width = 300
        _b.controls[0].scale = transform.Scale(1, alignment=alignment.center_right)
        _b.controls[0].border_radius = 35
        _b.controls[0].disabled = False
        _b.controls[0].update()

    def _min(e):
        _b.controls[0].width = 120
        _b.controls[0].scale = transform.Scale(0.9, alignment=alignment.center_right)
        _b.controls[0].border_radius = border_radius.only(
            top_right=0,
            bottom_right=0,
            top_left=35,
            bottom_left=35,
        )
        _b.controls[0].disabled = True
        _b.controls[0].update()

    _a = Container(
        width=300,
        height=550,
        bgcolor="#1e293b",
        border_radius=35,
        padding=padding.only(left=20, top=60, right=120),
        content=Column(
            controls=[
                Row(
                    alignment="end",
                    controls=[
                        Container(
                            on_click=lambda e: _max(e),
                            content=Text(
                                "X",
                                size=12,
                                weight="w800",
                            ),
                        )
                    ],
                ),
                Container(
                    content=Text(
                        "Welcome\nLine Indent",
                        size=22,
                        weight="bold",
                    ),
                ),
                Container(padding=padding.only(top=10, bottom=10)),
                Container(
                    content=Column(
                        controls=[
                            Text(
                                "Settings",
                                size=11,
                                weight="bold",
                                color="white60",
                            ),
                            Text(
                                "Account",
                                size=11,
                                weight="bold",
                                color="white60",
                            ),
                            Text(
                                "Profile",
                                size=11,
                                weight="bold",
                                color="white60",
                            ),
                        ]
                    )
                ),
                Container(padding=padding.only(top=150)),
                Container(
                    content=Text(
                        "Log out?",
                        size=14,
                        weight="bold",
                    ),
                ),
            ],
        ),
    )

    _card_container = Row(scroll="auto")
    _task_container = Column()
    _top = Container(
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#111827", "#1f2937"],
        ),
        border_radius=30,
        padding=padding.only(top=15, left=15),
        content=Column(
            controls=[
                Container(
                    content=ResponsiveRow(
                        alignment="spaceBetween",
                        controls=[
                            Text(
                                "Dashboard",
                                col={"xs": 6, "sm": 6},
                                no_wrap=True,
                                size=20,
                                weight="bold",
                            ),
                            Container(
                                col={"xs": 2, "sm": 2},
                                on_click=lambda e: _min(e),
                                content=Text(
                                    "ⓘ",
                                    weight="bold",
                                    no_wrap=True,
                                ),
                            ),
                        ],
                    ),
                ),
                Container(padding=padding.only(top=20)),
                Text(
                    "CATEGORIES",
                    size=12,
                    color="white60",
                    no_wrap=True,
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    bgcolor="transparent",
                    content=_card_container,
                ),
            ]
        ),
    )

    _b = Row(
        alignment="end",
        controls=[
            Container(
                width=300,
                height=550,
                bgcolor="#475569",
                border_radius=35,
                animate=animation.Animation(duration=500, curve="decelerate"),
                scale=transform.Scale(1, alignment=alignment.center_right),
                animate_scale=animation.Animation(duration=500, curve="decelerate"),
                padding=5,
                content=Column(
                    alignment="start",
                    controls=[
                        _top,
                        Container(
                            padding=padding.only(left=12, right=12, top=5),
                            content=Text(
                                "TASKS TODAY",
                                size=12,
                                color="white60",
                                no_wrap=True,
                            ),
                        ),
                        Container(
                            padding=padding.only(right=12, left=12),
                            bgcolor="transparent",
                            content=_task_container,
                        ),
                    ],
                ),
            )
        ],
    )

    l = ["Business", "Personal", "Family"]
    t = ["40 tasks", "12 tasks", "7 tasks"]
    p = [90, 123, 45]
    for index in range(3):
        _ = Card(
            elevation=15,
            content=Container(
                width=160,
                height=100,
                bgcolor="#1e293b",
                border_radius=5,
                padding=15,
                content=Column(
                    alignment="spaceBetween",
                    controls=[
                        Container(
                            content=Column(
                                spacing=3,
                                controls=[
                                    Text(
                                        t[index],
                                        color="white60",
                                        size=12,
                                    ),
                                    Text(
                                        l[index],
                                        size=20,
                                    ),
                                ],
                            )
                        ),
                        Container(
                            width=160,
                            height=5,
                            bgcolor="white12",
                            border_radius=20,
                            padding=padding.only(right=p[index]),
                            content=Container(
                                bgcolor="pink",
                            ),
                        ),
                    ],
                ),
            ),
        )
        _card_container.controls.append(_)

    r = ["Daily meeting with team", "Check emails", "Lunch with John", "Meditation"]

    for index in range(4):
        _task_container.controls.append(
            ResponsiveRow(
                spacing=-5,
                controls=[
                    Container(
                        col={"xs": 8},
                        height=40,
                        border_radius=border_radius.only(
                            top_left=9, bottom_left=9, top_right=0, bottom_right=0
                        ),
                        padding=12,
                        expand=True,
                        bgcolor="#1e293b",
                        content=Text(
                            r[index],
                            size=10,
                            no_wrap=True,
                        ),
                    ),
                    Container(
                        height=40,
                        col={"xs": 4},
                        alignment=alignment.center_right,
                        bgcolor="#1e293b",
                        animate=animation.Animation(1000, "ease"),
                        border_radius=border_radius.only(
                            top_left=0, bottom_left=0, top_right=9, bottom_right=9
                        ),
                        on_hover=lambda e: DeleteAnimation(e),
                        content=Row(
                            alignment="end",
                            spacing=0,
                            controls=[
                                Text(
                                    "FINISHED?",
                                    no_wrap=True,
                                    opacity=0,
                                    size=9,
                                    offset=transform.Offset(0, 0),
                                    animate_offset=animation.Animation(
                                        duration=900, curve="ease"
                                    ),
                                    animate_opacity=200,
                                ),
                            ],
                        ),
                    ),
                ],
            )
        )

    #
    _c = Container(
        width=300,
        height=550,
        border_radius=35,
        content=Stack(
            width=300,
            height=550,
            controls=[
                _a,
                _b,
            ],
        ),
    )

    page.add(_c)


if __name__ == "__main__":
    flet.app(target=main)
