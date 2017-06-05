########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arango Manrique
########################################

import numpy as np
import operator
from sklearn.cluster import KMeans
from scipy.stats import kurtosis
import math


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
    meanx = np.mean([item[0] for item in blackPointsImg])
    meany = np.mean([item[1] for item in blackPointsImg])
    return (round(meanx), round(meany))

def calculateDensePoints(blackPointsImg, numberDensePoints=10):
    positions = blackPointsImg
    kmeansDensePoints = KMeans(n_clusters=numberDensePoints, n_jobs=-1).fit(positions)
    densePoints = kmeansDensePoints.cluster_centers_
    ind = np.argsort(densePoints[:, 0])

    # Switch the ordering (so it's decreasing order)
    rind = ind[::-1]

    # Return the matrix with rows in the specified order
    densePoints = densePoints[rind]

    return densePoints


#Calculates Fisher Kurtosis by default, returns an array (it could return Pearson's measure of kurtosis)
def calculateKurtosis(blackPointsImg):
    listY = [y[0] for y in blackPointsImg]
    listX = [x[1] for x in blackPointsImg]
    matrix = np.array([listY, listX])

    return kurtosis(matrix.T)

def calculateEccentricity(img):
    listY = [y[0] for y in img]
    listX = [x[1] for x in img]
    a = max(listX) - min(listX)
    b = max(listY)- min(listY)
    return math.sqrt((a*a)-(b*b))/a if b < a else math.sqrt((a * a) + (b * b)) / a

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


def calculateGradient(blackPoints, imageShape):
    # Find gradient in a grid 4x4
    fixedForGradient = np.zeros(imageShape)
    for blPoint in blackPoints:
        fixedForGradient[blPoint[0]][blPoint[1]] = 1

    matrixGradient = []
    for i in np.split(fixedForGradient, 5):
        tmpRow = []
        for j in np.split(i, 5, axis=1):
            gradient = np.gradient(j)
            tmpRow.append((np.trace(gradient[0]), np.trace(gradient[1])))

        matrixGradient.append(tmpRow)

    # Just the important gradients of a signature
    return matrixGradient[1:4]


def calculatePressure(imageGrayScale):

    matrixPresure = []
    for i in np.split(imageGrayScale, 4):
        tmpRow = []
        for j in np.split(i, 4, axis=1):
            findPressure = []
            for row in j:
                for col in row:
                    if col != 255:
                        findPressure.append(col)

            tmpRow.append(round(np.mean(findPressure),3))

        matrixPresure.append(tmpRow)

    # Just the important gradients of a signature
    return matrixPresure

