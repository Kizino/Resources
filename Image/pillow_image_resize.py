# python3 -m pip install --upgrade Pillow
from PIL import Image


size_40 = (40,40)

image = Image.open('sams_icon.png')
# image.show()

image.thumbnail(size_40)
image.save('output/sams_icon_40x40.png')