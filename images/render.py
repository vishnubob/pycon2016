#!/usr/bin/env python

from PIL import Image

def ratio(res, width=None, height=None):
    assert width or height
    ratio = float(res[0]) / float(res[1])
    if width:
        return (width, width * ratio)
    return map(int, (height * ratio, height))

def resize_and_crop(image, size, anchor="topleft"):
    (width, height) = map(float, image.size)
    (_width, _height) = map(float, size)
    new_width = (width * _height / height)
    new_height = (height * _width / width)
    if new_width > _width:
        _size = (int(round(new_width)), int(round(_height)))
    else:
        _size = (int(round(_width)), int(round(new_height)))
    if anchor == "topleft":
        crop = (0, 0, size[0], size[1])
    elif anchor == "topright":
        crop = (_size[0] - size[0], 0, _size[0], size[1])
    elif anchor == "bottomleft":
        crop = (0, _size[1] - size[1], size[0], _size[1])
    elif anchor == "center":
        x = int(round((_size[0] - size[0]) / 2.0))
        x = max(0, x)
        y = int(round((_size[1] - size[1]) / 2.0))
        y = max(0, y)
        crop = (x, y, x + size[0], y + size[1])
    return image.resize(_size, resample=Image.LANCZOS).crop(crop)

def composite(images, target_fn):
    target = Image.new("RGB", TargetSize, "white")
    for (imga, pos) in zip(images, sizes):
        (imgfn, anchor) = imga
        size = (pos[2] - pos[0], pos[3] - pos[1])
        img = Image.open(imgfn)
        img = resize_and_crop(img, size, anchor=anchor)
        target.paste(img, box=pos)
    target.save(target_fn)

MaxSize = (1024, 768)
TargetSize = ratio(MaxSize, height=700)

GinkgoImages = [
    ("ginkgo_3.jpg", "center"),
    ("ginkgo_2.png", "topleft"),
    ("ginkgo_4.jpg", "bottomleft"),
    ("ginkgo_1.jpg", "topleft"),
]

HobbyImages = [
    ("sonic_storyboard_board.jpg", "center"),
    ("bee_drink.jpg", "center"),
    ("camera_battery_removal.jpg", "center"),
    ("turkey.jpg", "center"),
]

GardenImages = [
    ("weather_station.jpg", "center"),
    ("garden.jpg", "center"),
    ("garden_controller.jpg", "center"),
    ("weather_base_station.jpg", "center"),
]

LaserCutterImages = [
    ("laser_cutting_4.jpg", "topleft"),
    ("laser_cutting_3.jpg", "center"),
    ("laser_cutting_2.jpg", "topright"),
    ("laser_cutting_1.jpg", "center"),
]

PhysicalImages = [
    ("physical_4.jpg", "center"),
    ("physical_3.jpg", "topright"),
    ("physical_1.jpg", "topleft"),
    ("physical_2.jpg", "center"),
]

MachineAgeImages = [
    ("machine_age_2.jpg", "topright"),
    ("machine_age_1.jpg", "topright"),
    ("machine_age_3.jpg", "topleft"),
    ("machine_age_4.jpg", "center"),
]

AtomicAgeImages = [
    ("atomic_age_1.png", "center"),
    ("atomic_age_3.jpg", "center"),
    ("atomic_age_4.jpg", "topleft"),
    ("atomic_age_2.jpg", "center"),
]

CNCImages = [
    ("cnc_3.jpg", "center"),
    ("cnc_4.jpg", "center"),
    ("cnc_1.jpg", "center"),
    ("cnc_2.jpg", "center"),
]


(width, height) = TargetSize
ratio = 1.0 / ((1 + 5 ** .5) / 2.0)
_23_width = int(round(ratio * width))
_13_width = width - _23_width

_23_height = int(round(ratio * height))
_13_height = height - _23_height

sizes = [
    [0, 0, _13_width, _23_height], 
    [_13_width, 0, width, _23_height],
    [0, _23_height, _23_width, height],
    [_23_width, _23_height, width, height],
]

composite(GinkgoImages, "images/ginkgo.png")
composite(HobbyImages, "images/hobbies.png")
composite(GardenImages, "images/garden.png")
composite(LaserCutterImages, "images/laser.png")
composite(PhysicalImages, "images/physical.png")
composite(MachineAgeImages, "images/machine_age.png")
composite(AtomicAgeImages, "images/atomic_age.png")
composite(CNCImages, "images/cnc.png")

