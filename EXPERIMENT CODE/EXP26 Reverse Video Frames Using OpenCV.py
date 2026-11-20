
import cv2

def reverse_video(input_file, output_file):
    cap = cv2.VideoCapture(input_file)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    if not frames:
        return

    height, width, _ = frames[0].shape
    fps = 30

    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for frame in reversed(frames):
        out.write(frame)

    out.release()

reverse_video("input.mp4", "reverse.mp4")
