import cv2

# Open the video stream
cap = cv2.VideoCapture(0)

# Define bounding box coordinates
x, y, w, h = 250, 100, 200, 250

while True:
    # Read the next frame from the video stream
    ret, frame = cap.read()

    # Extract region of interest using bounding box coordinates
    roi = frame[y:y+h, x:x+w]

    # Display the ROI
    cv2.imshow('ROI', roi)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()