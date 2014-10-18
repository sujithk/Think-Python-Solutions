class Rectangle(object):
	print """Represents a rectangle. 

    attributes: width, height, corner.
    """

class point(object):
p = Point()
def find_center(rect):
	print """Returns a Point at the center of a Rectangle."""
	p.x = rect.corner.x + rect.width/2.0
	p.y = rect.corner.y + rect.height/2.0
	return p


def grow_rectangle(rect, dwidth, dheight):
	rect.width += dwidth
	rect.height += dheight

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

center = find_center(box)
	print_point(center)

	print box.width
	print box.height
	print 'grow'
grow_rectangle(box, 50, 100)
	print box.width
	print box.height

def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print 'blank'
    print_point(blank)


main()
