from shape import *

def determinate_solution(sol_equa, line):
	x = line.vector.x * sol_equa + line.point.x
	y = line.vector.y * sol_equa + line.point.y
	z = line.vector.z * sol_equa + line.point.z
	solution = Point(x, y, z)
	return (solution)
