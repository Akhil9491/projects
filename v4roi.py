import cv2

# Load YOLOv4 model
net = cv2.dnn.readNetFromDarknet("yolov4.cfg", "yolov4.weights")

# Set backend and target to use OpenCV's CUDA implementation for GPU acceleration (optional)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
# Define ROI
roi_x, roi_y, roi_w, roi_h = 200, 100, 400, 400  # example values

# Create a mask for the ROI
mask = np.zeros((frame_height, frame_width), dtype=np.uint8)
mask[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w] = 255
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Apply the mask to the frame to get only the ROI
    roi_frame = cv2.bitwise_and(frame, frame, mask=mask)

    # Run object detection on the ROI frame
    blob = cv2.dnn.blobFromImage(roi_frame, 1 / 255, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(net.getUnconnectedOutLayersNames())

    # Extract detections from the YOLOv4 model output
    detections = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold:
                center_x, center_y, w, h = (detection[0:4] * np.array([roi_w, roi_h, roi_w, roi_h])).astype(np.int)
                x, y = center_x - w // 2, center_y - h // 2
                detections.append((x, y, w, h))

    # Track objects in the ROI
    tracker.update(detections)

    # Draw bounding boxes around tracked objects
    for track in tracker.tracks:
        if not track.is_confirmed() or track.time_since_update > max_age:
            continue
        x, y, w, h = track.to_tlbr().astype(np.int)
        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Object Tracking", frame)
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
