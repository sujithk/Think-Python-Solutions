def is_triangle(a,b,c):
	if (a>b+c or b>a+c or c>a+b):
		return "cannnot form atriangle"
	else:
		return "traingle"

print is_triangle(12,10,2)
