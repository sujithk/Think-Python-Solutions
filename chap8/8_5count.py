def count(word,target):
	count=0
	for letter in word:
		if letter==target:
			count=count+1
	print count


count('sujitht','t')
