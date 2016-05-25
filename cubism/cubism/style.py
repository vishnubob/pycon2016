__all__ = ["get_style"]

class BaseStyle(object):
    StyleSheet = {
        "cut-stroke": {"stroke-width": "1", "stroke": "rgb(0, 0, 255)", "stroke-opacity": "1", "fill": "none"},
        "engrave-stroke": {"stroke-width": "1", "stroke": "rgb(255, 0, 0)", "stroke-opacity": "1", "fill": "none"},
        "engrave-area": {"fill": "rgb(0, 0, 0)", "fill-opacity": "1"},
    }
    PageSizes = {}

    def get_style(self, name):
        return self.StyleSheet[name]

    def get_css(self):
        css = '\n'
        for (style_id, style_def) in self.StyleSheet.items():
            print style_id
            style_def = str.join('\n', ["%s: %s;" % kv for kv in style_def.items()])
            css += "%s { %s }\n" % (style_id, style_def)
        return css
    
    def get_pagesize(self, name):
        return self.PageSizes[name]

class Example(BaseStyle):
    StyleSheet = {
        "cut-stroke": {"stroke-width": "1", "stroke": "rgb(255, 255, 255)", "stroke-opacity": "1", "fill": "none"},
        "engrave-stroke": {"stroke-width": "1", "stroke": "rgb(0, 255, 0)", "stroke-opacity": "1", "fill": "none"},
        "engrave-area": {"fill": "rgb(0, 0, 0)", "fill-opacity": "1"},
    }

class Ponoko(BaseStyle):
    StyleSheet = {
        "cut-stroke": {"stroke-width": "0.01mm", "stroke": "rgb(0, 0, 255)", "stroke-opacity": "1", "fill": "none"},
        "engrave-stroke": {"stroke-width": "0.01mm", "stroke": "rgb(255, 0, 0)", "stroke-opacity": "1", "fill": "none"},
        "engrave-area": {"fill": "rgb(0, 0, 0)", "fill-opacity": "1"},
    }

    PageSizes = {
        "P1": ("7.1in", "7.1in"),
        "P2": ("15.1in", "15.1in"),
        "P3": ("31.1in", "15.1in"),
        "24x12": ("23.47in", "11.46in"),
    }

def get_style(name=None):
    if name == "ponoko":
        return Ponoko
    if name == "example":
        return Example
    if name == None:
        return BaseStyle
