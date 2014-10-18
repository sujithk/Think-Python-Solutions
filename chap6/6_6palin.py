def first(a):
	return a[0]
def last(a):
	return a[-1]
def middle(a):
	return a[1:-1]
def is_palin(a):
	if first(a)==last(a):
		return "is palindrome"
	else:
		return "false"

print is_palin("suji")
