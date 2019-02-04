string=raw_input()
string1=string
for i in 'aeiou':
    string=string.replace(i,"")
for i in 'bcdfghjklmnpqrstvwxyz':
    string1=string1.replace(i,"")
print string1+string
