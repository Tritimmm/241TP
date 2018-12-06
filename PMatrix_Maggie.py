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
assert(connections(links1) == [[  0,   0,     1,   0],
                               [1/3,   0,     0, 1/2],
                               [1/3,   0,     0, 1/2],
                               [1/3,   1,     0,   0]])
print("Success.")


def convergence(diag):
    P, D, Pinv = diag[0], diag[1], diag[2]
    print("D:", np.linalg.matrix_power(D, 80))
    N = len(D)
    x0 = np.array([1 for i in range(N)])
    x1 = P @ np.linalg.matrix_power(D, 80) @ Pinv @ x0
    x1 = np.real(x1)    
    return x1
    
x = [[1, 5], [2, 5], [1, 3, 5], [4], [1, 5], [2, 6], [0, 1]]
    
print(convergence(diagM(connections(x))))
    

A = [[  0,   0,     1,   0],
                               [1/3,   0,     0, 1/2],
                               [1/3,   0,     0, 1/2],
                               [1/3,   1,     0,   0]]

N = len(A)
x0 = np.array([1/N for i in range(N)])
x1 = A @ x0
def simple(A, x0, x1, depth=1):
    if depth == 10:
        print(x1)
        return x1
    else:
        x0 = x1
        x1 = A @ x0
        simple(A, x0, x1, depth + 1)
    
# print(simple(A, x0, x1))
