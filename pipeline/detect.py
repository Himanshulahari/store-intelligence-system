from ultralytics import YOLO
import supervision as sv
import cv2
import requests
from datetime import datetime
import uuid
from emit import (
    create_entry_event,
    create_zone_event,
    create_queue_event
)

VIDEO_PATH = "data/store1/CAM 5 - billing.mp4"
CAMERA_NAME = "CAM 5 - billing"

video_name = VIDEO_PATH.lower()

if "entry" in video_name:
    CAMERA_TYPE = "entry"

elif "billing" in video_name:
    CAMERA_TYPE = "billing"

else:
    CAMERA_TYPE = "zone"

model = YOLO("yolov8n.pt")

tracker = sv.ByteTrack()

box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

cap = cv2.VideoCapture(VIDEO_PATH)

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

        if CAMERA_TYPE == "entry":

            event = create_entry_event(
                count,
                CAMERA_NAME
            )

        elif CAMERA_TYPE == "billing":

            event = create_queue_event(
                count,
                CAMERA_NAME
            )

        else:

            event = create_zone_event(
                count,
                "ZONE_01",
                CAMERA_NAME
            )

        requests.post(
            "http://127.0.0.1:8000/events/ingest",
            json=event
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
        f"Camera: {CAMERA_NAME}",
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