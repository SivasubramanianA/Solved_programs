n=int(input())
palin=0
temp=n
while n>0:
    rem=n%10
    palin=palin*10+rem
    n=n//10
if temp==palin:
    print "palindrome"
else:
    print "no"
