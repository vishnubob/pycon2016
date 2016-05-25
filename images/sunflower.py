import math
import svgwrite

def sunflower(canvas, size, florets=200, floret_radius=5):
    center = map(lambda pos: pos / 2.0, size)
    constant = (min(center) - floret_radius * 2.0) / math.sqrt(florets)
    for idx in range(1, 1 + florets):
        radius = constant * math.sqrt(idx)
        angle = idx * math.radians(137.5)
        pt = (radius * math.cos(angle), radius * math.sin(angle))
        pt = map(sum, zip(center, pt))
        canvas.add(dwg.circle(pt, fill="lightgrey", r=floret_radius))

size = (700, 700)
dwg = svgwrite.Drawing("images/sunflower.svg", size=size)
sunflower(dwg, size, floret_radius=10)
dwg.save()
