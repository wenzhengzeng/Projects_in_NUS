"""
n=input()
n1=int(input())
n2=int(input())
n3=len(n)
s1=n[0:n1]
s2=n[n3-n2:n3]
print(s1+s2)"""
"""s=input()
a=int(input())
a1=len(s)
if(a==a1):
    print('False\nTrue\nTrue\nFalse')
elif(a>a1):
    print('True\nTrue\nFalse\nTrue')
else:
    print('False\nFalse\nFalse\nTrue')"""
"""n1=input()
m1=input()
n=int(n1)
m=int(m1)
n2=float(n1)
m2=float(m1)
print(n+m)
print('\n')
print(n-m)
print('\n')
print(n*m)
print('\n')
print(int(n/m))
print('\n')
print(n2/m2)
print('\n')
print(n**m)
print('\n')
print(n%m)"""
"""n=input()
#print(n[1])
i=0
j=len(n)
while n[i]!=' ':
    i+=1
while n[j-1]!=' ':
    j-=1
print(n[i:j])"""
n=input()
i=0
j=len(n)
j1=j
while n[i]!=' ':
    i+=1
while n[j-1]!=' ':
    j-=1
a1=int(n[0:i])
a2=int(n[i+1:j-1])
a3=int(n[j:j1-1])
if a1<60:
    print('False')
elif ((a2>=60) or (a3>=60)):
    print('Tru                 e')
else:
    print('False')
    