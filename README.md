# AI-driven-system-for-patrolling-and-bandobast-automation

# Overview

CopMap AI is an AI-powered system designed to assist police operations such as patrolling, bandobast (crowd control), and checkpoint monitoring. The system uses computer vision and machine learning models to analyze camera feeds, detect crowd density, identify suspicious activity, and generate automated alerts and intelligence summaries.

This project demonstrates how AI can support police officers by providing real-time insights from surveillance data.

# Problem Understanding

Police departments monitor large areas using CCTV cameras. Manual monitoring is inefficient and prone to human error. AI systems can assist by automatically detecting:
Crowd density changes
Suspicious objects
Potential security threats
Abnormal activity patterns
The goal is not to replace officers, but to assist them with real-time intelligence.


# AI can support police operations in:

Patrolling

Monitoring CCTV feeds

Detecting unusual crowd behavior

Alerting officers to suspicious activities

Bandobast (Crowd Control)

Crowd density estimation

Detecting sudden crowd build-ups

Identifying potential stampede risks

Nakabandi (Checkpoint Monitoring)

Vehicle detection

Object detection

Suspicious behavior detection

# Risks of False Positives

AI systems can sometimes produce incorrect alerts.

Possible issues:

Misidentifying objects

Incorrect crowd estimates

Environmental noise in camera feeds

Mitigation strategies:

Human verification

Confidence thresholds

Multi-camera validation

Continuous model improvement

# System Architecture

Camera Feed

↓

YOLO Object Detection

↓

Crowd Density Analysis

↓

Suspicious Activity Detection

↓

Alert Engine

↓

FastAPI Backend

↓

RAG Intelligence Engine

↓

CopMap Dashboard / Police System


# Tech Stack

Python

FastAPI

YOLOv8 (Ultralytics)

OpenCV

Transformers (HuggingFace)

Sentence Transformers

Vector Database (ChromaDB / FAISS)


# Assignment_Copmap
│
main.py

crowd_analysis.py

alert_engine.py

rag_summary.py

requirements.txt

README.md

# Testing the System

Open /docs

Select POST /analyze

Upload an image

Execute
# Example
{
  "detections": ["person", "person", "backpack"],
  
  "crowd_analysis": {
  
    "people_count": 2,
    
    "density": "LOW"
    
  },
  
  "alerts": []
}
## Author

# Pradnya Devendra Ukey
# IIT Kharagpur
