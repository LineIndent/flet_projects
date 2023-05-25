""" Menu Flet App UI Design """


""" The modules """
import flet
from flet import (
    Page,
    Row,
    Container,
    margin,
    alignment,
    Card,
    Column,
    border_radius,
    padding,
    Image,
    animation,
    border,
)

from flet import *
from flet.transform import Scale

""" Like the one for the image, tis one does the exact same thing but with smaller scalling """


def scaleUp(x):

    if x.control.scale != 1.5:
        x.control.scale = 1.5
    else:
        x.control.scale = 1
    x.control.update()


""" Scale animation for the image"""


def scaleUpImage(x):

    """We check the scale of the image first, and if it's not the set value, we scale up, else, we return it back to the original scale"""
    if x.control.scale != 1.7:
        x.control.scale = 1.7
    else:
        x.control.scale = 1.6
    x.control.update()


""" Card function that creates the base card and also adds the image. """

""" Note: it takes two arguments, which we pass when we call an instnace of this function down below"""


def card(color_1, color_2):

    img = Container(
        on_hover=lambda x: scaleUpImage(x),
        scale=Scale(scale=1.6),
        animate_scale=animation.Animation(800, "bounceOut"),
        content=Image(
            src=f"./burger.png",
            width=250,
            height=220,
        ),
    )

    return Column(
        horizontal_alignment="center",
        spacing=1,
        controls=[img],
    )


""" ingredients function:
        it takes two arguments: one for the name of the ingredient and the other for width because the length of names vary and so will the width 
"""


def ingredients(width, text):
    return Container(
        # We also created a seperate scale up animation for these
        on_hover=lambda x: scaleUp(x),
        scale=Scale(scale=1),
        animate_scale=animation.Animation(800, "bounceOut"),
        border_radius=border_radius.all(5),
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#475569", "#334155"],
        ),
        width=width,
        height=22,
        alignment=alignment.center,
        content=(Text(text, color="#f3f4f6", size=14, weight="w300")),
    )


""" Here we create the top value, the number or grams of the unit, i.e. calories, fat, carbs, and protein """

# It takes in one argument
def nutrition_unit(unit):
    return Container(
        alignment=alignment.bottom_center,
        margin=margin.only(bottom=-5),
        content=(
            Text(
                unit,
                color="white",
                size=14,
                weight="w400",
                no_wrap=True,
            )
        ),
    )


""" Here we do the same but with minor changes to text and color """
# Also takes in one arguemnt
def nutrition_value(text):
    return Container(
        alignment=alignment.top_center,
        margin=margin.only(top=-5),
        content=(
            Text(
                text,
                color="#64748b",
                size=10,
                weight="w200",
                no_wrap=True,
            )
        ),
    )


def main(page: Page):
    """Basic set up for flet app"""
    page.title = "Menu App UI Design"
    """ You can center the app window to the middle of the screen """
    # page.window_center()
    page.window_width = 700
    page.window_height = 800

    """ Let's start by creating the base card of the app """

    """ card is a method which takes in two arguments, both being colors for the background """
    """ we pass two colors as arguemnts """
    new_card = card("#fffbeb", "#fef3c7")

    """ We will create a function to retrun the container with the info.
        Now, we can create an instance of each ingredient and place them into the UI.
        Make sure to pass in the name and width 
    """
    wagu = ingredients(55, "Wagu")
    cheese = ingredients(65, "Cheese")
    mushroom = ingredients(90, "Mushroom")
    onions = ingredients(65, "Onions")

    """ For the nutritional values, we need to create two functions, similar to the ingredients function.
    Now create the values below with their respective numbers as arguments.  
    
    """
    calories_unit = nutrition_unit("250")
    calories_value = nutrition_value("calories")

    fat_unit = nutrition_unit("21g")
    fat_value = nutrition_value("fat")

    carbs_unit = nutrition_unit("125g")
    carbs_value = nutrition_value("carbs")

    protein_unit = nutrition_unit("32g")
    protein_value = nutrition_value("protein")

    t = Card(
        content=Container(
            alignment=alignment.center,
            content=Container(
                content=Column(
                    horizontal_alignment="center",
                    controls=[
                        new_card,
                        # Padding before the main content
                        Container(
                            padding=padding.only(top=30),
                        ),
                        # Title of the menu item
                        Row(
                            controls=[
                                Text(
                                    "Classic Cheeseburger",
                                    color="#e2e8f0",
                                    size=23,
                                    weight="w700",
                                ),
                            ],
                        ),
                        # We need to create the ingredients row
                        Row(
                            controls=[
                                wagu,
                                cheese,
                                mushroom,
                                onions,
                            ]
                        ),
                        # More padding
                        Container(
                            padding=padding.only(top=10),
                        ),
                        # Menu item description
                        Row(
                            controls=[
                                Text(
                                    "Our simple, classic cheeseburger begins with\na 100% pure beef burger seasoned with just\na pinch of salt and pepper. You'll love it!",
                                    color="#64748b",
                                    size=13,
                                    weight="w300",
                                    no_wrap=True,
                                )
                            ]
                        ),
                        # More padding
                        Container(
                            padding=padding.only(top=10),
                        ),
                        # Now for the nutritional values
                        Row(
                            alignment="center",
                            spacing=40,
                            controls=[
                                Column(
                                    controls=[
                                        calories_unit,
                                        calories_value,
                                    ],
                                ),
                                Column(
                                    controls=[
                                        fat_unit,
                                        fat_value,
                                    ],
                                ),
                                Column(
                                    controls=[
                                        carbs_unit,
                                        carbs_value,
                                    ],
                                ),
                                Column(
                                    controls=[
                                        protein_unit,
                                        protein_value,
                                    ],
                                ),
                            ],
                        ),
                        # More padding
                        Container(
                            padding=padding.only(top=40),
                        ),
                        # To finish, we can add a price tag and a add button
                        Row(
                            alignment="start",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Row(
                                        controls=[
                                            Container(
                                                alignment=alignment.bottom_center,
                                                margin=margin.only(bottom=-5),
                                                padding=padding.only(right=10),
                                                content=(
                                                    Text(
                                                        "$7.99",
                                                        color="white",
                                                        size=18,
                                                        weight="w400",
                                                        no_wrap=True,
                                                    )
                                                ),
                                            ),
                                            # I used an elevated button, but any other tpye can be used
                                            ElevatedButton(
                                                content=(
                                                    Text("Add", size=18, weight="w700")
                                                ),
                                                # text="Add To Card",
                                                bgcolor="#f7ce7c",
                                                color="black",
                                                width=230,
                                                height=40,
                                                # expand=True,
                                            ),
                                        ]
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
                padding=padding.all(20),
                alignment=alignment.center,
                border_radius=border_radius.all(12),
                gradient=LinearGradient(
                    begin=alignment.bottom_left,
                    end=alignment.top_right,
                    colors=["#1f2937", "#111827"],
                ),
            ),
        ),
        width=350,
        height=650,
        elevation=10,
    )

    """ I'm gonna start with a container for the background to get that gradient effect. """

    c = Container(
        Column(
            alignment="center",
            controls=[
                t,
            ],
        ),
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            # colors=["#111827", "#1e3a8a"],
            # colors=["#1e3a8a", "#111827"],
            colors=["#1e293b", "#475569"],
        ),
        alignment=alignment.center_right,
        padding=padding.only(right=40),
        width=1900,
        height=900,
        margin=margin.all(-10),
    )

    """ Add the container to the main page, root """
    page.add(c)
    page.update()


""" assets_dir is the folder that contians images. """

flet.app(target=main, assets_dir="assets")
