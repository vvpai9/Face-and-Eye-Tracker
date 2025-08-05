import cv2
import time

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

eyes_closed = False
start_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Blue bounding box for face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) == 0:
            # Eyes are closed
            if not eyes_closed:
                eyes_closed = True
                start_time = time.time()

            elapsed = time.time() - start_time
            cv2.putText(frame, "Eyes Closed", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            if elapsed >= 3:
                cv2.putText(frame, "WARNING: Eyes Closed Too Long!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        else:
            # Eyes are open
            for (ex, ey, ew, eh) in eyes:
                # Green bounding box for open eyes
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            if eyes_closed:
                eyes_closed = False
                closed_duration = time.time() - start_time
                if closed_duration > 1:
                    print(f"Eyes were closed for {closed_duration:.2f} seconds")

    cv2.imshow('Face & Eye Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
