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

#Test cases
links1 = [[1,2,3],[3],[0],[1,2]]
print("Testing connections()")
assert(connections(links1) == [[  0,   0,   1,   0],
                               [1/3,   0,   0, 1/2],
                               [1/3,   0,   0, 1/2],
                               [1/3,   1,   0,   0]])
print("Success.")

print(diagM(connections(links1)))


