__all__ = ["get_style"]

class BaseStyle(object):
    StyleSheet = {
        "#cut-stroke": {"stroke-width": "1", "stroke": "rgb(0, 0, 255)", "stroke-opacity": "1", "fill": "none"},
        "#engrave-stroke": {"stroke-width": "1", "stroke": "rgb(255, 0, 0)", "stroke-opacity": "1", "fill": "none"},
        "#engrave-area": {"fill": "rgb(0, 0, 0)", "fill-opacity": "1"},
    }

    def get_style(self, name):
        return self.StyleSheet[name]

    def get_css(self):
        css = '\n'
        for (style_id, style_def) in self.StyleSheet.items():
            print style_id
            style_def = str.join('\n', ["%s: %s;" % kv for kv in style_def.items()])
            css += "%s { %s }\n" % (style_id, style_def)
        return css

class Ponoko(BaseStyle):
    # All sizes are in mm
    Sizes = {
        "P1": (790, 384),
        "P2": (384, 384),
        "P3": (181, 181),
        "24x12": (596, 291),
    }

    """
    StyleSheet = {
        "#cut-stroke": {"stroke-width": 0.01, "stroke": "rgb(0, 0, 255)", "stroke-opacity": "1", "fill": "none"},
        "#engrave-stroke": {"stroke-width": 0.01, "stroke": "rgb(255, 0, 0)", "stroke-opacity": "1", "fill": "none"},
        "#engrave-area": {"fill": "rgb(0, 0, 0)", "fill-opacity": "1"},
    }
    """

def get_style(name=None):
    if name == "ponoko":
        return Ponoko
    if name == None:
        return BaseStyle
