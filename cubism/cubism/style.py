
class Style(object):
    StyleMap = {
        "cut-stroke": {"stroke-width": 0.01, "stroke": "rgb(0, 0, 255)", "stroke-opacity": "1"},
        "engrave-stroke": {"stroke-width": 0.01, "stroke": "rgb(255, 0, 0)", "stroke-opacity": "1"},
        "engrave-area": {"fill": "rgb(0, 0, 0)", "fill-opacity": "1"},
    }

    def get_style(self, name):
        return self.StyleMap[name]

class Ponoko(Style):
    # All sizes are in mm
    Sizes = {
        "P1": (790, 384),
        "P2": (384, 384),
        "P3": (181, 181),
        "24x12": (596, 291),
    }

    StyleMap = {
        "cut-stroke": {"stroke-width": 0.01, "stroke": "rgb(0, 0, 255)", "stroke-opacity": "1"},
        "engrave-stroke": {"stroke-width": 0.01, "stroke": "rgb(255, 0, 0)", "stroke-opacity": "1"},
        "engrave-area": {"fill": "rgb(0, 0, 0)", "fill-opacity": "1"},
    }

