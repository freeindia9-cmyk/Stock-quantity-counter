import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image
from ultralytics import YOLO

# 1. Page Configuration
st.set_page_config(
    page_title="DHARMENDRA KUMAR (MISHRA) - Accurate Stock Counter Engine",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Cyberpunk Emerald UI CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(-45deg, #022c22, #064e3b, #0f172a, #065f46, #022c22);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
        color: #ecfdf5;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .floating-header {
        background: linear-gradient(90deg, #34d399, #10b981, #06b6d4, #a7f3d0, #34d399);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 38px;
        font-weight: 900;
    }

    .designer-badge {
        display: inline-block;
        background: rgba(52, 211, 153, 0.2);
        border: 1px solid rgba(52, 211, 153, 0.6);
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 700;
        color: #34d399;
    }

    .metric-card {
        background: rgba(6, 78, 59, 0.45);
        border: 1px solid rgba(52, 211, 153, 0.3);
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        backdrop-filter: blur(12px);
    }
    
    .metric-value {
        font-size: 32px;
        font-weight: 900;
        color: #34d399;
    }
</style>
""", unsafe_allow_html=True)

# 3. Model Loader
@st.cache_resource
def load_yolo_model():
    # Standard YOLO model (YOLOv8x/n)
    return YOLO('yolov8n.pt') 

try:
    model = load_yolo_model()
except Exception as e:
    st.error("Model load karne me dikkat hui. 'ultralytics' package installed rakhein.")

# 4. Header Section
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.markdown('<div style="font-size: 50px;">📦</div>', unsafe_allow_html=True)

with col_title:
    st.markdown('<h1 class="floating-header">DHARMENDRA KUMAR (MISHRA)</h1>', unsafe_allow_html=True)
    st.markdown('<span class="designer-badge">✨ ARCHITECT & DESIGNER: RAJVEER</span>', unsafe_allow_html=True)
    st.caption("🔍 High-Precision AI Stock Detection & Verification Engine")

st.divider()

# 5. Sidebar Controls
with st.sidebar:
    st.markdown("### ⚙️ Detection Sensitivity Controls")
    st.info("💡 Oversampling/Duplicate Counting ko rokne ke liye settings tuned hain.")
    
    # High Confidence prevents random false detects
    conf_threshold = st.slider("Min Confidence Filter", 0.30, 0.95, 0.60, 0.05)
    
    # Strict Overlap Suppression (IoU) prevents double-counting 1 bag
    iou_threshold = st.slider("Strict Overlap Suppressor (IoU)", 0.10, 0.60, 0.35, 0.05)

# 6. File Upload & Processing
uploaded_file = st.file_uploader("📸 Upload Stock Image for Measurement", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read Image
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 🖼️ Original Uploaded Image")
        st.image(image, use_container_width=True)

    # Run AI Model with strict overlap suppression
    results = model.predict(
        source=img_array,
        conf=conf_threshold,
        iou=iou_threshold,
        max_det=1000
    )

    detected_labels = []
    res = results[0]

    # Render bounding boxes
    annotated_img = res.plot()

    for box in res.boxes:
        cls_id = int(box.cls[0])
        item_name = model.names[cls_id]
        detected_labels.append(item_name)

    with col2:
        st.markdown("### 🤖 AI Detected Stock Image")
        st.image(annotated_img, use_container_width=True)

    st.markdown("---")
    st.markdown("### 📊 Stock Measurement Report")

    if len(detected_labels) > 0:
        # Exact Summary Calculation
        df_summary = pd.Series(detected_labels).value_counts().reset_index()
        df_summary.columns = ["Product Name", "Measured Quantity"]

        unique_product_categories = len(df_summary)
        total_physical_items = len(detected_labels)

        # Dashboard Metrics
        m1, m2 = st.columns(2)
        with m1:
            st.markdown(f'''
                <div class="metric-card">
                    <div style="color: #a7f3d0; font-size: 14px;">TOTAL DISTINCT PRODUCTS</div>
                    <div class="metric-value">{unique_product_categories}</div>
                </div>
            ''', unsafe_allow_html=True)

        with m2:
            st.markdown(f'''
                <div class="metric-card">
                    <div style="color: #a7f3d0; font-size: 14px;">TOTAL PHYSICAL QUANTITY COUNTED</div>
                    <div class="metric-value" style="color: #06b6d4;">{total_physical_items}</div>
                </div>
            ''', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.dataframe(df_summary, use_container_width=True)

    else:
        st.warning("⚠️ Image me koi product detect nahi hua. Sidebar se Confidence threshold kam karke dobara try karein.")

st.markdown("<br><hr><div style='text-align: center; color: #34d399; font-weight: 700;'>⚡ Designed & Developed by Dharmendra Kumar (Mishra)</div>", unsafe_allow_html=True)
