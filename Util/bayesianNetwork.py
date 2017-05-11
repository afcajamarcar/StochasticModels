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

def filter(grayScaleSignature):
    filteredSignature = grayScaleSignature < 128
    return filteredSignature.astype(int)

img = filter(resizeSignature('Signature.jpg'))

plt.imshow(img)

plt.show()







