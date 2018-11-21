#jiayizha

#turn a list of links into a matrix
#the i,j entry of which represents the connection between links i,j

import numpy as np

def connections(links):
    result = [[0]*len(links) for i in range(len(links))]
    for i in range(len(links)): #use index as write-up
        try:
            weight = 1/len(links[i]) 
            for j in links[i]:
                result[i][j]=weight
        except: #dangling link
            #weight =
            pass
    return result    


#test cases
links1 = [[1,2,3],[3],[0],[1,2]]
print("Testing connections()")
assert(connections(links1) == [[0, 1/3, 1/3, 1/3],
                               [0,   0,   0,   1],
                               [1,   0,   0,   0],
                               [0, 1/2, 1/2,   0]]