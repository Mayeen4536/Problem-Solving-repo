def flippingMatrix(matrix):
    # Write your code here
    # n = len(matrix)*2
    v = 0
    for i in range(n):
        for j in range(n):
            l = []
            l.append(matrix[i][j]) # current matrix
            l.append(matrix[2 * n - 1 - i][j])  # bottom left
            l.append(matrix[i][2 * n - 1- j]) # top right
            l.append(matrix[2* n - 1 - i][2 * n - 1- j]) # bottom right
    
            maxv = max(l)
            #print(l)
            #print(max(l))
            
            v += maxv

    return v

n = 2
