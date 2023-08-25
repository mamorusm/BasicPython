n = int(input("nの値を入力: "))

# TODO
m=2
while n>m:
    if n%m==0:
        print("これは素数ではありません")
        break
    m+=1
if n==m:
    print("これは素数です")
if n==1:
     print('1は素数ではありません')