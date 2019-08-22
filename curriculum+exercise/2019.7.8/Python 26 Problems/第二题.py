a1=input()
a=a1.split()
i=0
l=len(a1)
result=int(a[0])
d=''
while result>1:
    b=result%2
    result=int(result/2)
    d=d+str(b)
d=d+str(1)
k=int(a[1])
if k==1:
    print(True)
else:
    print(False)

