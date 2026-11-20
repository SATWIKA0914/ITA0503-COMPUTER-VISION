
import cv2

img = cv2.imread("smile.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)

for (x, y, w, h) in smiles:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(img, "Smile", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.putText(img, "Smiles Detected: " + str(len(smiles)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.imshow("Smile Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
