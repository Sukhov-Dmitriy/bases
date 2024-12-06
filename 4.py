import numpy as np
import matplotlib.pyplot as plt


def print_image1(img):
    plt.imshow(img, cmap='binary', vmin=0, vmax=255)
    plt.savefig("1.png")


def print_image2(img):
    plt.imshow(img, cmap='binary', vmin=0, vmax=255)
    plt.savefig("2.png")


img = np.array(list(map(float, input().split()))).reshape(28, 28)

img1 = np.zeros((14, 14))
for i in range(14):
    for j in range(14):
        img1[i, j] = img[2 * i:2 * i + 1, j * 2:j * 2 + 1].mean()

print_image1(img1)

img2 = np.zeros((7, 7))
for i in range(7):
    for j in range(7):
        img2[i, j] = img1[2 * i:2 * i + 1, j * 2:j * 2 + 1].mean()

print_image2(img2)