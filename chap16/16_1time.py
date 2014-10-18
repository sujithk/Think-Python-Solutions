class Time(object):
	print """Represent the time of day.
		attributes:hour,minute,second"""
time=Time()
time.hour=11
time.minute=59
time.second=30
def print_time():
	print "hour:minute:second"
	return '%.2d:%.2d:%.2d'% (time.hour,time.minute,time.second)


print print_time()
