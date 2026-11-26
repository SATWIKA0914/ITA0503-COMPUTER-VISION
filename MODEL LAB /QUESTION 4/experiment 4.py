
import cv2
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

    rotated = cv2.rotate(
        img, cv2.ROTATE_90_COUNTERCLOCKWISE
    )

    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image - 270 Degrees", rotated)

    output_path = os.path.join(
        os.path.dirname(path), "EXP4_OUTPUT.png"
    )

    cv2.imwrite(output_path, rotated)

    print("IMAGE ROTATED SUCCESSFULLY")
    print("OUTPUT SAVED SUCCESSFULLY")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
