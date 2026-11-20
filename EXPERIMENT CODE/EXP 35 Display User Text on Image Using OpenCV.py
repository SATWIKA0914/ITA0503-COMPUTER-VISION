
import cv2
import numpy as np

def create_text():
    h = int(input("Enter image height: "))
    w = int(input("Enter image width: "))
    text = input("Enter text: ")

    img = np.ones((h, w, 3), dtype=np.uint8) * 255

    cv2.putText(img, text, (50, h//2),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 255), 2)

    cv2.imshow("Text on Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_text()
