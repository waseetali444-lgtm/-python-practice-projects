import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['project image 1.jpg', 'project image 2.jpg']
images = []

for filename in filenames:
    img = Image.open(filename)
    img = img.resize((400, 400))
    images.append(np.array(img))

iio.imwrite('team.gif', images, duration=500, loop=0)