
import cv2
import numpy as np

def remove_background():
    img = cv2.imread(input("Enter image path: "))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 0, 180])
    upper = np.array([180, 50, 255])

    mask = cv2.inRange(hsv, lower, upper)

    result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

    collage = np.hstack((img, result))

    cv2.imshow("Original Image and Background Removed", collage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

remove_background()
