from utils import *
import numpy as np


def warpPerspective(img, transform_matrix, output_width, output_height):


    """
    TODO : find warp perspective of image_matrix and return it
    :return a (width x height) warped image
    """

    res = np.zeros((output_width,output_height,3), dtype="int")
    for x in range(len(img)) :
        for y in range(len(img[0])) :
           primNum = np.dot(transform_matrix,[x,y,1])
           zegX = int (primNum[0] / primNum[2])
           zegY = int (primNum[1] / primNum[2])
           if (0 <= zegY and zegY < output_height):
                if(0 <= zegX and zegX < output_width) :
                    res[zegX][zegY] = img[x][y]

    return res


def grayScaledFilter(img):
    greyTranMatrix = np.array(([1/3,1/3,1/3],[1/3,1/3,1/3],[1/3,1/3,1/3]),dtype="float")
    return Filter(img,greyTranMatrix)
    """
    TODO : Complete this part based on the description in the manual!
    
    """



def crazyFilter(img):
    crazyFTranMatrix = np.array(([0,1,1],[1,0,0],[0,0,0]),dtype="float")
    """
    TODO : Complete this part based on the description in the manual!
    """
    return Filter(img,crazyFTranMatrix)


def customFilter(img):
    customTranMAtrix = np.array(([0,0,1],[0,1,0],[1,0,0]))
    return Filter(img,customTranMAtrix)
    """
    TODO : Complete this part based on the description in the manual!
    """



def scaleImg(img, scale_width, scale_height):
    res = np.zeros((len(img) * scale_width, len(img[0]) * scale_height, 3), dtype="int")
    for x in range(len(img) * scale_width) :
        for y in range(len(img[0]) * scale_height) :
           newX = int (x / scale_width)
           newY = int (y / scale_height)
           res[x][y] = img[newX][newY]

    return res
    """
    TODO : Complete this part based on the description in the manual!
    """



def cropImg(img, start_row, end_row, start_column, end_column):
    #res = np.zeros((end_row - start_row, end_column - start_column, 3), dtype="int")
    res = img[start_column : end_column,start_row : end_row]

    return res
    """
    TODO : Complete this part based on the description in the manual!
    """



if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    showImage(image_matrix, title="Input Image")

    # TODO : Find coordinates of four corners of your inner Image ( X,Y format)
    #  Order of coordinates: Upper Left, Upper Right, Down Left, Down Right
    pts1 = np.float32([[106, 214], [379,179], [158, 644], [496, 571]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    m = getPerspectiveTransform(pts1, pts2)

    warpedImage = warpPerspective(image_matrix, m, width, height)
    showWarpPerspective(warpedImage)

    grayScalePic = grayScaledFilter(warpedImage)
    showImage(grayScalePic, title="Gray Scaled")

    crazyImage = crazyFilter(warpedImage)
    showImage(crazyImage, title="Crazy Filter")

    customImage =customFilter(warpedImage)
    showImage(customImage,title="customImage")

    croppedImage = cropImg(warpedImage, 50, 300, 50, 225)
    showImage(croppedImage, title="Cropped Image")

    scaledImage = scaleImg(warpedImage, 2, 3)
    showImage(scaledImage, title="Scaled Image")
