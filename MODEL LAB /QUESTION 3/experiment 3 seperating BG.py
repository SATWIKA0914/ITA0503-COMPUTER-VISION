
import cv2
import numpy as np
from tkinter import Tk, filedialog
import os

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Input Image",
    filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
)

root.destroy()

img = cv2.imread(path)

if img is None:
    print("IMAGE NOT FOUND")
else:
    print("IMAGE LOADED SUCCESSFULLY")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    foreground_mask = cv2.bitwise_not(mask)

    result = cv2.bitwise_and(
        img, img, mask=foreground_mask
    )

    cv2.imshow("Original Image", img)
    cv2.imshow("Background Mask", mask)
    cv2.imshow("Foreground Output", result)

    output_path = os.path.join(
        os.path.dirname(path), "EXP3_OUTPUT.png"
    )

    cv2.imwrite(output_path, result)

    print("BACKGROUND REMOVED SUCCESSFULLY")
    print("OUTPUT SAVED SUCCESSFULLY")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
