from matplotlib import transforms
from Tkinter import *
from tkFileDialog import askopenfilename
from matplotlib.patches import Ellipse
from PIL import Image
from matplotlib.axes import Axes
import resize as rz
import matplotlib.pyplot as plt
import bayesianNetwork as bN
import numpy as np

def drawEllipse(img):
    listY = [y[0] for y in img]
    listX = [x[1] for x in img]
    a = max(listX) - min(listX)
    b = max(listY) - min(listY)
    return a,b

def concat_images(imga, imgb):
    """
    Combines two color image ndarrays side-by-side.
    """
    ha,wa = imga.shape[:2]
    hb,wb = imgb.shape[:2]
    max_height = np.max([ha, hb])
    total_width = wa+wb
    new_img = np.zeros(shape=(max_height, total_width, 3), dtype=np.uint8)
    new_img[:ha,:wa]=imga
    new_img[:hb,wa:wa+wb]=imgb
    return new_img

def concat_n_images(image_path_list):
    """
    Combines N color images from a list of image paths.
    """
    output = None
    for i, img_path in enumerate(image_path_list):
        img = plt.imread(img_path)[:,:,:3]
        if i==0:
            output = img
        else:
            output = concat_images(output, img)
    return output

if __name__ == "__main__":

    # first of all, the base transformation of the data points is needed
    base = plt.gca().transData
    rot = transforms.Affine2D().rotate_deg(270)

    #Input File
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    img = rz.resizeSignature(filename)

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
    plt.axis('off')

    # Plot Ellipse
    subplot = plt.subplot()
    b, a = drawEllipse(blackPoints)
    ell = Ellipse((centerMass[0], centerMass[1]*-1), b+10, a+10, edgecolor='black', facecolor='none',linewidth=5)
    subplot.add_patch(ell)

    # plt.plot([y positions of the points], [x positions of the points])
    # plt.plot([testSkewLeft[1], testSkewRight[1]], [testSkewLeft[0], testSkewRight[0]], 'k')
    # plt.plot([testSkewLeft[1], testSkewLeft[1]], [testSkewLeft[0], testSkewRight[0]], 'k')
    print "Angle signature", testSkew

    #Save Scanned Signature
    plt.savefig("test.PNG",dpi = 700)
    plt.axis('on')

    #Collage 2 images
    original = rz.resizeOriginal(filename)
    scanned = Image.open('test.PNG')
    sn = rz.resizeScanned(scanned)
    images = [original,sn]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    #Text
    data = "CenterMass= {0}\nEccentricity= {1}\nKurtosis= {2}\nAngle Signature= {3}".format(centerMass, eccentricity, bN.calculateKurtosis(blackPoints), testSkew)
    plt.text(-160, -20, data, fontsize=12)

    #Label
    subplot.set_xlabel('Original Signature                                                                                                                                           Scanned Signature')

    #FullScreen
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())

    #Show graphics
    plt.imshow(new_im)
    plt.show()