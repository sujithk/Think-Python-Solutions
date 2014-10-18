def do_four(f):
	f()
	f()	
	f()
	f()
def print_spam():
	print 'spam'

do_four(print_spam)
