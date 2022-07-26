import numpy as np
import cv2

img = cv2.imread('Resources/shapes.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 200, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Here,Igave input as a sides of a geometric shape
g=int(input("Enter Shape:"))

cv2.imshow("img", img)
i=0
for contour in contours:
    if i == 0:
        i = 1
        continue
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    
    if (len(approx) == g):
        cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)
    elif len(approx)>8 and g>8:
        cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)
cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()