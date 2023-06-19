import yaml
import os
from utilities.router import fx_router
from utilities.links import fx_nav_links


def open_yaml_script() -> dict:
    with open("fx_config.yml", "r") as file:
        docs = yaml.safe_load(file)

    return docs


def check_fweb_directory_exists():
    _dir = None
    for root, dirs, files in os.walk("."):
        if "web" in dirs:
            _dir = os.path.join(root, "web")
            break

        if not _dir:
            _dir = os.path.join(os.getcwd(), "web")
            os.mkdir(_dir)


def update_fweb_directory(docs: dict):
    for file in os.listdir("web"):
        if file.endswith(".py"):
            found = False
            for page in docs["navigation"]:
                if page.get(next(iter(page))) == file:
                    found = True
                    break
            if not found:
                os.remove(os.path.join("web", file))


def temporary_file_for_routing(docs: dict):
    with open("temp.txt", "w") as f:
        for page in docs["navigation"]:
            for key in page:
                route = os.path.splitext(page[key])[0]
                f.write(f"{fx_router(route)}")


def set_site_name(docs: dict):
    site_name = f"'{docs['site-name']}',"

    with open("./core/header.py", "r") as fHeader:
        header = fHeader.read()

    with open("./core/drawer.py", "r") as fDrawer:
        drawer = fDrawer.read()

    header_start_idx = header.index("# start #")
    header_end_idx = header.index("# end #")

    drawer_start_idx = drawer.index("# start #")
    drawer_end_idx = drawer.index("# end #")

    header_modified_string = (
        header[:header_start_idx] + "# start #\n" + site_name + header[header_end_idx:]
    )

    drawer_modified_string = (
        drawer[:drawer_start_idx] + "# start #\n" + site_name + drawer[drawer_end_idx:]
    )

    with open("./core/header.py", "w") as w:
        w.write(header_modified_string)

    with open("./core/drawer.py", "w") as w:
        w.write(drawer_modified_string)


def create_router_file():
    with open("temp.txt", "r") as r:
        routers = r.read()

    with open("./core/navigation.py", "r") as r:
        pre_code = r.read()

    start_idx = pre_code.index("# begin #")
    end_idx = pre_code.index("# finish #")

    code_to_add = routers

    modified_string = (
        pre_code[:start_idx] + "# begin #\n" + code_to_add + pre_code[end_idx:]
    )

    with open("./core/navigation.py", "w") as f:
        f.write(modified_string)

    os.remove("temp.txt")


def create_fx_views(docs: dict):
    file_list: list = []
    for page in docs["navigation"]:
        for key in page:
            filename = f"{page[key]}"
            filepath = os.path.join("web", filename)
            file_list.append(filepath)

    with open("fx_template.py", "r") as file:
        fx_template = file.read()

    for filepath in file_list:
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write(fx_template)


def create_navigation_pages():
    with open("./core/navigation.py", "r") as r:
        pre_code = r.read()

    start_idx = pre_code.index("# start #")
    end_idx = pre_code.index("# end #")

    code_to_add = "\n".join(fx_nav_links())

    modified_string = (
        pre_code[:start_idx] + "# start #\n" + code_to_add + pre_code[end_idx:]
    )

    with open("./core/navigation.py", "w") as f:
        f.write(modified_string)


def script():
    try:
        docs = open_yaml_script()

    except FileNotFoundError as e:
        print(e)

    try:
        check_fweb_directory_exists()

    except Exception as e:
        print(e)

    try:
        update_fweb_directory(docs)

    except Exception as e:
        print("Looping over fweb: ", e)

    try:
        temporary_file_for_routing(docs)

    except Exception as e:
        print(e)

    try:
        set_site_name(docs)

    except Exception as e:
        print("Site-name error: ", e)

    try:
        create_router_file()

    except Exception as e:
        print(e)

    try:
        create_fx_views(docs)

    except Exception as e:
        print(e)

    try:
        create_navigation_pages()

    except Exception as e:
        print(e)


script()
