import cv2

face = cv2.imread("faces/5.jpg")
gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)


for (x, y, w, h) in faces:
    roi = gray[y:y+h, x:x+w]
    edges = cv2.Canny(roi, 100, 200)
    height, width = roi.shape
    left_half = roi[0:height, 0:int(width/2)]
    right_half = roi[0:height, int(width/2):width]

    left_mean = cv2.mean(left_half)
    right_mean = cv2.mean(right_half)
    asymmetry = abs(left_mean[0] - right_mean[0])
    cv2.rectangle(face, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(face, f"Asymmetry: {asymmetry:.2f}", (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
cv2.imwrite('faces/out/55.jpg', face)
cv2.waitKey(0)
