
a1=input()
a=a1.split()
result=(int(a[0]))&(2**int(a[1]))
if result:
    print('True')
else:
    print('False')

