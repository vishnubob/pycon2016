#!/usr/bin/env python

from scad import *

class FlowerPot(SCAD_Object):
    radius_ratio = 0.6
    collar_height_radius = 0.2
    height = inch2mm(2.5)
    thickness = inch2mm(1/8.0)
    standoff = thickness / 2.0
    top_radius = height / 2.0
    bottom_radius = top_radius * radius_ratio
    drain_hole = bottom_radius * .2
    bottom_thickness = thickness + standoff
    collar_radius = top_radius + thickness
    collar_height = height * collar_height_radius

    def scad(self):
        outer_pot = Cylinder(r1=self.bottom_radius, r2=self.top_radius, h=self.height)
        collar = Cylinder(r=self.collar_radius, h=self.collar_height)
        collar = Translate(z=self.height - self.collar_height)(collar)
        outer_pot = Union()(collar, outer_pot)
        inner_pot = Cylinder(r1=self.bottom_radius - self.thickness, r2=self.top_radius - self.thickness, h=self.height - self.bottom_thickness)
        inner_pot = Translate(z=self.bottom_thickness)(inner_pot)
        standoff = Cylinder(r=self.bottom_radius - self.thickness, h=self.standoff)
        inner_pot = Union()(inner_pot, standoff)
        pot = Difference()(outer_pot, inner_pot)
        drain_hole = Cylinder(r=self.drain_hole, h=self.bottom_thickness)
        pot = Difference()(pot, drain_hole)
        pot = Render()(pot)
        return pot

pot = FlowerPot()
pot.render("flowerpot.scad")
stlfn = "flowerpot.stl"
if not os.path.exists(stlfn):
    pot = SCAD_Globals(fn=100)(pot)
    pot.render(stlfn)

