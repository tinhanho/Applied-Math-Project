from matplotlib import pyplot as plt
from scipy.interpolate import CubicSpline
import numpy as np
from PIL import Image

def Cubic_Spline_Way():
    img = plt.imread("2.jpg")
    img = img.copy()
    img = img.tolist()
    height = len(img)
    width = len(img[0])
    depth = len(img[0][0])
    height_append = (np.ones((width, depth), dtype=int)*255).tolist()
    width_append = (np.ones((1, depth), dtype=int)*255).tolist()

    for i in range(height):
        img.append(height_append)

    for j in range(height+1):
        for k in range(width):
            img[j].append(width_append[0])

    img_org = plt.imread("2.jpg")
    img_org = img_org.copy().tolist()
    img = np.array(img)

    for i in range(height):
        for j in range(width):
            img[i*2][j*2][0] = img_org[i][j][0]
            img[i*2][j*2][1] = img_org[i][j][1]
            img[i*2][j*2][2] = img_org[i][j][2]

    for i in range(height):
        for j in range(width):
            if(i%2!=0 or j%2!=0):
                img[i][j] = 255

    for j in range(width):
        xdata = []
        ydata = []
        for i in range(height):
            xdata.append(i * 2)
            ydata.append(img_org[i][j][0])

        f = CubicSpline(xdata, ydata)

        for i in range(height):
            img[i * 2 + 1][j * 2][0] = int(f(i * 2 + 1))

    for j in range(width):
        xdata = []
        ydata = []
        for i in range(height):
            xdata.append(i * 2)
            ydata.append(img_org[i][j][1])

        f = CubicSpline(xdata, ydata)

        for i in range(height):
            img[i * 2 + 1][j * 2][1] = int(f(i * 2 + 1))

    for j in range(width):
        xdata = []
        ydata = []
        for i in range(height):
            xdata.append(i * 2)
            ydata.append(img_org[i][j][2])

        f = CubicSpline(xdata, ydata)

        for i in range(height):
            img[i * 2 + 1][j * 2][2] = int(f(i * 2 + 1))


    for i in range(height):
        xdata = []
        ydata = []
        for j in range(width):
            xdata.append(j * 2)
            ydata.append(img_org[i][j][0])

        f = CubicSpline(xdata, ydata)

        for j in range(width):
            img[i * 2][j * 2 + 1][0] = int(f(j * 2 + 1))

    for i in range(height):
        xdata = []
        ydata = []
        for j in range(width):
            xdata.append(j * 2)
            ydata.append(img_org[i][j][1])

        f = CubicSpline(xdata, ydata)

        for j in range(width):
            img[i * 2][j * 2 + 1][1] = int(f(j * 2 + 1))

    for i in range(height):
        xdata = []
        ydata = []
        for j in range(width):
            xdata.append(j * 2)
            ydata.append(img_org[i][j][2])

        f = CubicSpline(xdata, ydata)

        for j in range(width):
            img[i * 2][j * 2 + 1][2] = int(f(j * 2 + 1))


    # Last

    for i in range(height):
        xdata = []
        ydata = []
        for j in range(width):
            xdata.append(j * 2 + 1)
            ydata.append(img[i * 2][j * 2 + 1][0])

        f = CubicSpline(xdata, ydata)

        for j in range(width):
            img[i * 2 + 1][j * 2 + 1][0] = int(f(j * 2 + 1))

    for i in range(height):
        xdata = []
        ydata = []
        for j in range(width):
            xdata.append(j * 2 + 1)
            ydata.append(img[i * 2][j * 2 + 1][1])

        f = CubicSpline(xdata, ydata)

        for j in range(width):
            img[i * 2 + 1][j * 2 + 1][1] = int(f(j * 2 + 1))

    for i in range(height):
        xdata = []
        ydata = []
        for j in range(width):
            xdata.append(j * 2 + 1)
            ydata.append(img[i * 2][j * 2 + 1][2])

        f = CubicSpline(xdata, ydata)

        for j in range(width):
            img[i * 2 + 1][j * 2 + 1][2] = int(f(j * 2 + 1))

    # f, axs = plt.subplots(1, 2, figsize=(10, 8), width_ratios=[1, 2])
    # img_org = np.array(img_org)
    # axs[0].imshow(img_org)
    # axs[1].imshow(img)
    # plt.show()
    im = Image.fromarray(img.astype(np.uint8))
    im.save("out2_CubicSpline.jpg")

def Linear_Way():
    img = plt.imread("2.jpg")
    img = img.copy()
    img = img.tolist()
    height = len(img)
    width = len(img[0])
    depth = len(img[0][0])
    height_append = (np.ones((width, depth), dtype=int) * 255).tolist()
    width_append = (np.ones((1, depth), dtype=int) * 255).tolist()

    for i in range(height):
        img.append(height_append)

    for j in range(height + 1):
        for k in range(width):
            img[j].append(width_append[0])

    img_org = plt.imread("2.jpg")
    img_org = img_org.copy().tolist()
    img = np.array(img)

    for i in range(height):
        for j in range(width):
            img[i * 2][j * 2][0] = img_org[i][j][0]
            img[i * 2][j * 2][1] = img_org[i][j][1]
            img[i * 2][j * 2][2] = img_org[i][j][2]

    for i in range(height):
        for j in range(width):
            if (i % 2 != 0 or j % 2 != 0):
                img[i][j] = 255

    for j in range(width):
        for i in range(height):
            if i != height-1:
                img[i * 2 + 1][j * 2][0] = (img[i*2][j*2][0]+img[i*2+2][j*2][0])/2

    for j in range(width):
        for i in range(height):
            if i != height-1:
                img[i * 2 + 1][j * 2][1] = (img[i*2][j*2][1]+img[i*2+2][j*2][1])/2

    for j in range(width):
        for i in range(height):
            if i != height-1:
                img[i * 2 + 1][j * 2][2] = (img[i*2][j*2][2]+img[i*2+2][j*2][2])/2

    for i in range(height):
        for j in range(width):
            if j != width-1:
                img[i * 2][j * 2 + 1][0] = (img[i*2][j*2][0] + img[i*2][j*2+2][0])/2

    for i in range(height):
        for j in range(width):
            if j != width-1:
                img[i * 2][j * 2 + 1][1] = (img[i*2][j*2][1] + img[i*2][j*2+2][1])/2

    for i in range(height):
        for j in range(width):
            if j != width-1:
                img[i * 2][j * 2 + 1][2] = (img[i*2][j*2][2] + img[i*2][j*2+2][2])/2

    for i in range(height):
        for j in range(width):
            if j != width-1:
                img[i*2+1][j*2+1][0] = (img[i*2+1][j*2][0] + img[i*2+1][j*2+2][0])/2

    for i in range(height):
        for j in range(width):
            if j != width-1:
                img[i*2+1][j*2+1][1] = (img[i*2+1][j*2][1] + img[i*2+1][j*2+2][1])/2

    for i in range(height):
        for j in range(width):
            if j != width-1:
                img[i*2+1][j*2+1][2] = (img[i*2+1][j*2][2] + img[i*2+1][j*2+2][2])/2

    # f, axs = plt.subplots(1, 2, figsize=(10, 8), width_ratios=[1, 2])
    # img_org = np.array(img_org)
    # axs[0].imshow(img_org)
    # axs[1].imshow(img)
    # plt.show()
    im = Image.fromarray(img.astype(np.uint8))
    im.save("out2_Linear.jpg")
def Mixed_Way():
    img = plt.imread("2.jpg")
    img = img.copy()
    img = img.tolist()
    height = len(img)
    width = len(img[0])
    depth = len(img[0][0])
    height_append = (np.ones((width, depth), dtype=int) * 255).tolist()
    width_append = (np.ones((1, depth), dtype=int) * 255).tolist()

    for i in range(height):
        img.append(height_append)

    for j in range(height + 1):
        for k in range(width):
            img[j].append(width_append[0])

    img_org = plt.imread("2.jpg")
    img_org = img_org.copy().tolist()
    img = np.array(img)

    for i in range(height):
        for j in range(width):
            img[i * 2][j * 2][0] = img_org[i][j][0]
            img[i * 2][j * 2][1] = img_org[i][j][1]
            img[i * 2][j * 2][2] = img_org[i][j][2]

    for i in range(height):
        for j in range(width):
            if (i % 2 != 0 or j % 2 != 0):
                img[i][j] = 255

    for j in range(width):
        for i in range(height):
            if i != height-1:
                img[i * 2 + 1][j * 2][0] = (img[i*2][j*2][0]+img[i*2+2][j*2][0])/2

    for j in range(width):
        for i in range(height):
            if i != height-1:
                img[i * 2 + 1][j * 2][1] = (img[i*2][j*2][1]+img[i*2+2][j*2][1])/2

    for j in range(width):
        for i in range(height):
            if i != height-1:
                img[i * 2 + 1][j * 2][2] = (img[i*2][j*2][2]+img[i*2+2][j*2][2])/2

    for i in range(height):
        for j in range(width):
            if j != width-1:
                img[i * 2][j * 2 + 1][0] = (img[i*2][j*2][0] + img[i*2][j*2+2][0])/2

    for i in range(height):
        for j in range(width):
            if j != width-1:
                img[i * 2][j * 2 + 1][1] = (img[i*2][j*2][1] + img[i*2][j*2+2][1])/2

    for i in range(height):
        for j in range(width):
            if j != width-1:
                img[i * 2][j * 2 + 1][2] = (img[i*2][j*2][2] + img[i*2][j*2+2][2])/2

    # Last

    for i in range(height):
        xdata = []
        ydata = []
        for j in range(width):
            xdata.append(j * 2 + 1)
            ydata.append(img[i * 2][j * 2 + 1][0])

        f = CubicSpline(xdata, ydata)

        for j in range(width):
            img[i * 2 + 1][j * 2 + 1][0] = int(f(j * 2 + 1))

    for i in range(height):
        xdata = []
        ydata = []
        for j in range(width):
            xdata.append(j * 2 + 1)
            ydata.append(img[i * 2][j * 2 + 1][1])

        f = CubicSpline(xdata, ydata)

        for j in range(width):
            img[i * 2 + 1][j * 2 + 1][1] = int(f(j * 2 + 1))

    for i in range(height):
        xdata = []
        ydata = []
        for j in range(width):
            xdata.append(j * 2 + 1)
            ydata.append(img[i * 2][j * 2 + 1][2])

        f = CubicSpline(xdata, ydata)

        for j in range(width):
            img[i * 2 + 1][j * 2 + 1][2] = int(f(j * 2 + 1))

    # f, axs = plt.subplots(1, 2, figsize=(10, 8), width_ratios=[1, 2])
    # img_org = np.array(img_org)
    # axs[0].imshow(img_org)
    # axs[1].imshow(img)
    # plt.show()
    im = Image.fromarray(img.astype(np.uint8))
    im.save("out2_Mixed.jpg")

