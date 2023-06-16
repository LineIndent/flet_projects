import flet as ft
import pandas as pd
from math import pi


# Step 2: Importing and Loading the Data
sales_data = pd.read_csv("ft_data_science_10--/sales.csv")

# process and clean the data
sales_data = sales_data.replace("n.a.", pd.NA)
sales_data = sales_data.dropna()

# if columns are strings, convert them to the right dtypes for summation
for MONTH in sales_data.columns[2:]:
    sales_data[MONTH] = sales_data[MONTH].str.replace(",", "")
    sales_data[MONTH] = sales_data[MONTH].str.replace("not available", "0")
    sales_data[MONTH] = sales_data[MONTH].str.replace("not avilable", "0")
    sales_data[MONTH] = pd.DataFrame(sales_data, columns=[MONTH], dtype=float)

# # Print a sample of 20 rows from the cleaned DataFrame
# sample_rows = sales_data.head(10)
# print(sample_rows)

# # Step 3: Exploratory Data Analysis
# # Checking the data structure and summary statistics
# print(sales_data.head())
# print(sales_data.info())
# print(sales_data.describe())

# max_num = []
# for MONTH in sales_data.columns[2:]:
#     max_num.append(sales_data[MONTH].sum())

# max_num = max(max_num)
# print(max_num)

# this generates a list of data about each column **
# describe = sales_data.describe().to_dict()
# print(describe)

# for key, value in describe.items():
#     for k, v in describe[key].items():
#         # print(f"{k} = {v}")
#         pass


class DataVisualization(ft.UserControl):
    def __init__(self, month_sum: float, max_sum: float, spacing: int, color: str):
        self.month_sum: float = month_sum
        self.delta_sum: float = max_sum - self.month_sum

        self.chart: ft.Control = ft.PieChart(
            sections=[
                ft.PieChartSection(value=self.month_sum, color=color, radius=15),
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

    def get_event(self, e):
        print(self.month_sum)

    def build(self):
        return self.chart


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    colors = []
    for num in range(1, 13):
        colors.append(f"teal{num}00")

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

    max_num = []
    for MONTH in sales_data.columns[5:]:
        max_num.append(sales_data[MONTH].sum())
    max_num = max(max_num)

    stack = ft.Stack(scale=ft.Scale(0.60))
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
        size += 20

    page.add(
        ft.Container(
            width=500,
            height=500,
            bgcolor=ft.colors.with_opacity(0.005, "white10"),
            content=stack,
        )
    )

    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
