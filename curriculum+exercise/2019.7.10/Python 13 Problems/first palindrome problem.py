def rev(a_string):
    l = list(a_string) 
    new_string = ""
    while len(l)>0:
        new_string += l.pop() 
    return new_string
a=input()
b=rev(a)
if a==b:
    print('Yes')
else:
    print('No')
