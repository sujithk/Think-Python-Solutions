def is_triangle(a,b,c):
	if (a>b+c or b>a+c or c>a+b):
		return "cannnot form atriangle"
	else:
		return "traingle"
def check_triangle():
	a=1
	b=3
	c=2
	return is_triangle(a,b,c)

print check_triangle()
