n1=int(input())
def digui(n,a,b,c):
    if n==1:
        return a
    if n==2:
        return b
    if n==3:
        return c
    if n>3:
        return a*digui(n-1,a,b,c)+b*digui(n-2,a,b,c)+c*digui(n-3,a,b,c)
d=input()
d1=d.split()
a1=int(d1[0])
b1=int(d1[1])
c1=int(d1[2])
result=digui(n1,a1,b1,c1)
print(result)
