from datetime import datetime
import uuid


def create_entry_event(track_id, camera_id):

    return {
        "event_id": str(uuid.uuid4()),
        "event_type": "entry",
        "visitor_id": f"visitor_{track_id}",
        "camera_id": camera_id,
        "event_timestamp": datetime.now().isoformat(),
        "is_staff": False
    }


def create_zone_event(track_id, zone_id, camera_id):

    return {
        "event_id": str(uuid.uuid4()),
        "event_type": "zone_entered",
        "visitor_id": f"visitor_{track_id}",
        "zone_id": zone_id,
        "camera_id": camera_id,
        "event_timestamp": datetime.now().isoformat()
    }


def create_queue_event(track_id, camera_id):

    return {
        "event_id": str(uuid.uuid4()),
        "event_type": "queue_completed",
        "visitor_id": f"visitor_{track_id}",
        "camera_id": camera_id,
        "event_timestamp": datetime.now().isoformat()
    }