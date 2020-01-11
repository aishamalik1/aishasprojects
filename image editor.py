"""
Author: Aisha Malik

Print images and change their color channels, permute their colors, or decrypt photos.
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

# this makes image look better on a macbook pro
def imageshow(img, dpi=200):
    if dpi > 0:
        F = plt.gcf()
        F.set_dpi(dpi)
    plt.imshow(img)


#def rgb_ints_example():
#    '''should produce red,purple,green squares
#    on the diagonal, over a black background'''
#    # RGB indexes
#    red,green,blue = range(3)
#    # img array 
#    # all zeros = black pixels
#    # shape: (150 rows, 150 cols, 3 colors)
#    img = np.zeros((150,150,3), dtype=np.uint8)
#    for x in range(100):
#        for y in range(100):
#            # red pixels
#            img[x,y,red] = 255
#            # purple pixels
#            # set all 3 color components
#            img[x+25, y+25,:] = (128, 0, 128)
#            # green pixels
#            img[x+50,y+50,green] = 255
#    return img
#
#plt.imshow(rgb_ints_example())

def onechannel(pattern, rgb):
    red,green,blue = range(3)
    pattern = plt.imread(pattern)
    newpattern = np.copy(pattern)
    shape = newpattern.shape
#    npat = np.array(newpattern, dtype = newpattern.dtype)
    for x in range(shape[0]):
        for y in range(shape[1]):
            if newpattern[x,y,rgb] != 1:
                newpattern[x,y] = [0,0,0]
    return newpattern


def permutecolorchannels(img, perm):
    red,blue,green = range(3)
    img = plt.imread(img)
    newimg = np.copy(img) #editable version of img
    shape = img.shape
    for x in range(shape[0]):
        for y in range(shape[1]):
                newimg[x,y,perm[0]] = img[x,y,0]
                newimg[x,y,perm[1]] = img[x,y,1]
                newimg[x,y,perm[2]] = img[x,y,2]
    return newimg

"""
Correct permutation to revert colors to normal = [1,2,0]
"""

def decrypt(image, key):
    img = plt.imread(image)
    secretimg = np.copy(img)
    shape = img.shape
    key = np.load(key)
    for x in range(shape[0]):
        for y in range(shape[1]):
            red = img[x,y,0]^key[y]
            green = img[x,y,1]^key[y]
            blue = img[x,y,2]^key[y]
            secretimg[x,y,:] = (red, green, blue)
    return secretimg
            
def main():
    plt.imshow(onechannel('pattern.png', 0))
    plt.pause(0.001)
    plt.imshow(onechannel('pattern.png', 1))
    plt.pause(0.001)
    plt.imshow(onechannel('pattern.png', 2))
    plt.pause(0.001)
    plt.imshow(permutecolorchannels('permcolors.jpg', [1,2,0]))
    plt.pause(0.001)
    plt.imshow(decrypt('secret.bmp','key.npy'))
    
main()