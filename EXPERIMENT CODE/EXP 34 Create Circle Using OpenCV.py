
import cv2
import numpy as np

def create_circle():
    h = int(input("Enter height: "))
    w = int(input("Enter width: "))

    img = np.ones((h, w, 3), dtype=np.uint8) * 255
    output = img.copy()

    cv2.circle(output, (w//2, h//2), min(h,w)//4, (0,0,255), 3)

    cv2.putText(img, "INPUT", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)
    cv2.putText(output, "OUTPUT", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2)

    collage = np.hstack((img, output))
    cv2.imshow("Input and Output", collage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_circle()
