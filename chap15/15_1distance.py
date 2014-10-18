import math
class point():
	print """distance b/w points."""
p=point()
q=point()
p.x=2
q.x=4
p.y=1
q.y=3
def distance_between_points():
	c=p.x-q.x
	d=p.y-q.y
	distance=math.sqrt(c**2+d**2)
	return distance

print distance_between_points()
