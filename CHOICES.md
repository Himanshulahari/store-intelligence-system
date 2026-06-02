# CHOICES.md

# Engineering Decisions and Tradeoffs

## Why YOLOv8?

YOLOv8 was selected because:

* Fast inference speed
* Good person detection performance
* Easy integration
* Suitable for real-time applications

## Why ByteTrack?

ByteTrack was selected because:

* Maintains consistent IDs
* Handles temporary missed detections
* Lightweight and reliable

## Why SQLite?

SQLite was selected because:

* Simple setup
* No external database required
* Sufficient for MVP scale

## Why Event-Based Architecture?

Generating events provides:

* Better analytics
* Historical tracking
* Easy metric computation

## Tradeoffs

### Accuracy vs Simplicity

A lightweight solution was preferred over a highly complex system to ensure reliability and maintainability.

### Entry/Exit Counting

Virtual line crossing was implemented as a practical approach. More advanced zone-based tracking could further improve accuracy.

### Re-Entry Handling

Unique tracker IDs reduce duplicate counting, though perfect re-identification is outside the scope of this MVP.

## Future Improvements

* Multi-camera tracking
* Staff identification
* Customer journey analysis
* Heatmaps
* Advanced anomaly detection
