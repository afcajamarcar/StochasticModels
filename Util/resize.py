########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arango Manrique
########################################



from PIL import Image
from resizeimage import resizeimage
import cv2




# Read a image, convert to gray scale and resized.
def resizeSignature(nameSignature):
    signatureArray = nameSignature.split('.')

    with open("../Signatures/" + nameSignature, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_contain(image, [500, 500])
            cover.save("../Signatures/" + signatureArray[0] + '_resized.' + signatureArray[1], image.format)

    img = cv2.imread("../Signatures/" +  signatureArray[0] + '_resized.' + signatureArray[1], 0)

    return img

