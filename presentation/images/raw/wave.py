import svgwrite

def wave(size, finger_count, finger_width, thickness):
    center = map(lambda pos: pos / 2.0, size)
    pen_x = center[0] - ((finger_count + 1) / 2.0 * finger_width)
    pen_y = center[1]
    y_map = [thickness, 0, -thickness, 0]
    x_map = [0, finger_width]
    for idx in range(finger_count * 2 + 2):
        pen_x += x_map[idx % 2]
        pen_y += y_map[idx % 4]
        yield (pen_x, pen_y)

size = (800, 200)
path = [pt for pt in wave(size, finger_count=12, finger_width=50, thickness=20)]
path = ("M %s,%s" % path[0]) + str.join(' ', ["L %s,%s" % pt for pt in path[1:]])
dwg = svgwrite.Drawing("images/wave.svg", size=size)
dwg.add(dwg.path(d=path, fill="none", stroke="red", stroke_width=10))
dwg.save()
