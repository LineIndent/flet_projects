import flet as ft


# create the landing class ...
class Landing(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            padding=ft.padding.only(top=0, left=20, right=20, bottom=15),
            col={"sm": 12, "md": 12, "lg": 6},
        )

        self.title = ft.Text(
            "LineHub: Explore, Share, and Learn Every Line Counts", size=30
        )

        self.subtitle = ft.Text(
            "Have something intresting to share? Fill out the form and add your links so others can see and learn!",
            size=15,
        )

        self.content = ft.Column([self.title, self.subtitle], expand=True)


# create FORM state class
class FormData:
    tags: list[list[str]] = [
        ["Programming", "white10"],
        ["Engineering", "white10"],
        ["Software", "white10"],
        ["DataScience", "white10"],
        ["Robotics", "white10"],
        ["MachineLearning", "white10"],
        ["AI", "white10"],
        ["WebDev", "white10"],
        ["Electronics", "white10"],
        ["Cybersecurity", "white10"],
        ["Mathematics", "white10"],
        ["Physics", "white10"],
        ["Biotechnology", "white10"],
        ["ComputerVision", "white10"],
        ["IoT", "white10"],
        ["Database", "white10"],
    ]

    # METHOD: update on click tags ...
    @staticmethod
    def update_tags(tag: list[str], instance: object):
        new_tag = [tag[0], ft.colors.with_opacity(0.61, "green")]

        FormData.tags = [
            new_tag if item[0] == new_tag[0] else [item[0], "white10"]
            for item in FormData.tags
        ]

        instance.tags.controls = instance.render_tags()
        instance.tags.update()


# create the form class ...
class Form(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True, border=ft.border.all(1, "white10"), padding=20, border_radius=6
        )

        self.title = ft.TextField(bgcolor="transparent")
        self.tags = ft.Row(self.render_tags(), wrap=True)

        self.name = ft.TextField(bgcolor="transparent", expand=1)
        self.link = ft.TextField(bgcolor="transparent", expand=2)

        self.commit = ft.TextButton(
            "Commit Line!",
            height=45,
        )

        self.content = ft.Column(
            [
                ft.Text("Say Something"),
                self.title,
                ft.Divider(height=10, color="transparent"),
                #
                ft.Text("Select Tag"),
                self.tags,
                ft.Divider(height=10, color="transparent"),
                #
                ft.Text("Add Media"),
                ft.Row([self.name, self.link]),
                ft.Divider(height=10, color="transparent"),
                #
                ft.Row([self.commit], alignment="center"),
            ]
        )

    # method: render tags ...
    def render_tags(self):
        return [
            ft.Container(
                ft.Text(name, size=11, weight="w300"),
                bgcolor=bgcolor,
                padding=6,
                border_radius=4,
                animate=ft.Animation(1000, "decelerate"),
                # set on click method ,,,
                on_click=lambda _, name=name, bgcolor=bgcolor: FormData.update_tags(
                    [name, bgcolor], self
                ),
            )
            for name, bgcolor in FormData.tags
        ]


def main(page: ft.Page):
    page.add(
        ft.SafeArea(
            ft.Stack(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Divider(height=10, color="transparent"),
                                ft.Container(
                                    content=ft.ResponsiveRow(
                                        controls=[
                                            # Landing ...
                                            Landing(),
                                            ft.Container(
                                                # form ...
                                                Form(),
                                                padding=ft.padding.only(
                                                    left=20, right=20
                                                ),
                                                col={"sm": 12, "md": 12, "lg": 6},
                                            ),
                                        ],
                                        vertical_alignment="center",
                                    ),
                                    border=ft.border.only(
                                        top=ft.BorderSide(2, "white10"),
                                        bottom=ft.BorderSide(2, "white10"),
                                    ),
                                    padding=ft.padding.only(top=20, bottom=20),
                                ),
                            ],
                        )
                    )
                ],
                expand=True,
            )
        )
    )


ft.app(main)
