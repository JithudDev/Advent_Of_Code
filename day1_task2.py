
l=[]
while True:
	try:
		k=int(input())
		l.append(k)
	except:
		break
	
c=l[0]+l[1]+l[2]
r=0
for i in range(3,len(l)):
	ns=c+l[i]-l[i-3]
	#print(c,ns)
	if(ns>c):
		r+=1
	c=ns
print(r)
	
