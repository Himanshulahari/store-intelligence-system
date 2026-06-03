import json


def load_events(file_path):
    events = []

    with open(file_path, "r") as f:
        for line in f:
            events.append(json.loads(line))

    return events