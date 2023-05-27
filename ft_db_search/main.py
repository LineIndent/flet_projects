import flet
from flet import *
import asyncio
import aiosqlite


class Database:
    def async_with_connection(func):
        async def wrapper(*args, **kwargs):
            connection = await aiosqlite.connect("./database.db")
            try:
                result = await func(connection, *args, **kwargs)
                await connection.commit()
                return result
            finally:
                await connection.close()

        return wrapper

    @async_with_connection
    async def async_create_table(connection):
        cursor = await connection.cursor()
        await cursor.execute(
            """CREATE TABLE if not exists users (id INTEGER PRIMARY KEY, name TEXT)"""
        )

    @async_with_connection
    async def async_insert_user(connection, name):
        cursor = await connection.cursor()
        await cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))

    @async_with_connection
    async def async_select_users(connection):
        cursor = await connection.cursor()
        await cursor.execute("SELECT name FROM users")
        return await cursor.fetchall()

    async def start():
        names = [
            "George",
            "Shawn",
            "Robert",
            "Steven",
            "William",
            "James",
            "Christopher",
            "James",
            "Michael",
            "Donovan",
            "Jessica",
            "Stephanie",
            "Ann",
            "Emma",
            "Heather",
            "Anna",
            "Kelli",
            "Pauline",
            "Tanya",
            "Kathy",
        ]

        for name in names:
            await Database.async_insert_user(name)


class DropdownMenu(UserControl):
    def __init__(self):
        self.controls_list = {}
        super().__init__()

    def check_instance(self, e, height):
        obj = self.controls_list["data"]
        if height == 0:
            self.controls_list["search"].content.controls[
                2
            ].value = f"{height} results found"
            self.controls_list["search"].content.update()
            self.leave(e)
        else:
            obj.height = 70 + (height * 20)
            obj.update()

    def leave(self, e):
        obj = self.controls_list["data"]
        obj.height = 50
        obj.update()

    async def filter_data_table(self, e):
        records = await Database.async_select_users()
        name_list = Column(
            scroll="auto",
            spacing=20,
            expand=True,
            alignment=MainAxisAlignment.END,
        )
        obj = self.controls_list["data"]
        obj.content = Container(
            padding=padding.only(top=60, left=15, right=15, bottom=10),
            content=name_list,
        )

        if e.data.lower() == "":
            obj.content = None
            self.controls_list["search"].content.controls[2].value = f"0 results found"
            self.controls_list["search"].content.update()
            self.leave(e)
            self.leave(e)
        else:
            count = 0
            for names in records:
                for name in names:
                    if e.data.lower() in name.lower():
                        name_list.controls.append(
                            Row(
                                visible=True,
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Text(name, size=12),
                                    Text("name", italic=True, size=10, color="white54"),
                                ],
                            )
                        )
                        count += 1
                self.controls_list["search"].content.controls[
                    2
                ].value = f"{count} results found"
                self.controls_list["search"].content.update()
                self.check_instance(e, count)

    def drop_down_search(self):
        _object_ = Container(
            width=450,
            height=50,
            bgcolor="white10",
            border_radius=6,
            padding=8,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.SEARCH_ROUNDED,
                        size=17,
                        opacity=0.85,
                    ),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_color="white",
                        cursor_width=1,
                        color="white",
                        hint_text="Search",
                        on_change=lambda e: asyncio.run(self.filter_data_table(e)),
                    ),
                    Text(size=9, italic=True, color="white54"),
                ],
            ),
        )
        self.controls_list["search"] = _object_
        return _object_

    def drop_down_data_box(self):
        _object_ = Container(
            width=450,
            height=50,
            bgcolor="white10",
            border_radius=6,
            alignment=alignment.bottom_center,
            animate=animation.Animation(300, "decelerate"),
            clip_behavior=ClipBehavior.HARD_EDGE,
        )
        self.controls_list["data"] = _object_
        return _object_

    def build(self):
        return Stack(
            width=450,
            height=500,
            expand=True,
            controls=[
                self.drop_down_data_box(),
                self.drop_down_search(),
            ],
        )


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.add(
        DropdownMenu(),
    )
    page.update()


if __name__ == "__main__":
    # # Run this once...
    # asyncio.run(Database.async_create_table())
    # asyncio.run(Database.start())
    flet.app(target=main)
