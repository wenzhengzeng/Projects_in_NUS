n=input().split()
b=[]
for i in range(0,int(n[0])):
    x=list(map(int,input().split()))
    b.append(x[0]**2+x[1]**2)
sum=0
b=sorted(b)
k=int(n[1])-1
if b[k]>int(b[k]):
    print(int(b[k])+1)
else:
    print(int(b[k]))

