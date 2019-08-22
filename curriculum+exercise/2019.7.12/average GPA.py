n=int(input())
i=0
j=0
a=[]
b=[]
m=0
sum=0
while i<n:
    a.append(input())
    c=a[i].split()
    if c[1]=='1':
        b.append(a[i])
        sum+=float(c[2])
        m+=1
    i+=1
if m:
    i=0
    while i<m:
        print(str(b[i]))
        i+=1
    print(sum/m)
else:
    print(float(0))



    
