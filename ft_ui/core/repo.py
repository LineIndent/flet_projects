import flet as ft
import yaml
from bs4 import BeautifulSoup
import httpx
import asyncio


with open("fx_config.yml", "r") as file:
    docs = yaml.safe_load(file)

repo = docs["repo-url"]


class RepoData(ft.Row):
    def __init__(self):
        asyncio.run(self.get_repo_data())

        super().__init__()

    async def get_repo_data(self):
        controls_list: list = []

        span_elements: list = [
            "Counter js-social-count",
            "Counter",
            "css-truncate css-truncate-target text-bold mr-2",
        ]

        async with httpx.AsyncClient() as client:
            response = await client.get(repo)
            data = response.content

        soup = BeautifulSoup(data, "html.parser")

        for span in span_elements:
            span_element = soup.find("span", span)
            if span_element is not None:
                text_content = span_element.text.strip()
                controls_list.append(ft.Text(text_content, size=12, weight="bold"))

            else:
                pass

        self.controls = controls_list

        # return controls_list
