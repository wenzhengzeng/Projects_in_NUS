# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:36:38 2019

@author: xujianyao
"""
def dic(list1,list2,n):
    lis2=[]
    for i in range(n):
        
        temp=[]
        temp.append(list2[i])
        lis2.append(temp)
    dicti={list1[0]:lis2[0]}
    for i in range(1,n):
        if dicti.get(list1[i],"wrong")=="wrong":
            dicti.update({list1[i]:lis2[i]})
        else:
            dicti[list1[i]].append(list2[i])
            dicti.update({list1[i]:dicti[list1[i]]})
    return dicti
def average(num):
    leng=len(num)
    sum=0
    for i in range(leng):
        sum=sum+num[i]
    ave=float(sum)/leng
    return ave
"""
list1=["aa","b","c"]
list2=[2,4,5]
dict=dic(list1,list2,3)
print(dict)
"""

lin1=input().split()
lin2=input().split()
lin3=input().split()


lin1_num=[]
lin3_num=[]
for i in range(2):
    lin1_num.append(int(lin1[i]))
for i in range(lin1_num[0]):
    lin3_num.append(int(lin3[i]))
    
lin=[]
for i in range(lin1_num[1]):
    lin.append(input().split())
for i in range(lin1_num[1]):
    temp=[]
    for j in range(2):
        temp.append(int(lin[i][j]))
    lin[i]=temp
k=lin1_num[1]
for i in range(k):
    sum=0
    ge=0
    list1=lin2[lin[i][0]-1:lin[i][1]]
    list2=lin3_num[lin[i][0]-1:lin[i][1]]
    leng=lin[i][1]-lin[i][0]+1
    diction=dic(list1,list2,leng)
    for j in diction:
        sum=sum+average(diction[j])
        ge=ge+1
    print("{:.10}".format(float(sum)/ge))
      
    
    
        
    
