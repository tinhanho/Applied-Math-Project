import numpy as np
import math
from PIL import Image
from matplotlib import pyplot as plt

def BiCubic(x):
    a = -0.5
    if abs(x) <= 1:
        return (a + 2) * abs(x) ** 3 - (a + 3) * abs(x) ** 2 + 1
    elif abs(x) < 2:
        return a * abs(x) ** 3 - 5 * a * abs(x) ** 2 + 8 * a * abs(x) - 4 * a
    else:
        return 0

def BiCubic_interpolation(img, dstH, dstW):
    scrH, scrW, _ = img.shape
    img_padded = np.pad(img, ((1, 1), (1, 1), (0, 0)), 'edge')
    retimg = np.zeros((dstH, dstW, 3), dtype=np.uint8)
    
    for i in range(dstH):
        for j in range(dstW):
            scrx = i * (scrH - 2) / (dstH - 1)
            scry = j * (scrW - 2) / (dstW - 1)
            x = math.floor(scrx)
            y = math.floor(scry)
            u = scrx - x
            v = scry - y
            tmp = np.zeros(3)  # Initialize with zeros to sum RGB channels
            
            for ii in range(-1, 3):  # Adjust range to include all 16 pixels
                for jj in range(-1, 3):
                    if x + ii < 0 or y + jj < 0 or x + ii >= scrH - 1 or y + jj >= scrW - 1:
                        continue
                    tmp += img_padded[x + ii + 1, y + jj + 1] * BiCubic(ii - u) * BiCubic(jj - v)
            
            # Clip and cast to uint8
            retimg[i, j] = np.clip(tmp, 0, 255).astype(np.uint8)
    
    return retimg

# The rest of your code
def bicubic():
    im_path = "PIL.jpg"
    image = np.array(Image.open(im_path))
    image2 = BiCubic_interpolation(image, image.shape[0] * 2, image.shape[1] * 2)
    image2 = Image.fromarray(image2, 'RGB')
    image2.save('BiCubic_interpolation.jpg')
    f, axs = plt.subplots(1, 2, figsize=(10, 8), width_ratios=[1, 2])
    image = np.array(image)
    axs[0].imshow(image)
    axs[1].imshow(image2)
    plt.show()
