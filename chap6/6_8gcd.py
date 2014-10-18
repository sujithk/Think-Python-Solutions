def gcd(a,b):
	if a==0:
		return b
	elif b==0:
		return a
	else:
		return (b,a%b)


print gcd(0,5)
