#ysato #jiayizha
#241TP
import numpy as np

#turn a list of links into a matrix
#the j,i entry of which represents the connection between links i,j
#returns initial matrix M with stochastic cols
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
    #for reducible graphs
    damp = 0.85
    N = len(result)
    ones = np.ones(N)
    for row in range(len(result)):
        for col in range(len(result[0])):
            result[row][col] = (damp * result[row][col]) 
    result += (((1-damp)/N) * ones)
    return result    

#diagonalize M
def diagM(M):
    eigval , P = np.linalg.eig(M)
    D=np.diag(list(eigval))
    Pinv=np.linalg.inv(P)
    return [P,D,Pinv]

#convergence of graph
def convergence(diag):
    P, D, Pinv = diag[0], diag[1], diag[2]
    N = len(D)
    x0 = np.array([1 for i in range(N)])
    x1 = P @ np.linalg.matrix_power(D, 80) @ Pinv @ x0
    x1 = np.real(x1)    
    return x1

#return the order
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

