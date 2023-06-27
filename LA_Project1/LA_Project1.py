# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

def row_swap(matrix, r1, r2) :
    dummy = np.copy(matrix[r1])
    matrix[r1] = matrix[r2]
    matrix[r2] = dummy
def zeroOp(matrix,numR, numC) :

    for x in range(numR,rowNum - 1) :
        c = matrix[x + 1, numC] / matrix[numR,numC]
        dummyRow = matrix[numR] * c
        matrix[x + 1] -= dummyRow
def zeroOpUp(matrix, numR, numC) :
    for x in range(numR) :
        c = matrix[x,numC]
        dummyRow = matrix[numR] * c
        matrix[x] -= dummyRow
def zeroPassDown(matrix) :
    checkRow = np.zeros(colNum)

    for x in range(rowNum) :
        dumRow = matrix[x]
        #print("checkRow :",checkRow, '\n')
        if np.array_equiv(dumRow ,checkRow) :
            #print("found the zero row! :", x,"\n")
            for y in range(rowNum) :
                dRow = matrix[rowNum - 1 - y]
                if np.array_equiv(dRow ,checkRow) != 1 :
                    #print("found the none zero row ! : ", rowNum - 1 - y, "\n")
                    row_swap(matrix,x,rowNum - 1 - y)
#get raw number and column number
inpIntArray = [int(x) for x in input().split()]
rowNum = inpIntArray[0]
colNum = inpIntArray[1]

#get the Matrix
inpMatrix = np.zeros((rowNum, colNum))
for y in range(rowNum) :
    inpRowArray = [int(x) for x in input().split()]
    for z in range(colNum) :
        position =[int(colNum * y + z) ]
        np.put(inpMatrix, position, inpRowArray[z])
#print("input matrix : \n ",inpMatrix , "\n")
#check if first element is 0 and swap if needed

#star of Eclon form, find pivot
curRow = 0
zeroPassDown(inpMatrix)
for curCol in range(colNum) :
    if inpMatrix[curRow, curCol] == 0:
        #print("found 0! must swap:", curRow,"\n")
        for z in range(curRow,rowNum):
            if inpMatrix[z, curCol] != 0:
                row_swap(inpMatrix, curRow, z)
                #print(f'swaped{cur} ')
    for y in range(curRow,rowNum) :
        if inpMatrix[y,curCol] != 0 :
            #inpMatrix[y] /= inpMatrix[y,curCol]

            #make rest of the column 0
            zeroOp(inpMatrix,y, curCol)


            if curRow != (rowNum - 1) :
                curRow += 1
            break
#end of echlon form, Begin echlon reduction
#print("echlon : \n", inpMatrix  ,"\n")
curRow = rowNum
x = 0
while x < curRow :
    for y in range(colNum - 1) :
         if inpMatrix[curRow - 1 - x,y] != 0 :
            #print("We are at Row : \n", curRow)
            #print("found the one! :\n",curRow - 1 - x,", ",y,", ",inpMatrix[curRow - 1 - x,y])
            inpMatrix[curRow - 1 - x] /= inpMatrix[curRow - 1 - x, y]
            zeroOpUp(inpMatrix,curRow - 1 - x,  y)
            #print("After ZeroOpUp :\n", inpMatrix, "\n")
            if curRow != 0 :
                curRow -= 1
            x = -1
            break
    x +=1
#Print the matrix

for x in range(rowNum):
    for y in range(colNum) :
        print(inpMatrix[x,y], end= " ")
    print( )

#end og reduced echlon, begin print result
#if(rowNum < colNum - 1) :
checkArray = np.zeros((rowNum,1))
#freeFound = 0
for x in range(rowNum) :
        #if freeFound == 1 :
            #break
    pivotPass = 0
    #print("reset the pivotPass see :3 :", pivotPass,"\n")
    for y in range(colNum - 1) :
            if inpMatrix[x, y] != 0 and pivotPass:
                #print("is pivotPass really on? :3 :", pivotPass, "\n")
                #print("reached the freeNum in :", x ,", ", y,"\n")
                #freeNum  = y
                inpMatrix[:,colNum - 1] -= (inpMatrix[:,y] * 10 )
                inpMatrix[:,y] -= inpMatrix[:,y]
                #print("what we changed : ", inpMatrix[:,:y], "\n")
                #print("The Asw Col : ",inpMatrix[:,colNum - 1])
                #freeFound = 1
                #break
            #elif inpMatrix[x,y] == 0 :
                #print("reached zero in : ", x,", ", y, "\n")
                #dummyCol = inpMatrix[:,y]
                #if np.array_equiv(dummyCol ,checkArray) :

                    #print("Found all Zero Col\n")
                    #freeNum = y
                    #freeFound = 1
                    #break
            elif inpMatrix[x,y] != 0 :
                #print("Passed the Pivot\n")
                pivotPass = 1
#print("the final result :\n",inpMatrix)
#print("free Num is : ", freeNum)
for x in range(colNum ) :
    dummyCol = inpMatrix[:,x]
    #print("dummyCol :", dummyCol , "\n")
    if  np.array_equiv(dummyCol ,checkArray):
        print(f'X{(x + 1)} = 10')
    for y in range(rowNum) :
        if inpMatrix[y,x] == 1 :
            print(f'X{(x + 1)} = {inpMatrix[y,colNum -1]}')