from . point import Point
from . utils import *
import math

__all__ = ["Face", "PythonLogoFace", "SunflowerFace"]

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
        cut_style = self.design.style.get_style("cut-stroke")
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

class PythonLogoFace(Face):
    Paths = {
        'LowerPython': 'M 154.077889,50.996396 L 154.077889,72.183968 C 154.077889,88.610406 139.997645,102.436037 123.941517,102.436039 L 75.757056,102.436039 C 62.558525,102.436039 51.636715,113.608810 51.636713,126.682184 L 51.636713,172.115896 C 51.636713,185.046592 63.005031,192.652283 75.757056,196.362041 C 91.027346,200.803063 105.670755,201.605668 123.941517,196.362041 C 136.086304,192.884139 148.061865,185.884841 148.061859,172.115896 L 148.061859,153.931292 L 99.877399,153.931292 L 99.877399,147.869756 L 148.061859,147.869756 L 172.182209,147.869756 C 186.202297,147.869756 191.426757,138.197265 196.302534,123.679221 C 201.339050,108.733121 201.124749,94.360024 196.302534,75.186931 C 192.837697,61.382304 186.220127,50.996396 172.182209,50.996396 L 154.077889,50.996396 z',
        'LowerPythonEye': 'M 126.977644,166.054365 C 131.978443,166.054370 136.029800,170.107105 136.029800,175.118859 C 136.029797,180.148444 131.978437,184.238969 126.977644,184.238969 C 121.994707,184.238969 117.925487,180.148444 117.925487,175.118859 C 117.925491,170.107105 121.994702,166.054365 126.977644,166.054365 z',
        'UpperPython': 'M 98.809132,0.001636 C 90.562286,0.039537 82.686732,0.735191 75.757056,1.948001 C 55.343098,5.515082 51.636715,12.981291 51.636713,26.750250 L 51.636713,44.934859 L 99.877399,44.934859 L 99.877399,50.996396 L 51.636713,50.996396 L 33.532400,50.996396 C 19.512314,50.996396 7.235925,59.331227 3.396028,75.186931 C -1.033245,93.361247 -1.229708,104.702316 3.396028,123.679221 C 6.825148,137.804895 15.014352,147.869752 29.034434,147.869756 L 45.620684,147.869756 L 45.620684,126.070469 C 45.620684,110.321771 59.397313,96.430116 75.757056,96.430113 L 123.941517,96.430113 C 137.354363,96.430113 148.061865,85.507044 148.061859,72.183968 L 148.061859,26.750250 C 148.061859,13.819556 137.032883,4.106081 123.941517,1.948001 C 115.654488,0.583587 107.055978,-0.036265 98.809132,0.001636',
        'UpperPythonEye': 'M 72.720929,14.627178 C 77.703860,14.627178 81.773086,18.717695 81.773086,23.747287 C 81.773082,28.759052 77.703860,32.811787 72.720929,32.811787 C 67.720134,32.811785 63.668772,28.759050 63.668772,23.747287 C 63.668771,18.717697 67.720134,14.627178 72.720929,14.627178 z'
    }
    Size = 200

    def load_matrix(self, matrix):
        matrix = map(float, matrix.split(','))

    def apply_matrix(self, matrix, pathcmd, xy):
        keys = ('a', 'b', 'c', 'd', 'e', 'f')
        ns = dict(zip(keys, matrix))
        ns['x'] = xy[0]
        ns['y'] = xy[1]
        if pathcmd.islower():
            ns['e'] = 0
            ns['f'] = 0
        x = eval("a * x + c * y + e", ns)
        y = eval("b * x + d * y + f", ns)
        return (x, y)

    def transform(self, path, matrix):
        path = path.split(' ')[::-1]
        new_path = []
        while path:
            thing = path.pop()
            if ',' in thing:
                xy = map(float, thing.split(','))
                xy = self.apply_matrix(matrix, cmd, xy)
                xy = "%f,%f" % xy
                new_path.append(xy)
            else:
                cmd = thing
                new_path.append(cmd)
        new_path = str.join(' ', new_path)
        return new_path

    def render(self, dwg):
        super(PythonLogoFace, self).render(dwg)
        target_size = min(*self.design.size) * .75
        scale_factor = target_size / float(self.Size)
        offset = self.center - (target_size / 2.0)
        matrix = (scale_factor, 0, 0, scale_factor, offset.x, offset.y)
        engrave_style = self.design.style.get_style("engrave-stroke")
        cut_style = self.design.style.get_style("cut-stroke")
        for (path_name, path) in self.Paths.items():
            path = self.transform(path, matrix)
            if "eye" in path_name.lower():
                style = cut_style
            else:
                style = engrave_style
            path = dwg.path(d=path, **style)
            dwg.add(path)


class SunflowerFace(Face):
    # https://en.wikipedia.org/wiki/Fermat%27s_spiral
    Florets = 200
    Angle = 137.5
    FloretAreaRatio = .2
    SunflowerAreaRatio = .8

    @property
    def radius(self):
        return (min(*self.design.size) / 2.0) * self.SunflowerAreaRatio

    @property
    def constant(self):
        constant = self.radius / math.sqrt(self.Florets)
        return constant

    @property
    def floret_radius(self):
        sunflower_area = math.pi * self.radius ** 2
        floret_area = (sunflower_area / self.Florets) * self.FloretAreaRatio
        return math.sqrt(floret_area / math.pi)

    def render(self, dwg):
        super(SunflowerFace, self).render(dwg)
        cut_style = self.design.style.get_style("cut-stroke")
        floret_radius = self.floret_radius
        for pt in self.sunflower(self.Florets, self.constant):
            pt = pt + self.center
            floret = dwg.circle(pt, r=floret_radius, **cut_style)
            dwg.add(floret)

    def sunflower(self, florets, constant):
        for idx in range(1, 1 + florets):
            radius = constant * math.sqrt(idx)
            angle = idx * math.radians(137.5)
            xy = from_polar(radius, angle)
            yield Point(*xy)
