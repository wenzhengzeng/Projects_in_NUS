n=int(input())
k=0
y=[]
for i in range(0,n):
    x=input().split()
    y.append(int(x[0])/int(x[1]))
    if k<float(y[i]):
        k=float(y[i])
print(k)
