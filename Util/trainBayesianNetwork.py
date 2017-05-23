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
import matplotlib.pyplot as plt
import resize as rz
import bayesianNetwork as bN
import gaussianSmoothing as GaussS
from tkFileDialog import askopenfilename
import numpy as np


if __name__ == "__main__":

    # first of all, the base transformation of the data points is needed
    base = plt.gca().transData
    rot = transforms.Affine2D().rotate_deg(270)

    filename = askopenfilename()
    img = rz.resizeSignature(filename)

    # Image filtering
    imgSmooted = GaussS.gaussianBlur(1, 0.5, img)
    imgFiltered = bN.filter(imgSmooted)

    # Calculate the ones in the matrix.
    blackPoints = bN.calculateBlackPoints(imgFiltered)

    # Calculate the center of mass
    centerMass = bN.centroid(blackPoints)
    print "CenterMass (row, col)", centerMass

    # Calculate the eccentricity
    eccentricity = bN.calculateEccentricity(blackPoints)
    print "Eccentricity", eccentricity
    # Calculate the representative points of a signature
    densePoints = bN.calculateDensePoints(blackPoints)
    print "Dense Points(20)", densePoints

    # Calculate Kurtosis of blackpoints in signature
    print "Kurtosis (row, col)", bN.calculateKurtosis(blackPoints)

    # Print skew detection
    testSkew = bN.skewDetection(imgFiltered)
    print "Angle signature", testSkew




