########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arango Manrique
########################################

from gaussianSmoothing import gaussianBlur
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

def calculateEccentricity(img):
    listY = [y[0] for y in img]
    listX = [x[1] for x in img]
    a = max(listX) - min(listX)
    b = max(listY)- min(listY)
    eccentricity = math.sqrt((a*a)-(b*b))/a
    return eccentricity

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