#!/usr/bin/env python

from cubism import Design, PythonLogoFace, SunflowerFace

# Acrylic - Clear
#   0.06in, 0.08in, 0.118in, 0.177in, 0.220in, 0.354in
#   P1, P2, P3

# Plywood - Birch
#   0.016in, 0.06in, 0.125in
#   P1, 24x12

Config = {
    "birch_7_7_06.svg": {
        "size": ("2.25in", "2.25in"),
        "thickness": "0.06in",
        "pagesize": "P1",
        "teeth": 4,
        "style": "ponoko",
    },
    "birch_7_7_06_python.svg": {
        "size": ("2.25in", "2.25in"),
        "thickness": "0.06in",
        "pagesize": "P1",
        "teeth": 4,
        "style": "ponoko",
        "face_class": PythonLogoFace,
    },
    "birch_7_7_06_sunflower.svg": {
        "size": ("2.25in", "2.25in"),
        "thickness": "0.06in",
        "pagesize": "P1",
        "teeth": 4,
        "style": "ponoko",
        "face_class": SunflowerFace,
    }
}

def render_config(filename):
    kw = Config[filename]
    cube = Design(**kw)
    cube.render(filename)

if __name__ == "__main__":
    for fn in Config:
        render_config(fn)
