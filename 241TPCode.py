#241TP--Page Rank
#jiayizha #ysato

import numpy as np

###run wrapper() on input

def irreachable(start,goal,links,visited=None):
    if visited==None:
        visited=set()
        visited.add(start)
    if goal in visited: return False
    else:
        for tmp in links[start]:
            visited.add(tmp)
            for nextTmp in links[tmp]:
                visited.add(nextTmp)
                irreachable(nextTmp,goal,links,visited)
    return True

#return True if links produce a reducible graph
def isReducible(links):
    for i in range(len(links)):
        needToVisit=list(range(len(links)))
        needToVisit.remove(i)
        for j in links[i]: #this is like breadth first search?? (actually don't even know the word)
            needToVisit.remove(j)
        for k in needToVisit:
            if irreachable(i,k,links): return True
    return False

#turn a list-in-list into a matrix that represents the probability of
#going from one node to another in one step
def connections(links):
    result = [[0]*len(links) for i in range(len(links))]
    for i in range(len(links)): #use index as write-up
        try:
            weight = 1/len(links[i]) 
            for j in links[i]:
                result[j][i]=weight
        except ZeroDivisionError:
            weight = 1/len(links)
            for j in range(len(links)):
                result[i][j] = weight
    return result    

#diagonalize M
def diagM(M): 
    eigval , P = np.linalg.eig(M)
    D=np.diag(list(eigval))
    Pinv=np.linalg.inv(P)
    return [P,D,Pinv]

def convergence(diag):
    P, D, Pinv = diag[0], diag[1], diag[2]
    N = len(D)
    x0 = np.array([1 for i in range(N)])
    x1 = P @ np.linalg.matrix_power(D, 80) @ Pinv @ x0
    x1 = np.real(x1)    
    return x1

def sortLink(probabilityArray):
    probablityList=probabilityArray.tolist()
    tmpList=[]
    result=[]
    for i in range(len(probablityList)):
        tmpList.append((probablityList[i],i))
    tmpList=sorted(tmpList, reverse=True)
    for i in range(len(tmpList)):
        result.append(tmpList[i][1])
    return result

def wrapper(links):
    rankArray=convergence(diagM(connections(links)))
    return sortLink(rankArray)
