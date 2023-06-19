"""
Method: Generates a list of routers to be inserted inside the Navigation() class
"""


def fx_router(route):
    string = f"\tif route.control.data == '/{route}':\n\t\tself.page.views.append(self.page.data[route.control.data].loader.load_module().FxView(self.page, self.docs))\n\t\tself.page.go(route.control.data)\n\n"

    string = string.expandtabs(8)
    return string
