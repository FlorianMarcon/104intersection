from math import tan, radians
from display import *

def	cone_intersection(line, cone):
	angle = radians(cone.angle)
	angle = pow(tan(angle), 2)
	second = pow(line.vector.x, 2) + pow(line.vector.y, 2)
	second = second - (pow(line.vector.z, 2) * angle)
	first = (line.point.x * line.vector.x) + (line.point.y * line.vector.y)
	first = (first * 2) - (2 * line.point.z * line.vector.z * angle)
	zero = pow(line.point.x, 2) + pow(line.point.y, 2)
	zero = zero - (pow(line.point.z, 2) * angle)
	delta = pow(first, 2) - 4 * second * zero
	if delta == 0:
		display_one_solution(second, first, zero, line)
	elif delta > 0:
		display_two_solution(second, first, zero, line)
	else:
		print ("No intersection point.")
