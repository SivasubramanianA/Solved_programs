a,b=raw_input().split()
c,d=raw_input().split()
e,f=raw_input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
if a==c==e or b==d==f or a==b or c==d or e==f:
    print "yes"    
else:
    print "no"
