import flet as ft


# Define a final class to handle data between controls
# Some dumy data to filll out the table
dummy_data = {
    0: {"name": "Apple", "description": "Red and juicy", "quantity": 5, "price": 1.99},
    1: {
        "name": "Bread",
        "description": "Whole wheat loaf",
        "quantity": 2,
        "price": 3.49,
    },
    2: {
        "name": "Milk",
        "description": "Organic whole milk",
        "quantity": 1,
        "price": 2.99,
    },
    3: {
        "name": "Carrot",
        "description": "Fresh and crunchy",
        "quantity": 10,
        "price": 0.99,
    },
    4: {
        "name": "Eggs",
        "description": "Free-range brown eggs",
        "quantity": 12,
        "price": 2.79,
    },
    5: {
        "name": "Chicken",
        "description": "Boneless skinless breasts",
        "quantity": 2,
        "price": 7.99,
    },
    6: {
        "name": "Banana",
        "description": "Ripe and yellow",
        "quantity": 6,
        "price": 0.49,
    },
}


class Controller:
    items: dict = dummy_data
    counter: int = len(items)

    @staticmethod
    def get_items():
        return Controller.items

    @staticmethod
    def add_item(data: dict):
        Controller.items[Controller.counter] = data
        Controller.counter += 1


# Define style and attributes for header class
header_style = {
    "height": 60,
    "bgcolor": "#081d33",
    "border_radius": ft.border_radius.only(top_left=15, top_right=15),
    "padding": ft.padding.only(left=15, right=15),
}


# A method that creates and returns a textfield
def search_field(function: callable):
    return ft.TextField(
        border_color="transparent",
        height=20,
        text_size=14,
        content_padding=0,
        cursor_color="white",
        cursor_width=1,
        color="white",
        hint_text="Search",
        on_change=function,
    )


# A method that adds a container to the search_field
def search_bar(control: ft.TextField):
    return ft.Container(
        width=350,
        bgcolor="white10",
        border_radius=6,
        opacity=0,
        animate_opacity=300,
        padding=8,
        content=ft.Row(
            spacing=10,
            vertical_alignment="center",
            controls=[
                ft.Icon(
                    name=ft.icons.SEARCH_ROUNDED,
                    size=17,
                    opacity=0.85,
                ),
                control,
            ],
        ),
    )


# Define header class
class Header(ft.Container):
    def __init__(self, dt: ft.DataTable):
        super().__init__(**header_style, on_hover=self.toggle_search)
        # create a dt attribute
        self.dt = dt

        # create a textfield for search/filter
        self.search_value = search_field(self.filter_dt_rows)

        # create a searchbox
        self.search = search_bar(self.search_value)

        # define other class attributes
        self.name = ft.Text("Line Indent")
        self.avatar = ft.IconButton("person")

        # compile the attributes inside the header contianer
        self.content = ft.Row(
            alignment="spaceBetween", controls=[self.name, self.search, self.avatar]
        )

    # define method that toggles search box visibility
    def toggle_search(self, e: ft.HoverEvent):
        self.search.opacity = 1 if e.data == "true" else 0
        self.search.update()

    # define a placeholder method for filtering data
    def filter_dt_rows(self, e):
        # finally, we can filter the data based on the characters in the search box
        # we need to access th data table instance's rows
        for data_rows in self.dt.rows:
            # I'm only fitlering based on column one
            # so only the first index position [0]
            data_cell = data_rows.cells[0]
            # we change the visibility against whats being typed in the search box.
            # we also handle case sensitivity by setting everything to lower case, i.e, lower()
            data_rows.visible = (
                True
                if e.control.value.lower() in data_cell.content.value.lower()
                else False
            )

            data_rows.update()

        ...


# Define form class styling and attributes
form_style = {
    "border_radius": 8,
    "border": ft.border.all(1, "#ebebeb"),
    "bgcolor": "white10",
    "padding": 15,
}


# Define a method that creates and returns a textfield
def text_field():
    return ft.TextField(
        border_color="transparent",
        height=20,
        text_size=13,
        content_padding=0,
        cursor_color="black",
        cursor_width=1,
        cursor_height=18,
        color="black",
    )


# ext define a container to wrap the textfield in
def text_field_container(expand: bool | int, name: str, control: ft.TextField):
    return ft.Container(
        expand=expand,
        height=45,
        bgcolor="#ebebeb",
        border_radius=6,
        padding=8,
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Text(value=name, size=9, color="black", weight="bold"),
                control,
            ],
        ),
    )


# Next, define a form class
class Form(ft.Container):
    def __init__(self, dt: ft.DataTable):
        super().__init__(**form_style)
        # create a dt attribute
        self.dt = dt

        # define the 4 row textfields
        self.row1_value = text_field()
        self.row2_value = text_field()
        self.row3_value = text_field()
        self.row4_value = text_field()

        # define and wrap each inside a container
        self.row1 = text_field_container(True, "Row One", self.row1_value)
        self.row2 = text_field_container(3, "Row Two", self.row2_value)
        self.row3 = text_field_container(1, "Row Three", self.row3_value)
        self.row4 = text_field_container(1, "Row Four", self.row4_value)

        # define a button to submit the data
        self.submit = ft.ElevatedButton(
            text="Submit",
            style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=8)}),
            on_click=self.submit_data,
        )

        # compile all the attibutes into the class contianer
        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Row(controls=[self.row1]),
                ft.Row(controls=[self.row2, self.row3, self.row4]),
                ft.Row(controls=[self.submit], alignment="end"),
            ],
        )

    # defie a method to submit data
    def submit_data(self, e: ft.TapEvent):
        # we get the value for each textfield and create a data structure for it.
        data = {
            "col1": self.row1_value.value,
            "col2": self.row2_value.value,
            "col3": self.row3_value.value,
            "col4": self.row4_value.value,
        }

        # next, we call the controller and add the data to our items dict
        Controller.add_item(data)

        # finally, clear the entries and re populate the data table
        self.clear_entries()
        self.dt.fill_data_table()

    # define a method to clear entries post-submit
    def clear_entries(self):
        self.row1_value.value = ""
        self.row2_value.value = ""
        self.row3_value.value = ""
        self.row4_value.value = ""

        self.content.update()


# Define some data table style, attributes, and columns
column_names = ["Column One", "Column Two", "Column Three", "Column Four"]

data_table_style = {
    "expand": True,
    "border_radius": 8,
    "border": ft.border.all(2, "#ebebeb"),
    "horizontal_lines": ft.border.BorderSide(1, "#ebebeb"),
    "columns": [
        # use list comprehension to create dt columns
        ft.DataColumn(ft.Text(index, size=12, color="black", weight="bold"))
        for index in column_names
    ],
}


# Next, define a class for the data table
class DataTable(ft.DataTable):
    def __init__(self):
        super().__init__(**data_table_style)
        # create a attirbute to get items
        self.df = Controller.get_items()

    def fill_data_table(self):
        # clear the data table rows for new/updated batch
        self.rows = []
        # check dict data type to understand following loop
        for values in self.df.values():
            # create a new DataRow
            data = ft.DataRow()
            data.cells = [
                ft.DataCell(ft.Text(value, color="black")) for value in values.values()
            ]

            self.rows.append(data)

        self.update()


def main(page: ft.Page):
    page.bgcolor = "#fdfdfd"

    table = DataTable()
    header = Header(dt=table)
    form = Form(dt=table)

    page.add(
        ft.Column(
            expand=True,
            controls=[
                # header ...
                header,
                ft.Divider(height=2, color="transparent"),
                # form ...
                form,
                ft.Column(
                    scroll="hidden",
                    expand=True,
                    controls=[ft.Row(controls=[table])],  # table ...
                ),
            ],
        )
    )

    page.update()
    # we can fill out the dt after we add the control to the page
    table.fill_data_table()


ft.app(target=main)
