import streamlit as st
import pandas as pd
import time
from PIL import Image
import json

# 1. Page Configuration
st.set_page_config(
    page_title="DHARMENDRA KUMAR MISHRA - AI Stock Auditor",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Fixed Dynamic Neon Cyberpunk Emerald Styling (High Contrast & Visible Buttons)
st.markdown("""
<style>
    /* Dynamic Background */
    .stApp {
        background: linear-gradient(-45deg, #022c22, #042f2e, #0f172a, #065f46, #022c22);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        color: #f8fafc;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Header Title Glow */
    .floating-header {
        background: linear-gradient(90deg, #34d399, #06b6d4, #a7f3d0, #67e8f9, #34d399);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px;
        font-weight: 900;
        letter-spacing: -1px;
        animation: gradientShift 5s ease infinite alternate;
        margin: 0;
        display: inline-block;
        filter: drop-shadow(0 0 12px rgba(52, 211, 153, 0.6));
    }

    /* Designer Badge */
    .designer-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(6, 182, 212, 0.2);
        border: 1.5px solid #34d399;
        padding: 6px 20px;
        border-radius: 30px;
        font-size: 14px;
        font-weight: 800;
        letter-spacing: 1.5px;
        color: #67e8f9;
        box-shadow: 0 0 15px rgba(52, 211, 153, 0.4);
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    .logo-frame {
        display: inline-block;
        padding: 8px;
        border-radius: 24px;
        background: linear-gradient(135deg, #34d399, #06b6d4);
        box-shadow: 0 0 25px rgba(52, 211, 153, 0.7);
    }

    /* Metric Cards */
    .metric-card {
        background: rgba(6, 78, 59, 0.6);
        border: 1.5px solid #34d399;
        border-radius: 20px;
        padding: 22px;
        text-align: center;
        backdrop-filter: blur(16px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }

    .metric-title {
        font-size: 14px;
        color: #a7f3d0;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    .metric-value {
        font-size: 38px;
        font-weight: 900;
        margin-top: 8px;
        background: linear-gradient(90deg, #34d399, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* MAIN ACTION BUTTON FIX (High Contrast Visible Solid Button) */
    div.stButton > button {
        background: linear-gradient(135deg, #059669 0%, #0d9488 50%, #0284c7 100%) !important;
        color: #ffffff !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        border: 2px solid #67e8f9 !important;
        border-radius: 14px !important;
        padding: 16px 28px !important;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.8) !important;
        width: 100% !important;
        cursor: pointer !important;
        margin-top: 15px !important;
        margin-bottom: 15px !important;
        display: block !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #10b981 0%, #14b8a6 50%, #38bdf8 100%) !important;
        box-shadow: 0 0 30px rgba(56, 189, 248, 1) !important;
        transform: translateY(-2px) !important;
    }

    /* FILE UPLOADER FULL STYLING FIX (Removes White Box & White Text) */
    [data-testid="stFileUploader"] section {
        background: rgba(4, 47, 46, 0.85) !important;
        border: 2px dashed #34d399 !important;
        border-radius: 18px !important;
        padding: 20px !important;
    }

    [data-testid="stFileUploader"] section div, 
    [data-testid="stFileUploader"] section span,
    [data-testid="stFileUploader"] section p,
    [data-testid="stFileUploader"] label {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
    }

    /* File Uploader Browse Button Fix */
    [data-testid="stFileUploader"] section button {
        background-color: #065f46 !important;
        color: #ffffff !important;
        border: 1px solid #34d399 !important;
        border-radius: 10px !important;
        font-weight: 800 !important;
        padding: 8px 16px !important;
        box-shadow: 0 0 10px rgba(52, 211, 153, 0.3) !important;
    }

    [data-testid="stFileUploader"] section button:hover {
        background-color: #047857 !important;
        border-color: #67e8f9 !important;
        color: #ffffff !important;
    }

    .image-preview-card {
        background: rgba(6, 78, 59, 0.45);
        border: 1.5px solid rgba(52, 211, 153, 0.4);
        border-radius: 18px;
        padding: 18px;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .section-title {
        color: #67e8f9;
        font-weight: 800;
        text-shadow: 0 0 10px rgba(6, 182, 212, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Setup
with st.sidebar:
    st.markdown("<h3 class='section-title'>🖼️ Brand Logo Studio</h3>", unsafe_allow_html=True)
    logo_file = st.file_uploader("Upload App Logo", type=["png", "jpg", "jpeg"])
    st.divider()
    st.markdown("<h3 class='section-title'>🤖 Vision AI Key</h3>", unsafe_allow_html=True)
    gemini_api_key = st.text_input("Google Gemini API Key", type="password", help="Enter API Key for live OCR Batch No & Product Name reading.")
    st.info("💡 **Batch No. OCR Mode Active:** Reads Product Name, Batch Number, and Quantities.")

# 4. Header Section
col_logo, col_title = st.columns([1, 5])

with col_logo:
    if logo_file is not None:
        st.markdown('<div class="logo-frame">', unsafe_allow_html=True)
        st.image(logo_file, width=110)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="logo-frame" style="font-size: 55px; padding: 12px 24px;">📦</div>', unsafe_allow_html=True)

with col_title:
    st.markdown("""
    <div style="display: flex; flex-direction: column; gap: 6px;">
        <h1 class="floating-header">DHARMENDRA KUMAR MISHRA</h1>
        <div>
            <span class="designer-badge">⚡ ARCHITECT & DESIGNER: RAJVEER</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("🔍 Visual AI Stock Matching, Batch No. Verification & Inventory Audit Engine")

st.divider()

# 5. Dual Photo Upload Studio
st.markdown("<h3 class='section-title'>📸 Dual Photo Input Studio</h3>", unsafe_allow_html=True)
col_img1, col_img2 = st.columns(2)

with col_img1:
    st.markdown('<div class="image-preview-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #a7f3d0;'>📑 1. Upload Stock List Image</h4>", unsafe_allow_html=True)
    list_image_file = st.file_uploader(
        "Upload Stock List Photo (With Product Name & Batch No)",
        type=["png", "jpg", "jpeg"],
        key="list_uploader"
    )
    if list_image_file:
        img_list = Image.open(list_image_file)
        st.image(img_list, caption="Uploaded Stock List Image", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_img2:
    st.markdown('<div class="image-preview-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #a7f3d0;'>📦 2. Upload Physical Stock Goods Photo</h4>", unsafe_allow_html=True)
    stock_image_file = st.file_uploader(
        "Upload Physical Stock Photo (Showing Batch Nos & Products)",
        type=["png", "jpg", "jpeg"],
        key="stock_uploader"
    )
    if stock_image_file:
        img_stock = Image.open(stock_image_file)
        st.image(img_stock, caption="Uploaded Physical Stock Photo", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Ultra High-Sensitive Batch & Product OCR Google Vision AI Engine
def process_images_with_vision_ai(api_key, list_img, stock_img):
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        
        strict_audit_prompt = """
        You are an Ultra-High Precision Visual AI Batch & Stock Auditor.
        Analyze Image 1 (Stock List/Invoice) and Image 2 (Physical Stock Photos).

        METICULOUS TASK INSTRUCTIONS:
        1. Read Image 1 using high-sensitivity OCR. Extract:
           - Product Name
           - Batch No / Lot No (If not mentioned in document, state 'N/A' or 'Not Specified')
           - Expected Quantity
        2. Read Image 2 (Physical Goods Photo). Check product names, Batch Nos on boxes/labels, and physical counts.
        3. Match items based on Product Name AND Batch No:
           - Calculate "Shortage / Missing": (Expected Count - Found Count).
           - Set "Audit Status":
             * "✅ Fully Present" if Found == Expected and Batch No matches.
             * "⚠️ Partial Shortage" if Found > 0 and Found < Expected.
             * "❌ Completely Missing" if Found == 0.
             * "⚡ Batch Mismatch" if product is present but Batch No differs.

        FORMAT REQUIREMENT:
        Return ONLY a raw JSON array of objects with EXACTLY these keys (do NOT include markdown ```json wrapper):
        [
          {
            "Product Name": "Paracetamol 500mg",
            "Batch No": "BTH-2026-901",
            "Expected (List)": 50,
            "Found (Photo)": 50,
            "Shortage / Missing": 0,
            "Audit Status": "✅ Fully Present"
          }
        ]
        """
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[strict_audit_prompt, list_img, stock_img]
        )
        
        clean_json = response.text.replace("
