# DESIGN.md

# Store Intelligence System Design

## Overview

This project processes CCTV footage from retail stores and generates business intelligence metrics such as:

* Store Occupancy
* Unique Visitors
* Entry / Exit Counts
* Visitor Funnel Metrics
* Anomaly Detection

## Architecture

CCTV Video
↓
YOLOv8 Person Detection
↓
ByteTrack Multi Object Tracking
↓
Event Generation
↓
SQLite Database
↓
FastAPI Backend
↓
Analytics APIs & Dashboard

## Components

### Detection Pipeline

* YOLOv8 for person detection
* ByteTrack for visitor tracking
* Entry/Exit counting using line crossing
* Occupancy monitoring

### Event Storage

* Events stored in SQLite database
* Structured event schema

### Backend APIs

* Metrics API
* Events API
* Analytics API
* Funnel API

## Assumptions

* One tracker ID represents one visitor.
* Staff and customers are treated similarly in MVP version.
* Camera placement is fixed.

## Limitations

* Accuracy depends on camera angle.
* Heavy occlusion may affect tracking.
* Entry/Exit counting uses a virtual line approach.
