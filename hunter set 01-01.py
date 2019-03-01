n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(0,n):
	if(l.count(l[i])!=1):
		l1.append(l[i])
s=set(l1)
if len(l1)==0:
	print ("unique")
else:
    print(*s,)
