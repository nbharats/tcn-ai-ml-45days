import gradio as gr
from ultralytics import YOLO
import numpy as np
import cv2

model = YOLO("best.pt")

def get_severity(coverage_pct):
    if coverage_pct == 0:
        return "NONE"
    elif coverage_pct <= 3:
        return "LOW"
    elif coverage_pct <= 10:
        return "MEDIUM"
    elif coverage_pct <= 20:
        return "HIGH"
    else:
        return "CRITICAL"

def detect_potholes(image):
    results = model.predict(image, conf=0.45)[0]
    annotated = results.plot()

    h, w = image.shape[:2] if hasattr(image, "shape") else (results.orig_shape[0], results.orig_shape[1])
    total_area = h * w

    boxes = results.boxes
    details = []
    box_area_sum = 0

    if boxes is not None and len(boxes) > 0:
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = float(box.conf[0])
            area = (x2 - x1) * (y2 - y1)
            box_area_sum += area
            details.append(f"Detection: confidence={conf:.2f}, box area={int(area)}px")

    coverage_pct = (box_area_sum / total_area) * 100 if total_area > 0 else 0
    severity = get_severity(coverage_pct)

    summary = f"Detections: {len(details)}\n"
    summary += f"Coverage: {coverage_pct:.2f}% of image\n"
    summary += f"Severity: {severity}\n\n"
    summary += "\n".join(details) if details else "No potholes detected."

    return annotated, summary

demo = gr.Interface(
    fn=detect_potholes,
    inputs=gr.Image(type="numpy", label="Upload road photo"),
    outputs=[
        gr.Image(type="numpy", label="Detected potholes"),
        gr.Textbox(label="Details & Severity", lines=10),
    ],
    title="Pothole & Defect Detector",
    description="Upload a road photo to detect potholes with bounding boxes, confidence scores, and a severity rating based on defect coverage.",
)

demo.launch(share=True, debug=False)
