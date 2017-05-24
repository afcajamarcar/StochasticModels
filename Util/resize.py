########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arango Manrique
########################################
import scipy
from PIL import Image
from resizeimage import resizeimage
import numpy as np

# Read a image, convert to gray scale and resized.
# When train is true, read of train dataset.
# When genuine is true, read of genuine signatures.

def resizeSignature(nameSignature, train=True, genuine=True):
    if train and genuine:
        with open(nameSignature, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_contain(image, [500, 300]).convert('L')
                cover = np.asanyarray(cover)
                #cover = scipy.misc.imresize(image, (500,500), map()ode='L')
    elif train and not genuine:
        with open(nameSignature, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_contain(image, [500, 300]).convert('L')
                cover = np.asanyarray(cover)
    return cover

def resizeOriginal(nameSignature):
    with open(nameSignature, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_contain(image, [500, 300])
    return cover

def resizeScanned(image):
    cover = resizeimage.resize_contain(image, [500, 300])
    return cover
