from datetime import datetime
import reflex as rx
import calendar

cal = calendar.Calendar()

# some dummy data for UI purposes
dummyData = {
    "2023-11-1": "rgba(255, 255, 255, 0.05)",
    "2023-11-2": "rgba(0, 255, 0, 0.35)",
    "2023-11-3": "rgba(0, 255, 0, 75)",
    "2023-11-4": "rgba(0, 255, 0, 75)",
    "2023-11-5": "rgba(255, 255, 255, 0.05)",
    "2023-11-6": "rgba(255, 255, 255, 0.05)",
    "2023-11-7": "rgba(255, 255, 255, 0.05)",
    "2023-11-8": "rgba(255, 255, 255, 0.05)",
    "2023-11-9": "rgba(255, 255, 255, 0.05)",
    "2023-11-10": "rgba(0, 255, 0, 0.25)",
    "2023-11-11": "rgba(255, 255, 255, 0.05)",
    "2023-11-12": "rgba(255, 255, 255, 0.05)",
    "2023-11-13": "rgba(255, 255, 255, 0.05)",
    "2023-11-14": "rgba(0, 255, 0, 0.35)",
    "2023-11-15": "rgba(255, 255, 255, 0.05)",
    "2023-11-16": "rgba(0, 255, 0, 0.35)",
    "2023-11-17": "rgba(0, 255, 0, 0.35)",
    "2023-11-18": "rgba(255, 255, 255, 0.05)",
    "2023-11-19": "rgba(255, 255, 255, 0.05)",
    "2023-11-20": "rgba(0, 255, 0, 0.35)",
    "2023-11-21": "rgba(0, 255, 0, 75)",
    "2023-11-22": "rgba(0, 255, 0, 0.35)",
    "2023-11-23": "rgba(0, 255, 0, 0.35)",
    "2023-11-24": "rgba(0, 255, 0, 0.35)",
    "2023-11-25": "rgba(255, 255, 255, 0.05)",
    "2023-11-26": "rgba(0, 255, 0, 0.55)",
    "2023-11-27": "rgba(0, 255, 0, 0.55)",
    "2023-11-28": "rgba(255, 255, 255, 0.05)",
    "2023-11-29": "rgba(255, 255, 255, 0.05)",
    "2023-11-30": "rgba(255, 255, 255, 0.05)",
    "2023-12-1": "rgba(255, 255, 255, 0.05)",
    "2023-12-2": "rgba(255, 255, 255, 0.05)",
    "2023-12-3": "rgba(0, 255, 0, 0.55)",
    "2023-12-4": "rgba(0, 255, 0, 0.55)",
    "2023-12-5": "rgba(255, 255, 255, 0.05)",
    "2023-12-6": "rgba(0, 255, 0, 0.25)",
    "2023-12-7": "rgba(0, 255, 0, 0.35)",
    "2023-12-8": "rgba(0, 255, 0, 0.35)",
    "2023-12-9": "rgba(0, 255, 0, 75)",
    "2023-12-10": "rgba(0, 255, 0, 0.35)",
    "2023-12-11": "rgba(255, 255, 255, 0.05)",
    "2023-12-12": "rgba(255, 255, 255, 0.05)",
    "2023-12-13": "rgba(255, 255, 255, 0.05)",
    "2023-12-14": "rgba(255, 255, 255, 0.05)",
    "2023-12-15": "rgba(255, 255, 255, 0.05)",
    "2023-12-16": "rgba(0, 255, 0, 0.55)",
    "2023-12-17": "rgba(0, 255, 0, 0.25)",
    "2023-12-18": "rgba(0, 255, 0, 0.35)",
    "2023-12-19": "rgba(0, 255, 0, 75)",
    "2023-12-20": "rgba(255, 255, 255, 0.05)",
    "2023-12-21": "rgba(255, 255, 255, 0.05)",
    "2023-12-22": "rgba(0, 255, 0, 0.55)",
    "2023-12-23": "rgba(255, 255, 255, 0.05)",
    "2023-12-24": "rgba(0, 255, 0, 75)",
    "2023-12-25": "rgba(255, 255, 255, 0.05)",
    "2023-12-26": "rgba(0, 255, 0, 0.55)",
    "2023-12-27": "rgba(0, 255, 0, 0.35)",
    "2023-12-28": "rgba(255, 255, 255, 0.05)",
    "2023-12-29": "rgba(255, 255, 255, 0.05)",
    "2023-12-30": "rgba(0, 255, 0, 75)",
    "2023-12-31": "rgba(255, 255, 255, 0.05)",
    "2024-1-1": "rgba(255, 255, 255, 0.05)",
    "2024-1-2": "rgba(0, 255, 0, 0.25)",
    "2024-1-3": "rgba(255, 255, 255, 0.05)",
    "2024-1-4": "rgba(255, 255, 255, 0.05)",
    "2024-1-5": "rgba(255, 255, 255, 0.05)",
    "2024-1-6": "rgba(255, 255, 255, 0.05)",
    "2024-1-7": "rgba(0, 255, 0, 0.55)",
    "2024-1-8": "rgba(0, 255, 0, 75)",
    "2024-1-9": "rgba(255, 255, 255, 0.05)",
}

# define a set of heat signature colors
colors = [
    "rgba(255, 255, 255, 0.05)",
    "rgba(0, 255, 0, 0.25)",
    "rgba(0, 255, 0, 0.35)",
    "rgba(0, 255, 0, 0.55)",
    "rgba(0, 255, 0, 75)",
]


class State(rx.State):
    year: int = datetime.now().year
    month: int = datetime.now().month

    calendar_data: list[list[str]]

    # define a method to clear calendar data
    def clear_calendar_grid(self):
        self.calendar_data = []

    # define a method to populate the grid
    def get_calendar_data(self):
        self.clear_calendar_grid()

        for week in cal.monthdayscalendar(self.year, self.month):
            temp_list: list = []
            for day in week:
                if day != 0:
                    if f"{self.year}-{self.month}-{day}" in dummyData:
                        temp_list.append(
                            [str(day), dummyData[f"{self.year}-{self.month}-{day}"]]
                        )

                    else:
                        temp_list.append([str(day), "rgba(255, 255, 255, 0.05)"])

                else:
                    temp_list.append([" ", "none"])

            self.calendar_data.append(temp_list)

    # define month classes as per Python calendar module
    month_class: dict[int, str] = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    # define days of the week
    date_class: dict[int, str] = {
        0: "Mo",
        1: "Tu",
        2: "We",
        3: "Th",
        4: "Fr",
        5: "Sa",
        6: "Su",
    }

    # define method to change month (and eyar)
    def delta_calendar(self, delta: int):
        if delta == 1:
            if self.month + delta > 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1

        if delta == -1:
            if self.month + delta < 1:
                self.month = 12
                self.year -= 1

            else:
                self.month -= 1

        self.clear_calendar_grid()
        self.get_calendar_data()

    task_form_toggle: bool = False
    task_input: str = "Enter a new task ..."

    # define a method to toggle open/close form
    def change(self):
        self.task_form_toggle = not (self.task_form_toggle)

    # define method to update input value
    def set_text(self, task_input):
        self.task_input = task_input

    task_list: dict[str, bool]
    completed_tasks: int

    # first, define method to add task to task list
    def add_task_to_list(self):
        self.task_list[self.task_input] = False
        self.task_input = ""

    # define a method to keep track of compelted tasks
    def get_completed_tasks(self, delta: bool):
        self.completed_tasks += 1 if delta is True else -1

    # define a method to change heat map of current day
    # based on completed tasks
    def change_heat_map(self, data):
        for item in self.task_list:
            if item == data[0]:
                data[1] = not (data[1])
                self.task_list[item] = data[1]
                self.get_completed_tasks(data[1])
                yield

        self.update_day_color()

    # finaly, define a method to update the UI
    def update_day_color(self):
        outer_list: list = []
        for weeks in self.calendar_data:
            inner_list: list = []
            for day in weeks:
                # check to see if it's today
                if day[0] == str(datetime.now().day):
                    # set the gradient color based on the number of copleted tasks
                    day[1] = colors[self.completed_tasks]
                    inner_list.append(day)

                else:
                    inner_list.append(day)

            outer_list.append(inner_list)

        self.calendar_data = outer_list


cal_days_style = {
    "width": "50px",
    "height": "50px",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "border_radius": "6px",
}


# define method to return text
def calendar_days(data):
    return rx.container(
        rx.text(data[1], font_size="16px", font_weight="bold"),
        style=cal_days_style,
    )


# define a method to toggle form
def task_form():
    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_body(
                    rx.input(
                        value=State.task_input,
                        on_change=State.set_text,
                    )
                ),
                rx.hstack(
                    rx.modal_footer(
                        rx.button("Close"),
                        on_click=State.change,
                    ),
                    rx.modal_footer(
                        rx.button(
                            "Add",
                            on_click=State.add_task_to_list,
                        ),
                    ),
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                padding="0.75rem",
            )
        ),
        is_open=State.task_form_toggle,
    )


cal_row_style = {
    "width": "50px",
    "height": "50px",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "border_radius": "6px",
}


def calendar_grid_row(data: list[str]):
    return rx.container(
        rx.text(data[0], font_size="14px"),
        background_color=data[1],
        style=cal_row_style,
    )


# deinfe method to return grid UI
def calendar_grid(data):
    return rx.vstack(
        rx.hstack(rx.foreach(data, calendar_grid_row)),
    )


# define a method to dispay the tasks
def task_row(data: dict):
    return rx.checkbox(
        data[0],
        size="lg",
        color_scheme="green",
        is_checked=data[1],
        on_blur=State.change_heat_map(data),
    )


@rx.page(route="/", on_load=State.get_calendar_data)
def index() -> rx.Component:
    return rx.vstack(
        # form
        task_form(),
        # dark/light toggle && form
        rx.hstack(
            rx.icon(tag="add", cursor="pointer", on_click=State.change),
            rx.color_mode_button(
                rx.color_mode_icon(),
                color_scheme="none",
                _dark={"color": "white"},
                _light={"color": "black"},
            ),
            width="100%",
            display="flex",
            justify_content="end",
            padding="0.75rem 2rem",
        ),
        # calendar start ...
        rx.hstack(
            rx.icon(
                tag="chevron_left", cursor="pointer", on_click=State.delta_calendar(-1)
            ),
            rx.spacer(),
            rx.text(
                f"{State.month_class[State.month]} {State.year}",
                width="150px",
                display="flex",
                justify_content="center",
            ),
            rx.spacer(),
            rx.icon(
                tag="chevron_right", cursor="pointer", on_click=State.delta_calendar(1)
            ),
            display="flex",
            align_items="center",
            justify_content="center",
            spacing="2rem",
        ),
        rx.hstack(
            # calendar days of the wekk
            rx.foreach(
                State.date_class,
                calendar_days,
            ),
        ),
        # calendar grid ...
        rx.foreach(
            State.calendar_data,
            calendar_grid,
        ),
        # task section
        rx.hstack(
            rx.foreach(
                State.task_list,
                task_row,
            ),
            padding="2rem 0rem",
            spacing="25px",
        ),
    )


app = rx.App()
