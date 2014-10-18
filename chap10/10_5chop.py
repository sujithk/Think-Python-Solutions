def chop(a):
	for v in a:
		del a[0]
		del a[-1]
		return a


print chop([1,2,3,4])
