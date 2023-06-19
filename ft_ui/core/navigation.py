import flet as ft


class Navigation(ft.Row):
    def __init__(
        self,
        page: ft.Page,
        docs: dict,
        function: callable,
        alignment="center",
    ):
        self.page = page
        self.docs = docs

        # self.page.on_route_change = self.set_app_router
        self.function = function

        self.index: int
        self.current = -1

        super().__init__(
            alignment=alignment,
        )

        self.controls = [
            # DO NOT REMOVE 'start' and 'end' markers!!
            # start #
            ft.Text(
                size=11,
                weight="bold",
                spans=[
                    ft.TextSpan(
                        "Installation",
                        data="/installation",
                        on_click=lambda e: self.set_app_router(e),
                    )
                ],
            ),  # end #
        ]

    def set_app_router(self, route):
        self.page.views.clear()
        # begin #
        if route.control.data == "/installation":
            self.page.views.append(
                self.page.data[route.control.data]
                .loader.load_module()
                .FxView(self.page, self.docs)
            )
            self.page.go(route.control.data)

        # finish #
        self.page.update()
