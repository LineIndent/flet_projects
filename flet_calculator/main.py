import flet
from flet import *

from cardGen import CardGenerator
from custom_title_bar import CustomTitleBar
from data import ReturnData


def main(page: Page):

    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True

    _title_bar_ = CustomTitleBar()

    _main_contianer = Container(
        expand=True,
        margin=-10,
        gradient=RadialGradient(
            center=Alignment(0, -1.25),
            radius=1.4,
            colors=[
                "#42445f",
                "#393b52",
                "#33354a",
                "#2f3143",
                "#292b3c",
                "#222331",
                "#1a1a25",
                "#1a1b26",
                "#21222f",
                "#1d1e2a",
            ],
        ),
        padding=15,
        content=Column(
            expand=True,
            controls=[
                _title_bar_,
                Row(
                    expand=True,
                    alignment="center",
                    vertical_alignment="end",
                    spacing=40,
                ),
                Container(padding=padding.only(bottom=100)),
            ],
        ),
    )

    dic = ReturnData()
    for key in dic:
        _test = CardGenerator(
            dic[key]["colors"],
            dic[key]["title"],
            dic[key]["subtitle"],
            dic[key]["price"],
            dic[key]["icon"],
            dic[key]["card_icon"],
            dic[key]["card_type"],
            dic[key]["card_number"],
        )

        _main_contianer.content.controls[1].controls.append(_test)

    page.add(_main_contianer)

    page.update()


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
