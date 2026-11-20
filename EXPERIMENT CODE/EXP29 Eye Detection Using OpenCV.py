
import cv2

img = cv2.imread("eye.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.putText(img, "Eyes Detected: " + str(len(eyes)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.imshow("Eye Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
