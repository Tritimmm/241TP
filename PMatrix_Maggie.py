#jiayizha

import numpy as np

#turn a list of links into a matrix
#the j,i entry of which represents the connection between links i,j
#returns initial matrix M with stochastic cols
#(I'm terrible at naming things, so change it if you like)
def connections(links):
    result = [[0]*len(links) for i in range(len(links))]
    for i in range(len(links)): #use index as write-up
        try:
            weight = 1/len(links[i]) 
            for j in links[i]:
                result[j][i]=weight
        except: #dangling link
            #weight =
            pass
    return result    

#diagonalize M
def diagM(M): #question: will P always be invertible?
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
    rankArray=convergence(diagM(connections(x)))
    return sortLink(rankArray)

#############################TEST CASE#############################
links1 = [[1,2,3],[3],[0],[1,2]]
print("Testing connections()")
assert(connections(links1) == [[  0,   0,     1,   0],
                               [1/3,   0,     0, 1/2],
                               [1/3,   0,     0, 1/2],
                               [1/3,   1,     0,   0]])
print("Success.")


x = [[1,3,4],[0,2,4],[3,6],[2,4,6],[5,8],[4,6,8],[0,7,9],[0,6,8],[2,9],[0,2,8]]