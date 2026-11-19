
import cv2

img = cv2.imread("input.jpg")


roi = img[50:250, 50:250]


copy = roi.copy()

img[250:450, 300:500] = copy


cv2.imshow("Original Image", cv2.imread("input.jpg"))
cv2.imshow("ROI Output", img)

cv2.imwrite("roi_output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
