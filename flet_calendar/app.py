from flet import (
    flet,
    Page,
    Column,
    Row,
    Container,
    Text,
    alignment,
    LinearGradient,
    animation,
    IconButton,
    icons,
    transform,
    padding,
)

from datetime import date
import calendar

obj = calendar.Calendar()


def main(page: Page):

    _content_dic = {}
    _year_now = int(date.today().strftime("%Y"))
    _month_now = int(date.today().strftime("%m"))
    _day_now = int(date.today().strftime("%d"))

    def DeleteAnimation(e):
        if e.data == "true":
            e.control.content.controls[0].offset = transform.Offset(-0.50, 0)
            e.control.content.controls[0].update()

            e.control.content.controls[0].opacity = 1
            e.control.content.controls[0].update()
        else:
            e.control.content.controls[0].offset = transform.Offset(0, 0)
            e.control.content.controls[0].update()

            e.control.content.controls[0].opacity = 0
            e.control.content.controls[0].update()

    def _create_entry(e):
        _content_column.controls.append(
            Row(
                controls=[
                    Container(
                        border_radius=8,
                        padding=12,
                        expand=True,
                        gradient=LinearGradient(
                            begin=alignment.center_left,
                            end=alignment.center_right,
                            colors=["#1e293b", "shadow"],
                        ),
                        content=Text(
                            f"You have a task on\n{e.control.data}",
                            size=10,
                        ),
                    ),
                    Container(
                        alignment=alignment.center_right,
                        animate=animation.Animation(1000, "ease"),
                        on_hover=lambda e: DeleteAnimation(e),
                        content=Row(
                            alignment="end",
                            spacing=0,
                            controls=[
                                Text(
                                    "DELETE",
                                    opacity=0,
                                    size=9,
                                    offset=transform.Offset(0, 0),
                                    animate_offset=animation.Animation(
                                        duration=900, curve="ease"
                                    ),
                                    animate_opacity=200,
                                ),
                                IconButton(
                                    icon=icons.DELETE_ROUNDED,
                                    icon_size=19,
                                    icon_color="#dc2626",
                                ),
                            ],
                        ),
                    ),
                ],
            )
        )
        _content_column.update()

    def _highlight_date(e):

        if e.control.bgcolor == "#0c4a6e":
            pass
        else:
            if e.data == "true":
                e.control.bgcolor = "white10"
                e.control.update()
            else:
                e.control.bgcolor = "#0c0f16"
                e.control.update()

    def _popup(e):
        _title.visible = False
        _title.update()
        if e.control.height != _main.height * 0.55:
            e.control.height = _main.height * 0.55
            e.control.update()

            for key in _content_dic:
                for month in _content_dic[key]:
                    if month == _month_now and key == _year_now:
                        _content_dic[key][month].visible = True
                        _content_dic[key][month].update()
        else:
            for key in _content_dic:
                for month in _content_dic[key]:
                    if month == _month_now and key == _year_now:
                        _content_dic[key][month].visible = False
                        _content_dic[key][month].update()

            e.control.height = _main.height * 0.13
            e.control.update()
            _title.visible = True
            _title.update()

    # 1
    _main = Container(
        width=290,
        height=590,
        border_radius=35,
        bgcolor="black",
        padding=8,
        alignment=alignment.bottom_center,
    )

    # 2
    _main_column = Column(spacing=2, scroll="auto", alignment="start")

    # 3
    _calendar_container = Container(
        width=_main.width,
        height=_main.height * 0.13,
        border_radius=30,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#1e293b", "#0f172a"],
        ),
        alignment=alignment.center,
        # 3.1 => do this after 3
        on_click=lambda e: _popup(e),
        animate=animation.Animation(duration=320, curve="decelerate"),
    )

    # 4
    _calendar_container.content = _main_column

    # 5
    _title = Container(
        content=Text(
            "SCHEDULE",
            color="white70",
            weight="bold",
        )
    )
    _main_column.controls.append(_title)

    # 6
    _content_column = Column(
        scroll="auto",
        expand=True,
        alignment="start",
        controls=[
            Container(
                padding=15,
                content=Text(
                    "Scheduled Tasks",
                    color="white70",
                    weight="bold",
                    size=13,
                ),
            )
        ],
    )

    # 7
    _main.content = Column(
        alignment="end",
        controls=[
            Container(
                expand=True,
                content=_content_column,
            ),
            _calendar_container,
        ],
    )

    # 8
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    # 9
    weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    _row_weekday = Row(
        spacing=2,
        alignment="center",
    )

    # 10
    for day in weekday:
        _row_weekday.controls.append(
            Container(
                width=32,
                height=32,
                border_radius=5,
                alignment=alignment.center,
                content=Text(day, size=9, color="white70"),
            )
        )

    #

    # 11
    for year in range(2022, 2024):
        _content_dic[year] = {}
        for month in range(11, 12):
            #
            _inner_column = Column(
                horizontal_alignment="start",
                spacing=2,
            )
            _inner = Container(
                visible=False,
                content=_inner_column,
            )
            _main_column.controls.append(_inner)
            #
            _row_year = Row(
                spacing=2,
                alignment="center",
                controls=[
                    Text(f"{months[month - 1]} {year}", size=12),
                ],
            )
            _inner_column.controls.append(_row_year)
            #
            _inner_column.controls.append(_row_weekday)

            #
            for days in obj.monthdayscalendar(year, month):
                _row = Row(
                    spacing=2,
                    alignment="center",
                )
                _inner_column.controls.append(_row)
                for day in days:
                    if day != 0:
                        __ = Container(
                            width=32,
                            height=32,
                            bgcolor="#0c0f16",
                            border_radius=5,
                            alignment=alignment.center,
                            content=Text(
                                f"{day}",
                                size=10,
                                color="white70",
                            ),
                            data=f"{months[month - 1]} {day}, {year}",
                            on_click=lambda e: _create_entry(e),
                            on_hover=lambda e: _highlight_date(e),
                        )
                        _row.controls.append(__)

                        # if month == _month_now and day == _day_now:
                        #     __.bgcolor = "#0c4a6e"

                    else:
                        _row.controls.append(
                            Container(
                                width=32,
                                height=32,
                                border_radius=8,
                            )
                        )

            _content_dic[year][month] = _inner

    # first setup
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.add(
        Container(
            width=1400,
            height=750,
            padding=padding.only(right=120),
            alignment=alignment.center_right,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                # colors=["#111827", "#1e3a8a"],
                # colors=["#1e3a8a", "#111827"],
                colors=["#0f172a", "#64748b"],
            ),
            content=Column(
                alignment="center",
                horizontal_alignment="center",
                controls=[_main],
            ),
        )
    )
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
