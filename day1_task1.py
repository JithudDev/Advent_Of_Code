﻿
l=[]
while True:
	try:
		k=int(input())
		l.append(k)
	except:
		break
	
c=0

for i in range(1,len(l)):
	if l[i]>l[i-1]:
		c+=1
print(c)
	
