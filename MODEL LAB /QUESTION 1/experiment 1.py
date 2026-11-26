
import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg *.png *.jpeg")]
)
root.destroy()

img = cv2.imread(path)

if img is None:
    print("IMAGE NOT FOUND")
else:
    print("IMAGE LOADED SUCCESSFULLY")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.cornerHarris(gray, 2, 3, 0.04)
    corners = cv2.dilate(corners, None)

    img[corners > 0.01 * corners.max()] = [0, 0, 255]

    print("CORNERS DETECTED SUCCESSFULLY")

    cv2.namedWindow("Harris Corner Detection",
                    cv2.WINDOW_NORMAL)

    cv2.imshow("Harris Corner Detection", img)

    print("OUTPUT WINDOW OPENED")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
