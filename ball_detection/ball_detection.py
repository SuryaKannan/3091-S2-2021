# import cv2
# import numpy as np
#
# img = cv2.imread('group 4/frame000041.png')
# dimensions = img.shape
# print("Image Size:" + str(dimensions))
#
# blur_img = cv2.GaussianBlur(img, (7, 7), cv2.BORDER_DEFAULT)
# hsv_img = cv2.cvtColor(blur_img, cv2.COLOR_BGR2HSV)
# low = np.array([,20])
#
# cv2.imshow("Original", gray_img)
# cv2.waitKey(0)

import cv2
import numpy as np

def nothing(x):
    pass

# Load image
image = cv2.imread('group 4/frame000000.png')

# Create a window
cv2.namedWindow('image')

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('HMin', 'image', 0, 179, nothing)
cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

# Set default value for Max HSV trackbars
cv2.setTrackbarPos('HMax', 'image', 179)
cv2.setTrackbarPos('SMax', 'image', 255)
cv2.setTrackbarPos('VMax', 'image', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

while(1):
    # Get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', 'image')
    sMin = cv2.getTrackbarPos('SMin', 'image')
    vMin = cv2.getTrackbarPos('VMin', 'image')
    hMax = cv2.getTrackbarPos('HMax', 'image')
    sMax = cv2.getTrackbarPos('SMax', 'image')
    vMax = cv2.getTrackbarPos('VMax', 'image')

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    # Print if there is a change in HSV value
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    # Display result image
    cv2.imshow('image', result)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

#
# # adaptive threshold
# thresh1 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
# contours1, ret = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
# img_contour1 = img.copy()
# cv2.drawContours(image=img_contour1, contours=contours1, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
#
# circles1 = cv2.HoughCircles(thresh1, cv2.HOUGH_GRADIENT, 1, 80, param1=50, param2=20, minRadius=0, maxRadius=0)
# circles1 = np.uint16(np.around(circles1))
# img_circles1 = img.copy()
#
# if circles1 is not None:
#     for i in circles1[0, :]:
#         # draw the outer circle
#         cv2.circle(img_circles1, (i[0], i[1]), i[2], (0, 255, 0), 2)
#         # draw the center of the circle
#         cv2.circle(img_circles1, (i[0], i[1]), 2, (0, 0, 255), 3)
#
# # multiple object detection
#
# ret, thresh2 = cv2.threshold(gray_img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# # noise removal
# kernel = np.ones((3,3),np.uint8)
# opening = cv2.morphologyEx(thresh2,cv2.MORPH_OPEN,kernel, iterations = 2)
# # sure background area
# sure_bg = cv2.dilate(opening,kernel,iterations=3)
# # Finding sure foreground area
# dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
# ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# # Finding unknown region
# sure_fg = np.uint8(sure_fg)
# unknown = cv2.subtract(sure_bg,sure_fg)
#
# # Marker labelling
# ret, markers = cv2.connectedComponents(sure_fg)
# # Add one to all labels so that sure background is not 0, but 1
# markers = markers+1
# # Now, mark the region of unknown with zero
# markers[unknown==255] = 0
#
# img_multiple = img.copy()
# markers = cv2.watershed(img_multiple,markers)
# img_multiple[markers == -1] = [255,0,0]
#
# # showing images
#
# numpy_horizontal1 = np.hstack((cv2.cvtColor(thresh1, cv2.COLOR_GRAY2BGR), img_contour1, img_circles1))
# # numpy_horizontal = np.hstack((img_contour, cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)))
# # numpy_horizontal1 = np.hstack((img_contour1, img_circles1))
#
# # cv2.imshow("Original", img)
# cv2.imshow("Adaptive Result", numpy_horizontal1)
# # cv2.imshow("Manual Result", img_contour)
# # cv2.imshow("Adaptive Result", img_contour1)
# cv2.imshow("Multiple Object", img_multiple)
# cv2.waitKey(0)
