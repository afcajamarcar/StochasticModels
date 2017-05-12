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
import matplotlib.pyplot as plt
import numpy as np

def filter(grayScaleSignature):
    filteredSignature = grayScaleSignature < 128
    return filteredSignature.astype(int)

img = filter(resizeSignature('Signature.jpg'))

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
print centroid(img)
plt.imshow(img)

plt.show()







