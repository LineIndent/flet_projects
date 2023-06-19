import flet as ft


def create_rail(number: int, title: list, funcOne: list, funcTwo: list):
    rail_list: list = [
        ft.Divider(height=35, color="transparent"),
    ]

    if number != 0:
        for index in range(number):
            rail_list.append(
                ft.Container(
                    content=ft.Text(
                        title[index],
                        size=12,
                        color=ft.colors.with_opacity(0.55, "white10"),
                    ),
                    on_click=funcOne[index],
                    on_hover=funcTwo[index],
                )
            )

        return rail_list

    else:
        pass
