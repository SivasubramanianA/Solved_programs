n=int(input())
Sum=0
while(n>0):
    rem=n%10
    Sum=Sum+rem
    n/=10
print Sum
