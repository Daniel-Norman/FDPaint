import math
from scipy import misc
import matplotlib.pyplot as plt

name = 'bg'
f = open('%s.coe' % name, 'w')
image = misc.imread('%s.png' % name)
f.write('memory_initialization_radix=2;\n')
f.write('memory_initialization_vector=\n')
pixels_written = 0
for row in image:
    for pixel in row:
        if len(pixel) > 3 and pixel[3] < 200:
            # Convert the transparent pixel to pure blue
            # (FDPaint interprets pure blue as transparent for stamps)
            pixel[0] = 0
            pixel[1] = 0
            pixel[2] = 255
            pixel[3] = 255
        else:
            pixel[0] = 32 * math.floor(pixel[0] / 32)
            pixel[1] = 32 * math.floor(pixel[1] / 32)
            pixel[2] = 64 * math.floor(pixel[2] / 64)
        f.write('{0:03b}{1:03b}{2:02b}'.format(int(math.floor(pixel[0] / 32)),
                                                 int(math.floor(pixel[1] / 32)),
                                                 int(math.floor(pixel[2] / 64))))
        pixels_written += 1
        if pixels_written == len(image) * len(row):
            f.write(';\n')
        else:
            f.write(',\n')

plt.imshow(image)
plt.show()

f.close()
