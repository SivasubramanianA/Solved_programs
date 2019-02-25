n=int(input())
rem=0
op=0
while(n>0):
    rem=n%10
    op+=rem*rem
    n/=10
print op
