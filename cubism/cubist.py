#!/usr/bin/env python

from cubism import Cube, Design

def inch2mm(sz):
    return sz * 25.4

width = (790 - 40) / 3.0
height = (384 - 40) / 2.0
thickness = inch2mm(0.118)

spec = Design(width=width, height=height, thickness=thickness, teeth=4, style="ponoko")
cube = Cube(spec)
cube.render("test.svg")
