""" 
App Material: Neural Network Builder Guide 
    1. https://www.cs.toronto.edu/~kriz/cifar.html
    2. https://www.kaggle.com/code/viratkothari/image-classification-of-cifar-10-using-tensorflow 
    
"""


import flet as ft

import os

# import time
import numpy as np

from tensorflow.keras import models
from PIL import Image

class_names: dict[int, str] = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck",
}

# import your neural network model...
model = models.load_model("baseline_model.keras")


# setup image processing and predications...
def classify(model, image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    img = img.resize((32, 32))
    data = np.asarray(img)
    probs = model.predict(np.array([data])[:1])

    prob = probs.max()
    pred = class_names[np.argmax(probs)]

    return prob, pred


# upload  class ...
class Upload(ft.Row):
    def __init__(self, result_instance):
        super().__init__(alignment="center", spacing=30)

        self.result_instance = result_instance

        self.file_name = ft.Text("Select image...")
        self.toggle_pick_file = ft.FilePicker(on_result=self.image_path)
        self.pick_file_btn = ft.IconButton("upload", on_click=self.select_file)

        self.controls = [
            self.file_name,
            self.pick_file_btn,
            self.toggle_pick_file,
        ]

    def select_file(self, e):
        self.toggle_pick_file.pick_files(
            initial_directory=os.getcwd(),
        )

    def get_model_predictions(self, path: str):
        res1, res2 = classify(model, path)

        self.result_instance.result_name.value = res2.capitalize()
        self.result_instance.result_name.update()

        for index in range(int(res1 * 100)):
            self.result_instance.results.value = f"{index}%"
            self.result_instance.results.update()
            time.sleep(0.025)

    def image_path(self, e: ft.FilePickerResultEvent):
        # get the path and name of the file from the event (e.files)

        path = ", ".join(map(lambda f: f.path, e.files)) if e.files else ""

        res = ", ".join(map(lambda f: f.name, e.files)) if e.files else ""

        self.file_name.value = f"File Name: {res}"
        self.result_instance.image_display.image_src = path

        self.file_name.update()
        self.result_instance.update()

        self.get_model_predictions(path)


# Result class ...
class Result(ft.Row):
    def __init__(self):
        super().__init__(expand=True)

        self.results = ft.Text("0%", size=42)
        self.result_name = ft.Text(size=18)

        self.image_display = ft.Container(image_fit="fit", expand=1)

        self.prediction_display = ft.Container(
            expand=1,
            content=ft.Column(
                spacing=0,
                horizontal_alignment="center",
                alignment="center",
                controls=[self.result_name, self.results],
            ),
            alignment=ft.alignment.center,
        )

        self.controls = [
            self.image_display,
            ft.VerticalDivider(thickness=1),
            self.prediction_display,
        ]


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window_full_screen = True
    page.padding = 25

    result = Result()
    upload = Upload(result)

    page.add(upload, ft.Divider(thickness=1), result)
    page.update()


ft.app(target=main, assets_dir="demo_images")
