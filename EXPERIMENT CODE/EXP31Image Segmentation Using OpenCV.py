
import cv2
import numpy as np

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.putText(img, "Input Image", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.putText(thresh, "Segmented Image", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 2)

thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

collage = np.hstack((img, thresh))

cv2.imshow("Image Segmentation", collage)
cv2.waitKey(0)
cv2.destroyAllWindows()
