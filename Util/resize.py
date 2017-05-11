from PIL import Image
from resizeimage import resizeimage


with open('Calamardo_Guapo.jpg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [3000, 3000], validate=False)
        cover.save('Calamardo_Guapo_Resized.jpg', image.format)