#!/usr/bin/env python

import svgwrite
from collections import namedtuple

class Specification(object):
    def __init__(self, width=4, height=4, thickness=1/8.0, teeth=4):
        self.width = width
        self.height = height
        self.size = Point(self.width, self.height)
        self.thickness = thickness
        self.teeth = teeth
        
        if (teeth % 2) == 0:
            # even
            self.negative_teeth = teeth
            self.positive_teeth = teeth - 1
        else:
            self.positive_teeth = teeth
            self.negative_teeth = teeth + 1

    def step(self, length, polarity):
        teeth = self.teeth * 2 + 1
        step = length / float(teeth)
        (prev_polarity, polarity, next_polarity) = polarity
        if polarity:
            offset = 0
            thickness = [0, self.thickness, 0, -self.thickness]
        else:
            offset = self.thickness
            thickness = [0, -self.thickness, 0, self.thickness]
        step_list = [step] * (teeth - 2)
        if prev_polarity:
            step_list = [0] + step_list + [step]
        else:
            step_list = [self.thickness, step - self.thickness] + step_list
        if next_polarity:
            step_list = step_list + [step]
        else:
            step_list = step_list + [step - self.thickness]
        #yield (step_list[0], offset)
        step_idx = 1
        yield (step_list[0], offset)
        for idx in range(len(step_list) * 2 - 3):
            _cliff = thickness[idx % 4]
            _step = 0
            if _cliff == 0:
                _step = step_list[step_idx]
                step_idx += 1
            yield (_step, _cliff)

PointBase = namedtuple("PointBase", ('x', 'y'))
class Point(PointBase):
    def __new__(cls, x=0, y=0):
        self = super(Point, cls).__new__(cls, x, y)
        return self

    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.x + other, self.y + other)
        return self.__class__(self.x + other[0], self.y + other[1])

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.x - other, self.y - other)
        return self.__class__(self.x - other[0], self.y - other[1])
    
    def __mul__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.x * other, self.y * other)
        return self.__class__(self.x * other[0], self.y * other[1])
    
    def __div__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.x / other, self.y / other)
        return self.__class__(self.x / other[0], self.y / other[1])
    
    def __neg__(self):
        return self.__class__(-self.x, -self.y)

class Face(object):
    EdgeList = ["right", "down", "left", "up"]

    def __init__(self, spec, polarity=(1, 1, 1, 1), center=None):
        center = center if center != None else (0, 0)
        self.center = Point(*center)
        self.spec = spec
        self.pen = Point(0, 0)
        self.polarity = map(bool, polarity)
        self.dirmap = {
            "right": (Point(1, 0), Point(0, 1), self.spec.width),
            "down": (Point(0, 1), Point(-1, 0), self.spec.height),
            "left": (Point(-1, 0), Point(0, -1), self.spec.width),
            "up": (Point(0, -1), Point(1, 0), self.spec.height),
        }

    @property
    def thickness(self):
        return self.spec.thickness

    @property
    def x_step(self):
        return self.spec.width / (self.spec.teeth * 2.0 - 1)

    @property
    def y_step(self):
        return self.spec.height / (self.spec.teeth * 2.0 - 1)

    def debug_step(self, dwg, *args):
        # top-left
        x_offset = self.center.x - (self.spec.width / 2.0)
        y_offset = self.center.y - (self.spec.height / 2.0)
        pen = Point(x_offset, y_offset)
        for (_step, _thickness) in self.spec.step(*args):
            _step = Point(_step, 0)
            pen = pen + _step
            dl = dwg.line(start=(pen[0], 0), end=(pen[0], 400), stroke='green', stroke_width=1, fill='none')
            dwg.add(dl)

    def corner(self, name):
        h_width = self.spec.width / 2.0
        h_height = self.spec.height / 2.0
        half_pt = Point(h_width, h_height)
        if name == "right":
            return self.center + (-h_width, -h_height)
        if name == "down":
            return self.center + (h_width, -h_height)
        if name == "left":
            return self.center + (h_width, h_height)
        if name == "up":
            return self.center + (-h_width, h_height)

    def render(self, dwg):
        # top-left
        pts = []
        ptlist = []
        for (edge_idx, direction) in enumerate(self.EdgeList):
            polarity = (self.polarity[(edge_idx - 1) % 4], self.polarity[edge_idx], self.polarity[(edge_idx + 1) % 4])
            self.pen = self.corner(direction)
            #self.debug_step(dwg, self.spec.width, polarity)
            ptlist += list(self.wave(direction, polarity))
        pts += ["M %s,%s" % ptlist[0]] + ["L %s,%s" % pt for pt in ptlist[1:]]
        d = str.join(' ', pts)
        path = dwg.path(d=d, fill='none', stroke_width=1, stroke='black')
        dwg.add(path)
        insert = self.corner("right")
        #dbox = dwg.rect(insert=insert, size=(self.spec.width, self.spec.height), stroke='red', stroke_width=1, fill='none')
        #dwg.add(dbox)

    def wave(self, direction, polarity):
        (step, thickness, length) = self.dirmap[direction]
        for (_step, _thickness) in self.spec.step(length, polarity):
            _step = step * _step
            _thickness = thickness * _thickness
            self.pen = self.pen + _step + _thickness
            yield self.pen

class Cube(object):
    Faces = [
        (1, 1, 1, 1), 
        (1, 1, 1, 1),
        (1, 0, 1, 0), 
        (0, 0, 0, 0), 
        (0, 0, 0, 0),
        (1, 0, 1, 0),
    ]

    def __init__(self, specification):
        self.specification = specification
        self.margin = (20, 20)

    def iter_faces(self):
        center = self.specification.size / 2.0
        pen = center + self.margin
        for (face_idx, face) in enumerate(self.Faces):
            yield (pen, face)
            pen = pen + Point(self.specification.width, 0)
            if face_idx == 2:
                pen = center + self.margin + Point(0, self.specification.height)

    def render(self, filename):
        dwg = svgwrite.Drawing(filename)
        for (center, polarity) in self.iter_faces():
            f = Face(self.specification, center=center, polarity=polarity)
            f.render(dwg)
        dwg.save()

spec = Specification(width=400, height=400, thickness=10, teeth=4)
cube = Cube(spec)
cube.render("test.svg")
