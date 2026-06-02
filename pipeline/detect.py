from ultralytics import YOLO
import supervision as sv
import cv2
import requests
from datetime import datetime
import uuid

camera_name = "CAM4"

model = YOLO("yolov8n.pt")

tracker = sv.ByteTrack()

box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

cap = cv2.VideoCapture(f"data/{camera_name}.mp4")

previous_count = -1
unique_visitors = set()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame, conf=0.5)[0]

    detections = sv.Detections.from_ultralytics(results)

    detections = tracker.update_with_detections(detections)

    for tracker_id in detections.tracker_id:
        unique_visitors.add(int(tracker_id))

    count = len(detections)

    if count != previous_count:

        requests.post(
            "http://127.0.0.1:8000/events/ingest",
            json={
                "event_id": str(uuid.uuid4()),
                "store_id": "store_1",
                "visitor_id": f"visitor_{count}",
                "event_type": "occupancy",
                "timestamp": datetime.now().isoformat(),
                "zone_id": camera_name,
                "confidence": 0.95,
                "is_staff": False
            }
        )

        previous_count = count

    cv2.putText(
        frame,
        f"People Count: {count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Total Visitors: {len(unique_visitors)}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        f"Camera: {camera_name}",
        (20, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    print("Tracker IDs:", detections.tracker_id)

    labels = [
        f"ID {tracker_id}"
        for tracker_id in detections.tracker_id
    ]

    frame = box_annotator.annotate(
        scene=frame,
        detections=detections
    )

    frame = label_annotator.annotate(
        scene=frame,
        detections=detections,
        labels=labels
    )

    cv2.imshow("Store Intelligence Dashboard", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()