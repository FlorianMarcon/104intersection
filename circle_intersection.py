from shape import *
from display import *

def	circle_intersection(line, circle):
	second = pow((line.vector.x), 2) + pow((line.vector.y), 2)
	second = second + pow((line.vector.z), 2)
	first = (line.vector.x * line.point.x) + (line.vector.y * line.point.y)
	first = first + (line.vector.z * line.point.z)
	first = first * 2
	zero = pow(line.point.x, 2) + pow(line.point.y, 2) + pow(line.point.z, 2)
	zero = zero - pow(circle.rayon, 2)
	delta = pow(first, 2) - 4 * second * zero
	if delta == 0:
		display_one_solution(second, first, zero, line)
	elif delta > 0:
		display_two_solution(second, first, zero, line)
	else:
		print ("No intersection point.")
