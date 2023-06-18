""" Flet Data Visulization With Pandas """

import flet as ft
import pandas as pd
from math import pi


""" 
Start off with the main pie chart class
"""


class DataVisualization(ft.UserControl):
    def __init__(
        self,
        month_sum: float,
        max_sum: float,
        color: str,
        spacing: int,
    ):
        """3 main value instances for the pie chart"""
        self.month_sum: float = month_sum
        self.delta_sum: float = max_sum - self.month_sum
        self.color: str = color
        self.spacing: int = spacing

        """ Make an instance of the pie chart """
        self.chart: ft.Control = ft.PieChart(
            sections=[
                ft.PieChartSection(value=self.month_sum, color=self.color, radius=15),
                ft.PieChartSection(
                    value=self.delta_sum,
                    color=ft.colors.with_opacity(0.025, "white"),
                    radius=15,
                ),
            ],
            sections_space=0,
            center_space_radius=self.spacing,
            rotate=ft.Rotate(pi / 2),
        )

        super().__init__()

    def build(self):
        return self.chart


def main(page: ft.Page):
    """We'll be using a dataset online in CSV format. Make sure the data is in the same dir."""

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    """ First let's create a list of colors """
    colors: list = []
    for num in range(1, 15):
        colors.append(f"purple{num}00")

    """ Next we import the data set and process it """
    sales_data = pd.read_csv("ft_data_science_10--/sales.csv")

    sales_data = sales_data.replace("n.a.", pd.NA)
    sales_data = sales_data.dropna()

    """ We need to covert the columns from string to floats """
    """ I'm only using some of the months """
    for MONTH in sales_data.columns[5:]:
        sales_data[MONTH] = sales_data[MONTH].str.replace(",", "")
        sales_data[MONTH] = sales_data[MONTH].str.replace("not available", "0")
        sales_data[MONTH] = sales_data[MONTH].str.replace("not avilable", "0")
        sales_data[MONTH] = pd.DataFrame(sales_data, columns=[MONTH], dtype=float)

    """ Now let's create some list variables to use in the UI """
    month_list: list = []
    max_num: list = []
    sum_list: list = []
    for MONTH in sales_data.columns[5:]:
        month_list.append(MONTH)
        max_num.append(sales_data[MONTH].sum())

    sum_list = max_num
    max_num = float(max(max_num))

    """ Create the main stack where the pie charts will stack on top of each other """
    stack = ft.Stack(scale=ft.Scale(0.65))
    size = 60
    for index, MONTH in enumerate(sales_data.columns[5:]):
        stack.controls.append(
            DataVisualization(
                month_sum=sales_data[MONTH].sum(),
                max_sum=max_num,
                color=colors[index],
                spacing=size,
            )
        )

        size += 30

    """ To animate the chart based on hover, we can 
        implement the following logic ...
    """

    def highlight_data(e):
        if e.data == "true":
            for index, chart in enumerate(stack.controls[:]):
                if index != e.control.data:
                    chart.chart.sections[0].color = ft.colors.with_opacity(
                        0.05, "white10"
                    )
                    chart.update()

        else:
            for index, chart in enumerate(stack.controls[:]):
                if index != e.control.data:
                    chart.chart.sections[0].color = colors[index]
                    chart.update()

    """ Create the sum columns """
    col = ft.Column(alignment="center")
    for index in range(len(month_list)):
        col.controls.append(
            ft.Container(
                on_hover=lambda e: highlight_data(e),
                data=index,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            alignment="start",
                            controls=[
                                ft.Container(
                                    width=9,
                                    height=9,
                                    shape=ft.BoxShape("circle"),
                                    bgcolor=colors[index],
                                ),
                                ft.Text(month_list[index], size=14, weight="bold"),
                            ],
                        ),
                        ft.Row(
                            alignment="end",
                            controls=[
                                ft.Text(
                                    sum_list[index],
                                    size=13,
                                    weight="bold",
                                )
                            ],
                        ),
                    ],
                ),
            )
        )

    """ Create the main page control here ... """
    page.add(
        ft.Row(
            alignment="center",
            controls=[
                ft.Container(
                    width=500,
                    height=500,
                    bgcolor=ft.colors.with_opacity(0.009, "white10"),
                    content=stack,
                ),
                ft.Container(
                    width=400,
                    height=500,
                    padding=50,
                    bgcolor=ft.colors.with_opacity(0.009, "white10"),
                    content=col,
                ),
            ],
        )
    )

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
