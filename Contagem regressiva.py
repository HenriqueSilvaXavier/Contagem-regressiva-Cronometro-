import time
t=int(input("Digite o tempo(em segundos): "))
seconds=t
minutes=00
while seconds>60:
	seconds=seconds-60
	minutes=minutes+1
while minutes>0 or seconds>0:
	timer="{:02d}:{:02d}".format(minutes, seconds)
	print(timer, end="\r")
	time.sleep(1)
	if seconds>0:
		seconds=seconds-1
	elif seconds==0:
		seconds=59
		minutes=minutes-1
print("{:02d}:{:02d}".format(minutes, seconds))