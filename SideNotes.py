#Important Theorems:
    Perron–Frobenius Theorem
#Eigenstuff:
    we want to be able to apply the probablity matrix M over and over again, so we diagnalize it. (M is always gonna be a sqr matrix, so we can do this).



#############################TEST CASE#############################
links1 = [[1,2,3],[3],[0],[1,2]]
dangle = [[1,2,3],[3],[0],[1,2], []]
print("Testing connections()")
# assert(connections(links1) == [[  0,   0,     1,   0],
#                                [1/3,   0,     0, 1/2],
#                                [1/3,   0,     0, 1/2],
#                                [1/3,   1,     0,   0]])
# # assert(connections(dangle) == [[0,   0,   1.0,  0,     0], 
#                                [1/3, 0,   0,    0.5,   0], 
#                                [1/3, 0,   0,    0.5,   0], 
#                                [1/3, 1.0, 0,    0,     0], 
#                                [0.2, 0.2, 0.2,  0.2, 0.2]])
#might need to update this section to account for damping factor
print("Success.")


x = [[1,3,4],[0,2,4],[3,6],[2,4,6],[5,8],[4,6,8],[0,7,9],[0,6,8],[2,9],[0,2,8]]
