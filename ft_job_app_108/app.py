""" Flet Job App """

# modules
import flet as ft
import aiohttp
import asyncio


# now create the individual components for the application
class JobEntry(ft.Container):
    def __init__(
        self,
        job_area,
        col={"xs": 12, "sm": 12, "md": 12, "lg": 12, "xl": 11},
        expand=True,
    ):
        super().__init__(col=col, expand=expand)

        self.job_area = job_area

        self.input_query = ft.TextField(
            border_color="transparent",
            height=50,
            on_submit=lambda e: asyncio.run(self.run_compilation(e)),
        )

        self.loader = ft.ProgressBar(
            value=0,
            bar_height=1.25,
            bgcolor="transparent",
            color="#64b687",
        )

        self.grid = ft.GridView(
            expand=True,
            runs_count=5,
            max_extent=350,
            child_aspect_ratio=1,
            spacing=45,
            run_spacing=45,
        )

        self.column = ft.Column(
            horizontal_alignment="center",
            spacing=0,
            controls=[
                ft.Divider(height=20, color="transparent"),
                ft.Container(
                    content=ft.Row(
                        spacing=4,
                        alignment="center",
                        controls=[
                            # title
                            ft.Column(
                                alignment="center",
                                horizontal_alignment="start",
                                controls=[
                                    ft.Text(
                                        "PySearch",
                                        style=ft.TextThemeStyle("headlineMedium"),
                                        weight="bold",
                                    ),
                                ],
                            ),
                            ft.Column(
                                alignment="center",
                                horizontal_alignment="start",
                                controls=[
                                    ft.Text(
                                        "- Search Engine",
                                        style=ft.TextThemeStyle("headlineMedium"),
                                        weight="bold",
                                    ),
                                ],
                            ),
                        ],
                    )
                ),
                ft.Divider(height=20, color="transparent"),
                # text field
                ft.Container(
                    content=self.input_query,
                    height=50,
                    border=ft.border.all(1, "#64b687"),
                    border_radius=6,
                    shadow=ft.BoxShadow(
                        spread_radius=8,
                        blur_radius=16,
                        color=ft.colors.with_opacity(0.25, "black"),
                        offset=(5, 5),
                    ),
                ),
                ft.Divider(height=20, color="transparent"),
                self.loader,
            ],
        )

        self.content = self.column

    # we'll be running the logic via async to make the application smooth for the UX
    async def run_compilation(self, e):
        # let's make the app a little more UX friendly
        await self.remove_results()
        await asyncio.gather(self.run_loader(), self.get_data())
        await asyncio.sleep(2)
        await self.stop_loader()
        await self.show_results()

    async def run_loader(self):
        self.loader.value = True
        self.loader.update()

    async def stop_loader(self):
        self.loader.value = 0
        self.loader.update()

    async def show_results(self):
        for container in self.grid.controls[:]:
            container.opacity = 1
            container.update()

    async def remove_results(self):
        for container in self.grid.controls[:]:
            container.opacity = 0
            container.update()

    # let's add some UI to the ssearch compoenent
    def highlight_box(self, e):
        for index, container in enumerate(self.grid.controls[:]):
            if e.control.data != index:
                if e.data == "true":
                    container.opacity = 0.25
                else:
                    container.opacity = 1

                container.update()

    def redirect_to_url(self, e, route):
        e.page.launch_url(route)

    def custom_text(self, title, subtitle):
        return ft.Text(
            title,
            weight="bold",
            size=14,
            overflow=ft.TextOverflow.ELLIPSIS,
            spans=[ft.TextSpan(text=subtitle, style=ft.TextStyle(weight="w300"))],
        )

    # let's work the main logic first then add the UI-based logic later
    # the following async method gets data from a custom API
    async def get_data(self):
        temp_list = []
        async with aiohttp.ClientSession() as session:
            # this PAI link is a custom endpoint that contians many real life python related job ads.
            async with session.get("https://api-pourhakimi.vercel.app/") as response:
                res = await response.json()

                # now we can loop the JSON data and create a UI for each individual data point
                for index, __ in enumerate(res["data"]):
                    temp_list.append(
                        ft.Container(
                            on_hover=lambda e: self.highlight_box(e),
                            # on long press, the user can be directed to the job ad
                            on_long_press=lambda e, route=res["data"][index][
                                "job_apply_link"
                            ]: self.redirect_to_url(e, route),
                            opacity=0,
                            animate_opacity=ft.Animation(700, "ease"),
                            data=index,
                            border=ft.border.all(1, "#64b687"),
                            border_radius=6,
                            padding=30,
                            shadow=ft.BoxShadow(
                                spread_radius=8,
                                blur_radius=16,
                                color=ft.colors.with_opacity(0.25, "black"),
                                offset=(5, 5),
                            ),
                            content=ft.Column(
                                alignment="spaceBetween",
                                spacing=0,
                                controls=[
                                    # we can now add the data in this column
                                    self.custom_text(
                                        "Title: ",
                                        res["data"][index]["job_title"].capitalize(),
                                    ),
                                    self.custom_text(
                                        "Employer: ",
                                        res["data"][index][
                                            "employer_name"
                                        ].capitalize(),
                                    ),
                                    self.custom_text(
                                        "Employment Type: ",
                                        res["data"][index][
                                            "job_employment_type"
                                        ].capitalize(),
                                    ),
                                    self.custom_text(
                                        "Description: ",
                                        res["data"][index]["job_description"].replace(
                                            "\n", ""
                                        ),
                                    ),
                                    # note that the response tags can also be  changed and there are many more data that can be extracted from the API **
                                ],
                            ),
                        )
                    )

        # we set the grid controls list to the temp list(updated)
        self.grid.controls = temp_list
        # put self.grid as the content for the first compoenent
        self.job_area.content = self.grid
        self.job_area.update()


class JobSearchResult(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        col={"xs": 12, "sm": 12, "md": 12, "lg": 12, "xl": 11},
        alignment=ft.alignment.center,
    ):
        super().__init__(col=col, alignment=alignment)
        self.page = page
        self.height = self.page.height


# create a class called app to gather all application componenets


class App(ft.UserControl):
    def __init__(
        self,
        page: ft.Page,
    ):
        self.page = page
        self.job_result = JobSearchResult(self.page)
        self.job_entry = JobEntry(self.job_result)
        self.row = ft.ResponsiveRow(
            alignment="center",
            vertical_alignment="center",
        )
        super().__init__()

    def build(self):
        self.row.controls.append(self.job_entry)
        self.row.controls.append(ft.VerticalDivider(width=25, color="transparent"))
        self.row.controls.append(self.job_result)
        return self.row


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#1f262f"
    page.padding = 35

    theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thickness=3,
            radius=10,
            main_axis_margin=-20,
            thumb_color="#64b687",
        )
    )

    page.theme = theme

    app = App(page)
    page.add(app)
    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
