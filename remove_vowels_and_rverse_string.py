len=int(input())
string=raw_input()
for i in 'aeiou':
    string=string.replace(i,"")
print string[::-1]
