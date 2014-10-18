def check_fermat(a,b,c,n):
	if n>2:
		if ((a**n+b**n)==c**n):
			return "fermat was wrong" 
		else:
			return "not work"

def fermat_input():
	a=4
	b=2
	c=1	
	n=3
	return check_fermat(a,b,c,n)

print fermat_input()
