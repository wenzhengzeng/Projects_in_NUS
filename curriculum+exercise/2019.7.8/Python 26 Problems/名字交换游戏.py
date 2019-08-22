a=input()
b=input()
c=input()
d=input()
d1=int(d[0])
d2=int(d[2])
d3=int(d[4])
if d1:
    k=a
    a=b
    b=k
if d2:
    k=b
    b=c
    c=k
if d3:
    k=c
    c=a
    a=k
print(a)
print('\n')
print(b)
print('\n')
print(c)

