import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image

st.set_page_config(page_title="Pothole & Defect Detector", layout="centered")

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

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

st.title("Pothole & Defect Detector")
st.write("Upload a road photo to detect potholes with bounding boxes, confidence scores, and a severity rating based on defect coverage.")

uploaded = st.file_uploader("Upload road photo", type=["jpg", "jpeg", "png", "webp"])

if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")
    image_np = np.array(image)

    results = model.predict(image_np, conf=0.45)[0]
    annotated = results.plot()

    h, w = image_np.shape[:2]
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

    st.image(annotated, caption="Detected potholes", use_container_width=True)

    st.subheader("Details")
    st.write(f"**Detections:** {len(details)}")
    st.write(f"**Coverage:** {coverage_pct:.2f}% of image")
    st.write(f"**Severity:** {severity}")

    if details:
        for d in details:
            st.text(d)
    else:
        st.write("No potholes detected.")
