n=int(input('enter the number of terms: '))
a=0
b=1
s=0
if n<0:
    print('not possible')
elif(n==1):
    print(1)
else:
    while(s<n):
        print(a)
        c=a+b
        a=b
        b=c
        s+=1
