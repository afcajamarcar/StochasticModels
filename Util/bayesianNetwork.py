########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arando Manrique
########################################
from resize import resizeSignature
import matplotlib.pyplot as plt
from resizeimage import resizeimage

def filter(grayScaleSignature):
    filteredSignature = grayScaleSignature < 128
    return filteredSignature.astype(int)

img = filter(resizeSignature('Signature.jpg'))

plt.imshow(img)

# plt.show()

print resizeimage.path






