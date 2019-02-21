string=raw_input()
alphabet="abcdefghijklmnopqrstuvwxyz"
string=string.lower()
temp=""
for i in string:
    if(i in alphabet):
        temp+=i
for i in alphabet:
    if(i not in temp):
        count=0
    else:
        count=+1
if(count<=0):
    print "no"
else:
    print "yes"
