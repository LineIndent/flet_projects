import flet as ft
from bs4 import BeautifulSoup
import httpx
import asyncio
from math import pi


class RepoData(ft.Row):
    def __init__(
        self,
        docs: dict,
        alignment="start",
        vertical_alignment="center",
    ):
        self.docs = docs
        self.repo = self.docs["repo-url"]

        self.repo_data = asyncio.run(self.get_repo_data())

        super().__init__(alignment=alignment, vertical_alignment=vertical_alignment)

        self.controls = [
            ft.Column(
                opacity=1,
                animate_opacity=ft.Animation(500, "ease"),
                alignment="center",
                horizontal_alignment="start",
                spacing=2.5,
                controls=[
                    ft.Text("LineIndent/fletxible", size=11, weight="w700"),
                    ft.Row(
                        alignment="center",
                        vertical_alignment="center",
                        controls=self.repo_data,
                    ),
                ],
            ),
        ]

    # Method: gets the repo details based on the input repo URL ...
    async def get_repo_data(self):
        controls_list: list = []

        icon_elements = ["LABEL_OUTLINED", "STAR_BORDER_SHARP", "CALL_SPLIT_SHARP"]

        span_elements: list = [
            "css-truncate css-truncate-target text-bold mr-2",
            "Counter js-social-count",
            "Counter",
        ]

        async with httpx.AsyncClient() as client:
            response = await client.get(self.repo)
            data = response.content

        soup = BeautifulSoup(data, "html.parser")

        for i, span in enumerate(span_elements):
            span_element = soup.find("span", span)
            if span_element is not None:
                text_content = span_element.text.strip()

                if i == 0:
                    icon = ft.Icon(
                        name=icon_elements[i], size=10, rotate=ft.Rotate(pi / 4)
                    )
                else:
                    icon = ft.Icon(name=icon_elements[i], size=10)

                controls_list.append(
                    ft.Row(
                        alignment="center",
                        spacing=0,
                        controls=[
                            icon,
                            ft.Text(
                                text_content,
                                size=10,
                                weight="w200",
                            ),
                        ],
                    )
                )

            else:
                pass

        return controls_list
