n=input()
n1=n.split()
a1=int(n1[0])
a2=int(n1[1])
a3=int(n1[2])
a4=int(n1[3])
a5=int(n1[4])
k1=0
k2=0
if((a1 and a2)>a5) or (a3+a4<=a5):
    k1=1
if((a3 or a4)<a1) and (a4*a5>=a1):
    k2=1
if((k1+k2)==0):
    print('True')
else:
    print('False')
    
