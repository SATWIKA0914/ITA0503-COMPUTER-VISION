
import cv2
import pytesseract

def extract_text():
    path = input("Enter video path: ")
    cap = cv2.VideoCapture(path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        text = pytesseract.image_to_string(frame)

        if text.strip():
            print("Extracted Text:", text)

        cv2.imshow("Video", frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

extract_text()
