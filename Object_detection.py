from ultralytics import YOLO

class ObjectDetector:

    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, image_path):

        results = self.model(image_path)

        detections = []

        for r in results:
            for box in r.boxes:
                label = r.names[int(box.cls)]
                detections.append(label)

        return detections