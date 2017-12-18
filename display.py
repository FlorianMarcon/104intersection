from determinate_solution import *
import sys
from math import sqrt

def	display_line():
	print ("straight line going through the (", end ="")
	print (sys.argv[2], end = "")
	print (",", end= "")
	print (sys.argv[3], end = "")
	print (",", end= "")
	print (sys.argv[4], end="")
	print (") point and of direction vector (", end= "")
	print (sys.argv[5], end = "")
	print (",", end= "")
	print (sys.argv[6], end = "")
	print (",", end="")
	print (sys.argv[7], end = "")
	print (")")

def	display_one_solution(second, first, zero, line):
	sol_equa = -first / (2 * second)
	point = determinate_solution(sol_equa, line)
	print ("1 intersection point :")
	print ("(", end = '')
	print ("%.3f" % point.x, end = '')
	print (", ", end="")
	print ("%.3f" % point.y, end = '')
	print (", ", end="")
	print ("%.3f" % point.z, end = '')
	print (")")

def	display_two_solution(second, first, zero, line):
	delta = pow(first, 2) - 4 * second * zero
	sol_equa = (-first + sqrt(delta)) / (2 * second)
	point = determinate_solution(sol_equa, line)
	print ("2 intersection points :")
	print ("(", end = '')
	print ("%.3f" % point.x, end = '')
	print (", ", end="")
	print ("%.3f" % point.y, end = '')
	print (", ", end="")
	print ("%.3f" % point.z, end = '')
	print (")")
	sol_equa = (-first - sqrt(delta)) / (2 * second)
	point = determinate_solution(sol_equa, line)
	print ("(", end = '')
	print ("%.3f" % point.x, end = '')
	print (", ", end="")
	print ("%.3f" % point.y, end = '')
	print (", ", end="")
	print ("%.3f" % point.z, end = '')
	print (")")
