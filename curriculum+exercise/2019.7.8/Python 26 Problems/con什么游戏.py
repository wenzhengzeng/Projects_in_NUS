a=input()
b=input()
c=input()
d=input()
k1=a+b+c
k2=a+c+b
k3=b+a+c
k4=b+c+a
k5=c+a+b
k6=c+b+a
if ((k1==d) or (k2==d) or (k3==d) or (k4==d) or (k5==d) or (k6==d)):
    print('No')
else:
    print('Yes')
