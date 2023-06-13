# import flet as ft
# import pandas as pd


# Step 2: Importing and Loading the Data
# sales_data = pd.read_csv("ft_data_science_105/sales.csv")

# process and clean the data
# sales_data = sales_data.replace("n.a.", pd.NA)
# sales_data = sales_data.dropna()

# if columns are strings, convert them to the right dtypes for summation
# for MONTH in sales_data.columns[2:]:
#     sales_data[MONTH] = sales_data[MONTH].str.replace(",", "")
#     sales_data[MONTH] = sales_data[MONTH].str.replace("not available", "0")
#     sales_data[MONTH] = sales_data[MONTH].str.replace("not avilable", "0")
#     sales_data[MONTH] = pd.DataFrame(sales_data, columns=[MONTH], dtype=float)

# Print a sample of 20 rows from the cleaned DataFrame
# sample_rows = sales_data.head(10)
# print(sample_rows)

# Step 3: Exploratory Data Analysis
# Checking the data structure and summary statistics
# print(sales_data.head())
# print(sales_data.info())
# print(sales_data.describe())

# print(sales_data["JANUARY"].sum())

# describe = sales_data.describe().to_dict()

# for key, value in describe.items():
#     for k, v in describe[key].items():
#         # print(f"{k} = {v}")
#         pass


# def main(page: ft.Page):
#     page.update()


# if __name__ == "__main__":
#     ft.flet.app(target=main)


import math

import flet as ft
import flet.canvas as cv


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def cont(w, h):
        return ft.Container(
            width=w,
            height=h,
            # border=ft.border.all(1, "white"),
            # shape=ft.BoxShape("circle"),
            content=ft.Stack(
                expand=True,
                controls=[
                    ft.Container(
                        height=32,
                        width=32,
                        shape=ft.BoxShape("circle"),
                        bgcolor="white",
                        left=0,
                        top=0,
                    ),
                    ft.Container(
                        width=32,
                        height=32,
                        shape=ft.BoxShape("circle"),
                        bgcolor="white",
                        right=0,
                        top=0,
                    ),
                    ft.Container(
                        width=32,
                        height=32,
                        shape=ft.BoxShape("circle"),
                        bgcolor="white",
                        left=0,
                        bottom=0,
                    ),
                    ft.Container(
                        width=32,
                        height=32,
                        shape=ft.BoxShape("circle"),
                        bgcolor="white",
                        right=0,
                        bottom=0,
                    ),
                ],
            ),
        )

    page.add(
        ft.Container(
            expand=True,
            width=500,
            height=500,
            alignment=ft.alignment.center,
            content=ft.Stack(
                [
                    cont(100, 100),
                    cont(200, 200),
                    cont(250, 250),
                ],
                expand=True,
            ),
        )
    )


ft.app(main)
