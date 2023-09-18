# Flet ToDo App Mobile iOS/Android
import flet as ft


# seperate the style sheet for the  components in a dict

_dark: str = ft.colors.with_opacity(0.5, "white")
_light: str = ft.colors.with_opacity(1, "black")

toggle_style_sheet: dict = {"icon": ft.icons.DARK_MODE_ROUNDED, "icon_size": 18}
add_style_sheet: dict = {"icon": ft.icons.ADD_ROUNDED, "icon_size": 18}

item_style_sheet: dict = {
    "height": 50,
    "expand": True,
    "border_color": _dark,
    "cursor_height": 24,
    "hint_text": "Add your todo item here ...",
    "content_padding": 15,
}

todo_item_style_sheet: dict = {"height": 50, "border_radius": 4}


# create a class for each todo item
class ToDoItem(ft.Container):
    # before we initilize the contianer and send it to the UI, we can check the theme to set the broder color

    def __init__(self, hero: object, description: str, theme: str):
        if theme == "dark":
            todo_item_style_sheet["border"] = ft.border.all(1, _dark)
        else:
            todo_item_style_sheet["border"] = ft.border.all(1, _light)

        super().__init__(**todo_item_style_sheet)
        self.hero = hero
        self.description = description

        self.tick = ft.Checkbox(on_change=lambda e: self.strike(e))
        self.text: ft.Text = ft.Text(
            spans=[ft.TextSpan(text=self.description)], size=14
        )
        self.delete: ft.IconButton = ft.IconButton(
            icon=ft.icons.DELETE_ROUNDED,
            icon_color="red700",
            on_click=lambda e: self.delete_text(e),
        )

        self.content: ft.Row = ft.Row(
            alignment="spaceBetween",
            controls=[
                ft.Row(controls=[self.tick, self.text]),
                self.delete,
            ],
        )

    # method: strike out text if checkbox is clicked
    def strike(self, e):
        if e.control.value is True:
            self.text.spans[0].style = ft.TextStyle(
                decoration=ft.TextDecoration.LINE_THROUGH, decoration_thickness=2
            )

        else:
            self.text.spans[0].style = ft.TextStyle()

        self.text.update()

    # method: delete an item from the list
    def delete_text(self, e):
        self.hero.todo_area.controls.remove(self)
        self.hero.todo_area.update()
        self.hero.item_size()


# main content area
class Hero(ft.SafeArea):
    def __init__(self, page: ft.Page):
        super().__init__(minimum=10, maintain_bottom_view_padding=True)
        self.page = page
        self.title: ft.Text = ft.Text("Todo List", size=20, weight="w800")
        self.toggle: ft.IconButton = ft.IconButton(
            **toggle_style_sheet, on_click=lambda e: self.switch(e)
        )
        self.item: ft.TextField = ft.TextField(**item_style_sheet)
        self.add: ft.IconButton = ft.IconButton(
            **add_style_sheet, on_click=lambda e: self.add_item(e)
        )

        self.todo_area: ft.Column = ft.Column(expand=True, spacing=18)
        self.counter: ft.Text = ft.Text("0 items", italic=True)

        self.main: ft.Column = ft.Column(
            controls=[
                ft.Row(
                    alignment="spaceBetween",
                    controls=[self.title, self.toggle],
                ),
                ft.Divider(height=20),
                ft.Divider(height=10, color="transparent"),
                ft.Text("1. Add your todo item below."),
                ft.Row(controls=[self.item, self.add], alignment="spaceBetween"),
                ft.Divider(height=10, color="transparent"),
                ft.Row(
                    alignment="spaceBetween",
                    controls=[
                        ft.Text("2. List of todo items."),
                        self.counter,
                    ],
                ),
                self.todo_area,
            ]
        )

        self.content = self.main

    # we can keep track of the number of items in the list
    def item_size(self):
        if len(self.todo_area.controls[:]) == 1:
            self.counter.value = f"{len(self.todo_area.controls[:])} item"

        else:
            self.counter.value = f"{len(self.todo_area.controls[:])} items"

        self.counter.update()

    def add_item(self, e):
        if self.item.value != "":
            if self.page.theme_mode == ft.ThemeMode.DARK:
                self.todo_area.controls.append(ToDoItem(self, self.item.value, "dark"))
            else:
                self.todo_area.controls.append(ToDoItem(self, self.item.value, "light"))

            self.todo_area.update()
            self.item_size()
            self.item.value = ""
            self.item.update()

        else:
            pass

    def switch(self, e):
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.toggle.icon = ft.icons.LIGHT_MODE_ROUNDED
            self.item.border_color = _light

            for item in self.todo_area.controls[:]:
                item.border = ft.border.all(1, _light)

        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.toggle.icon = ft.icons.DARK_MODE_ROUNDED
            self.item.border_color = _dark

            for item in self.todo_area.controls[:]:
                item.border = ft.border.all(1, _dark)

        self.page.update()


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    theme = ft.Theme()
    page.theme = theme

    hero: object = Hero(page)
    page.add(hero)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
