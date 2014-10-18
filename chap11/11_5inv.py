def histogram(s):
	d=dict()
	for c in s:
		d[c]=1+d.get(c,0)
	return d
def invert_dict(v):
	inv=dict()
	for key in v:
		val=v[key]
		inv.setdefault(val,[])
		inv[val].append(key)
	return inv

hist=histogram('parrot')
inv=invert_dict(hist)
print inv
