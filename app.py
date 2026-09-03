import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image
from ultralytics import YOLO

# 1. Page Configuration
st.set_page_config(
    page_title="DHARMENDRA KUMAR (MISHRA) - Strict Stock Reconciliation Engine",
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

    .status-card-pass {
        background: rgba(16, 185, 129, 0.2);
        border: 2px solid #10b981;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        color: #34d399;
        font-size: 22px;
        font-weight: 900;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    }

    .status-card-fail {
        background: rgba(239, 68, 68, 0.2);
        border: 2px solid #ef4444;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        color: #f87171;
        font-size: 22px;
        font-weight: 900;
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# 3. Model Loader
@st.cache_resource
def load_yolo_model():
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
    st.caption("🔍 High-Precision AI Stock Verification & Strict Reconciliation Engine")

st.divider()

# 5. Sidebar Controls
with st.sidebar:
    st.markdown("### ⚙️ Detection Controls")
    conf_threshold = st.slider("Min Confidence Filter", 0.30, 0.95, 0.55, 0.05)
    iou_threshold = st.slider("Overlap Suppressor (IoU)", 0.10, 0.60, 0.30, 0.05)

st.markdown("### 📋 Step 1: Expected Invoice / Bill Items Entry")

# Sample Default Bill / Expected Items Data
default_bill_data = pd.DataFrame([
    {"Product Name": "bag", "Expected Quantity": 1},
    {"Product Name": "fan", "Expected Quantity": 2},
    {"Product Name": "chair", "Expected Quantity": 1},
])

bill_df = st.data_editor(default_bill_data, num_rows="dynamic", use_container_width=True, key="bill_editor")

st.markdown("---")
st.markdown("### 📸 Step 2: Upload Physical Stock Image")
uploaded_file = st.file_uploader("Upload Image to Verify with Invoice/Bill", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### 🖼️ Physical Image")
        st.image(image, use_container_width=True)

    # YOLO AI Detection
    results = model.predict(
        source=img_array,
        conf=conf_threshold,
        iou=iou_threshold,
        max_det=1000
    )

    res = results[0]
    annotated_img = res.plot()

    detected_labels = []
    for box in res.boxes:
        cls_id = int(box.cls[0])
        item_name = model.names[cls_id].strip().lower()
        detected_labels.append(item_name)

    with col2:
        st.markdown("#### 🤖 AI Bounding Box Detection")
        st.image(annotated_img, use_container_width=True)

    st.markdown("---")
    st.markdown("### 📊 Strict Item-by-Item Reconciliation Report")

    # Clean & Group Invoice Data
    bill_df_clean = bill_df.dropna(subset=["Product Name"]).copy()
    bill_df_clean["Product Name"] = bill_df_clean["Product Name"].astype(str).str.strip().str.lower()
    bill_dict = bill_df_clean.groupby("Product Name")["Expected Quantity"].sum().to_dict()

    # Clean & Group AI Detections Data
    detected_counts = pd.Series(detected_labels).value_counts().to_dict()

    # Combine all unique product names from both Bill and AI Detection
    all_products = sorted(list(set(bill_dict.keys()).union(set(detected_counts.keys()))))

    reconciliation_list = []
    has_mismatch = False

    for prod in all_products:
        exp_qty = int(bill_dict.get(prod, 0))
        found_qty = int(detected_counts.get(prod, 0))
        diff = found_qty - exp_qty

        if diff == 0:
            status = "✅ MATCHED PERFECTLY"
        elif diff < 0:
            status = f"🚨 MISSING ({abs(diff)} Item/s Short)"
            has_mismatch = True
        else:
            status = f"⚠️ EXTRA ({diff} Extra/Duplicate)"
            has_mismatch = True

        reconciliation_list.append({
            "Product Name": prod.title(),
            "Invoice/Bill Quantity": exp_qty,
            "Image Detected Quantity": found_qty,
            "Difference": diff,
            "Status": status
        })

    report_df = pd.DataFrame(reconciliation_list)

    # Overall Match Status Badge
    if not has_mismatch and len(report_df) > 0:
        st.markdown('<div class="status-card-pass">🎉 SUCCESS: ALL ITEMS MATCHED PERFECTLY WITH INVOICE!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-card-fail">❌ ALERT: STOCK MISMATCH DETECTED! ITEMS ARE MISSING / UNMATCHED!</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Show detailed item-wise reconciliation table
    st.dataframe(report_df, use_container_width=True)

st.markdown("<br><hr><div style='text-align: center; color: #34d399; font-weight: 700;'>⚡ Designed & Developed by Dharmendra Kumar (Mishra)</div>", unsafe_allow_html=True)
    
