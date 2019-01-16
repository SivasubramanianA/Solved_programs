n=int(input())
j=0
if n>1:
    for i in range(2,n):
        if n%i==0:
            j=j+1
if j<=0:
    print "yes"
else:
    print "no"
