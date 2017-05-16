########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arango Manrique
########################################
from resize import resizeSignature
from gaussianSmoothing import gaussianBlur
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from scipy.stats import kurtosis


def filter(grayScaleSignature):
    filteredSignature = grayScaleSignature < 64
    return filteredSignature.astype(int)

img = resizeSignature('Signature_2.jpg')

def calculateBlackPoints(img):
    ones = []
    for x in xrange(len(img)):
        for y in xrange(len(img[0])):
            if x > 3 and y > 3 and x < (len(img)-3) and y < (len(img[0])-3) and img[x, y] == 1:
                ones.append((x, y))
    return ones




def centroid(img):
    ones = calculateBlackPoints(img)
    sumx = 0
    sumy = 0
    for item in ones:
        sumy += item[0]
        sumx += item[1]
    meanx = sumx/float(len(ones))
    meany = sumy/float(len(ones))

    return (round(meanx), round(meany))

def calculateDensePoints(img, numberDensePoints=30):
    positions = calculateBlackPoints(img)
    kmeansDensePoints = KMeans(n_clusters=numberDensePoints, random_state=0, n_jobs=-1).fit(positions)
    return kmeansDensePoints.cluster_centers_

#Calculates Fisher Kurtosis by default, returns an array (it could return Pearson's measure of kurtosis)
def calculateKurtosis(img):
    return kurtosis(img)


# Image filtering
imgSmooted = gaussianBlur(2,3,img)
imgFiltered = filter(imgSmooted)

# Calculate the ones in the matrix.
some = calculateBlackPoints(imgFiltered)

# Just for print the matrix
list1= [ x[0] for x in some ]
list2= [ x[1] for x in some ]
plt.plot(list1, list2, "ro")

# Calculate the representative points of a signature
densePoints = calculateDensePoints(imgFiltered)


print calculateKurtosis(imgFiltered)
# For print in better way
# densePoints[:,[0, 1]] = densePoints[:,[1, 0]]
# plt.plot(list1, list2, "ro")
densePoints = densePoints.T
plt.plot(densePoints[0],densePoints[1], "+")

plt.show()







