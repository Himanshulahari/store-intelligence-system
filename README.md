# Store Intelligence System

## Overview

Store Intelligence System is an AI-powered retail analytics platform developed for the **Purplle Tech Challenge 2026**.

The system processes CCTV video streams from retail stores and converts them into structured events and actionable insights. Using computer vision and tracking techniques, the platform monitors customer movement, visitor activity, occupancy, and conversion-related events.

The generated events are stored and exposed through REST APIs for analytics and operational monitoring.

---

# Problem Statement

Retail stores generate large amounts of CCTV footage that are difficult to analyze manually.

The objective of this project is to transform raw CCTV streams into structured retail intelligence by:

* Detecting customers in video feeds
* Tracking customer movement
* Generating store events
* Monitoring occupancy
* Tracking store entries
* Monitoring billing activity
* Producing analytics through APIs

The system converts video streams into meaningful business intelligence for retail operations.

---

# Key Objectives

* Monitor customer activity across multiple store cameras
* Generate real-time visitor events
* Estimate occupancy and customer traffic
* Track unique visitors using object tracking
* Build conversion funnel analytics
* Detect operational anomalies
* Provide API-based access to store insights

---

# Features

## Computer Vision Pipeline

* Person Detection using YOLOv8
* Multi-Object Tracking using ByteTrack
* Real-Time CCTV Processing
* Unique Visitor Estimation
* Entry Monitoring
* Zone Monitoring
* Billing Area Monitoring

## Analytics Engine

* Occupancy Tracking
* Visitor Analytics
* Conversion Funnel Analysis
* Event Aggregation
* Store-Level Analytics
* Anomaly Detection

## Backend Services

* FastAPI REST APIs
* SQLite Event Storage
* Event Ingestion APIs
* Analytics APIs
* Health Monitoring Endpoint

---

# Tech Stack

| Component        | Technology |
| ---------------- | ---------- |
| Language         | Python     |
| Object Detection | YOLOv8     |
| Tracking         | ByteTrack  |
| Video Processing | OpenCV     |
| API Framework    | FastAPI    |
| Database         | SQLite     |
| ORM              | SQLAlchemy |
| Testing          | Pytest     |
| Containerization | Docker     |

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
FastAPI Ingestion API
      │
      ▼
SQLite Event Storage
      │
      ▼
Analytics Engine
      │
      ▼
REST API Endpoints
```

---

# Dataset Description

The challenge dataset contains multiple store layouts and camera feeds.

```text
data/
├── store1/
│   ├── CAM 1 - zone.mp4
│   ├── CAM 2 - zone.mp4
│   ├── CAM 3 - entry.mp4
│   ├── CAM 5 - billing.mp4
│   └── Store 1 - layout.png
│
├── store2/
│   ├── entry1.mp4
│   ├── entry2.mp4
│   ├── zone.mp4
│   ├── billing_area.mp4
│   └── store 2 - layout.png
│
├── pos_transactions.csv
└── sample_events.jsonl
```

### Camera Types

| Camera Type    | Purpose                      |
| -------------- | ---------------------------- |
| Entry Camera   | Customer entry monitoring    |
| Zone Camera    | Customer movement monitoring |
| Billing Camera | Conversion monitoring        |
| Layout Images  | Store layout reference       |

---

# Event Schema

The system generates structured retail events based on camera type and visitor activity.

## Supported Event Types

| Event Type | Description |
|------------|-------------|
| entry | Customer detected entering the store |
| zone_entered | Customer detected inside a monitored zone |
| queue_completed | Customer detected at billing / checkout area |

## Sample Event

```json
{
  "event_id": "evt_001",
  "event_type": "entry",
  "visitor_id": "visitor_12",
  "camera_id": "CAM 3 - entry",
  "event_timestamp": "2026-06-03T20:30:00"
}
```

---

# Assumptions

The following assumptions were used while building the solution:

1. Each camera stream belongs to a predefined store area.
2. YOLOv8 person detections represent customer candidates.
3. ByteTrack IDs are used as temporary visitor identifiers.
4. Entry cameras represent ingress points.
5. Billing cameras represent conversion events.
6. Layout images are reserved for future heatmap analytics.
7. Events are stored locally using SQLite.
8. Cross-camera re-identification is not implemented in the current version.

---

# Project Structure

```text
Store_Intelligence_Challenge/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
│   ├── metrics.py
│   ├── funnel.py
│   ├── anomalies.py
│   ├── ingestion.py
│   └── health.py
│
├── pipeline/
│   ├── detect.py
│   ├── tracker.py
│   ├── emit.py
│   ├── run.sh
│   └── screenshots/
│
├── tests/
│   ├── test_home.py
│   ├── test_health.py
│   ├── test_analytics.py
│   └── test_emit.py
│
├── data/
├── output/
│   └── events.jsonl
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── yolov8n.pt
```

---

# API Endpoints

## Home

```http
GET /
```

Returns API status information.

---

## Health Check

```http
GET /health
```

Returns application health status.

---

## Ingest Event

```http
POST /events/ingest
```

Stores generated events in the database.

---

## Get Events

```http
GET /events
```

Returns all stored events.

---

## Analytics

```http
GET /analytics
```

Returns aggregated analytics metrics.

---

# Analytics Generated

The system generates:

* Total Events
* Occupancy Events
* Store Coverage
* Visitor Counts
* Conversion Metrics
* Funnel Statistics
* Zone Activity Insights

---

# Sample Analytics Output

```json
{
  "total_events": 1245,
  "occupancy_events": 1172,
  "stores_monitored": 2
}
```

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/Himanshulahari/store-intelligence-system.git
cd Store_Intelligence_Challenge
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project Locally

## Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# How to Process Videos

Run the detection pipeline:

```bash
python pipeline/detect.py
```

Inside `detect.py`, configure the desired video:

```python
VIDEO_PATH = "data/store1/CAM 3 - entry.mp4"
```

Examples:

### Store 1 Entry Camera

```python
VIDEO_PATH = "data/store1/CAM 3 - entry.mp4"
```

### Store 1 Billing Camera

```python
VIDEO_PATH = "data/store1/CAM 5 - billing.mp4"
```

### Store 2 Entry Camera

```python
VIDEO_PATH = "data/store2/entry1.mp4"
```

### Store 2 Zone Camera

```python
VIDEO_PATH = "data/store2/zone.mp4"
```

The pipeline automatically:

* Detects people
* Tracks visitors
* Generates structured events
* Stores events in SQLite
* Writes generated events to:

```text
output/events.jsonl

---

# Running Tests

```bash
python -m pytest -v
```

Current test coverage includes:

* Home Endpoint
* Health Endpoint
* Analytics Endpoint
* Event Generation Logic

---

# Running with Docker

## Build Docker Image

```bash
docker build -t store-intelligence .
```

## Run Container

```bash
docker run -p 8000:8000 store-intelligence
```

## Docker Compose

```bash
docker-compose up --build
```

---

# Results

The system successfully:

* Detects customers from CCTV feeds
* Tracks visitors using ByteTrack
* Generates structured retail events
* Stores events in SQLite
* Produces JSONL event logs (`output/events.jsonl`)
* Exposes analytics through FastAPI APIs
* Provides real-time monitoring dashboards

---

# Future Enhancements

* Customer Journey Analytics
* Queue Length Estimation
* Heatmap Generation
* Cross-Camera Re-Identification
* Dwell Time Analytics
* Real-Time Dashboard
* Alerting and Notifications
* Advanced Anomaly Detection

---

# Screenshots

## Detection Dashboard

![Dashboard](pipeline/screenshots/dashboard.png)

## API Documentation

![Docs](pipeline/screenshots/docs.png)

## Events API

![Events](pipeline/screenshots/events.png)

## Analytics API

![Analytics](pipeline/screenshots/analytics.png)

---

# Challenge Submission

Developed for the **Purplle Tech Challenge 2026** to demonstrate how computer vision and analytics can transform retail CCTV footage into actionable store intelligence.
