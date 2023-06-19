"""
Method: Returns a string to create the fx_config.yml file
"""


def create_yaml_file():
    string = """
  site-name: "fletxible."
  repo-url: "https://github.com/LineIndent/fletxible"
  
  theme:
    - bgcolor: "pink"
    
  navigation:
    - Home: "index.py"
  """

    return string
