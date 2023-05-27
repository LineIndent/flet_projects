""" Flet Dropdown Tutorial """

# modules
import flet
from flet import *


# the dropdown app will have two distinct parts : a top section and bottom section
#
# we'll start with the top
class MainContainer(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        # we'll return some basic title/subtitle UI
        return Container(
            width=275,
            height=60,
            content=Column(
                spacing=5,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(
                        "Modern Dropdown Control in Flet",
                        size=10,
                        weight="w400",
                        color="white54",
                    ),
                    Text(
                        "Line Indent",
                        size=30,
                        weight="bold",
                    ),
                ],
            ),
        )


# now we'll start laying out the second part of the dropdown app
class DropDownContainer(UserControl):
    def __init__(
        self,
        initials: str,
        name: str,
        gen: str,
        title: str,
        description: str,
        salary: str,
    ):
        self.initials = initials
        self.name = name
        self.gen = gen
        self.title = title
        self.description = description
        self.salary = salary
        super().__init__()

    # The dropdown contianer will have two parts ...

    # animate expansion of the contianer
    def ExpandContainer(self, e):
        if self.controls[0].height != 180:
            self.controls[0].height = 180
            self.controls[0].update()
        else:
            self.controls[0].height = 90
            self.controls[0].update()

    def TopContainer(self):
        return Container(
            width=265,
            height=70,
            content=Column(
                spacing=0,
                controls=[
                    Row(
                        controls=[
                            Container(
                                width=40,
                                height=40,
                                bgcolor="white24",
                                border_radius=40,
                                alignment=alignment.center,  # aligns content center...
                                content=Text(
                                    self.initials,  # pass args into class ...
                                    size=11,
                                    weight="bold",
                                ),
                            ),
                            VerticalDivider(width=2),
                            Container(
                                content=Column(
                                    spacing=1,
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        Text(self.name, size=11),
                                        Text(self.gen, size=9, color="white54"),
                                    ],
                                )
                            ),
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            Container(
                                content=IconButton(
                                    icon=icons.ARROW_DROP_DOWN_CIRCLE_ROUNDED,
                                    icon_size=20,
                                    on_click=lambda e: self.ExpandContainer(e),
                                )
                            )
                        ],
                    ),
                ],
            ),
        )

    # in order to miminize code UI, we'll use some logic to generate the employee data
    # this logic can be scaled up as well with a few minor tweeks...
    def GetEmployeeData(self):
        items = [
            ["Job Title", self.title],
            ["Description", self.description],
            ["Salary", self.salary],
        ]
        l = []  # empty list to return after append ...

        for item in items:
            l.append(
                Row(
                    controls=[
                        Column(
                            expand=1,  # 1:2 expand ratio
                            horizontal_alignment=CrossAxisAlignment.START,
                            controls=[
                                Text(
                                    item[0],  # first element of the first inner list
                                    size=9,
                                    weight="bold",
                                ),
                            ],
                        ),
                        Column(
                            expand=2,  # 1:2 expand ratio
                            horizontal_alignment=CrossAxisAlignment.END,
                            controls=[
                                Text(
                                    item[1],  # first element of the first inner list
                                    size=9,
                                    weight="bold",
                                    color="white54",
                                ),
                            ],
                        ),
                    ]
                )
            )
        return l  # return the list

    # now for the bottom container
    def BottomContainer(self):
        #  we can now unpack the list as such
        title, description, salary = self.GetEmployeeData()
        return Container(
            width=265,
            height=100,
            content=Column(
                spacing=12,
                controls=[
                    # add the unpacked list here ...
                    title,
                    description,
                    salary,
                ],
            ),
        )

    # what we return to the main function below ...
    def build(self):
        return Container(
            width=275,
            height=90,
            bgcolor="white10",
            border_radius=11,
            animate=animation.Animation(400, "decelerate"),
            padding=padding.only(left=10, right=10, top=10),
            # clip behavior allows us to clip the conents to the container,
            # this cancels out the overflow but it's costly production wise ...
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.TopContainer(),
                    self.BottomContainer(),
                ],
            ),
        )


# main function => run appp
def main(page: Page):
    page.title = "Flet Modern Dropdown"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    main_container = Container(
        width=280,
        height=600,
        bgcolor="black",
        border_radius=40,
        padding=20,
        content=Column(
            scroll="hidden",
            # add the classes here ...
            controls=[
                # dividers here ...
                Divider(height=20, color="transparent"),
                MainContainer(),
                Divider(height=30, color="white24"),
                Text("Employees", size=12),
                DropDownContainer(
                    "J.S",
                    "James T. Smith",
                    "Engineer",
                    "Senior Softeware Engineer II",
                    "Full Stack",
                    "$120,000",
                ),
                DropDownContainer(
                    "K.W",
                    "Keven W. White",
                    "Designer",
                    "UI/UX Engineer",
                    "Front End",
                    "$95,000",
                ),
                DropDownContainer(
                    "K.W",
                    "Kevin E. White",
                    "Designer",
                    "UI/UX Engineer",
                    "Front End",
                    "$95,000",
                ),
                DropDownContainer(
                    "A.H",
                    "Alta M. Howard",
                    "Engineer",
                    "Junior Softeware Engineer",
                    "Back End",
                    "$115,000",
                ),
            ],
        ),
    )
    page.add(main_container)
    page.update()
    pass


if __name__ == "__main__":
    flet.app(target=main)
