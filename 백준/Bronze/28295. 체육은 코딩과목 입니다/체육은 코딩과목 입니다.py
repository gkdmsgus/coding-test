r = 3600
for i in range(10):
    a = int(input())
    if a==1:
        r +=90
    elif a==2:
        r += 180
    elif a==3:
        r -= 90
r2 = r % 360 
if r2 == 90:
    print("E")
elif r2 == 180:
    print("S")
elif r2 == 270:
    print("W")
else:
    print("N")