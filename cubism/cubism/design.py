from . point import Point
from . style import get_style

__all__ = ["Design"]

class Design(object):
    def __init__(self, width=None, height=None, thickness=None, teeth=None, style=None):
        self.width = width
        self.height = height
        self.size = Point(self.width, self.height)
        self.thickness = thickness
        self.teeth = teeth
        self.style = get_style(style)()
        
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

