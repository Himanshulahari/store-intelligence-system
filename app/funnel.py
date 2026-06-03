def calculate_funnel(events):

    entries = 0
    billing = 0

    for event in events:

        if event.get("event_type") == "entry":
            entries += 1

        if event.get("event_type") in [
            "queue_completed"
        ]:
            billing += 1

    conversion_rate = 0

    if entries > 0:
        conversion_rate = round(
            billing / entries * 100,
            2
        )

    return {
        "entries": entries,
        "billing": billing,
        "conversion_rate": conversion_rate
    }