import flet as ft
from base import FxControls
from components import typography as fxType
from components import block as fxCode


intro = """
Fletxible is a Python web boilerplate project designed to provide a solid foundation for building web applications with Python and Flet. The project comes pre-configured with a range of tools and features to make it easy for developers to get started building their applications, without the need to spend time setting up infrastructure or configuring tools.
"""

pip = """
Fletxible is published as a Python package and can be installed with pip, ideally by using a virtual environment. Open up a terminal and install Fletxible using the following command:
"""

pip_command = """```python
pip3 install Fletxible
```
"""

pip_outro = """
This will automatically install compatible versions of all dependencies including Flet.
"""

app_intro = """
After installing Fletxible, you can test if it's working properly by running the following command:
"""

app_command = """
```python
fletxible-init
```
"""

app_outro = """
If the package was installed correctly, you should see the following directories:
    - core              
    - components
    - utilities 

As well as the following files:
    - main.py
    - script.py
    - base.py
    - fx_tempalte.py
    - fx_config.yml
"""

script = """
First, open up your fx_config.yml file and make sure the following are present:
"""

config = """```yaml
site-name: "fletxible."
repo-url: "https://github.com/LineIndent/fletxible"

theme:
  - bgcolor: "teal"

navigation:
  - Home: "index.py"
  - About: "about.py
```
"""

change_config = """
You can replace the default configuration with your own data. The navigation header will generate files with names correpsonding to the python file. 
"""

script_two = """
When you're set with your config file (fx_config.yml), navigate to your terminal and run the following command to generate your files inside a directory called web:
"""

script_cmd = """```python
python3 script.py
```
"""

conclusion = """
That's it! You now have your pages set up along with the necessary routing and layout. 
You can open the web directory and start creating your pages immediately!
"""


class FxView(ft.View):
    def __init__(
        self,
        page: ft.Page,
        docs: dict,
        route="",  # set your routes here ...
        bgcolor="#23262d",
        padding=0,
    ) -> None:
        self.page = page
        self.docs = docs

        self.page.on_resize = self.fx_dynamics

        self.fx_view = FxControls(
            self.page, self.docs, self.fx_controls(), self.fx_rail()
        )

        super().__init__(route=route, bgcolor=bgcolor, padding=padding)

        self.controls = [ft.Container(expand=True, content=self.fx_view)]

    def fx_dynamics(self, event) -> None:
        if self.page.width <= 850:
            self.fx_view.set_application_to_mobile()
        else:
            self.fx_view.set_application_to_desktop()

    # Method: Create your side rails(fx_right panel) here by passing in strings...
    def fx_rail(self) -> list:
        return [
            "Installation",
            "Application Setup",
            "Configuration",
        ]

    # Method: Create your layout here. Create your UI inside this list ...
    def fx_controls(self) -> list:
        return [
            ft.Divider(height=35, color="transparent"),
            ft.Divider(height=25, color="transparent"),
            # start your layout design here ...
            fxType.heading(f"Getting Started"),
            fxType.paragraph(intro),
            fxType.subtitle(f"Installation"),
            ft.Divider(height=5, color="transparent"),
            fxType.subtitle(f"with PIP", key=1),
            fxType.paragraph(pip),
            fxCode.CodeBlock(pip_command),
            fxType.paragraph(pip_outro),
            fxType.subtitle(f"Application Setup", key=2),
            fxType.paragraph(app_intro),
            fxCode.CodeBlock(app_command),
            fxType.paragraph(app_outro),
            fxType.subtitle(f"Configure YAML File", key=3),
            fxType.paragraph(script),
            fxCode.CodeBlock(config),
            fxType.paragraph(change_config),
            fxType.paragraph(script_two),
            fxCode.CodeBlock(script_cmd),
            fxType.paragraph(conclusion),
            # end your layout design here ...
            ft.Divider(height=15, color="transparent"),
        ]
