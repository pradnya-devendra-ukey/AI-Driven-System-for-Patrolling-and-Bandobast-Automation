from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import shutil

app = FastAPI()

model = YOLO('yolov8n.pt')

@app.get('/')
def home():
    return {'message':'CopMap AI server running'}

@app.post('/analyze')
async def analyze(file: UploadFile = File(...)):
    path = f'temp_{file.filename}'

    with open(path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = model(path)

    detections = []
    for r in results:
        for box in r.boxes:
            label = r.names[int(box.cls)]
            detections.append(label)

    return {'detected_objects': detections, 'total_objects': len(detections)}
