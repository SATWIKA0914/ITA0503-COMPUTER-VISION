
import cv2


img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
x = cv2.convertScaleAbs(sobel_x)
y = cv2.convertScaleAbs(sobel_y)
result = cv2.addWeighted(x, 0.5, y, 0.5, 0)
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Filtered Image", result)

cv2.imwrite("sobel_output.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
