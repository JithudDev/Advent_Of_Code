
x=y=0
t=0
while True:
	try:
		a,k=input().split()
		k=int(k)
		if a=='forward':
			x+=k
			y+=t*k
		elif a=='down':
			t+=k
		elif a=='up':
			t-=k
		#print(x,y)
	except:
		break
print(x*y)
	
