# TODO
def prime(n):
        m=2
        while n>m:
            if n%m==0:
                return(False)
                break
            m+=1
        if n==m:
            return(True)
        if n==1:
            return(False)
try:
    n=int(input('n:'))
    if n<=0:
        print('自然数を入力してください')
    if n>0:
        print(prime(n))
except(ValueError):
    print('自然数を入力してください')

