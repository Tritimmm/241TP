#ysato #jiayizha
#241TP
import numpy as np

#turn a list of links into a matrix
#the j,i entry of which represents the connection between links i,j
#returns probability matrix M with stochastic cols
def connections(links):
    result = [[0]*len(links) for i in range(len(links))]
    for i in range(len(links)): #use index as write-up
        try:
            weight = 1/len(links[i])
            for j in links[i]:
                result[j][i] = weight
        except ZeroDivisionError: #for dangling nodes
            weight = 1/len(links)
            for j in range(len(links)):
                result[i][j] = weight
    #for reducible graphs
    damp = 0.85
    N = len(result)
    ones = np.ones(N)
    #multiply matrix by damping factor
    for row in range(len(result)):
        for col in range(len(result[0])):
            result[row][col] = (damp * result[row][col])
    #take weighted average of probability matrix and all-one matrix
    result += (((1-damp)/N) * ones)
    return result

#diagonalize probability matrix
def diag(M):
    #get eigenvalues and eigenvectors of matrix
    eigval , P = np.linalg.eig(M)
    D = np.diag(list(eigval))
    Pinv = np.linalg.inv(P)
    return [P,D,Pinv]

#convergence of matrix
def convergence(diag):
    P, D, Pinv = diag[0], diag[1], diag[2]
    error = 0.00000001
    N = len(D)
    #initial pagerank vector
    x0 = np.array([1 for i in range(N)])
    x1 = P @ D @ Pinv @ x0
    x1 = np.real(x1)
    #find the limit of the random walk
    while (np.linalg.norm(x1 - x0, 2) > error):
        x0 = x1
        x1 = np.real(P @ D @ Pinv @ x0)
    return x1

#return the order of the links
def sortLink(probabilityArray):
    probablityList = probabilityArray.tolist()
    tmpList = []
    result = []
    #make a tuple for each link (P(i),i)
    for i in range(len(probablityList)):
        tmpList.append((probablityList[i],i))
    #sort by the probability (descending order)
    tmpList = sorted(tmpList, reverse=True)
    #take out the link indices from the ordered tuples
    #to get the rank of each link
    for i in range(len(tmpList)):
        result.append(tmpList[i][1])
    return result

#wrapper: returns ranking of each element in given input
def rank(links):
    rankArray = convergence(diag(connections(links)))
    ranks = sortLink(rankArray)
    return ranks
