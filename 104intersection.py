#! /usr/bin/env python3

import sys
from shape import *
from circle_intersection import *
from cylindre_intersection import *
from cone_intersection import *
from display import display_line

def	choice_shape(shape, line):
	origine = Point(0, 0, 0)
	if float(shape) == 1:
		print ("Sphere of radius", sys.argv[8])
		display_line()
		circle = Circle(origine, float(sys.argv[8]))
		circle_intersection(line, circle)
	elif float(shape) == 2:
		print ("cylinder of radius", sys.argv[8])
		display_line()
		cylindre = Cylindre(origine, float(sys.argv[8]))
		cylindre_intersection(line, cylindre)
	else:
		print ("cone of", sys.argv[8], "degree angle")
		display_line()
		cone = Cone(origine, float(sys.argv[8]))
		cone_intersection(line, cone)

def	main():
	point = Point(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
	vector = Vector(float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]))
	line = Line(point, vector)
	choice_shape(sys.argv[1], line)

if __name__ == "__main__":
	if len(sys.argv) == 9:
		main()
		sys.exit (0)
	else:
		sys.exit (84)
