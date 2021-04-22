    
def swapRows(m):
    # Bubble sort our rows based off the first element 
    for i in range(len(m)):
        max = i
        tmp = []       
        for j in range(i+1 ,len(m)):
            if abs(m[max][0]) < abs(m[j][0]):
                max=j
        # Swap rows
        tmp  = m[i]
        m[i] = m[max]
        m[max] = tmp

def addRowsUpper(m):
    # look at each column starting at the end
    for i in range(0,len(m)-1)[::-1]:
        # look at the correct upper echelon for that row 
        for j in range(i+1,len(m[0])-1)[::-1]:
            mult = m[i][j]
            for k in range(len(m[0])):
                m[i][k] = m[i][k] - m[j][k]*mult
                
def addRowsLower(m):
    # look at each column 
    for i in range(1, len(m)): 
        # look at the correct lower echelon for that row 
        for j in range(i):
            # row multiplier for subtracting to make lower echelon zero
            if(m[j][j] != 0):
                rowMult =  m[i][j]/m[j][j]
            else:
                rowMult = 0
            for k in range(len(m[0])):
                m[i][k] = m[i][k] - m[j][k]*rowMult
            
def multiplyRows(m):
    # Divide the row by the current row diagonal echelon 
    #   to make our diagonal echelon 1
    for i in range(len(m)):
        if m[i][i] == 0:
            continue
        divide = m[i][i]
        for j in range(len(m[i])):
            m[i][j]=m[i][j]/divide

def solve(m):
    # Back substitution
    # Solves each row by multiplying the corresponding solutions (x,y,z) then
    # subtracting the sum-1 from the row constant to find the next solution.
    # wow that's worded bad
    solution = [ 1.0 for i in range(len(m[0])-1)]
    for i in range(len(m))[::-1]:
        for j in range(len(m[0])-1)[::-1]:
            sum=0
            for k in range(len(m[0])-1):
                sum += m[i][k]*solution[k]
        solution[i] = m[i][-1] - (sum-1)
    
    return solution
    

def gaussJordan(m):
    swapRows(m)
    addRowsLower(m)
    multiplyRows(m)
    addRowsUpper(m)
    
def gauss(m):
    swapRows(m)
    addRowsLower(m)
    multiplyRows(m)
    return solve(m)

def inverseGausJordan(m):

    swapRows(m)
    I = [[1,0,0],
         [0,1,0],
         [0,0,1]]
    
    # look at each column 
    for i in range(1, len(m)): 
        # look at the correct lower echelon for that row 
        for j in range(i):
            # row multiplier for subtracting to make lower echelon zero
            if(m[j][j] != 0):   
                rowMult =  m[i][j]/m[j][j]
            else:
                rowMult = 0
            for k in range(len(m[0])):
                m[i][k] = m[i][k] - m[j][k]*rowMult
            for k in range(len(I[0])):
                I[i][k] = m[i][k] - m[j][k]*rowMult
    
def Gausdeterminant(m):
    print("Work space")
    swapRows(m)
    printMat(m)
    addRowsLower(m)
    
    printMat(m)
    print("Work space")

    
def printMat(m):
    for i in m:
        for j in i:
            print(" {0:6.2f} ".format(j),end='')
        print("")
    
def main():
    m = [[ 1, 0, 2, 1],
         [ 2,-1, 3,-1],
         [ 4, 1, 8, 2]]
         
    print("Original")
    printMat(m)
    
    print("\n\nAlgorithm 1: Gauss-Jordan Elimination")
    gaussJordan(m)
    printMat(m)
    print("Solution is:",[round(m[i][len(m)],3) for i in range(len(m))])
    
    # out of time :(
    '''print("\n\nAlgorithm 2: Compute matrix inverse using Gauss-Jordan elimination")
    m = [[ 1,-1, 0],
         [-2, 2,-1],
         [ 0, 1,-2]
        ]
        
    inverseGausJordan(m)
    '''
    m = [[ 1, 0, 2, 1],
         [ 2,-1, 3,-1],
         [ 4, 1, 8, 2]]
    
    print("\n\nAlgorithm 3:Gauss Elimination")
    solution = gauss(m)
    printMat(m)
    print("Solution is:",[round(i,3) for i in solution])
    
    # out of time :(
    '''print("\n\nAlgorithm 4: Matrix determinant using Gaussian elimination")
    m = [[ 1,-1, 0],
         [-2, 2,-1],
         [ 0, 1,-2]
        ]
    Gausdeterminant(m)'''

if __name__=="__main__":
    main()
