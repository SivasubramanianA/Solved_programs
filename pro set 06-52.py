a1,a2=map(int,raw_input().split())
b1,b2=map(int,raw_input().split())
c1,c2=map(int,raw_input().split())
d1,d2=map(int,raw_input().split())
if(a1==b1 and c1==d1 and a2==d2 and b2==c2):
    print "yes"
else:
    print "no"
