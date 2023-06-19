import flet as ft


class Annotations(ft.Container):
    def __init__(
        self,
        annotations_msg: str,
        *args,
        **kwargs,
    ):
        self.annotations_msg = annotations_msg

        self.annotation = ft.Tooltip(
            padding=10,
            vertical_offset=20,
            message=self.annotations_msg,
            bgcolor="#20222c",
            text_style=ft.TextStyle(color="white"),
            content=ft.Icon(
                name=ft.icons.ADD,
                size=15,
                rotate=ft.Rotate(0, ft.alignment.center),
                animate_rotation=ft.Animation(400, "easeOutBack"),
            ),
        )

        kwargs.setdefault("width", 21)
        kwargs.setdefault("height", 21)
        kwargs.setdefault("bgcolor", "white24")
        kwargs.setdefault("shape", ft.BoxShape("circle"))
        kwargs.setdefault("alignment", ft.alignment.center)
        kwargs.setdefault("content", self.annotation)
        kwargs.setdefault("animate", 400)
        kwargs.setdefault("on_hover", lambda e: self.change_rotation(e))
        super().__init__(*args, **kwargs)

    def change_rotation(self, e):
        if e.data == "true":
            self.bgcolor = "#dd6058"
            self.content.content.rotate = ft.Rotate(0.75, ft.alignment.center)

        else:
            self.bgcolor = "white24"
            self.content.content.rotate = ft.Rotate(0, ft.alignment.center)

        self.update()
