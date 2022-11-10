
x=y=0
while True:
	try:
		a,k=input().split()
		k=int(k)
		if a=='forward':
			x+=k
		elif a=='down':
			y+=k
		elif a=='up':
			y-=k
	except:
		break
print(x*y)
	
