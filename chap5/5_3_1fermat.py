def check_fermat(a,b,c,n):
	if n>2:
		if ((a**n+b**n)==c**n):
			return "fermat was wrong" 
		else:
			return "not work"

print check_fermat(4,2,1,3)
