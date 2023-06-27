# This is a sample Python script.
import pandas as pd
import os
import numpy as np
import math
from matplotlib import pyplot as plt
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input = pd.read_csv("covid_cases.csv")
    inpWorld = input["World"]
    randNums = np.random.choice(len(inpWorld), math.floor(len(inpWorld) * 0.95), False)
    chosenInp  = np.ndarray((math.floor(len(inpWorld) * 0.95),2),dtype=float)
    for i in range(len(randNums)):
        numb = randNums[i]
        chosenInp[i][0] = numb
        chosenInp[i][1] = inpWorld[numb]
    testDatas = np.ndarray((math.ceil(len(inpWorld) * 0.05),2), dtype = float)
    j = 0
    for i in range(len(inpWorld)) :
        if i not in randNums :
            testDatas[j][0] = i
            testDatas[j][1] = inpWorld[i]
            j = j + 1


    ax = np.ndarray((len(chosenInp), 2), dtype = float)
    temp = np.ones(len(chosenInp))
    #print(ax[:,0].shape)
    ax[:,0] = temp
    y = np.ndarray((len(chosenInp), 1), dtype=float)
    for i in range(len(chosenInp)) :
        ax[i][1] = chosenInp[i][0]
        y[i] = chosenInp[i][1]
    at = np.transpose(ax)
    ata = np.dot(at, ax)
    invAta = np.linalg.inv(ata)
    aty = np.dot(at, y)
    x = np.dot(invAta, aty)

    print(x)
    xPos = np.linspace(0,len(chosenInp),len(chosenInp))
    yPos = xPos * x[1] + x[0]
    plt.plot(xPos,yPos)
    plt.scatter(testDatas[:, 0], testDatas[:, 1],marker = "*" ,c='red')
    plt.plot(inpWorld, label = "All data", c= 'green')
    plt.title("Linear Est")
    plt.show()

    #print(y.shape)
    for i in range(len(testDatas)) :
        print(f'Real Value :  { testDatas[i,1] }')
        dummy = testDatas[i, 0]
        dummy2 = dummy * x[1] + x[0]
        print(f'Estimated Value :  { dummy2 } ')
        print(f'Error :  {abs(testDatas[i,1] - dummy2)} ')
        print("-----------------------------------------------")

    ax2 = np.ndarray((len(chosenInp), 3),dtype = float)
    ax2[:,0:2] = ax
    for i in range(len(chosenInp)):
        ax2[i, 2] = math.pow(ax2[i, 1], 2)

    at2 = np.transpose(ax2)
    at2a = np.dot(at2, ax2)
    invAt2a = np.linalg.inv(at2a)
    at2y = np.dot(at2, y)
    x2 = np.dot(invAt2a, at2y)

    print(x2)
    xPos2 = np.linspace(0, len(chosenInp), len(chosenInp))
    yPos2 = xPos2 * xPos2 * x2[2] + xPos2 * x2[1] + x2[0]
    plt.plot(xPos2, yPos2)
    plt.title("Parabola Est")
    plt.plot(inpWorld, label = "All Data",c = 'green')
    plt.scatter(testDatas[:, 0], testDatas[:, 1], marker="*", c='red')
    plt.show()
    print("\n\n<<<<<<<<<<<<<<<< Parabola EST >>>>>>>>>>>>>>>>>>\n\n")
    for i in range(len(testDatas)) :
        print(f'Real Value :  { testDatas[i,1] }')
        dummy = testDatas[i, 0]
        dummy2  = dummy ** 2 * x2[2] + dummy * x2[1] + x2[0]
        print(f'Estimated Value :  { dummy2 }')
        print(f'Error :  {abs(testDatas[i,1] - dummy2)} ')
        print("-----------------------------------------------")