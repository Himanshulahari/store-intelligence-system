def detect_anomalies(events):

    queue_events = 0

    for event in events:

        if event.get("event_type") in [
            "queue_completed",
            "queue_abandoned"
        ]:
            queue_events += 1

    if queue_events > 20:
        return {
            "anomaly": "BILLING_QUEUE_SPIKE"
        }

    return {
        "anomaly": None
    }