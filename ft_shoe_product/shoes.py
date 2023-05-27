""" Product UI Using Dlet"""
""" The modules used"""
import flet
from flet import (
    Text,
    AlertDialog,
    TextField,
    TextButton,
    Column,
    Container,
    LinearGradient,
    alignment,
    border_radius,
    padding,
    Image,
    UserControl,
    Row,
    IconButton,
    margin,
    icons,
    border,
    Card,
    transform,
    animation,
    Icon,
    SnackBar,
    Checkbox,
    Page,
    Scale,
)


# Main class => App()
# Below is the starter code for running flet, so I'll go briefly over the info.
class App(UserControl):
    # First: a minor gradient maker function here to return a specific gradient,
    # you can use this or not, depends on the app
    def GradientGenerator(self, start, end):
        self.ColorGradient = LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=[
                start,
                end,
            ],
        )

        return self.ColorGradient

    # TEN: change image color
    def ChangeColor(self, e):
        # We can change the color of the item based on user selection as follows;
        # get the event on click data variable and pass it as a NEW src for the image variable self.img.
        # That's all there is to it.
        self.img.content.src = f"./assets/{e.control.data}.png"
        # Don't forget to update the self.img variable at the end
        self.img.update()

    # Main function holding the main contianer
    def MainContainer(self):
        # NINE: For the size row, I simply mapped out the UI the way I wanted and created the columns and rows accordingly.

        # Top and Bot rows respectivly
        self.TopRow = Row(spacing=0, tight=True)
        self.BotRow = Row(spacing=0, tight=True)

        # Using a for loop, we can minimize the lines of UI code written, making the code look cleaner
        # First loop for first top row
        for size in ["32", "34", "36", "38"]:
            # we append the self.TopRow controls with the checkboxes
            self.TopRow.controls.append(
                Checkbox(width=45, height=20, label=size, scale=transform.Scale(0.7))
            )

        # Smae as the top row
        for size in ["40", "42", "44", "46"]:
            self.BotRow.controls.append(
                Checkbox(width=45, height=20, label=size, scale=transform.Scale(0.7))
            )

        # This is the main contianer that will hold the checkboxes
        self.SizeBoxes = Container(
            margin=margin.only(right=10),
            alignment=alignment.center,
            content=Column(
                spacing=0,
                # Inside, I create two rows, each holding 4 checkboxes as I will demonstrate
                controls=[
                    self.TopRow,
                    self.BotRow,
                ],
            ),
        )

        # SEVEN: The iamge
        # The image starts with the black color, ut this can be changed as needed
        self.img = Container(
            scale=Scale(1.1),
            content=Image(
                src=f"./assets/black.png",
                fit="contain",
                # offset translates the image on the x and y axis
                offset=transform.Offset(-0.1, -0.2),
                animate_offset=animation.Animation(1000),
                # rotate siplye rotates the image
                rotate=transform.Rotate(12, alignment=alignment.center),
            ),
        )

        #   Main CONTAINER for all the UI stuff to go into
        self.MainFrame = Container(
            #    """ ONE: some dimensions for the inner container that holds the UI compoennts """
            width=360,
            height=620,
            padding=padding.all(20),
            gradient=self.GradientGenerator("#1f2937", "#111827"),
            border_radius=border_radius.all(25),
            # TWO: parent/main column for all the UI
            content=Column(
                controls=[
                    # THREE: start with the corner semi circle
                    Row(
                        alignment="end",
                        controls=[
                            Container(
                                alignment=alignment.top_right,
                                content=self.img,
                                width=260,
                                height=260,
                                margin=margin.only(top=-20, right=-20),
                                gradient=self.GradientGenerator("#d4d4d4", "#a3a3a3"),
                                border_radius=border_radius.only(
                                    bottom_left=300, top_right=25
                                ),
                            )
                        ],
                    ),
                    # FOUR: The title of the item
                    Row(
                        wrap=True,
                        alignment="start",
                        controls=[
                            Text(
                                "Nike Flex Control 4",
                                size=21,
                                weight="w600",
                                color="#fafafa",
                            )
                        ],
                    ),
                    # FIVE: Sub-title of the itm/description
                    Row(
                        wrap=True,
                        controls=[
                            Text(
                                "Emphasizing lightweight comfort and stability, the Nike Flex Control 4 is tailored to explosive workouts. Its lightweight, flexible upper has a midfoot strap for stability, while the sole has deep flex grooves to let your foot move naturally.",
                                color="#64748b",
                                size=13,
                                weight="w300",
                            )
                        ],
                    ),
                    # Some padding
                    Container(padding=padding.all(10)),
                    # SIX: Color row
                    # The color row also has a on_click function, which allows us to change the color of the itm.
                    # Let's pass in the image now.
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Container(
                                margin=margin.only(left=20),
                                alignment=alignment.center,
                                width=50,
                                height=20,
                                content=Text(
                                    "COLOR", color="#94a3b8", size=10, weight="w500"
                                ),
                            ),
                            Container(
                                margin=margin.only(right=30),
                                content=Row(
                                    controls=[
                                        Container(
                                            width=25,
                                            height=25,
                                            bgcolor="#6b7280",
                                            border_radius=border_radius.all(5),
                                            data="grey",
                                            on_click=lambda e: self.ChangeColor(e),
                                        ),
                                        Container(
                                            width=25,
                                            height=25,
                                            bgcolor="black",
                                            border_radius=border_radius.all(5),
                                            data="black",
                                            on_click=lambda e: self.ChangeColor(e),
                                        ),
                                        Container(
                                            width=25,
                                            height=25,
                                            bgcolor="#1e3a8a",
                                            border_radius=border_radius.all(5),
                                            data="blue",
                                            on_click=lambda e: self.ChangeColor(e),
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    ),
                    # Some more padding
                    Container(padding=padding.only(top=5)),
                    # EIGHT; The size row
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Container(
                                margin=margin.only(left=20),
                                alignment=alignment.center,
                                width=50,
                                height=20,
                                content=Text(
                                    "SIZE", color="#94a3b8", size=10, weight="w500"
                                ),
                            ),
                            # For the size row, I decided to make the code cleaner, by writing less of it, which is always the best practice when it comes to coding.
                            # So let's go back up the the main function
                            # After the logic, simply call the main variable in the main container
                            self.SizeBoxes,
                        ],
                    ),
                ]
            ),
        )

        # Returns the main container to the build function below
        return self.MainFrame

    # Build function that displays the content to the screen
    def build(self):
        return Container(
            content=(
                Column(
                    alignment="center",
                    controls=[
                        # Make sure to pass the main UI function into the build function
                        self.MainContainer(),
                    ],
                )
            ),
            # Some dimensions to the background
            width=1400,
            height=900,
            margin=margin.all(-10),
            gradient=self.GradientGenerator("#a78bfa", "#4c1d95"),
            alignment=alignment.center,
        )


# Basic flet components to get the app running
def start(page: Page):
    page.title = "Product UI Design"
    page.window_width = 1400
    page.window_height = 900
    page.update()

    # Add an instance of the App() class to the page before getting started
    app = App()
    page.add(app)


if __name__ == "__main__":
    # Also if you're following along, make sure to specify the folder where the images are located at
    flet.app(target=start, assets_dir="assets")

""" To run the flet app with HOT RELOAD, use the following
    flet -r filename.py
"""
