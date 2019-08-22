a=int(input())
b=int(input())
c=int(input())
def sq(x):
    i=1
    while i<=x**0.5:
        if i**2==x:
            break
        i+=1
    if i>x**0.5:
        print('False')
    else:
        print('True')
sq(a)
sq(b)
sq(c)

