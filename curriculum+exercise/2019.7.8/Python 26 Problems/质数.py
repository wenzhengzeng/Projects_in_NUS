n=int(input())
sum=0
j=0
for i in range(2,n+1):
    for j in range(2,i+1): #注意：range(x,y)指从x到y-1
        if(i%j==0):
            break
    if(j==i):
        sum+=1
print(sum)
'''i=2
while i<n+1 :
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
    if j==i:
        sum+=1
    i+=1
print(sum)'''
        
            
