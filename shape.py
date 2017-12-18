class	Point:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

class	Vector:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

class	Line:
	def __init__ (self, point, vector):
		self.point = point
		self.vector = vector

class	Circle:
	def __init__(self, point, rayon):
		self.point = point
		self.rayon = rayon

class	Cylindre:
	def __init__(self, point, rayon):
		self.point = point
		self.rayon = rayon

class	Cone:
	def __init__(self, point, angle):
		self.point = point
		self.angle = angle
