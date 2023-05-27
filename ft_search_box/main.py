""" Flet Search Bar """
# modules
import flet
from flet import *
import asyncio
import aiosqlite

# we need to get data from somewhere to show the search bar function.
# i'm gonna use a SQLite3 database => first I'll insert some data and then fetch the data within the search bar class.
# I'll be using async functions and decorators
class Database:
    # I've covered the following setup in a previous video, so I'll go by a little quickly here.
    # first we need a dcorator function that will automatically run a open connection and close it, and in the middle run a query for us, e.g. SELECT or INSERT
    def async_with_connection(func):
        async def wrapper(*args, **kwargs):
            # when we docrate a function, it'll run this wrapper first.
            # so 1. opens a cnnection
            connection = await aiosqlite.connect("./database.db")
            try:
                # it''s then run the function we passed above, i.e. func
                result = await func(connection, *args, **kwargs)
                await connection.commit()
                return result
            finally:
                # it'll then close the connection automatically
                await connection.close()

        return wrapper

    # now, we just need two functions, INSERT and SELECT and a table creation
    # make sure to decorate this with the conenction function
    @async_with_connection
    async def async_create_table(connection):
        cursor = await connection.cursor()
        await cursor.execute(
            """CREATE TABLE if not exists users (id INTEGER PRIMARY KEY, name VARCHAR(255))"""
        )

    # the insert query
    # typically, in a real application, we would also pass a second argument to the async_insert_user function becuase the info will come from user input.
    # in our case, we will manually input the data.
    @async_with_connection
    async def async_insert_user(connection, name):
        cursor = await connection.cursor()
        await cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))

    # finally, the select Query
    @async_with_connection
    async def async_select_user(connection):
        cursor = await connection.cursor()
        await cursor.execute("SELECT name FROM users")
        return await cursor.fetchall()

    # let's set up a small method to pass in some names
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


# I'm gonna put the search bar in a class so that it can easily be used across any application.
class DropDownSearchBar(UserControl):
    def __init__(self):
        self.controls_list = {}
        self.item_number = Text(size=9, italic=True, color="white54")
        super().__init__()

    def check_instance(self, e, height):
        # this method will expand and resize the search bar accordingly
        obj = self.controls_list["search"]  # fetch the main UI
        # recall that we passed count below, and we are now calling it as height. So whatever integer COUNT is, it's now also HEIGHT
        if height == 0:
            self.item_number.value = f"0 results found"
            self.item_number.update()
            # if the count is 0, that means there's no matching data,
            # therefore we have to resize it back to initial state
            # we can call a function here.
            self.leave(e)
        else:  # if the count is not zero, we can ajust the height based on the number of entires found
            obj.height = 60 + (height * 20)
            obj.update()

    def leave(self, e):
        # this will handle 0 or empty text feild
        obj = self.controls_list["search"]
        obj.height = 50
        obj.update()

    # now that we have data in the DB, we can start fetching and fitlering
    # becuase the DB queries are async, our fetch and filter function must be async as well
    async def filter_data_table(self, e):
        # fetch the data
        records = await Database.async_select_user()
        # we need to retrve the column we want to work with.
        obj = self.controls_list["search"]

        # we need to check two states, if the text field is empty or not
        # on_change allows us to get each thing a user types
        # typing = e.data
        if e.data.lower() == "":  # so if the search bar is empty
            # we will pass for now
            # we want to update the count here as well, if the list is empty
            # we actaully need to remove the data if we clear the text field
            for data in obj.content.controls[1].controls[:]:
                obj.content.controls[1].controls.remove(data)
                obj.content.update()

            self.item_number.value = f"No results found"
            self.item_number.update()

            # make sure to call the minimze function
            self.leave(e)
        else:  # if it's not empty,
            # we want to start getting the data and putting it into the column we created
            # set a counter that will determine height
            count = 0  # height counter
            for names in records:
                for name in names:
                    # so we check to see if a character is in a name, which is the data from the DB
                    if e.data.lower() in name.lower():
                        # if it is, we want to display it
                        # this is the index of the column we want to append
                        obj.content.controls[1].controls.append(
                            Row(
                                visible=True,
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Text(name, size=12),
                                    Text("name", italic=True, size=10, color="white54"),
                                ],
                            )
                        )
                        # add to the count
                        count += 1

                    # when the for loop is done, we need to expand/minimze aaccordingly and display number of results
                    # first, we can update the number of results
                    # recall that we created this self instance above, so now we can access it easily and change it.
                    self.item_number.value = f"{count} results found"
                    self.item_number.update()
                    #
                    # we now have to check the data and expand accordingly
                    # we can do this in methods
                    self.check_instance(e, count)

    # we need to create a method that generates the UI for the search bar
    def drop_down_search(self):
        # I want to store the actuall search bar in a dictionary, so I'll set it to a variable before passing it.
        _object_ = Container(
            width=450,
            height=50,
            bgcolor="white10",
            border_radius=6,
            padding=padding.only(top=15, left=21, right=21, bottom=15),
            # clip beahv. makes sure there's no overflow
            clip_behavior=ClipBehavior.HARD_EDGE,
            animate=animation.Animation(400, "decelerate"),
            content=Column(
                # this is the main control where things will be stored
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.START,
                controls=[
                    # first row will be the search field, followed by the data
                    Row(
                        spacing=10,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Icon(
                                name=icons.SEARCH_ROUNDED,
                                size=15,
                                opacity=0.90,
                            ),
                            TextField(
                                border_color="transparent",
                                height=20,
                                text_size=12,
                                content_padding=2,
                                cursor_color="white",
                                cursor_width=1,
                                hint_text="Search...",
                                # need to use asyncio.run() to run a async method!
                                on_change=lambda e: asyncio.run(
                                    self.filter_data_table(e)
                                ),
                            ),
                            # I want to display the number of items available in the data, or from whereever the data is being fetched.
                            # we need to create a self instance so we can access this field easily.
                            self.item_number,
                        ],
                    ),
                    # This is where data will be displayed.
                    Column(
                        scroll="auto",
                        expand=True,
                    ),
                ],
            ),
        )
        # in the main UI section, we can pass this object to a dict so we can acess it in another method
        self.controls_list["search"] = _object_
        return _object_

    # the main build return
    def build(self):
        return self.drop_down_search()


# our main function build
def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    page.padding = padding.only(top=200)
    page.bgcolor = "#212328"

    # add a instance of the class to the page
    page.add(
        DropDownSearchBar(),
    )
    page.update()


if __name__ == "__main__":
    # I'll run the query so we can have some names in the database to carry out the search function.
    # run this once and comment it out becuase the hot reload will run it multiple times.
    # asyncio.run(Database.async_create_table())
    # asyncio.run(Database.start())

    flet.app(target=main)
