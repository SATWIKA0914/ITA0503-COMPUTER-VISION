
import cv2
import numpy as np

img = cv2.imread("input.jpg")

kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.putText(img, "Input Image", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.putText(opening, "Opening Image", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

collage = np.hstack((img, opening))

cv2.imshow("Morphological Opening", collage)
cv2.waitKey(0)
cv2.destroyAllWindows()
