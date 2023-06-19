from flet_core import Text


def heading(title):
    return Text(value=title, size=21, weight="bold")


def subtitle(title, key=None):
    return Text(value=title, size=17, weight="w700", key=key)


def paragraph(title):
    return Text(value=title, size=12, weight="w400")
