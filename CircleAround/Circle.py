import cv2 as cv
import numpy as np

# importing and displaying color image
image = cv.imread('bobby.png')
cv.imshow("Bobby with Color", image)
cv.waitKey(0)

# converting the same image to grayscale and displaying it
grayim = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
cv.imshow("Bobby in Grayscale", grayim)
cv.waitKey(0)

# radius is set to area of interest and center of image is calculated
radius = 180
row, col = grayim.shape
center = [row/2, col/2]

# iterate through each pixel set value to 0 if it's outside of area of interest
for r in range(row):
    for c in range(col):
        distance = np.sqrt((center[0] - r) ** 2 + (center[1] - c) ** 2)
        if distance > radius:
            grayim[r, c] = 0
        else:
            grayim[r, c] = grayim[r, c]

# display final image after circle border
cv.imshow("Circle Border", grayim)
cv.waitKey(0)










