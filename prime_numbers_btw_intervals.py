s,e=raw_input().split()
s=int(s)
e=int(e)
for k in range(s+1,e):
    j=0
    if k>1:
        for i in range(2,k):
            if k%i==0:
                j=j+1
    if j<=0:
       print k,
