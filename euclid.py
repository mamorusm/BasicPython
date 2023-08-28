a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
if a<b:
    y=b%a
    while y!=0 and a!=0:
        if a<y:
            y=y%a
        else:
            a=a%y
    if a<y:
        print(y)
    else:
        print(a)
else:
    y=a%b
    while y!=0 and b!=0:
        if b<y:
            y=y%b
        else:
            b=b%y
    if b<y:
        print(y)
    else:
        print(b)
        