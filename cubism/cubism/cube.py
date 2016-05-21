import svgwrite
from . point import Point
from . style import get_style

__all__ = ["Cube"]

class Face(object):
    EdgeList = ["right", "down", "left", "up"]

    def __init__(self, design, polarity=(1, 1, 1, 1), center=None):
        center = center if center != None else (0, 0)
        self.center = Point(*center)
        self.design = design
        self.pen = Point(0, 0)
        self.polarity = map(bool, polarity)
        self.dirmap = {
            "right": (Point(1, 0), Point(0, 1), self.design.width),
            "down": (Point(0, 1), Point(-1, 0), self.design.height),
            "left": (Point(-1, 0), Point(0, -1), self.design.width),
            "up": (Point(0, -1), Point(1, 0), self.design.height),
        }

    @property
    def thickness(self):
        return self.design.thickness

    @property
    def x_step(self):
        return self.design.width / (self.design.teeth * 2.0 - 1)

    @property
    def y_step(self):
        return self.design.height / (self.design.teeth * 2.0 - 1)

    def debug_step(self, dwg, *args):
        # top-left
        x_offset = self.center.x - (self.design.width / 2.0)
        y_offset = self.center.y - (self.design.height / 2.0)
        pen = Point(x_offset, y_offset)
        for (_step, _thickness) in self.design.step(*args):
            _step = Point(_step, 0)
            pen = pen + _step
            dl = dwg.line(start=(pen[0], 0), end=(pen[0], 400), stroke='green', stroke_width=1, fill='none')
            dwg.add(dl)

    def corner(self, name):
        h_width = self.design.width / 2.0
        h_height = self.design.height / 2.0
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
        cut_style = self.design.style.get_style("#cut-stroke")
        for (edge_idx, direction) in enumerate(self.EdgeList):
            polarity = (self.polarity[(edge_idx - 1) % 4], self.polarity[edge_idx], self.polarity[(edge_idx + 1) % 4])
            self.pen = self.corner(direction)
            #self.debug_step(dwg, self.design.width, polarity)
            ptlist += list(self.wave(direction, polarity))
        pts += ["M %s,%s" % ptlist[0]] + ["L %s,%s" % pt for pt in ptlist[1:]]
        d = str.join(' ', pts)
        #path = dwg.path(d=d, id="cut-stroke")
        path = dwg.path(d=d, **cut_style)
        dwg.add(path)
        #insert = self.corner("right")
        #dbox = dwg.rect(insert=insert, size=(self.design.width, self.design.height), stroke='red', stroke_width=1, fill='none')
        #dwg.add(dbox)

    def wave(self, direction, polarity):
        (step, thickness, length) = self.dirmap[direction]
        for (_step, _thickness) in self.design.step(length, polarity):
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

    def __init__(self, design):
        self.design = design
        self.margin = (20, 20)

    def iter_faces(self):
        center = self.design.size / 2.0
        pen = center + self.margin
        for (face_idx, face) in enumerate(self.Faces):
            yield (pen, face)
            pen = pen + Point(self.design.width, 0)
            if face_idx == 2:
                pen = center + self.margin + Point(0, self.design.height)

    def render(self, filename):
        width = "790mm"
        height = "384mm"
        size = (width, height)
        viewbox = "0 0 790 384"
        dwg = svgwrite.Drawing(filename, size=size, viewBox=viewbox, debug=False)
        #dwg.defs.add(dwg.style(self.design.style.get_css()))
        for (center, polarity) in self.iter_faces():
            f = Face(self.design, center=center, polarity=polarity)
            f.render(dwg)
            #logo = PythonLogo(center=center)
            #logo.render(dwg)
        dwg.save()
