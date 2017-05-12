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

def filter(grayScaleSignature):
    filteredSignature = grayScaleSignature < 50
    return filteredSignature.astype(int)

img = resizeSignature('Signature.jpg')

def centroid(img):
    ones = []
    for x in xrange(len(img)):
        for y in xrange(len(img[0])):
                if img[x,y] == 1:
                    ones.append((x,y))
    sumx = 0
    sumy = 0
    for item in ones:
        sumy+=item[0]
        sumx+=item[1]
    meanx = sumx/len(ones)
    meany = sumy/len(ones)

    return (meanx, meany)


imgSmooted = gaussianBlur(2,2.5,img)
print imgSmooted[10]
imgFiltered = filter(imgSmooted)

print centroid(imgFiltered)
print imgFiltered

plt.imshow(imgFiltered)

plt.show()







