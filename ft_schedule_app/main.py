import flet
from flet import *
import schedule
from schedule import every, repeat, run_pending
import time
import datetime
from functools import partial
from threading import *


HEIGHT = 590
WIDTH = 280
global controlCounter
controlCounter = 0


class TitleClass(UserControl):
    def __init__(self):
        super().__init__()

    def _Data_(self):
        return Text(
            value=datetime.datetime.now().strftime("%A, %B %d"),
            size=11,
            weight="w500",
        )

    def _Time_(self):
        return Text(
            value=datetime.datetime.now().strftime("%I:%M").lstrip("0"),
            size=50,
            weight="bold",
        )

    def _Time(self):
        return Text(
            "Notifications Mobile App",
            size=13,
            weight="bold",
        )

    def build(self):
        return Container(
            padding=padding.only(top=20),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    self._Data_(),
                    self._Time_(),
                    Container(padding=6),
                    self._Time(),
                ],
            ),
        )


class ScheduleTask(UserControl):
    def __init__(self, hide: bool, func):
        self.hide = hide
        self.func = func
        super().__init__()

    def SelectTime(self, width: str):
        return Container(
            width=width,
            height=50,
            bgcolor="white24",
            border_radius=10,
            content=Dropdown(
                height=50,
                border_color="transparent",
                border_radius=10,
                text_style=TextStyle(
                    size=10,
                    color="white",
                    weight="bold",
                ),
                options=[
                    dropdown.Option("seconds"),
                    dropdown.Option("minutes"),
                    dropdown.Option("hours"),
                ],
            ),
        )

    def InputContainer(self, width: str, text: str):
        return Container(
            width=width,
            height=50,
            bgcolor="white24",
            border_radius=10,
            padding=8,
            content=Column(
                spacing=1,
                controls=[
                    Text(
                        value=text,
                        size=9,
                        color="white",
                        weight="bold",
                    ),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_color="white",
                        cursor_width=1,
                        color="white",
                    ),
                ],
            ),
        )

    def build(self):
        return Column(
            visible=self.hide,
            controls=[
                Text(
                    "Schedule Task",
                    size=15,
                    weight="bold",
                ),
                self.InputContainer(290, "Task Description"),
                Row(
                    alignment=MainAxisAlignment.START,
                    spacing=5,
                    controls=[
                        self.InputContainer(80, "Every"),
                        self.SelectTime(155),
                    ],
                ),
                Container(
                    alignment=alignment.center,
                    content=ElevatedButton(
                        on_click=partial(self.func),
                        bgcolor="teal900",
                        content=Text(
                            "Schedule",
                            size=11,
                            weight="bold",
                            color="white",
                        ),
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=8),
                            },
                            color={
                                "": "white",
                            },
                        ),
                        height=48,
                        width=200,
                    ),
                ),
            ],
        )


class CreateTasK(UserControl):
    def __init__(self, task: str, interval: str, duration: int):
        self.task = task
        self.interval = interval
        self.duration = duration
        super().__init__()

    def ScheduleAnimation(self):
        schedule.every(self.duration)
        pass

    def build(self):
        return Row(
            vertical_alignment="center",
            controls=[
                Container(
                    border_radius=8,
                    padding=12,
                    expand=True,
                    bgcolor="teal800",
                    content=Column(
                        spacing=2,
                        controls=[
                            Text(
                                self.task,
                                size=10,
                            ),
                            Text(
                                f"Every {self.interval} {self.duration}",
                                size=9,
                            ),
                        ],
                    ),
                ),
                Container(
                    alignment=alignment.center_right,
                    animate=animation.Animation(1000, "ease"),
                    content=Row(
                        alignment="end",
                        spacing=0,
                        controls=[
                            # Text(
                            #     "NOTIFICATION",
                            #     opacity=0,  # change to original => 0
                            #     size=9,
                            #     offset=transform.Offset(0, 0),
                            #     animate_offset=animation.Animation(
                            #         duration=900, curve="ease"
                            #     ),
                            #     animate_opacity=200,
                            # ),
                            IconButton(
                                icon=icons.NOTIFICATIONS_ACTIVE_ROUNDED,
                                icon_size=19,
                                opacity=0,
                                icon_color="#dc2626",
                                offset=transform.Offset(0, 0),  # position
                                animate_offset=animation.Animation(900),  # speed
                                animate_opacity=400,
                            ),
                        ],
                    ),
                ),
            ],
        )


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def _get_scheduler(e):
        if _time_container.height != HEIGHT * 0.80:
            _time_container.height = HEIGHT * 0.80
            _time_container.update()

            time.sleep(0.05)

            _time_container.content.controls[2].controls[0].visible = True
            _time_container.content.controls[2].controls[0].update()

        else:
            _time_container.height = HEIGHT * 0.35
            _time_container.update()

            time.sleep(0.05)

            _time_container.content.controls[2].controls[0].visible = False
            _time_container.content.controls[2].controls[0].update()

    def _notify(num: int):
        #
        _main_body_container.content.controls[num].controls[0].controls[
            1
        ].content.controls[0].offset = transform.Offset(-0.085, 0)
        #
        _main_body_container.content.controls[num].controls[0].controls[
            1
        ].content.controls[0].opacity = 1
        #
        _main_body_container.content.controls[num].controls[0].controls[
            1
        ].content.controls[0].update()
        #
        time.sleep(2)
        _main_body_container.content.controls[num].controls[0].controls[
            1
        ].content.controls[0].offset = transform.Offset(0, 0)

        _main_body_container.content.controls[num].controls[0].controls[
            1
        ].content.controls[0].opacity = 0

        _main_body_container.content.controls[num].controls[0].controls[
            1
        ].content.controls[0].update()

    def _set_task(e):
        global controlCounter

        description = (
            _time_container.content.controls[2]
            .controls[0]
            .controls[1]
            .content.controls[1]
            .value
        )
        interval = (
            _time_container.content.controls[2]
            .controls[0]
            .controls[2]
            .controls[0]
            .content.controls[1]
            .value
        )
        duration = (
            _time_container.content.controls[2]
            .controls[0]
            .controls[2]
            .controls[1]
            .content.value
        )

        _main_body_container.content.controls.append(
            CreateTasK(description, interval, duration)
        )
        _main_body_container.update()

        #

        #
        if duration == "seconds":
            schedule.every(int(interval)).seconds.do(_notify, controlCounter)
        if duration == "minutes":
            schedule.every(int(interval)).minutes.do(_notify, controlCounter)
        if duration == "hours":
            schedule.every(int(interval)).hours.do(_notify, controlCounter)

        controlCounter += 1

        #
        _time_container.height = HEIGHT * 0.35
        _time_container.update()

        time.sleep(0.05)

        _time_container.content.controls[2].controls[0].visible = False
        _time_container.content.controls[2].controls[0].update()

    #
    _time_container = Container(
        width=290,
        height=HEIGHT * 0.35,
        border_radius=42,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["teal300", "teal700", "teal800"],
        ),
        animate=animation.Animation(
            duration=1100, curve="elasticOut"
        ),  # easeOutBack, easeInBack
        padding=15,
        alignment=alignment.center,
        content=Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                TitleClass(),
                Container(padding=30),
                ScheduleTask(False, _set_task),
            ],
        ),
    )

    #
    _main_body_container = Container(
        width=WIDTH,
        height=HEIGHT * 0.95,
        border_radius=35,
        padding=padding.only(top=220, right=10, left=10, bottom=5),
        content=Column(
            scroll="auto",
            alignment=MainAxisAlignment.CENTER,
        ),
    )

    #
    _schedule_press = Column(
        alignment=MainAxisAlignment.END,
        horizontal_alignment="center",
        width=WIDTH,
        controls=[
            Container(
                width=WIDTH * 0.35,
                height=6,
                gradient=LinearGradient(
                    begin=alignment.bottom_left,
                    end=alignment.top_right,
                    colors=["teal500", "teal700", "teal800", "teal700", "teal500"],
                ),
                border_radius=30,
                animate=800,
                on_click=lambda e: _get_scheduler(e),
                content=None,
            )
        ],
    )

    _main_container = Container(
        width=WIDTH,
        height=HEIGHT,
        bgcolor="black",
        border_radius=45,
        padding=6,
        content=Stack(
            width=WIDTH,
            height=HEIGHT,
            controls=[
                _main_body_container,
                _time_container,
                _schedule_press,
            ],
        ),
    )

    page.add(
        Container(
            width=1500,
            height=800,
            margin=-20,
            padding=padding.only(right=80),
            gradient=RadialGradient(
                center=Alignment(-0.8, -0.8),
                radius=1.9,
                # the self.colors in this case is the list of colors from the pyhton dictioanry
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
            content=Row(
                alignment="end",
                controls=[
                    _main_container,
                    _main_container,
                ],
            ),
        )
    )
    page.update()

    def _animate_bottom_bar():
        while True:
            _schedule_press.controls[0].width = WIDTH * 0.40
            _schedule_press.controls[0].update()
            time.sleep(0.8)
            _schedule_press.controls[0].width = WIDTH * 0.30
            _schedule_press.controls[0].update()
            time.sleep(0.8)

    Thread(target=_animate_bottom_bar, daemon=True).start()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
