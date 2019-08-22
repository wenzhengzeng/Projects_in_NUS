a=int(input())
b=int(input())
c=int(input())
d=a
e=b
if c==0:
    print('1')
    print('0')
else:
    while c>1:
        x=d
        d=(a*d)-(b*e)
        e=(a*e)+(b*x)
        c-=1
    print(d)
    print(e)
    
