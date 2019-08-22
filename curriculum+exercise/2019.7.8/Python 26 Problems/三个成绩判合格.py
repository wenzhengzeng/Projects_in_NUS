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
a3=int(n[j:j1])
if a1<60:
    print('False')
elif ((a2>=60) or (a3>=60)):
    print('True')
else:
    print('False')
