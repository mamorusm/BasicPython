#問3.ユークリッドの互除法
a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))
def euc(a,b):
    if a<b:
        y=b%a
        while y!=0 and a!=0:
            if a<y:
                y=y%a
            else:
                a=a%y
        if a<y:
            return(y)
        else:
            return(a)
    else:
        y=a%b
        while y!=0 and b!=0:
            if b<y:
                y=y%b
            else:
                b=b%y
        if b<y:
            return(y)
        else:
            return(b) 
print(euc(a,b))


#問4.互いに素

def each(x):
    if euc(a,b)==1:
        return(True)
    else:
        return(False)
print(each(0)
)

#エクストラ問題
import random
from random import randint, randrange, random, uniform

sum=0
for i in range(1,100001):        
    a = randint(1,10000) 
    b = randint(1,10000)
    result=euc(a,b)
    if result==1:
        sum +=1
print(sum/100000)




