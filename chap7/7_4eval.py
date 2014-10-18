n='1+2*3'
def eval_loop():
	while true:
		if n=="done":
			break
		else:	
			r=eval(n)
			print r
	print r

eval_loop()
