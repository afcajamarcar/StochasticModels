from resize import resizeSignature
from matplotlib import transforms
from Tkinter import Tk
from tkFileDialog import askopenfilename
import matplotlib.pyplot as plt
import bayesianNetwork as bN
from matplotlib.patches import Ellipse

def drawEllipse(img):
    listY = [y[0] for y in img]
    listX = [x[1] for x in img]
    a = max(listX) - min(listX)
    b = max(listY) - min(listY)
    return a,b

if __name__ == "__main__":

    # first of all, the base transformation of the data points is needed
    base = plt.gca().transData
    rot = transforms.Affine2D().rotate_deg(270)

    #Input File
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    img = resizeSignature(filename)

    # Image filtering
    imgSmooted = bN.gaussianBlur(2, 1, img)
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

    listY = [y[0] for y in blackPoints]
    listX = [x[1] for x in blackPoints]
    plt.plot(listY, listX, "ro", transform=rot + base)

    # Print Center of mass
    plt.plot(centerMass[0], centerMass[1], "^", transform=rot + base)

    # Print dense points
    densePoints = densePoints.T
    plt.plot(densePoints[0], densePoints[1], "g+", transform=rot + base)
    print "Kurtosis (row, col)", bN.calculateKurtosis(blackPoints)

    # Print skew detection
    testSkew = bN.skewDetection(imgFiltered)

    subplot = plt.subplot()
    b, a = drawEllipse(blackPoints)
    ell = Ellipse((centerMass[0], centerMass[1]*-1), b+10, a+10, edgecolor='black', facecolor='none',linewidth=5)
    subplot.add_patch(ell)
    # plt.plot([y positions of the points], [x positions of the points])
    # plt.plot([testSkewLeft[1], testSkewRight[1]], [testSkewLeft[0], testSkewRight[0]], 'k')
    # plt.plot([testSkewLeft[1], testSkewLeft[1]], [testSkewLeft[0], testSkewRight[0]], 'k')
    print "Angle signature", testSkew

    plt.show()