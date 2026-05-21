import cv2
import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pyautogui


def main():
    # Load the hand landmarker model
    base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        num_hands=1,
    )
    detector = vision.HandLandmarker.create_from_options(options)

    def fingerFold(tip,pip):
        return tip.y > pip.y
        # Open webcam

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        result = detector.detect(mp_image)

        if result.hand_landmarks:
            hand = result.hand_landmarks[0]

            indexFold = fingerFold(hand[8], hand[6])
            middleFold = fingerFold(hand[12], hand[10])
            ringFold = fingerFold(hand[16], hand[14])
            pinkyFold = fingerFold(hand[20], hand[18])
            h, w, _ = frame.shape
            for lm in [hand[8], hand[12], hand[16], hand[20]]:
                x = int(lm.x * w)
                y = int(lm.y * h)
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            
            if indexFold and middleFold and ringFold and pinkyFold:
                cv2.putText(frame, "FIST", (50, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
                pyautogui.screenshot("full_screenshot.png")
                

        cv2.imshow("Hand Landmarks", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


def fingerFold(tip,pip):
    return tip.y > pip.y

