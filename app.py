import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import io

# 1. Page Configuration
st.set_page_config(
    page_title="DHARMENDRA KUMAR (MISHRA) - Superior AI Vision Stock Scanner",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Ultra-Futuristic Cyberpunk Glassmorphism UI CSS
st.markdown("""
<style>
    /* Animated Gradient Background */
    .stApp {
        background: radial-gradient(circle at top left, #064e3b, #022c22, #0f172a, #042f2e);
        background-size: 400% 400%;
        animation: gradientAnimation 12s ease infinite;
        color: #ecfdf5;
        font-family: 'Segoe UI', Roboto, Helvetica, sans-serif;
    }

    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .header-box {
        background: rgba(6, 78, 59, 0.35);
        border: 1px solid rgba(52, 211, 153, 0.4);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 24px;
        text-align: center;
        margin-bottom: 25px;
    }

    .floating-header {
        background: linear-gradient(90deg, #34d399, #10b981, #06b6d4, #a7f3d0, #34d399);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 40px;
        font-weight: 900;
        letter-spacing: 1px;
        margin: 0;
        filter: drop-shadow(0 0 15px rgba(52, 211, 153, 0.4));
    }

    .designer-badge {
        display: inline-block;
        background: linear-gradient(135deg, rgba(52, 211, 153, 0.2), rgba(6, 182, 212, 0.3));
        border: 1px solid rgba(52, 211, 153, 0.6);
        padding: 6px 18px;
        border-radius: 30px;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 1.5px;
        color: #34d399;
        box-shadow: 0 0 15px rgba(52, 211, 153, 0.3);
        margin-top: 10px;
    }

    .glass-card {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(52, 211, 153, 0.3);
        border-radius: 18px;
        padding: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }

    /* Primary Upload Button Override */
    [data-testid="stFileUploader"] section {
        background: rgba(6, 78, 59, 0.25) !important;
        border: 2px dashed #34d399 !important;
        border-radius: 16px !important;
        padding: 25px !important;
        transition: all 0.3s ease;
    }
    [data-testid="stFileUploader"] section:hover {
        border-color: #06b6d4 !important;
        box-shadow: 0 0 25px rgba(6, 182, 212, 0.4) !important;
    }

    .status-pass {
        background: rgba(16, 185, 129, 0.2);
        border: 2px solid #10b981;
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        color: #34d399;
        font-size: 22px;
        font-weight: 900;
        box-shadow: 0 0 30px rgba(16, 185, 129, 0.5);
    }

    .status-fail {
        background: rgba(239, 68, 68, 0.2);
        border: 2px solid #ef4444;
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        color: #f87171;
        font-size: 22px;
        font-weight: 900;
        box-shadow: 0 0 30px rgba(239, 68, 68, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("""
<div class="header-box">
    <h1 class="floating-header">DHARMENDRA KUMAR (MISHRA)</h1>
    <span class="designer-badge">✨ ARCHITECT & DESIGNER: RAJVEER</span>
    <p style="color: #a7f3d0; margin-top: 10px; font-weight: 600;">👁️ SUPERIOR AI VISION - LIVE STOCK & LABEL SCANNER ENGINE</p>
</div>
""", unsafe_allow_html=True)

# 4. Pure Vision Scanner Section
st.markdown("### 📸 Superior Vision Image Capture & Upload")

input_type = st.radio("Choose Input Mode:", ["📁 Upload Stock/Label Image", "📷 Live Camera Capture"], horizontal=True)

uploaded_image = None

if input_type == "📁 Upload Stock/Label Image":
    uploaded_image = st.file_uploader("Upload Product Label / Box Image", type=["jpg", "jpeg", "png"])
else:
    uploaded_image = st.camera_input("Take a photo of Product Label / Box")

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    
    st.markdown("---")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🖼️ Captured Stock Label")
        st.image(image, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### ⚡ AI OCR & Label Extraction")
        st.info("💡 Image Se Read Kiya Hua Data Niche Paste / Verify Karein:")
        
        extracted_data = st.text_area(
            "Extracted Label Text (Batch No, Code, Name):",
            value="",
            placeholder="Type or paste the extracted text from label...\nExample:\nProduct Name: Paracetamol 500mg\nBatch No: BTH-9982\nProduct Code: PRD-101",
            height=200
        )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🔍 Verification & Quality Inspection")

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    v1, v2, v3 = st.columns(3)
    
    with v1:
        search_name = st.text_input("Product Name to Verify", placeholder="e.g. Paracetamol")
    with v2:
        search_batch = st.text_input("Batch No. to Verify", placeholder="e.g. BTH-9982")
    with v3:
        search_code = st.text_input("Product Code to Verify", placeholder="e.g. PRD-101")
    
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Superior Match Check Logic
    if search_name or search_batch or search_code:
        full_text = extracted_data.lower()
        
        name_ok = (search_name.lower() in full_text) if search_name else True
        batch_ok = (search_batch.lower() in full_text) if search_batch else True
        code_ok = (search_code.lower() in full_text) if search_code else True

        if name_ok and batch_ok and code_ok and len(full_text) > 0:
            st.markdown('<div class="status-pass">🎉 SUPERIOR VISION RESULT: PASSED!<br><span style="font-size: 16px;">Product Name, Batch Number & Product Code Matched Successfully!</span></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-fail">🚨 SUPERIOR VISION RESULT: MISMATCH / FAILED!<br><span style="font-size: 16px;">One or more details (Batch/Name/Code) do not match the extracted label text.</span></div>', unsafe_allow_html=True)

st.markdown("<br><hr><div style='text-align: center; color: #34d399; font-weight: 700;'>⚡ Designed & Developed by Dharmendra Kumar (Mishra)</div>", unsafe_allow_html=True)
