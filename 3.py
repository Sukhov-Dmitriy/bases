import numpy as np
import matplotlib.pyplot as plt


def print_image(img):
    plt.imshow(img, cmap='binary', vmin=0, vmax=255)
    plt.savefig("1.png")


img = np.array(list(map(float, input().split()))).reshape(28, 28)
img = img[15:,:]
print_image(img)