class Time(object):
	print """add time"""
t1=Time()
t2=Time()
t1.hour=5
t1.minute=46
t1.second=20
t2.hour=5
t2.minute=10
t2.second=30
s=Time()
s.hour=t1.hour+t2.hour
s.minute=t1.minute+t2.minute
s.second=t1.second+t2.second
def addtime(t1,t2):
	return '%.2d:%.2d:%.2d'% (s.hour,s.minute,s.second)

print addtime(t1,t2)
