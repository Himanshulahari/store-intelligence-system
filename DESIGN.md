# DESIGN.md

# Store Intelligence System – Design Decisions

## Overview

The Store Intelligence System is designed to transform CCTV video streams into structured retail intelligence events and analytics.

The solution combines computer vision, object tracking, event generation, API services, and analytics modules to monitor customer activity across retail stores.

The architecture emphasizes:

* Simplicity
* Real-time processing
* Modularity
* Scalability
* Ease of deployment

---

# System Architecture

```text
Store Cameras
      │
      ▼
YOLOv8 Detection
      │
      ▼
ByteTrack Tracking
      │
      ▼
Event Generation Layer
      │
      ▼
FastAPI Backend
      │
      ▼
SQLite Storage
      │
      ▼
Analytics Engine
      │
      ▼
REST APIs
```

---

# AI-Assisted Design Decisions

The following engineering decisions were made with the assistance of AI-based research, comparison, and architectural exploration.

---

## Decision 1: YOLOv8n vs YOLOv8s

### Alternatives Considered

* YOLOv8n
* YOLOv8s

### Selected

**YOLOv8n**

### Reasoning

YOLOv8n was selected because the challenge focuses on real-time CCTV analytics rather than maximum detection accuracy.

Compared to YOLOv8s:

Advantages:

* Faster inference speed
* Lower memory consumption
* Better CPU performance
* Easier deployment on commodity hardware
* Sufficient accuracy for person detection

Tradeoff:

* Slightly lower detection accuracy than YOLOv8s

Decision:

The performance gain outweighed the small accuracy loss, making YOLOv8n the preferred choice.

---

## Decision 2: ByteTrack vs SORT

### Alternatives Considered

* SORT
* ByteTrack

### Selected

**ByteTrack**

### Reasoning

Retail analytics depends heavily on maintaining stable visitor identities across frames.

Compared to SORT:

Advantages:

* Better track continuity
* More robust under temporary occlusions
* Lower ID switching
* Higher tracking stability
* Better performance in crowded scenes

Tradeoff:

* Slightly higher computational overhead

Decision:

Because visitor counting accuracy is more important than minimal computational savings, ByteTrack was selected.

---

## Decision 3: FastAPI vs Flask

### Alternatives Considered

* Flask
* FastAPI

### Selected

**FastAPI**

### Reasoning

The challenge requires multiple APIs and clear documentation.

Advantages:

* Automatic OpenAPI documentation
* Built-in request validation
* Better developer productivity
* Faster development cycle
* Modern Python ecosystem

Tradeoff:

* Slightly steeper learning curve

Decision:

FastAPI significantly reduces backend development effort and improves maintainability.

---

## Decision 4: SQLite vs PostgreSQL

### Alternatives Considered

* SQLite
* PostgreSQL

### Selected

**SQLite**

### Reasoning

The project is designed as a challenge submission and local prototype.

Advantages:

* Zero configuration
* Lightweight deployment
* No external services required
* Easy testing and debugging

Tradeoff:

* Not suitable for large-scale production workloads

Decision:

SQLite provides the fastest and simplest deployment path for the challenge environment.

---

## Decision 5: Event-Based Architecture

### Design Choice

Instead of directly storing video analytics results, the system generates structured events.

Examples:

```json
{
  "event_type": "entry"
}
```

```json
{
  "event_type": "zone_entered"
}
```

```json
{
  "event_type": "queue_completed"
}
```

### Reasoning

Benefits:

* Decouples analytics from video processing
* Easier data storage
* Easier API integration
* Better scalability
* Enables future streaming architectures

Decision:

An event-driven architecture was selected to separate perception from analytics.

---

## Decision 6: JSONL Event Schema Design

### Alternatives Considered

* Relational-only storage
* CSV-based storage
* JSONL event streams

### Selected

**JSONL Event Schema**

### Reasoning

The challenge dataset already includes sample events in JSONL format.

Advantages:

* Human readable
* Easy debugging
* Compatible with event streaming systems
* Supports schema evolution
* Easy integration with APIs

Example:

```json
{
  "event_type": "entry",
  "camera_id": "cam1",
  "event_timestamp": "2026-03-08T18:10:05"
}
```

Decision:

JSONL was selected as the canonical event representation.

---

# Event Pipeline Design

The event pipeline converts raw video streams into structured events.

### Step 1

Video frames are captured using OpenCV.

### Step 2

YOLOv8 detects customers.

### Step 3

ByteTrack assigns tracking IDs.

### Step 4

Business events are generated.

Examples:

* Entry Events
* Zone Events
* Billing Events

### Step 5

Events are sent to FastAPI.

### Step 6

Events are stored in SQLite.

### Step 7

Analytics endpoints aggregate insights.

---

# Analytics Design

The analytics layer operates on stored events rather than raw video.

Generated metrics include:

* Total Events
* Occupancy Events
* Visitor Counts
* Store Coverage
* Funnel Metrics
* Conversion Metrics
* Zone Activity

Benefits:

* Faster analytics queries
* Lower computational cost
* Separation of concerns
* Easier future expansion

---

# Scalability Considerations

The architecture allows future migration to:

* PostgreSQL
* Kafka
* Redis
* Cloud Storage
* Real-Time Dashboards
* Distributed Processing

Because detection, tracking, storage, and analytics are separated into independent modules, each component can scale independently.

---

# Limitations

Current limitations include:

* No cross-camera re-identification
* No customer face recognition
* No heatmap generation
* No real-time dashboard deployment
* Analytics limited to generated events

These limitations were accepted to prioritize a reliable and maintainable MVP for the challenge.

---

# Conclusion

The Store Intelligence System uses a modular event-driven architecture to convert CCTV footage into actionable retail intelligence.

The chosen technologies—YOLOv8n, ByteTrack, FastAPI, SQLite, and JSONL-based events—provide a balance between performance, simplicity, and scalability while satisfying the challenge requirements.
