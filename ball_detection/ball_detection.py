import cv2
import numpy as np

def nothing(x):
    pass

# Load img
video = cv2.VideoCapture('Data/video.avi')

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

    ret, img = video.read()
    dimensions = img.shape
    # print("Image Size:" + str(dimensions))
    height = dimensions[0]
    width = dimensions[1]

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    # Print if there is a change in HSV value
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax, vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    # hough circles
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 80, param1=50, param2=20, minRadius=10, maxRadius=25)
    if circles is not None:
        circles = np.uint16(np.around(circles))
    img_circles = result.copy()

    close_range = 20
    centre_width = int(width/2)

    cv2.line(img_circles, (centre_width, 0), (centre_width, height), (255, 0, 0), 2)
    cv2.line(img_circles, (centre_width, centre_width-close_range), (centre_width, height), (0, 0, 255), 2)

    if circles is not None:
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(img_circles, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(img_circles, (i[0], i[1]), 2, (0, 0, 255), 3)
            distance = i[0]-centre_width
            print(distance)

    # Display result image
    cv2.imshow('image', img)
    cv2.imshow('result', img_circles)

    # Press Q on keyboard to stop recording
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# img = cv2.imread('group 4/frame000002.png')
# dimensions = img.shape
# print("Image Size:" + str(dimensions))
#
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower = np.array([0, 0, 0])
# upper = np.array([179, 57, 137])
# mask = cv2.inRange(hsv, lower, upper)
# result = cv2.bitwise_and(img, img, mask=mask)
#
# cv2.imshow("Mask Result", result)
#
# gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
#
# # hough circles
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 80, param1=50, param2=20, minRadius=10, maxRadius=25)
# if circles is not None:
#     circles = np.uint16(np.around(circles))
# img_circles = img.copy()
#
# if circles is not None:
#     for i in circles[0, :]:
#         # draw the outer circle
#         cv2.circle(img_circles, (i[0], i[1]), i[2], (0, 255, 0), 2)
#         # draw the center of the circle
#         cv2.circle(img_circles, (i[0], i[1]), 2, (0, 0, 255), 3)
#
# # showing images
# # cv2.imshow("Original", img)
# cv2.imshow("Hough Circle Result", img_circles)
# cv2.waitKey(0)
