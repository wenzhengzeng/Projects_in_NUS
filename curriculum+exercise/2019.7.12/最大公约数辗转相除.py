n=input().split()
a=int(n[0])
b=int(n[1])
x = a % b 
while (x != 0):
    a = b
    b = x
    x = a % b
print(b)    


