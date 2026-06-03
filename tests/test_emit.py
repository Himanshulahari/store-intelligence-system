from pipeline.emit import create_entry_event

def test_create_entry_event():
    event = create_entry_event(
        track_id=1,
        camera_id="CAM1"
    )

    assert event["event_type"] == "entry"
    assert event["camera_id"] == "CAM1"