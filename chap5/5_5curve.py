def draw(t, length, n):
	angle=50
	if n == 0:
		return fd(t, length*n)
		return	lt(t, angle)
		return	draw(t, length, n-1)
		return	rt(t, 2*angle)
		return	draw(t, length, n-1)
		return	lt(t, angle)
		return	bk(t, length*n)


print draw(10,15,5)
