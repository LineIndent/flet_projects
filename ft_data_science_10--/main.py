import flet as ft
import pandas as pd
from math import pi


class DataVisualization(ft.UserControl):
    def __init__(self, month_sum: float, max_sum: float, spacing: int, color: str):
        self.month_sum: float = month_sum
        self.delta_sum: float = max_sum - self.month_sum
        self.color = color

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
            center_space_radius=spacing,
            rotate=ft.Rotate((pi) / 2),
        )

        super().__init__()

    def build(self):
        return self.chart


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    colors: list = []
    for num in range(1, 13):
        colors.append(f"purple{num}00")

    # Step 2: Importing and Loading the Data
    sales_data = pd.read_csv("ft_data_science_10--/sales.csv")

    # process and clean the data
    sales_data = sales_data.replace("n.a.", pd.NA)
    sales_data = sales_data.dropna()

    # if columns are strings, convert them to the right dtypes for summation
    for MONTH in sales_data.columns[5:]:
        sales_data[MONTH] = sales_data[MONTH].str.replace(",", "")
        sales_data[MONTH] = sales_data[MONTH].str.replace("not available", "0")
        sales_data[MONTH] = sales_data[MONTH].str.replace("not avilable", "0")
        sales_data[MONTH] = pd.DataFrame(sales_data, columns=[MONTH], dtype=float)

    month_list = []
    max_num = []
    sum_list = []
    for MONTH in sales_data.columns[5:]:
        month_list.append(MONTH)
        max_num.append(sales_data[MONTH].sum())
    sum_list = max_num
    max_num = max(max_num)

    stack = ft.Stack(scale=ft.Scale(0.65))
    size = 60
    for index, MONTH in enumerate(sales_data.columns[5:]):
        stack.controls.append(
            DataVisualization(
                month_sum=sales_data[MONTH].sum(),
                max_sum=max_num,
                spacing=size,
                color=colors[index],
            )
        )
        size += 30

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
                                    size=14,
                                    weight="bold",
                                ),
                            ],
                        ),
                    ],
                ),
            )
        )

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
                    height=500,
                    width=400,
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
