def is_power(a,b):
	if a%b !=0:
		return "false"
	elif a%b==1:
		return "true"
	else:
		return "is power(a/b,b)"

print is_power(5,6)
