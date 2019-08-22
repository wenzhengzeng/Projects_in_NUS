a=input().split()
b=[]
for i in range(0,int(a[0])):
    b.append(input().split())
sum=0
for i in range(0,int(a[0])):
    for j in range(0,int(a[1])-1):
        if b[i][j]==b[i][j+1]:
            sum+=1
for i in range(0,int(a[1])):
    for j in range(0,int(a[0])-1):
        if b[j][i]==b[j+1][i]:
            sum+=1
print(sum)
        
    
