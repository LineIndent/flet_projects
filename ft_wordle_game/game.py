import flet
from flet import *

from nltk.corpus import words
from time import sleep
from random import choice

ROWS = []


def store_row_in_list(function):
    def wrapper(*args, **kwargs):
        res = function(*args, **kwargs)
        ROWS.append(res)
        return res

    return wrapper


class GameErrorHandler(UserControl):
    def __init__(self):
        super().__init__()

    @store_row_in_list
    def set_error_text(self):
        return Text(
            size=11,
            weight="bold",
        )

    def build(self):
        return Row(alignment=MainAxisAlignment.CENTER, controls=[self.set_error_text()])


class GameInputField(UserControl):
    def __init__(self, word: str):
        self.line = 0
        self.guess = 5
        self.word = word
        super().__init__()

    def get_letters(self, e):
        word = e.control.value
        is_word = e.control.value
        if len(word) == 5:
            if word in words.words():
                word = [*word]  # turn the characters into a list

                if is_word == self.word:
                    ROWS[6].value = f"CORRECT! The word is {self.word.upper()}"
                    ROWS[6].update()

                elif self.line > 5 or self.guess < 1:
                    ROWS[
                        6
                    ].value = f"Sorry, you ran out of tries. The word was {self.word.upper()}. Try again!"
                    ROWS[6].update()

                for index, box in enumerate(ROWS[self.line].controls[:]):
                    if word[index] in self.word:
                        if word[index] == self.word[index]:
                            box.content.value = word[index].upper()
                            box.content.offset = transform.Offset(0, 0)
                            box.content.opacity = 1
                            box.bgcolor = "green900"
                            box.update()
                            sleep(0.4)
                        else:
                            box.content.value = word[index].upper()
                            box.content.offset = transform.Offset(0, 0)
                            box.content.opacity = 1
                            box.bgcolor = "#b59e38"
                            box.update()
                            sleep(0.4)
                    else:
                        box.content.value = word[index].upper()
                        box.content.offset = transform.Offset(0, 0)
                        box.content.opacity = 1
                        box.update()
                        sleep(0.4)

                self.line += 1
                self.guess -= 1

            else:
                ROWS[6].value = "Must be a valid word. Try again!"
                ROWS[6].update()
        else:
            ROWS[6].value = "Word must be 5 letters long. Try Again!"
            ROWS[6].update()

        e.control.value = ""
        e.control.update()

    def clear_error(self, e):
        ROWS[6].value = ""
        ROWS[6].update()

    def build(self):
        return Row(
            spacing=20,
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Container(
                    height=45,
                    width=250,
                    border=border.all(0.5, colors.WHITE24),
                    border_radius=6,
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        controls=[
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
                                hint_text="Type a 5-letter word ...",
                                text_align="center",
                                hint_style=TextStyle(
                                    size=11,
                                ),
                                on_submit=lambda e: self.get_letters(e),
                                on_focus=lambda e: self.clear_error(e),
                            ),
                        ],
                    ),
                ),
            ],
        )


class GameGrid(UserControl):
    def __init__(self):
        super().__init__()

    @store_row_in_list
    def create_single_row_grid(self):
        row = Row(alignment=MainAxisAlignment.CENTER)
        for __ in range(5):
            row.controls.append(
                Container(
                    width=52,
                    height=52,
                    border=border.all(0.5, "white24"),
                    alignment=alignment.center,
                    clip_behavior=ClipBehavior.HARD_EDGE,
                    animate=animation.Animation(300, "decelerate"),
                    content=Text(
                        size=20,
                        weight="bold",
                        opacity=0,
                        offset=transform.Offset(0, 0.75),
                        animate_opacity=animation.Animation(400, "decelerate"),
                        animate_offset=animation.Animation(400, "decelerate"),
                    ),
                )
            )
        return row

    def build(self):
        return Column(
            controls=[
                self.create_single_row_grid(),
                self.create_single_row_grid(),
                self.create_single_row_grid(),
                self.create_single_row_grid(),
                self.create_single_row_grid(),
                self.create_single_row_grid(),
            ],
        )


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    #
    word = words.words()
    word = list(filter(lambda x: len(x) == 5, word))
    word = choice(word).lower()
    #
    page.add(
        Column(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[Text("WORDLE", size=25, weight="bold")],
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Text(
                            "Popular Word Game Clone Using Python & Flet",
                            size=11,
                            weight="bold",
                            color=colors.WHITE54,
                        )
                    ],
                ),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Text(
                            "Game Rules\n1. Green: Correct letter & position.\n2. Yellow: Correct letter but inccorect position.\n3. Black: Letter is not in word.",
                            size=11,
                            weight="bold",
                            color=colors.WHITE54,
                        )
                    ],
                ),
                Divider(height=20, color="transparent"),
                GameGrid(),
                Divider(height=10, color="transparent"),
                GameInputField(word),
                Divider(height=10, color="transparent"),
                GameErrorHandler(),
            ],
        )
    )
    #
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
