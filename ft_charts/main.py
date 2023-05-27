import flet as ft
import time


POINTS = [
    (0, 273.60),
    (1, 279.00),
    (2, 348.20),
    (3, 363.70),
    (4, 438.40),
    (5, 518.90),
    (6, 638.00),
    (7, 833.75),
    (8, 874.75),
    (9, 1096.50),
    (10, 1226.75),
    (11, 1577.00),
    (12, 1668.75),
    (13, 1200.00),
    (14, 1184.75),
    (15, 1061.25),
    (16, 1151.00),
    (17, 1257.25),
    (18, 1301.50),
    (19, 1493.25),
    (20, 1906.25),
    (21, 1753.90),
    (22, 1980.40),
]

BTC = [
    (9, 0.0008),
    (10, 0.07),
    (11, 0.95),
    (12, 13.44),
    (13, 817.36),
    (14, 314.24),
    (15, 430.05),
    (16, 963.74),
    (17, 13880.74),
    (18, 3843.52),
    (19, 7191.68),
    (20, 29001.19),
    (21, 39800.00),
]


class RealTimeChart(ft.UserControl):
    def __init__(self):
        #
        self.y_labels: list = []
        self.data_points: list = []
        self.points: list = POINTS
        #
        self.chart: ft.Control = ft.LineChart(
            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.WHITE),
            min_y=int(min(self.points, key=lambda y: y[1])[1]),
            max_y=int(max(self.points, key=lambda y: y[1])[1]),
            min_x=int(min(self.points, key=lambda x: x[0])[0]),
            max_x=int(max(self.points, key=lambda x: x[0])[0]),
            expand=True,
            left_axis=ft.ChartAxis(labels_size=50),
            bottom_axis=ft.ChartAxis(labels_interval=1, labels_size=40),
        )
        #
        self.line_chart: ft.Control = ft.LineChartData(
            color=ft.colors.GREEN,
            stroke_width=2,
            curved=True,
            stroke_cap_round=True,
            below_line_gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[
                    ft.colors.with_opacity(0.25, ft.colors.GREEN),
                    "transparent",
                ],
            ),
        )

        super().__init__()

    def create_data_point(self, x, y):
        return ft.LineChartDataPoint(
            x,
            y,
            selected_below_line=ft.ChartPointLine(
                width=0.5, color="white54", dash_pattern=[2, 4]
            ),
            selected_point=ft.ChartCirclePoint(stroke_width=1),
        )

    def get_data_points(self):
        for x, y in self.points:
            self.data_points.append(self.create_data_point(x, y))
            self.chart.update()
            time.sleep(0.05)

    def test_click(self, e):
        # switch the list
        self.switch_list(e)
        #
        self.chart.data_series = [self.line_chart]
        # get the new data points
        self.get_data_points()

    def switch_list(self, e):
        if e.control.data == "gold":
            self.points = POINTS
        if e.control.data == "btc":
            self.points = BTC

        self.data_points = []
        self.chart.data_series = []
        self.line_chart.data_points = self.data_points

        self.chart.min_y = int(min(self.points, key=lambda y: y[1])[1])
        self.chart.max_y = int(max(self.points, key=lambda y: y[1])[1])
        self.chart.min_x = int(min(self.points, key=lambda x: x[0])[0])
        self.chart.max_x = int(max(self.points, key=lambda x: x[0])[0])
        self.chart.update()
        time.sleep(0.5)

    def get_data_buttons(self, btn_name, data):
        return ft.ElevatedButton(
            btn_name,
            width=140,
            height=40,
            style=ft.ButtonStyle(
                shape={"": ft.RoundedRectangleBorder(radius=6)},
            ),
            bgcolor="teal600",
            color="black",
            data=data,
            on_click=lambda e: self.test_click(e),
        )

    def build(self):
        self.line_chart.data_points = self.data_points
        self.chart.data_series = [self.line_chart]

        return ft.Column(
            horizontal_alignment="center",
            controls=[
                ft.Text(
                    "Yearly Historical Prices for Bitcoin & Gold",
                    size=16,
                    weight="bold",
                ),
                self.chart,
            ],
        )


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    chart = RealTimeChart()
    page.add(
        ft.Column(
            expand=True,
            alignment="center",
            horizontal_alignment="center",
            controls=[
                ft.Container(
                    expand=1,
                    border_radius=6,
                    bgcolor=ft.colors.with_opacity(0.005, ft.colors.WHITE10),
                    content=ft.Row(
                        alignment="center",
                        controls=[
                            chart.get_data_buttons("Gold", "gold"),
                            chart.get_data_buttons("Bitcoin", "btc"),
                        ],
                    ),
                ),
                ft.Container(
                    expand=4,
                    content=chart,
                    padding=20,
                    border_radius=6,
                    bgcolor=ft.colors.with_opacity(0.005, ft.colors.WHITE10),
                ),
                # ft.Container(
                #     expand=2,
                #     border_radius=6,
                #     bgcolor=ft.colors.with_opacity(0.005, ft.colors.WHITE10),
                # ),
            ],
        ),
    )
    page.update()
    time.sleep(1)
    chart.get_data_points()


ft.app(main)
