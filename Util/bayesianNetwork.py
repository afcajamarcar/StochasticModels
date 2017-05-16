########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arango Manrique
########################################
from matplotlib import transforms

from resize import resizeSignature
from gaussianSmoothing import gaussianBlur
import matplotlib.pyplot as plt
import numpy as np
import operator
from sklearn.cluster import KMeans
from scipy.stats import kurtosis


def filter(grayScaleSignature):
    filteredSignature = grayScaleSignature < 64
    return filteredSignature.astype(int)

def calculateBlackPoints(img):
    ones = []
    for y in xrange(len(img)):
        for x in xrange(len(img[0])):
            if x > 3 and y > 3 and x < (len(img[0])-3) and y < (len(img)-3) and img[y, x] == 1:
                ones.append((y, x))
    return ones

def centroid(blackPointsImg):
    sumx = 0
    sumy = 0
    for item in blackPointsImg:
        sumy += item[0]
        sumx += item[1]
    meanx = sumx/float(len(blackPointsImg))
    meany = sumy/float(len(blackPointsImg))

    return (round(meanx), round(meany))

def calculateDensePoints(blackPointsImg, numberDensePoints=30):
    positions = blackPointsImg
    kmeansDensePoints = KMeans(n_clusters=numberDensePoints, random_state=0, n_jobs=-1).fit(positions)
    return kmeansDensePoints.cluster_centers_


#Calculates Fisher Kurtosis by default, returns an array (it could return Pearson's measure of kurtosis)
def calculateKurtosis(blackPointsImg):
    listY = [y[0] for y in blackPointsImg]
    listX = [x[1] for x in blackPointsImg]
    matrix = np.array([listY, listX])

    return kurtosis(matrix.T)


def skewDetection(img):
    middleLeft = img[ : , :len(img)/2]
    middleRight = img[ : , (len(img)/2)+1:]

    centerMassLeft = centroid(calculateBlackPoints(middleLeft))
    centerMassRight = centroid(calculateBlackPoints(middleRight))

    # fix center mass right
    centerMassRight = tuple(map(operator.add, centerMassRight, (250, 0)))

    def angle_between(p1, p2):
        ang1 = np.arctan2(*p1[::-1])
        ang2 = np.arctan2(*p2[::-1])
        return np.rad2deg((ang1 - ang2) % (2 * np.pi))

    return angle_between(centerMassLeft, centerMassRight)


if __name__ == "__main__":

    # first of all, the base transformation of the data points is needed
    base = plt.gca().transData
    rot = transforms.Affine2D().rotate_deg(270)

    img = resizeSignature('Signature.jpg')
    # Image filtering
    imgSmooted = gaussianBlur(2, 10, img)
    imgFiltered = filter(imgSmooted)


    # Calculate the ones in the matrix.
    blackPoints = calculateBlackPoints(imgFiltered)

    # Calculate the center of mass
    centerMass = centroid(blackPoints)
    print "CenterMass (row, col)", centerMass

    # Calculate the representative points of a signature
    densePoints = calculateDensePoints(blackPoints)

    # For print in better way
    # densePoints[:,[0, 1]] = densePoints[:,[1, 0]]
    # plt.plot(list1, list2, "ro")
    # Just for print the matrix
    listY = [y[0] for y in blackPoints]
    listX = [x[1] for x in blackPoints]
    plt.plot(listY, listX, "ro", transform=rot+base)

    # Print Center of mass
    plt.plot(centerMass[0], centerMass[1], "^", transform=rot+base)

    # Print dense points
    densePoints = densePoints.T
    plt.plot(densePoints[0], densePoints[1], "g+", transform=rot+base)

    print "Kurtosis (row, col)",calculateKurtosis(blackPoints)

    # Print skew detection
    testSkew = skewDetection(imgFiltered)

    # plt.plot([y positions of the points], [x positions of the points])
    #plt.plot([testSkewLeft[1], testSkewRight[1]], [testSkewLeft[0], testSkewRight[0]], 'k')
    # plt.plot([testSkewLeft[1], testSkewLeft[1]], [testSkewLeft[0], testSkewRight[0]], 'k')
    print "Angle signature", testSkew



    plt.show()







