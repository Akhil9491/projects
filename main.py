import cv2

cap = cv2.VideoCapture("/home/pi/vidl.mp4")
ret, frame = cap.read()

frame = cv2.resize(frame, (640, 480))
roi = cv2.selectROI(frame)

while True:

ret, frame = cap.read()

frame = cv2.resize(frame, (640, 480))

cv2.imshow("FRAME", frame)

if cv2.waitKey(1)60xFF == 27:
    break

cap.release()

cv2.dest
royAL
Windows()
