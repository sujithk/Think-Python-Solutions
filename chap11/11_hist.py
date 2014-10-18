def histogram(s):
	for c in s:
		d[c]=1+d.get(c,0)
	return d


def print_hist(h):
	for c in h:
		print c,h[c]



print_hist('parrot')
