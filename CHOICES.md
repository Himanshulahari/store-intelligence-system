# CHOICES.md

# Engineering Choices and Rationale

This document explains the major engineering decisions made during the development of the Store Intelligence System.

The objective was to build a solution that is accurate, lightweight, easy to deploy, and aligned with the requirements of the Purplle Tech Challenge 2026.

---

# Choice 1: Detection Model

## Selected

YOLOv8n

## Alternatives Considered

* YOLOv8n
* YOLOv8s
* YOLOv8m

## Reasoning

The challenge requires processing CCTV footage efficiently while maintaining reasonable detection accuracy.

YOLOv8n was selected because:

* Fast inference speed
* Lower memory usage
* Lightweight deployment
* Suitable for CPU execution
* Good person detection performance

Compared to larger YOLO variants, YOLOv8n provides significantly faster execution while maintaining sufficient accuracy for retail analytics.

### Tradeoff

Slightly lower accuracy compared to YOLOv8s and YOLOv8m.

### Final Decision

YOLOv8n provides the best balance between speed and accuracy for this challenge.

---

# Choice 2: Tracking Algorithm

## Selected

ByteTrack

## Alternatives Considered

* Centroid Tracking
* SORT
* ByteTrack

## Reasoning

Retail analytics depends on maintaining consistent visitor identities across frames.

ByteTrack was selected because:

* Better track continuity
* Lower ID switching
* Improved handling of temporary occlusions
* More reliable visitor counting
* Strong performance in crowded environments

### Tradeoff

Slightly higher computational cost than basic tracking methods.

### Final Decision

ByteTrack provides superior tracking quality, making it more suitable for visitor analytics.

---

# Choice 3: API Framework

## Selected

FastAPI

## Alternatives Considered

* Flask
* FastAPI

## Reasoning

The project requires multiple REST APIs and rapid backend development.

FastAPI was selected because:

* Automatic Swagger documentation
* Built-in request validation
* Modern asynchronous support
* Faster development cycle
* Easy API testing

### Tradeoff

Slightly more opinionated than Flask.

### Final Decision

FastAPI improves developer productivity and provides excellent API documentation out of the box.

---

# Choice 4: Database

## Selected

SQLite

## Alternatives Considered

* SQLite
* PostgreSQL
* MySQL

## Reasoning

The challenge solution is intended as a lightweight prototype.

SQLite was selected because:

* No setup required
* Lightweight deployment
* Easy local development
* Simple integration with SQLAlchemy
* Suitable for challenge-scale workloads

### Tradeoff

Not ideal for large-scale production deployments.

### Final Decision

SQLite offers the simplest and most reliable deployment experience for the challenge environment.

---

# Choice 5: Event Storage Format

## Selected

JSONL-Based Event Schema

## Alternatives Considered

* CSV
* Database-only records
* JSONL event streams

## Reasoning

The provided challenge resources include sample event data in JSONL format.

Benefits:

* Human readable
* Easy debugging
* Flexible schema evolution
* Compatible with streaming systems
* Easy API integration

Example:

```json
{
  "event_type": "entry",
  "camera_id": "cam1",
  "event_timestamp": "2026-03-08T18:10:05"
}
```

### Final Decision

JSONL was selected as the canonical event representation.

---

# Choice 6: Event-Driven Architecture

## Selected

Event-Based Processing

## Alternatives Considered

* Direct analytics from video
* Event-driven architecture

## Reasoning

Processing analytics directly from video creates tight coupling between perception and analytics.

Event-driven processing provides:

* Better modularity
* Easier maintenance
* Scalability
* Simpler analytics generation
* Clear separation of responsibilities

### Final Decision

Video processing generates structured events, and analytics operate on those events.

---

# Choice 7: Analytics Design

## Selected

Event-Based Analytics

## Reasoning

Analytics are generated from stored event data instead of raw video streams.

Advantages:

* Faster computation
* Reduced storage requirements
* Simpler query processing
* Easier future expansion

Generated metrics include:

* Total Events
* Occupancy Events
* Visitor Counts
* Conversion Metrics
* Funnel Analytics
* Zone Activity Insights

### Final Decision

Event-based analytics provide a clean and scalable architecture.

---

# AI-Assisted Usage Disclosure

AI tools were used during the design and implementation process to:

* Compare alternative architectures
* Evaluate tracking algorithms
* Evaluate detection model choices
* Review API design approaches
* Generate documentation drafts
* Refine engineering tradeoffs

All final engineering decisions, implementation, testing, integration, and validation were performed manually.

---

# Summary of Final Choices

| Category           | Selected Technology |
| ------------------ | ------------------- |
| Detection Model    | YOLOv8n             |
| Tracking Algorithm | ByteTrack           |
| API Framework      | FastAPI             |
| Database           | SQLite              |
| Event Format       | JSONL               |
| Architecture       | Event-Driven        |
| Video Processing   | OpenCV              |
| ORM                | SQLAlchemy          |
| Testing            | Pytest              |

---

# Conclusion

The selected technologies and design choices prioritize simplicity, performance, maintainability, and ease of deployment while meeting the functional requirements of the Purplle Tech Challenge 2026.

The resulting system demonstrates an end-to-end pipeline for transforming CCTV footage into actionable retail intelligence.
