import math
import random
import time
#得到距离矩阵的函数
def getdistmat(coordinates,num):

    distmat=[[0.]*num for i in range(num)]

    for i in range(num):
        for j in range(i,num):
            distmat[i][j] =distmat[j][i]=((coordinates[i][1]-coordinates[j][1])**2+(coordinates[i][0]-coordinates[j][0])**2)**0.5

    return distmat
    
#初始化SA参数 
def initpara():
    alpha = 0.99
    t =1000
    markovlen = 100
 
    return alpha,t,markovlen

#"旅行商问题 ( TSP , Traveling Salesman Problem )"
num=int(input())+1
t0 = time.time()

coordinates=[]
for i in range(num):
	temp_list=list(map(int,input().split()))
	coordinates.append(temp_list)

distmat = getdistmat(coordinates,num) #得到距离矩阵
#for i in range(num):
#    print (distmat[i])

solutionnew = list(range(num))

solutioncurrent = solutionnew.copy()
valuecurrent =0 
for i in range(num-1):
    valuecurrent += distmat[solutionnew[i]][solutionnew[i+1]]
valuecurrent += distmat[solutionnew[0]][solutionnew[num-1]]
#print(valuecurrent)

solutionbest = solutionnew.copy()
valuebest = valuecurrent
 
alpha,t2,markovlen = initpara()
t = t2
 
result = [] #记录迭代过程中的最优解
count=0
while time.time() - t0<9.5 and count<10*markovlen:
    count+=1
    for i in range(markovlen):
        while True:#产生两个不同的随机数
            loc1 = int(random.random()*(num-1))+1
            loc2 = int(random.random()*(num-1))+1
            #print(loc1,loc2)
            if loc1 != loc2:
                break
        solutionnew[loc1],solutionnew[loc2] = solutionnew[loc2],solutionnew[loc1]
        #print(solutionnew)
        valuenew=0
        for i in range(num-1):
            valuenew += distmat[solutionnew[i]][solutionnew[i+1]]
        valuenew += distmat[solutionnew[0]][solutionnew[num-1]]
       # print (valuenew)
        if valuenew<valuecurrent: #接受该解
            count=0
           
            #更新solutioncurrent 和solutionbest
            valuecurrent = valuenew
            solutioncurrent = solutionnew.copy()
 
            if valuenew < valuebest:
                valuebest = valuenew
                solutionbest = solutionnew.copy()
            
        else:#按一定的概率接受该解
            if random.random() < math.exp(-(valuenew-valuecurrent)/t):
                valuecurrent = valuenew
                solutioncurrent = solutionnew.copy()
            else:
                solutionnew = solutioncurrent.copy()
    t = alpha*t
    result.append(valuebest)
#用来显示结果
for i in range(1,num):
    print(solutionbest[i],end=' ')