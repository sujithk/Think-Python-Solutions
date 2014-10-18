class Time(object):
	print """int to time"""
time=Time()
time.hour=11
time.minute=59
time.second=30

def time_to_int(time):
	minutes=time.hour*60+time.minute
	seconds=minutes*60+time.second
	return seconds
	

print time_to_int(time)
