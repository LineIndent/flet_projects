""" Flet App """

"""
    In this video:
        1. Implement staack control.
        2. Hide/Show side navigation/menu
        3. Basic intro to listview and fitlering
        
"""

# modules
import flet
from flet import *
from navbar import (
    ModernNavBar,
)  # this module was build in a previous video, but I will provide the code


# we create the main stack class here
class MainStackContainer(UserControl):
    def __init__(self):
        super().__init__()

    # need a final function to hide the side menu when user clicks outside contianer
    def HideMenu(self, e):
        # main page control
        main = self.controls[0].content.controls[0].controls[0]
        # menu page control
        menu = self.controls[0].content.controls[1].controls[0]

        if menu.width == 185:
            menu.width = 0
            menu.border = None
            menu.update()

            main.opacity = 1
            main.update()

        else:
            pass

    def ShowMenu(self, e):
        # I'm going to get the control list index and set it to a variable to shroten the code
        # main page control
        main = self.controls[0].content.controls[0].controls[0]
        # menu page control
        menu = self.controls[0].content.controls[1].controls[0]

        if menu.width == 0:
            menu.width = 185
            menu.border = border.only(right=border.BorderSide(2, "purple300"))
            menu.update()

            main.opacity = 0.35
            main.update()

        else:
            menu.width = 0
            menu.border = None
            menu.update()

            main.opacity = 1
            main.update()

    def build(self):
        return Container(
            width=280,
            height=600,
            bgcolor="white",
            border_radius=32,
            border=border.all(8, "black"),
            padding=padding.only(top=25, left=5, right=5, bottom=25),
            content=Stack(
                expand=True,  # expand the stack control to fill the parent container
                controls=[
                    # we'll add the other classes here...
                    # this was the first page,
                    MainPage(self.ShowMenu, self.HideMenu),
                    # sidebar here...
                    MenuPage(self.ShowMenu),
                ],
            ),
        )


# The bottom stack should be the main page (the page that will show first)
class MainPage(UserControl):
    def __init__(self, function, function2):
        self.function = function
        self.function2 = function2
        super().__init__()

    # now we need a dummy list using ListView...
    def MakeList(self):
        dummy_list = ListView(
            expand=True,
            spacing=10,
            padding=20,
            auto_scroll=True,  # change this for auto scrolling to last item
        )

        for i in range(101):
            dummy_list.controls.append(
                Container(
                    alignment=alignment.center,
                    padding=8,
                    height=40,
                    bgcolor="#1d1d1d",
                    border_radius=8,
                    content=Text(i),
                    visible=True,
                    animate=animation.Animation(200, "decelerate"),
                )
            )

        return dummy_list

    # we can create a small method that helps filter odd and even numbers..
    def FilterList(self, e):
        # the checkbox return true if it's clicked, so...
        if e.data == "true":  # meaning it's been clicked
            # EVEN FILTER
            if e.control.label == "Even":  # if the box clicked has the label X
                # here we loop through the listView...
                for item in self.controls[0].content.controls[3].controls[:]:
                    # now we do some math to filter the evens
                    if (
                        item.content.value % 2 == 0
                    ):  # if the remainder is 0 (even numebr)
                        item.height = 0
                        item.update()
            # ODD FILTER
            if e.control.label == "Odd":  # if the box clicked has the label X
                # here we loop through the listView...
                for item in self.controls[0].content.controls[3].controls[:]:
                    # now we do some math to filter the evens
                    if (
                        item.content.value % 2 != 0  # if there is a remainder
                    ):  # if the remainder is 0 (even numebr)
                        item.height = 0
                        item.update()

        else:  # meaning it's been unclicked
            # EVEN FILTER
            if e.control.label == "Even":  # if the box clicked has the label X
                # here we loop through the listView...
                for item in self.controls[0].content.controls[3].controls[:]:
                    # now we do some math to filter the evens
                    if (
                        item.content.value % 2 == 0
                    ):  # if the remainder is 0 (even numebr)
                        item.height = 40
                        item.update()
            # ODD FILTER
            if e.control.label == "Odd":  # if the box clicked has the label X
                # here we loop through the listView...
                for item in self.controls[0].content.controls[3].controls[:]:
                    # now we do some math to filter the evens
                    if (
                        item.content.value % 2 != 0  # if there is a remainder
                    ):  # if the remainder is 0 (even numebr)
                        item.height = 40
                        item.update()

    # let's create a top bar with two checkboxes for fitlering
    def FilterBoxes(self):
        return Container(
            bgcolor="#1d1d1d",
            border_radius=8,
            content=Row(
                expand=True,
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Row(
                        spacing=0,
                        controls=[
                            Checkbox(
                                label="Odd",
                                fill_color="purple300",
                                on_change=lambda e: self.FilterList(e),
                            )
                        ],
                    ),
                    Row(
                        spacing=0,
                        controls=[
                            Checkbox(
                                label="Even",
                                fill_color="purple300",
                                on_change=lambda e: self.FilterList(e),
                            )
                        ],
                    ),
                ],
            ),
        )

    def build(self):
        return Container(
            expand=True,
            clip_behavior=ClipBehavior.HARD_EDGE,  # clip the content to prevent overflow
            opacity=1,
            animate_opacity=300,  # opacity is to create a blurred effect
            on_click=self.function2,  # add later...
            content=Column(
                controls=[
                    Row(
                        controls=[
                            Row(
                                expand=1,
                                alignment=MainAxisAlignment.START,
                                controls=[
                                    IconButton(
                                        icon=icons.MENU_ROUNDED,
                                        icon_size=15,
                                        icon_color="black",
                                        on_click=self.function,  # need to pass paramter here and in the menu class
                                    )
                                ],
                            ),
                            Row(
                                expand=3,
                                alignment=MainAxisAlignment.START,
                                controls=[
                                    Text(
                                        "Filter Your Data",
                                        size=15,
                                        color="black",
                                        weight="bold",
                                    )
                                ],
                            ),
                        ]
                    ),
                    Container(
                        padding=padding.only(left=15, right=15),
                        opacity=0.85,
                        content=Divider(height=5, color="black"),
                    ),
                    # add the components here ...
                    self.FilterBoxes(),
                    self.MakeList(),
                ]
            ),
        )


# The sidebar menu class
class MenuPage(UserControl):
    def __init__(self, function):
        self.function = function
        super().__init__()

    def build(self):
        return Container(
            width=0,
            bgcolor="white",
            animate=animation.Animation(400, "decelerate"),
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            Text(
                                # If a user wants a title ...
                            )
                        ]
                    ),
                    Column(expand=True, controls=[ModernNavBar()]),
                ],
            ),
        )


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "deeppurple200"

    page.add(MainStackContainer())
    page.update()


if __name__ == "__main__":
    flet.app(target=main)
