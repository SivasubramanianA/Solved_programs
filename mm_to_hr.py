m=int(input())
if m>60:
    h=m/60
    m1=m%60
    print h,m1
elif m<60:
    print "0",m
