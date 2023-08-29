# TODO
try:
    n=int(input('n:'))
    if n<=0:
         print('自然数を入力してください')
    if n>0:
        def prime(n):
                m=2
                while n>m:
                    if n%m==0:
                        return(1==2)
                        break
                    m+=1
                if n==m:
                    return(1==1)
                if n==1:
                    return(1==2)
        print(prime(n))
except(ValueError):
    print('自然数を入力してください')

