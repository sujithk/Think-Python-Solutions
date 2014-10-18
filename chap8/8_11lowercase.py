def any_lowercase(s):
	for c in s:
		if c.islower():
			return "true"
		else:
			return "false"

print any_lowercase("sujith")
