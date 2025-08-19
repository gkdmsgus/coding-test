str = list(input())

a =[]
for i in str:
    if i.isupper():
        a.append(i.lower())
    elif i.islower():
        a.append(i.upper())

a =''.join(a)

print(a)
