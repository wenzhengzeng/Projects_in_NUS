a=list(map(int,input().split()))
b=input().split()
d={}
x=0
for i in range(0,a[0]-1):
    d.update({str(i+2):int(b[i])})
t0=0
for i in range(1,a[2]):
    t0+=d[str(i+1)]
while a[4]>t0:
    t0+=a[1]
for i in range(a[2]+1,a[3]+1):
    x+=d[str(i)]
print(t0+x)

