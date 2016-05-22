import svgwrite
from . point import Point
from . style import get_style
from . face import Face
from . utils import unit

__all__ = ["Design"]

class Design(object):
    Faces = [
        (1, 1, 1, 1), 
        (1, 1, 1, 1),
        (1, 0, 1, 0), 
        (0, 0, 0, 0), 
        (0, 0, 0, 0),
        (1, 0, 1, 0),
    ]

    def __init__(self, size=(0, 0), thickness=0, teeth=1, pagesize=None, style=None, face_class=None):
        self.style = get_style(style)()
        self.size = size
        self.pagesize = pagesize
        self.thickness = thickness
        self.teeth = teeth
        self.face_class = face_class if face_class != None else Face
    
    def get_thickness(self):
        return self._thickness
    def set_thickness(self, thickness):
        self._thickness = unit(thickness).magnitude
    thickness = property(get_thickness, set_thickness)

    def check_design(self):
        if (self.pagesize.x < (self.width * 3)) or (self.pagesize.y < (self.height * 2)):
            msg = "The current page width can not fit the design"
            raise ValueError(msg)
        # XXX: check thickness

    def get_pagesize(self):
        if self._pagesize == None:
            return (self.width * 3, self.height * 2)
        return self._pagesize
    def set_pagesize(self, pagesize):
        if pagesize != None:
            if type(pagesize) in (str, unicode):
                pagesize = self.style.get_pagesize(pagesize)
            pagesize = Point(unit(pagesize[0]).magnitude, unit(pagesize[1]).magnitude)
        self._pagesize = pagesize
    pagesize = property(get_pagesize, set_pagesize)

    def get_size(self):
        return self._size
    def set_size(self, size):
        self._size = Point(unit(size[0]).magnitude, unit(size[1]).magnitude)
    size = property(get_size, set_size)

    def get_width(self):
        return self.size.x
    def set_width(self, val):
        self.size = (val, self.size.y)
    width = property(get_width, set_width)

    def get_height(self):
        return self.size.y
    def set_height(self, val):
        self.size = (self.size.x, val)
    height = property(get_height, set_height)

    @property
    def negative_teeth(self):
        return self.teeth + (self.teeth % 2)

    @property
    def positive_teeth(self):
        return self.teeth if (self.teeth % 2) else self.teeth - 1

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

    def iter_faces(self):
        center = self.size / 2.0
        page_center = self.pagesize / 2.0
        left_margin = (self.pagesize.x - self.width * 3) / 2.0
        top_margin = (self.pagesize.y - self.height * 2) / 2.0
        margin = Point(left_margin, top_margin)
        pen = center + margin
        for (face_idx, face) in enumerate(self.Faces):
            yield (pen, face)
            pen = pen + Point(self.width, 0)
            if face_idx == 2:
                pen = center + margin + Point(0, self.height)

    def render(self, filename):
        self.check_design()
        width = "%dmm" % self.pagesize.x
        height = "%dmm" % self.pagesize.y
        pagesize = (width, height)
        viewbox = "0 0 %d %d" % (self.pagesize.x, self.pagesize.y)
        dwg = svgwrite.Drawing(filename, size=pagesize, viewBox=viewbox, debug=False)
        for (center, polarity) in self.iter_faces():
            f = self.face_class(self, center=center, polarity=polarity)
            f.render(dwg)
            #logo = PythonLogo(center=center)
            #logo.render(dwg)
        #pagebox = dwg.rect(insert=(0, 0), size=self.pagesize, stroke='red', stroke_width=1, fill='none')
        #dwg.add(pagebox)
        dwg.save()
