########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arando Manrique
########################################



from PIL import Image
from resizeimage import resizeimage
import cv2


# Read a image, convert to gray scale and resized.
def resizeSignature(nameSignature):
    signatureArray = nameSignature.split('.')

    with open("../Signatures/" + nameSignature, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [500, 500], validate=False)
            cover.save("../Signatures/" + signatureArray[0] + '_resized.' + signatureArray[1], image.format)

    img = cv2.imread("../Signatures/" +  signatureArray[0] + '_resized.' + signatureArray[1], 0)

    # Return a numpy array (500,500). GrayScale
    return img

resizeSignature('Calamardo_Guapo.jpg')