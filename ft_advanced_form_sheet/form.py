import flet as ft
import flet_material as fm
import asyncio


PRIMARY = "teal"
fm.Theme.set_theme(theme=PRIMARY)

dummy_user_list: list = [["line.indent@gmail.com", 123123123]]


class CustomInputField(ft.UserControl):
    def __init__(self, password: bool, title: str):
        self.input = ft.TextField(
            height=45,
            border_color="#bbbbbb",
            border_width=0.6,
            cursor_height=14,
            cursor_width=1,
            cursor_color="white",
            color="white",
            text_size=13,
            bgcolor=fm.Theme.bgcolor,
            on_focus=lambda e: self.focus_shadow(e),
            on_blur=lambda e: self.blur_shadow(e),
            on_change=lambda e: self.set_loader_animation(e),
            password=password,
        )

        self.input_box = ft.Container(
            expand=True,
            content=self.input,
            animate=ft.Animation(300, "ease"),
            shadow=None,
        )

        self.loader = ft.ProgressBar(
            value=0,
            bar_height=1.25,
            color=PRIMARY,
            bgcolor="transparent",
            scale=ft.Scale(scale_x=1, alignment=ft.alignment.center_left),
        )

        self.status = fm.CheckBox(
            shape="circle",
            value=False,
            disabled=True,
            offset=ft.Offset(1, 0),
            opacity=0,
            animate_opacity=ft.Animation(200, "linear"),
            animate_offset=ft.Animation(350, "ease"),
            bottom=0,
            right=1,
            top=1,
        )

        self.object = self.create_input(title)
        super().__init__()

    def set_loader_animation(self, e):
        if len(self.input.value) != 0:
            self.loader.value = None
        else:
            self.loader.value = 0

        self.loader.update()

    async def set_validation_status_ok(self):
        self.loader.value = 0
        self.loader.update()

        self.status.offset = ft.transform.Offset(-0.5, 0)
        self.status.opacity = 1
        self.update()

        await asyncio.sleep(1)

        self.status.content.value = True
        self.status.animate_checkbox(e=None)
        self.status.update()

    def focus_shadow(self, e):
        #
        self.input.border_color = PRIMARY
        self.input_box.shadow = ft.BoxShadow(
            spread_radius=6,
            blur_radius=8,
            color=ft.colors.with_opacity(0.25, "black"),
            offset=ft.Offset(4, 4),
        )
        self.update()
        self.set_loader_animation(e=None)

    def blur_shadow(self, e):
        self.input_box.shadow = None
        self.input.border_color = "#bbbbbb"
        self.update()
        self.set_loader_animation(e=None)

    def create_input(self, title):
        return ft.Column(
            spacing=5,
            controls=[
                ft.Text(title, size=11, weight="bold", color="#bbbbbb"),
                ft.Stack(
                    controls=[
                        self.input_box,
                        self.status,
                    ],
                ),
                self.loader,
            ],
        )

    def build(self):
        return self.object


class MainFormUI(ft.UserControl):
    def __init__(self):
        #
        self.email = CustomInputField(False, "Email")
        self.password = CustomInputField(True, "Password")

        #
        self.submit: ft.Control = fm.Buttons(
            width=400,
            height=45,
            title="Submit",
            on_click=lambda e: asyncio.run(self.validate_entries(e)),
        )

        super().__init__()

    async def validate_entries(self, e):
        email_value = self.email.input.value
        password_value = self.password.input.value

        for user, password in dummy_user_list:
            if email_value == user and password_value == str(password):
                await asyncio.sleep(1)
                await self.email.set_validation_status_ok()
                await asyncio.sleep(1)
                await self.password.set_validation_status_ok()
                self.update()

    def build(self):
        return ft.Container(
            width=450,
            height=550,
            padding=40,
            border_radius=10,
            bgcolor=ft.colors.with_opacity(0.01, "white"),
            content=ft.Column(
                horizontal_alignment="center",
                alignment="center",
                controls=[
                    ft.Text(
                        "Validating Signin Form",
                        size=24,
                        weight="w700",
                        font_family="Roboto",
                        color=ft.colors.with_opacity(0.85, "white"),
                    ),
                    ft.Divider(height=25, color="transparent"),
                    self.email,
                    self.password,
                    ft.Divider(height=25, color="transparent"),
                    self.submit,
                ],
            ),
        )


def main(page: ft.Page):
    page.bgcolor = fm.Theme.bgcolor

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    #
    form = MainFormUI()

    page.add(form)
    page.update()


if __name__ == "__main__":
    ft.flet.app(target=main)
