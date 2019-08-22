n=input()
n1=n.split()
a=int(input())
b=input()
c=[]
i=a
sum=0
while i<len(n1):
    c.append(n1[i])
    if(b==n1[i]):
        sum+=1
    i+=1
print(sum)

    
