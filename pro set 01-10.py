n=int(input())
l=list(map(int,raw_input().split()))
f=0
if(n==0):
    print("0")
else:
    for i in range(1,n):
        for j in range(0,i):
            if (l[j]<l[i]):
                f=f+l[j]
print(f)
