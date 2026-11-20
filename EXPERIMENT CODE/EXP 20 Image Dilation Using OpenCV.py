
import cv2
import numpy as np

img = cv2.imread("input.jpg")

kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.putText(img, "Input Image", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.putText(dilation, "Dilated Image", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

collage = np.hstack((img, dilation))

cv2.imshow("Dilation - Input and Output", collage)
cv2.waitKey(0)
cv2.destroyAllWindows()
