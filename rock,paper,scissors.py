a,b=raw_input().split()
if((a=="R" and b=="P") or (a=="P" and b=="R")):
    print "P"
elif((a=="S" and b=="P") or (a=="P" and b=="S")):
    print "S"
elif((a=="S" and b=="R") or (a=="R" and b=="S")):
    print "R"
elif a==b:
    print "D"
