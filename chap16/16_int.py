class Time(object):
	print """int to time"""
time=Time()
time.hour=11
time.minute=59
time.second=30
seconds=60
minutes=30
def int_to_time(seconds):
	time=Time()
	minutes,time.second=divmod(seconds,60)
	time.hour,time.minute=divmod(minutes,60)
	return '%.2d:%.2d:%.2d'% (time.hour,time.minute,time.second)


print int_to_time(seconds)
