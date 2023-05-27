import flet
from flet import *
import re

CONTROLS = []
STATUS = []


def store_control_sub_reference(function):
    def wrapper(*args, **kwargs):
        reference = function(*args, **kwargs)
        locals()["kwargs"]["control"]
        if kwargs["control"] == 0:
            CONTROLS.append(reference)
        else:
            STATUS.append(reference)
        return reference

    return wrapper


class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
        self.common_passwords = ["password", "1234", "admin", "qwerty"]
        self.complexity_regex = re.compile(
            r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])"
        )

    def length_check(self):
        length = len(self.password)
        if length > 0 and length < 8:
            return 0
        elif length >= 8 and length < 12:
            return 1
        elif length >= 12 and length < 16:
            return 2
        elif length >= 16:
            return 3

    def character_check(self):
        characters = set(self.password)
        lower_case = set("abcdefghijklmnopqrstuvwxyz")
        upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        digits = set("0123456789")
        special_characters = set("!@#$%^&*()_+-=[]{};:,.<>/?`~")

        score = 0
        if any(char in lower_case for char in characters):
            score += 1
        if any(char in upper_case for char in characters):
            score += 1
        if any(char in digits for char in characters):
            score += 1
        if any(char in special_characters for char in characters):
            score += 1

        if score == 1:
            return 0
        elif score == 2:
            return 1
        elif score == 3:
            return 2
        elif score == 4:
            return 3

    def repeat_check(self):
        if len(self.password) == 0:
            return 2
        else:
            for i in range(len(self.password) - 2):
                if self.password[i] == self.password[i + 1] == self.password[i + 2]:
                    return 0
            return 1

    def sequential_check(self):
        if len(self.password) == 0:
            return 2
        else:
            for i in range(len(self.password) - 2):
                if (
                    self.password[i : i + 3].isdigit()
                    or self.password[i : i + 3].islower()
                    or self.password[i : i + 3].isupper()
                ):
                    return 0
            return 1


class AppWindow(UserControl):
    def __init__(self):
        super().__init__()

    def passowrd_status_okay(self, index, status):
        if status == 3:
            STATUS[index].controls[0].offset = transform.Offset(0, 0)
            STATUS[index].controls[0].opacity = 1
            STATUS[index].controls[0].content.value = True
            STATUS[index].controls[0].update()
        else:
            STATUS[index].controls[0].content.value = False
            STATUS[index].controls[0].offset = transform.Offset(-0.5, 0)
            STATUS[index].controls[0].opacity = 0
            STATUS[index].controls[0].update()

    def passowrd_length_status(self, strength):
        if strength == 0:
            CONTROLS[0].controls[1].controls[0].bgcolor = "red"
            CONTROLS[0].controls[1].controls[0].width = 40
        elif strength == 1:
            CONTROLS[0].controls[1].controls[0].bgcolor = "yellow"
            CONTROLS[0].controls[1].controls[0].width = 70
        elif strength == 2:
            CONTROLS[0].controls[1].controls[0].bgcolor = "green400"
            CONTROLS[0].controls[1].controls[0].width = 100
        elif strength == 3:
            CONTROLS[0].controls[1].controls[0].bgcolor = "green900"
            CONTROLS[0].controls[1].controls[0].width = 130
        else:
            CONTROLS[0].controls[1].controls[0].width = 0

        CONTROLS[0].controls[1].controls[0].opacity = 1
        CONTROLS[0].controls[1].controls[0].update()

        return self.passowrd_status_okay(0, strength)

    def character_check_status(self, strength):
        if strength == 0:
            CONTROLS[1].controls[1].controls[0].bgcolor = "red"
            CONTROLS[1].controls[1].controls[0].width = 40
        elif strength == 1:
            CONTROLS[1].controls[1].controls[0].bgcolor = "yellow"
            CONTROLS[1].controls[1].controls[0].width = 70
        elif strength == 2:
            CONTROLS[1].controls[1].controls[0].bgcolor = "green400"
            CONTROLS[1].controls[1].controls[0].width = 100
        elif strength == 3:
            CONTROLS[1].controls[1].controls[0].bgcolor = "green900"
            CONTROLS[1].controls[1].controls[0].width = 130
        else:
            CONTROLS[1].controls[1].controls[0].width = 0

        CONTROLS[1].controls[1].controls[0].opacity = 1
        CONTROLS[1].controls[1].controls[0].update()

        return self.passowrd_status_okay(1, strength)

    def repeat_check_status(self, strength):
        if strength == 0:
            CONTROLS[2].controls[1].controls[0].bgcolor = "red"
            CONTROLS[2].controls[1].controls[0].width = 65
        elif strength == 1:
            CONTROLS[2].controls[1].controls[0].bgcolor = "green900"
            CONTROLS[2].controls[1].controls[0].width = 130
        else:
            CONTROLS[2].controls[1].controls[0].width = 0

        CONTROLS[2].controls[1].controls[0].opacity = 1
        CONTROLS[2].controls[1].controls[0].update()

        if strength == 1:
            strength = 3
            return self.passowrd_status_okay(2, strength)
        else:
            return self.passowrd_status_okay(2, strength)

    def sequential_check_status(self, strength):
        if strength == 0:
            CONTROLS[3].controls[1].controls[0].bgcolor = "red"
            CONTROLS[3].controls[1].controls[0].width = 65
        elif strength == 1:
            CONTROLS[3].controls[1].controls[0].bgcolor = "green900"
            CONTROLS[3].controls[1].controls[0].width = 130
        else:
            CONTROLS[3].controls[1].controls[0].width = 0

        CONTROLS[3].controls[1].controls[0].opacity = 1
        CONTROLS[3].controls[1].controls[0].update()

        if strength == 1:
            strength = 3
            return self.passowrd_status_okay(3, strength)
        else:
            return self.passowrd_status_okay(3, strength)

    def check_password(self, e):
        password_strength_checker = PasswordStrengthChecker(e.data)

        password_length = password_strength_checker.length_check()
        self.passowrd_length_status(password_length)

        character_check = password_strength_checker.character_check()
        self.character_check_status(character_check)

        repeat_check = password_strength_checker.repeat_check()
        self.repeat_check_status(repeat_check)

        sequential_check = password_strength_checker.sequential_check()
        self.sequential_check_status(sequential_check)

    def password_text_field_display(self):
        return Row(
            spacing=20,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Icon(
                    name=icons.LOCK_OUTLINE_ROUNDED,
                    size=14,
                    opacity=0.85,
                ),
                TextField(
                    border_color="transparent",
                    bgcolor="transparent",
                    height=20,
                    width=200,
                    text_size=12,
                    content_padding=3,
                    cursor_color="white",
                    cursor_width=1,
                    color="white",
                    hint_text="Start typing a password ...",
                    hint_style=TextStyle(
                        size=11,
                    ),
                    on_change=lambda e: self.check_password(e),
                    password=True,
                ),
            ],
        )

    @store_control_sub_reference
    def check_criteria_display(self, criteria, description, control: int):
        return Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            spacing=5,
            controls=[
                Column(
                    spacing=2,
                    controls=[
                        Text(value=criteria, size=13, weight="bold"),
                        Text(value=description, size=9, color="white54"),
                    ],
                ),
                Row(
                    spacing=0,
                    alignment=MainAxisAlignment.START,
                    controls=[
                        Container(
                            height=5,
                            opacity=0,
                            animate=350,
                            border_radius=10,
                            animate_opacity=animation.Animation(350, "decelerate"),
                        ),
                    ],
                ),
            ],
        )

    @store_control_sub_reference
    def check_status_display(self, control: int):
        return Row(
            alignment=MainAxisAlignment.END,
            controls=[
                Container(
                    opacity=0,
                    offset=transform.Offset(-0.5, 0),
                    animate_offset=animation.Animation(800, "decelerate"),
                    animate_opacity=animation.Animation(800, "decelerate"),
                    border_radius=50,
                    width=21,
                    height=21,
                    alignment=alignment.center,
                    content=Checkbox(
                        scale=Scale(0.7),
                        fill_color="#7df6dd",
                        check_color="black",
                        disabled=True,
                    ),
                )
            ],
        )

    def password_strength_display(self):
        return Container(
            width=350,
            height=400,
            bgcolor="#1f262f",
            border_radius=10,
            padding=10,
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=2,
                controls=[
                    Divider(height=5, color="transparent"),
                    Text("Password Strength Check", size=21, weight="bold"),
                    Text(
                        "Type in a password and see how strong it is!",
                        size=11,
                        color="white54",
                        weight="w400",
                    ),
                    Divider(height=25, color="transparent"),
                    self.check_criteria_display(
                        "1. Length Check",
                        "Strong passwords are 12 char. or more.",
                        control=0,
                    ),
                    self.check_status_display(control=1),
                    Divider(height=10, color="transparent"),
                    self.check_criteria_display(
                        "2. Character Check",
                        "Upper, lower, and special characters.",
                        control=0,
                    ),
                    self.check_status_display(control=1),
                    Divider(height=10, color="transparent"),
                    self.check_criteria_display(
                        "3. Repeat Check",
                        "Check for any repetition (3+).",
                        control=0,
                    ),
                    self.check_status_display(control=1),
                    Divider(height=10, color="transparent"),
                    self.check_criteria_display(
                        "4. Sequential Check",
                        "Check for sequential strings.",
                        control=0,
                    ),
                    self.check_status_display(control=1),
                ],
            ),
        )

    def password_input_display(self):
        return Card(
            width=300,
            height=60,
            elevation=11,
            offset=transform.Offset(0, -0.25),
            content=Container(
                padding=padding.only(left=15),
                content=Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        self.password_text_field_display(),
                        IconButton(
                            icon=icons.COPY,
                            icon_size=16,
                        ),
                    ],
                ),
            ),
        )

    def build(self):
        return Card(
            elevation=20,
            content=Container(
                scale=Scale(1.05),
                width=400,
                height=420,
                border_radius=10,
                bgcolor="#1f262f",
                content=Column(
                    spacing=0,
                    horizontal_alignment="center",
                    controls=[
                        self.password_strength_display(),
                        self.password_input_display(),
                    ],
                ),
            ),
        )


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#212328"
    page.add(AppWindow())
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
