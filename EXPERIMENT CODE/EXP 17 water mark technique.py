
import cv2


img = cv2.imread("input.jpg")


overlay = img.copy()


cv2.putText(overlay, "SAMPLE WATERMARK", (250, 380),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0, 0, 255), 3, cv2.LINE_AA)


result = cv2.addWeighted(overlay, 0.35, img, 0.65, 0)


cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", result)


cv2.imwrite("watermark_output.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
