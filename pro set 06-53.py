string=raw_input()
count=0
alphabet="abcdefghijklmnopqrstuvwxyz"
string=string.lower()
for i in alphabet:
    if(i not in string):
        count=0
    else:
        count+=1
if(count==26):
    print "yes"
else:
    print "no"
