
def histogram(s):
	d=dict()
	for c in s:
		d[c]=1+d.get(c,0)
		return d

def print_hist(h):
	h=dict()
	g = h.keys()
	g.sort()
	for c in g:
		return c ,h[f]



h=histogram('parrot')
print print_hist(h)

