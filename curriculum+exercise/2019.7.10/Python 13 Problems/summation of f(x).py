def zhishu(x):
    for i in range(2,x):
        if (x % i) == 0:
            return 0   
    return 1
def sq(x):
    i=1
    while i<=x**0.5:
        if i**2==x:
            break
        i+=1
    if i>x**0.5:
       return 0
    else:
       return 1
n=int(input())
sum=10
j=2
while j<=n:
    if(zhishu(j)):
        sum+=j**2
    elif(sq(j)):
        sum+=2*(j**0.5)+1
    else:
        sum+=int(j**0.5)
    j+=1
print(int(sum))
