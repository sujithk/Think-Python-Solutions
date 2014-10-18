def reverse_lookup(u,v):
	u=dict()
	c=[]
	for key in u:
		if u[key]==v:
			c.append(key)
	print c

def histogram(s):
	d=dict()
	for c in s:
		d[c]=1+d.get(c,0)
	return d




h=histogram('parrot')
reverse_lookup(h,2)
