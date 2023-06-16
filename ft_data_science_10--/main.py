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


def main(page: ft.Page):
    chart = DataVisualization(103123.33, 370000.00, 60)
    chart1 = DataVisualization(263123.33, 370000.00, 80)
    chart2 = DataVisualization(123123.33, 370000.00, 100)
    page.add(
        ft.Stack(
            [
                chart,
                chart1,
                chart2,
            ]
        )
    )
    page.update()


class DataVisualization(ft.UserControl):
    def __init__(self, month_sum: float, max_sum: float, spacing: int):
        self.month_sum: float = month_sum
        self.delta_sum: float = max_sum - self.month_sum

        self.chart: ft.Control = ft.PieChart(
            sections=[
                # dynamic PieSection circle
                ft.PieChartSection(value=self.month_sum, color="teal600", radius=15),
                # background PieSection circle
                ft.PieChartSection(
                    value=self.delta_sum,
                    color=ft.colors.with_opacity(0.025, "white"),
                    radius=15,
                ),
            ],
            sections_space=0,
            center_space_radius=spacing,
            expand=True,
            rotate=ft.Rotate((pi) / 2),
            # on_chart_event=lambda e: self.hover_circle(e),
        )
        super().__init__()

    def build(self):
        return self.chart


if __name__ == "__main__":
    ft.flet.app(target=main)
