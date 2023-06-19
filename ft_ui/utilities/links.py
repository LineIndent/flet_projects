"""
Method: Generates a list of links to be inserted inside the Navigation() class
"""
import os


def fx_nav_links() -> list:
    links: list = []
    for file in os.listdir("web"):
        # Set the path of the file to loop over folders and only include files
        path = os.path.join("web", file)

        # If the path is NOT a folder, continue ...
        if not os.path.isdir(path):
            filename = os.path.splitext(file)[0]
            string = f"ft.Text(size=11, weight='bold', spans=[ft.TextSpan('{filename.capitalize()}', data='/{filename}', on_click=lambda e: self.set_app_router(e))]),"
            links.append(string)

    return links
