a=input().split()
b=input().split()
k=int(a[1])
i=0
c=[]
d=[]
while i<k:
    c.append(input().split())    
    i+=1
def go(x,n,n1):
    k=n
    sum=-1
    while k!='0':
        k=x[k]
        sum+=1
    print(sum)
def change(x,a):
    x[a[0]]=a[1]
    return x
i=0
s={}
k1=int(a[0])
while i<k1:
    s.update({str(i+1):b[i]})
    i+=1
i=0
while i<k:
    s=change(s,c[i])
    go(s,c[i][0],a[1])
    i+=1
