class rectangle():
	print """centre of the rectangle."""
class point():
	print "points"
box=rectangle()
box.width=100.0
box.height=200.0
box.corner=point()
box.corner.x=0.0
box.corner.y=0.0
p=point()
p.x=box.corner.x+box.width/2.0
p.y=box.corner.y+box.height/2.0
def find_center():
	return (p.x,p.y)

print find_center()
