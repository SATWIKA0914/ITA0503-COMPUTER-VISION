
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

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    kernel = np.ones((5, 5), np.uint8)

    closing = cv2.morphologyEx(
        binary, cv2.MORPH_CLOSE, kernel
    )

    cv2.imshow("Original Image", img)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Morphological Closing", closing)

    output_path = os.path.join(
        os.path.dirname(path), "EXP2_OUTPUT.png"
    )

    cv2.imwrite(output_path, closing)

    print("MORPHOLOGICAL CLOSING COMPLETED")
    print("OUTPUT SAVED SUCCESSFULLY")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
