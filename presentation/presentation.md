## Laser Cutters
## 3D Printers 
## and Python
&nbsp; <p />
May, 2016 - Giles Hall

# END #

# Giles Hall
## github.com/vishnubob
## <i>giles@polymerase.org</i>

Note:
My name is Giles Hall.  I've been using python since 1996, and at this point, I consider it my mother tongue.  I utilize python throughout my life.  

# END #
<section data-background-image="images/ginkgo.png" />

Note:
I work for a startup in Boston called "Ginkgo Bioworks" -- We apply techniques from synthetic biology and genetic engineering to build custom organisms for our customers.  We build thousands of custom of strains, and to do this at scale we rely heavily on python to help design, track and analyze our engineered samples.  If you are interested about Ginkgo and want to learn more, check us out gingobioworks.com.

# END #
<section data-background-image="images/hobbies.png" />

Note:
In my spare time, I explore my many hobbies; photography, gardening, cycling, cooking, electronics and making art.  For each one of my hobbies, I've written at least a handful of python scripts related to it.

# END #
<section data-background-image="images/garden.png" />

Note:
Here is a quick example.  In my backyard, I have a Davis weather station.  This transmit weather data wirelessly to a Raspberry Pi in my house.  Another Raspberry Pi in the basement monitors this data, and controls a set of relays that switch on spinklers for the garden.  Python is not just a programming language, it's one of the primary means I use to express myself creatively. 

# END #
<section data-background-image="images/not-art.jpg" />

Note: 
But, as powerful as python is, programming by its very nature is not a physical medium.  [beat] Frederic P. Brooks wrote one of my favorite quotes about computer programming in his book The Mythical Man-Month 

# END #
<blockquote>
&ldquo;The programmer, like the poet, works only slightly removed from pure thought-stuff. She builds her castles in the air, from air, creating by exertion of the imagination.&rdquo;
</blockquote>
&#45; Frederic P. Brooks, <i>The Mythical Man-Month</i>

Note:
"The programmer, like the poet, works only slightly removed from pure thought-stuff. She builds her castles in the air, from air, creating by exertion of the imagination."  [beat] The world is filled with these amazing but nebulous castles, but we can only really appreciate them with the aid of a computer.  You can't share your code like you would a painting or a sculpture or a well cooked meal.

# END #
# How do we make code physical and tangible?

Note:
I realize not everything I said is true, we use software to manipulate our physical world every day.
# END #

<section data-background-image="images/physical.png" />

Note:
Our computers produce sound, and light and churn out printed documents.  There are many ways you can write code to affect the physical world.  That's what I'm here to talk about, but first, some history.

# END #
<section data-background-image="images/machine_age.png" />

Note:
Before there were computers, people had to make things by hand.  The period between the late 19th century and the middle of the 20th century was collectively known as the "Machine Age".  During this time, we perfected the art of building parts at an industrial scale using a process called "subtractive manufacturing".  This includes technieques such as milling, turning, boring, broaching, sawing, reaming and tapping.  The general idea was to shape bulk stock into some kind of part by removing material with incredible precision.

# END #

<section data-background-image="images/atomic_age.png" />

Note:
After the 1950s, the world entered the atomic age and ushered in the digital computer.  During the 1940s and 50s, existing tools like mills and lathes were connected to electric motors that were controlled with punched tape.  This was the first step towards automation of machine tools, and as computers evolved in sophistication, it spawned a new field of fabrication called Computer Numerical Control, known as CNC.

# END #

<section data-background-image="images/cnc.png" />

Note:
Today, computer controlled automation is ubiquitous throughout all areas of manufacturing.  Not only has the computer hardware and software programming evolved in sophistication, but there are new manfacturing tools and processes that have only existed in the last few decades.  This includes plasma cutters, water jets, 5-axis milling machines, lithography... and two of my favorite technologies.

# END #

<image height="400px" src="images/zing.jpg" /> <image height="400px" src="images/thingomatic.jpg" />

Note:
laser cutters and 3D printers.  Let's examine each of these technologies individually, and discuss how we can use Python to create designs for these tools.  First, laser cutters!

# END #

# Laser Cutters

<image height="500px" src="images/zing.jpg" /> 

Note:
Laser-cutters are devices that utilize high-powered lasers to etch or cut a variety of different materials. 
Most commercially available laser cutters are capable of cutting and etching paper, wood, plastic, leather, and fabric up to a certain thickness.  
The laser tube is static to the device, typically mounted towards the back. 
Carefully positioned mirrors bounce the laser light to the laser head.  
The head is composed of mirrors and lenses that focus the laser beam onto the target material.  
Stepper motors move the head in the X/Y plane parallel to the work material, tracing out the contours for a given design.  
Laser cutters are incredibly precise, and are capable of producing complex designs with intricate detail.

# END #
<image height="600px" style="background: white;" src="images/raster_vs_vector.png" />

Note:
Digital designs for laser cutting typically start as vector graphics.  Design programs like Adobe Illustrator and Inkscape are vector illustration packages.  This is in contrast to programs like the GIMP and Photoshop, which are raster, or bitmap, oriented graphic packages.  Vector graphics make it easy for the software controlling the motion of the laser cutter to translate the graphics into motion.

# END #

# Laser Cutting Process

1. Select material (wood, plastic, etc)
2. Size your material
3. Build your design
    1. Mark your cut lines
    2. Mark your etch lines
4. Lay out your material on laser cutter bed
5. Upload your design and begin cut

Note:
The process of creating laser-cut designs is relatively straight forward.  After thinking about what your design should look like, you need to pick your material and its size.  If you are cutting, thinner is usually better than thicker.  Your design should be sized according to your size constraints, although vector graphics makes it easy to scale your design without losing detail.  Most laser control software requires that you indicate which parts of your design are meant to be cut, versus which should be etched.  This can be achieved with the color of the line, for example (red for cut, blue for etch).  When you are ready to execute your cut, you position your material on the laser bed, focus the laser beam, and uplaod your design file.  Every laser cutter provides its own driver, so the specifics will be dictated by the company who made the cutter.

# END #

<svg xmlns="http://www.w3.org/2000/svg" version="1.1"
      width="700" height="250" viewBox="0 0 700 250">
  <rect x="350" y="23" width="200" height="200" fill="darkred"
      stroke="white" stroke-width="10" />
  <circle cx="300" cy="100" r="80" fill="cyan"
      stroke="darkgrey" stroke-width="5" />
</svg>

```xml
<svg xmlns="http://www.w3.org/2000/svg" version="1.1"
      width="120" height="120" viewBox="0 0 236 120">
  <rect x="14" y="23" width="200" height="7" fill="red"
      stroke="black" stroke-width="1" />
  <circle cx="24" cy="33" r="25" fill="green"
      stroke="blue" stroke-width="2" />
</svg>
```

Note:
This is a simple example of an SVG document.  SVG files are XML documents, and a closely related cousin to HTML.  HTML and SVG share a lot of the attribute names for various tags, like width, height, style, and border.  They share style syntax as well, and later revisions of SVG support cascading style sheets. 

# END #
<svg xmlns="http://www.w3.org/2000/svg" version="1.1"
      width="600" height="240" viewBox="0 0 600 240">
    <path d="M 20,20 L 400,20 L 320,60 L 10,150 L 600,100, L 100,220"
        fill="none" stroke="white" stroke-width="10" />
</svg>

```xml
<svg xmlns="http://www.w3.org/2000/svg" version="1.1"
      width="600" height="240" viewBox="0 0 600 240">
    <path d="M 20,20 L 400,20 L 320,60 L 10,150 L 600,100, L 100,220"
        fill="none" stroke="white" stroke-width="10" />
</svg>
```

Note:
My favorite feature of SVG are paths.  A path is simply a list of connected line segments that are used to build complex ploygons.  Segments can be straight or curved with control points.  The path is defined by a string of characters.  It breaks up up into single letter commands like 'M' for "move" or "L" for line and then two or more numbers that represent coordinates.  You can do a lot with just circles and squares, but paths allow us to build incredibly complex shapes.  In this example, I just rattled off a few random points to make this squiggly line.

# END #
<section data-background-image="images/box_plain.jpg" />

Note:
For this talk, I wrote a python program to generate a laser cuttable cube that uses finger joints.  Even though this design is 2D, when put together like a puzzle, it produces a 3D shape.  The program is a few hundred lines, so we won't be able to discuss it in its entirety, but we will examine the geometry of the cube, and how to translate this into code.  This entire program is available at my GitHub repository for this talk. 

# END #

<section data-background-image="images/example_box.svg" />

Note:
This is what one of the generated designs looks like, and is sent verbatim to the laser cutting control software.

# END #

<section data-background-image="images/box_cutboard.png" />

Note:
And this is what the board looks like after it is cut by the laser cutter.  You can see a few scortch marks caused by small flame ups as the material briefly ignites from the laser.  As a bonus, the board has a refreshing burnt wood smell.

# END #
<section data-background-image="images/example_box_polarity.svg" />

Note:
Since the cube fits together like a puzzle, the edges of each face must interlock.  I think of these edges as being either positive or negative, and I've color coded them in to distinguish this feature.

# END #
<section data-background-image="images/teeth_schematic.svg" />

Note:
This shows a single edge, and the parameters we must consider when building code to generate it.  The width of the material dicates the height of each individual finger, and the length of the edge combined with the number of fingers dictates the width of each individual finger.  From these few configurable parameters, we can write a function that will draw a single edge.

# END #
```python
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
```

Note:
This function takes the size of a cube face as a tuple, the number of fingers in an edge, the width of a single finger and the thickness of the material and calculates various geometrical offsets.  First, we use the size of the face to find its center.  Along with the number of fingers and the finger width, we use the center position to calculate where our first point should occur.

We then build two lists of positional offsets, one for the finger width and the other for the finger depth.  We then iterate though each point, calculating the offsets for each.  The code exploits the fact that every other point moves forward through the edge, and every 2nd point raises the edge, while every 4th point lowers it.  We use the modulous operator to replay these offsets as we build the edge profile.

# END #
```python
size = (800, 200)
wavepts = list(wave(size, finger_count=12, finger_width=50, thickness=20))
path = ("M %s,%s" % path[0]) + 
        str.join(' ', ["L %s,%s" % pt for pt in path[1:]])
dwg = svgwrite.Drawing("images/wave.svg", size=size)
dwg.add(dwg.path(d=path, fill="none", stroke="red", stroke_width=10))
dwg.save()
```

Note:
Here is an example of how we would call the previous function.  Since the previous function was a generator that returns a list of positions, the caller takes these points and translates them into a string that is formatted as an SVG path.  Note that the first command is a Move command, followed by Line commands.

# END #

<img width="1000px" src="images/wave.svg" />

Note:
And this is the result of wave generator.  This is only a small piece of the overall box generator, but it's central to the overall design.  The code is object oriented and relatively easy to follow.  You can configure and customize it in many different ways, such as the size of the box, the thickness of material, and the designs on the box faces.  For example...

# END #
<section data-background-image="images/box_sunflower.jpg" />

Note:
Since the box generator has a base class that defines the geometric rules for each face, you can inherit from this class and hook into its rendering method.  In this example, I added a Fermat Spiral.  This simple mathematical function generates a pattern that is reminiscent of the pattern of seeds you find on a sunflower.

# END #

# Fermat's Spiral

``` python
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
```

Note:
It's an extremely simple design to express in code, and once again, you can change the parameters that make up the design.  This is how I like to work, to start simple with the definition and then add new complexities and customizations that build onto the framework of the initial design.

# END #

<image height="600" src="images/sunflower.svg" />

Note:
And SVG makes it really easy to layer in new elements to add to the design without requiring you to change its overall structure.  Coupled with python, it's the perfect technolgoy to express your laser cuttable designs.

# END #

# 3D Printers

<image height="600" src="images/thingomatic.jpg" />

Note:
3D printers are devices that can build 3D objects.  They range in price and sophistication, but the most common 3D printers available are known as a "Fused deposition modeling" systems.  3D printers work by breaking down 3D objects into 2D slices, that when stacked one on top of the other, will reconstruct the geomtery of the 3D object.  FDM printers work by extruding plastics at high temperatures.  Unlike laser cutters, 3D printers work in three axises.  The X and Y axis are utilized by the print head to deposit the material in the desired shape, and the Z-axis is used to advanace the model to the next 2D slice.

# END #

# 3D Printing Process

1. Design your objects
2. Generated an STL file
3. Slice your STL file
    1. Select layer size
    2. Select infill
4. Print GCODE on printer

Note:
This is the highlevel design pipeline for 3D printers.  Most 3D printing software consumes STL files and produce GCODE files.  STL files are not easy to generate by hand, since they represent your 3D object in triangle mesh form.  Personally, I don't think about my 3D objects I wish to design as a mesh of triangles, I think of them as solid objects.

# END #

<section data-background-image="images/cad.png" />

Note:
About five years ago, my girlfriend and I purchased our first 3D printer.  We were so excited when we got it, thinking of all the things we would design and print on it.  I was immediately frustrated with the standard tools people typically use to design CAD models for printing.  I would spend hours in programs like sketchup, building up a complex design only to realize I needed to change something core to the model.  Most of the design tools do not make it easy to make these kind of drastic changes.  It's like painting a family portrait only to realize you left our your brother.

There are more sophisticated 3D modelers out there, including some that allow for parametric designs, but most are expensive, or only run on Windows, or are difficult to learn.  I looked around to try to find a programmatic solution, and that's how I discovered OpenSCAD.

# END #

<image height="700px" src="images/openscad.png" />

Note:
OpenSCAD is utilizes "Constructive Solid Geometry".  The idea is to build your objects from 2D and 3D primitives, such as cubes, cylinders and spheres.  You position these solid objects in space, and then define boolean operations between them.  The two most common boolean operations are Union, to join two or more solids as one and Difference, to subtract one or more solids from another.

# END #
<image height="700px" src="images/drinking_glass.jpg" />

Note:
For example, consider a drinking glass.  It can be constructed with two cylinders.  


# END #

<section data-background-image="images/openscad_1.png" />

Note:
The first cylinder describes the outside surface, and the second describes the empty volume inside.   Using OpenSCAD, we would define the first cylinder with a second cylinder inside.  The inside cylinder would be offset in the Z-axis (the up axis), and would have a smaller radius then the first.  We would then subtract the inner cylinder from the outer cylinder to create its empty envelope.  In order for this to work, we need to offset the inner cylinder's from the outer cylinder.


# END #

<section data-background-image="images/openscad_2.png" />

# END #

<section data-background-image="images/openscad_3.png" />

# END #

```python
difference()
{
    cylinder(r=20, h=80);
    translate([0, 0, 1])
    {
        cylinder(r=18, h=80);
    }
}
```

# END #

<image height="700px" src="images/flowerpot.jpg" />

Note:

Let's examine something a little more complicated, a flower pot.  Flower pots are similar to drinking glasses, but they also have a few distinct features.  First, most flower pots are wider at the top and smaller at the bottom.  Although we would think of that shape as a cone, it's still described as a cylinder in OpenSCAD with two different radius sizes for each end.  Second, they usually have some kind of hole at the bottom to allow the water to drain.  And finally, they often provide a lipped collar at the top to make them easy to hold on to and move around.

Now that we have a feel for OpenSCAD's syntax, let's talk about how we can generate these files from python.  There are a few different python libraries that allow you to build OpenSCAD syntax from python, including a library I've written called `python-scad`.  Most of these libraries work in similar ways, wrapping OpenSCAD definitions with python classes.  For my demo, I will be using my library, but you can accomplish the same thing with any of the other alternative libraries.

# END #

```python
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
```

Note:
Most of SCAD objects I write in Python start out like this, with a series of parametric variables that help define the physical constraints of the object.  I try to write a few top level variables that are designed to be flexible, and then compute other variable values based on these initial values.  In this example, many variables for the flowerpot are derived from the flowerpots height.  This makes it easy to change the overall size of the flowerpot without changing each individual variable.

# END #

```python
    def scad(self):
        outer_pot = Cylinder(r1=self.bottom_radius, r2=self.top_radius, 
                        h=self.height)
        collar = Cylinder(r=self.collar_radius, h=self.collar_height)
        collar = Translate(z=self.height - self.collar_height)(collar)
        outer_pot = Union()(collar, outer_pot)
        inner_pot = Cylinder(r1=self.bottom_radius - self.thickness, 
                r2=self.top_radius - self.thickness, 
                h=self.height - self.bottom_thickness)
        inner_pot = Translate(z=self.bottom_thickness)(inner_pot)
        standoff = Cylinder(r=self.bottom_radius - self.thickness, 
                        h=self.standoff)
        inner_pot = Union()(inner_pot, standoff)
        pot = Difference()(outer_pot, inner_pot)
        drain_hole = Cylinder(r=self.drain_hole, 
                        h=self.bottom_thickness)
        pot = Difference()(pot, drain_hole)
        pot = Render()(pot)
        return pot
```

Note:
The code that builds our flowerpot is pretty boring.  We start from the outside and add other cylinders to carve out the spaces we need.  It's built entirely with the cylinder primitive, along with Unions and Translations.  Really, the hard part is imagining your model and breaking it down into primitive solids.  Once you've done this, building the design in code is incredibly straight-forward.

# END #
<section data-background-video="video/flowerpot.mp4" />

Note:
This is my printer at home, building a 2.5" flower pot.  It took about two hours to print.  You will notice that the printer is printing an outer wall that's not part of the actual design.  This wall is generated by the printer software, and is what is known as support material.  The lip of the flower pot hangs out in space, and without this support material, the printer wouldn't be able to successfully print the overhang.

# END #

<section data-background-image="images/flowerpot_actual.jpg" />

Note:
And here is the finished result.

# END #

# Snowflake Generator

# END #

<section data-background-image="images/snowflake_actual.jpg" />

Note:
Now I would like to wet your appetite by talking about two of my projects, one for laser cutting and the other for 3D printing.  The first is a project my girlfriend and I started about four years ago.  We were trying to figure out what to make our friends and family for the holidays.

# END #

<section data-background-image="images/snowflake_paper.jpg" />

Note:
Rachael found this amazing paper that describes a physical model to simulate the growth of snowflakes.  We translated the math from the paper into python code, and proceeded to make personalized snowflakes for everyone on our gift list.

# END #

<section data-background-image="images/snowflake_hexgrid_empty.jpg" />

Note:
The model works at the "mesoscopic" level, which is to say it models a collection of molecules, specifically water molecules, of an undefined unit.  The model starts by constructing a hexagonal grid.

# END #
<section data-background-image="images/snowflake_hexgrid_seeded.jpg" />

Note:
This grid is then populated grid with a homogenuous field of water molecules.  These water molecules can then move from one neighboring cell to another, and can switch between three defined states "vapour", "boundary", or "frozen".  The boundary state is used to describe water that is neither vaporous or frozen, but caught between these two states.  The initial field of water molecules are set to a vapour state, except for the cell in the middle, which is initialized to the frozen state.  From there, the simulation runs and a snowflake begins to form.

# END #

<section data-background-image="images/snowflake_hexgrid_step1.jpg" />

Note:
As the simulation progresses, the snowflake crystal begins to grow from the initial central seed.  

# END #

<section data-background-image="images/snowflake_hexgrid_step2.jpg" />

# END #

<section data-background-image="images/snowflake_bitmap.jpg" />

Note:
The result of this simulation is a complex bitmap, but instead of capturing RGB intensities on a cartesian grid, the bitmap stores the density of frozen water molecules within a hexagonal grid.  When the snowflake reaches a certain pre-detemined size, the simulation stops and the program proceeds to translate the snowflake into SVG files.

# END #

<img height="200px" src="images/snowflake_outline.jpg" /> <img height="200px" src="images/snowflake_density.jpg" />
<p />
<img height="400px" src="images/snowflake_combined.jpg" />

Note:
Two SVG files are produced and merged.  The first SVG file is a representation of densest parts of the snowflake.  That is, where the water molecules were in the highest abudance when they froze.  The second SVG file defines the outline of the snowflake.  These two files are then merged into a single SVG file, and sent to the laser cutter.

# END #

<section data-background-video="video/snowflakes.mp4" data-background-video-loop data-background-video-muted>
</section>

Note:
The mathematical model is both complex and sophisticated.  It has 8 different parameters that help define the overall structure of the final snowflake.  We took this one step further, and allowed the parameters to change over the snowflakes growth, the anology being as a snowflake grows in weight, it begins to fall and thus its environment changes.  To personalize these snowflakes, we used the name of the intended receipient as the seed to these parameters.  What makes this algorithm so incredible is the range of snowflake species we were able to produce from it.

# END #

# ROCKIT

# END #

<section data-background-image="images/rockit_launch.png" />

Note:
The second project I want to talk to you about is something I called Rockit, spelled ROCKIT.  Rockit is a model rocket generator, written in python, and capaable of producing a wide variety of model rocket designs.  This was one of the first projects I worked on that coupled Python with OpenSCAD.  

# END #

<section data-background-image="images/model_rocket_motors.jpg" />

Note:
If you are not familar with model rocketry, you should know there are a range of engine sizes.  These engines are made of solid propellant packed into a cardboard tube.  The sizes vary in length and diameter, requiring different sized engine holders.  To start a design, you first select an engine size.  Rockit uses this parameter to calculate other sizes, like the diameter of the rocket body and the overall rocket size.

# END #

<img width="1024px" src="images/exploded_rocket.png" />

Note:
A second design feature of these rockets are a coupling sleeve used to hold the segments of the rocket together.  They work a litle like legoes, making it easy to print a rocket and snap it together without the need for glue (although a little super glue goes a long way in ensuring your rocket stays together during its flight).

# END #

<section data-background-image="images/rockit_two_stage.png" />

Note:
You can even print the base of the rocket with sleeves, which allows you to build multi-stage rockets.

# END #

<img width="300px" src="images/rockit_tail_normal.png"> <img width="300px" src="images/rockit_tail_eight.png"> <img width="300px" src="images/rockit_tail_twist.png">

Note:
Rockit makes it easy to change different aspects of your design.  For example, you can swap in different kinds of nose cones, or you can add/remove fins.  One of my favorite design tweaks is to give the fins a slight tilt which makes the rocket rifle up as soon as it is launched.  Since your designs are reproducible, you can easily tweak an existing design and measure its performance characteristics compared to a previous design.

# END #

<section data-background-video="video/rocket_launch.mp4" data-background-video-loop data-background-video-muted>
</section>

Note:
I would say the only down side is that these rockets are easily damaged.  The hot gases from the motor can sometimes warp and distort the plastic and hard landings typically result in catestrophic failure.  But, I say who cares, you can just go home and print more rockets.

# END #

# Tool Access
* Public library
* Maker spaces
* Ponoko / Shapeways

Note:
I realize not everyone has access to these tools, but no worries, they might be able available to you within a few miles of your house.  In Boston, there are a number of local maker spaces that provide access to 3D printers and laser cutters.  Some  public libraries have booted up their own maker areas that provide access to these tools.  If you can't find anything local, you can always use some of the popular internet based service providers, such as Ponoko or Shapeways.  All the laser cut designs I brought for this talk were cut at Ponoko.  This whole field is rapidly changing, and new tools are coming out every year.  As the tools advance, the total cost of ownership comes down in price.

# END #

# GitHub Links

* [https://github.com/vishnubob/pycon2016](https://github.com/vishnubob/pycon2016)
* [https://github.com/vishnubob/snowflake](https://github.com/vishnubob/snowflake)
* [https://github.com/vishnubob/rockit](https://github.com/vishnubob/rockit)
* [https://github.com/vishnubob/pyscad](https://github.com/vishnubob/pyscad)

Note:
And here are URLs to the projects I mentioned, including a repository for this talk.  If you have any questions, feel free to find me during the conference or send me an email.

# END #

# Thank You!
<img width="700px" src="images/box_python.jpg" />

Note:
Thanks PyCON!  Enjoy the rest of the conference.
