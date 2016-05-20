#!/usr/bin/env python

import svgwrite
from collections import namedtuple

class Specification(object):
    def __init__(self, width=4, height=4, thickness=1/8.0, teeth=4):
        self.width = width
        self.height = height
        self.thickness = thickness
        self.teeth = teeth
        
        if (teeth % 2) == 0:
            # even
            self.negative_teeth = teeth
            self.positive_teeth = teeth - 1
        else:
            self.positive_teeth = teeth
            self.negative_teeth = teeth + 1

    def step(self):
        teeth = self.positive_teeth * 2 - 1 + 4
        x_step = self.width / float(teeth)
        x_step_list = [self.thickness, x_step * 2] + ([x_step] * (self.positive_teeth * 2 - 1)) + [x_step * 2, self.thickness]
        for idx in range((self.positive_teeth * 2 - 1 + 4) * 2):
            if idx % 2:
                yield x_step_list[idx / 2]
            else:
                yield 0

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

    def render(self, dwg):
        # top-left
        x_offset = self.center.x - (self.spec.width / 2.0)
        y_offset = self.center.y - (self.spec.height / 2.0)
        self.pen = Point(x_offset + self.spec.thickness, y_offset)
        ptlist = []
        if not self.polarity[0]:
            self.pen = self.pen + self.spec.thickness
        for (direction, positive) in zip(self.EdgeList, self.polarity):
            ptlist += list(self.wave(direction, positive=positive))
            break
        ptlist = ["M %s,%s" % ptlist[0]] + ["L %s,%s" % pt for pt in ptlist[1:]]
        d = str.join(' ', ptlist)
        path = dwg.path(d=d, fill='none', stroke_width=2, stroke='black')
        dwg.add(path)
        dbox = dwg.rect(insert=(x_offset, y_offset), size=(self.spec.width, self.spec.height), stroke='red', stroke_width=1, fill='none')
        dwg.add(dbox)

    def wave(self, direction, positive=True):
        (step, thickness, length) = self.dirmap[direction]
        if positive:
            step_length = length / (self.spec.teeth * 2.0 - 1)
            step = step * step_length
            thickness = thickness * self.spec.thickness
            step_map = [Point(), step]
            thickness_map = [-thickness, Point(), thickness, Point()]
        else:
            step_length = length / (self.spec.teeth * 2.0)
            step = step * step_length
            thickness = thickness * self.spec.thickness
            step_map = [Point(), step]
            thickness_map = [thickness, Point(), -thickness, Point()]
        count = self.spec.teeth * len(thickness_map) - 2
        """
        for idx in range(count):
            if idx == 0:
                yield self.pen
                continue
            _step = step_map[idx % 2]
            _thickness = thickness_map[idx % 4]
            #print (idx, self.pen, _step, _thickness)
            self.pen = self.pen + _step + _thickness
            yield self.pen
        """
        _step_map = iter(self.spec.step())
        idx = 0
        for step in self.spec.step():
            _step = Point(step, 0)
            _thickness = thickness_map[idx % 4]
            self.pen = self.pen + _step + _thickness
            yield self.pen
            idx += 1


class Cube(object):
    def __init__(self, specification):
        self.specification = specification

    def render(self, filename):
        dwg = svgwrite.Drawing(filename)
        f = Face(self.specification, center=(300, 300))
        f.render(dwg)
        #polarity = (0, 0, 0, 0)
        #f = Face(self.specification, center=(850, 300), polarity=polarity)
        #f.render(dwg)
        dwg.save()

spec = Specification(width=500, height=500, thickness=25, teeth=4)
cube = Cube(spec)
cube.render("test.svg")
