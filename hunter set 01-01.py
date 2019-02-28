n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
	if(l.count(l[i])!=1):
		l1.append(l[i])
s=set(l1)
print (*s,)
