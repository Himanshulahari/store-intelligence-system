# Store Intelligence System

## Overview

This project is an AI-powered Store Intelligence System built for the Purplle Tech Challenge 2026.

The system analyzes CCTV footage from multiple cameras to detect people, track visitors, estimate occupancy, and generate store events in real time.

---

## Features

* Multi-camera CCTV processing
* Person detection using YOLOv8
* Visitor tracking using ByteTrack
* Live occupancy counting
* Unique visitor estimation
* Event ingestion through FastAPI
* SQLite database storage
* Analytics API endpoints

---

## Tech Stack

* Python
* YOLOv8
* ByteTrack
* OpenCV
* FastAPI
* SQLite
* SQLAlchemy

---

## Architecture

CCTV Cameras (CAM1–CAM5)
↓
YOLOv8 Detection
↓
ByteTrack Tracking
↓
Occupancy Engine
↓
FastAPI API Layer
↓
SQLite Database
↓
Analytics Endpoints

---

## API Endpoints

### Health Check

GET /health

### Ingest Event

POST /events/ingest

### Get Events

GET /events

---

## Camera Mapping

| Camera | Purpose                    |
| ------ | -------------------------- |
| CAM1   | Product Zone Monitoring    |
| CAM2   | Product Zone Monitoring    |
| CAM3   | Entrance Monitoring        |
| CAM4   | Staff / Inventory Area     |
| CAM5   | Billing / Store Operations |

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Start API:

uvicorn app.main:app --reload

Run Detection Pipeline:

python pipeline/detect.py

---

## Future Improvements

* Dwell Time Analytics
* Heatmaps
* Queue Detection
* Re-identification across cameras
* Live Dashboard
* Anomaly Detection

## Screenshots

### Dashboard
![Dashboard](screenshots/dashboard.png)

### API Documentation
![Docs](screenshots/docs.png)

### Events API
![Events](screenshots/events.png)

### Analytics API
![Analytics](screenshots/analytics.png)