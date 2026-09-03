import streamlit as st
import cv2
import pandas as pd
import numpy as np
from PIL import Image
import easyocr
import re

# 1. Page Configuration
st.set_page_config(
    page_title="DHARMENDRA KUMAR (MISHRA) - Batch & Product Verification Engine",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS
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
        font-size: 36px;
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
    .status-pass {
        background: rgba(16, 185, 129, 0.25);
        border: 2px solid #10b981;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        color: #34d399;
        font-size: 22px;
        font-weight: 900;
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.4);
    }
    .status-fail {
        background: rgba(239, 68, 68, 0.25);
        border: 2px solid #ef4444;
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        color: #f87171;
        font-size: 22px;
        font-weight: 900;
        box-shadow: 0 0 25px rgba(239, 68, 68, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# 3. EasyOCR Engine Loader
@st.cache_resource
def load_ocr_reader():
    return easyocr.Reader(['en'], gpu=False)

try:
    reader = load_ocr_reader()
except Exception as e:
    st.error(f"OCR Engine Load error: {e}")

# 4. Header Section
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.markdown('<div style="font-size: 50px;">🔍</div>', unsafe_allow_html=True)

with col_title:
    st.markdown('<h1 class="floating-header">DHARMENDRA KUMAR (MISHRA)</h1>', unsafe_allow_html=True)
    st.markdown('<span class="designer-badge">✨ ARCHITECT & DESIGNER: RAJVEER</span>', unsafe_allow_html=True)
    st.caption("🏷️ Automatic Batch No., Product Code & Name Verification Engine")

st.divider()

# 5. Expected Invoice Entry Table
st.markdown("### 📋 Step 1: Expected Invoice / Bill Details")

default_invoice_data = pd.DataFrame([
    {
        "Product Name": "Paracetamol 500mg",
        "Product Code / No": "PRD-101",
        "Batch Number": "BTH-9982",
        "Quantity": 1
    },
    {
        "Product Name": "Abbott Syrup",
        "Product Code / No": "ABT-550",
        "Batch Number": "BTH-1240",
        "Quantity": 1
    }
])

invoice_df = st.data_editor(default_invoice_data, num_rows="dynamic", use_container_width=True, key="invoice_editor")

st.markdown("---")
st.markdown("### 📸 Step 2: Upload Stock Label / Product Image")

uploaded_file = st.file_uploader("Upload Image showing Product Name, Batch No. & Product Code", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_np = np.array(image)

    c1, c2 = st.columns([1, 1])

    with c1:
        st.markdown("#### 🖼️ Uploaded Label Image")
        st.image(image, use_container_width=True)

    with st.spinner("🔍 Reading Batch Number, Product Name & Product Code from Image..."):
        # Run OCR on Image
        ocr_results = reader.readtext(img_np)
        extracted_texts = [res[1].strip() for res in ocr_results]
        combined_text_raw = " ".join(extracted_texts)
        combined_text = combined_text_raw.lower()

    with c2:
        st.markdown("#### 📝 Raw OCR Extracted Text")
        st.text_area("Extracted Labels from Image", value=combined_text_raw, height=220)

    st.markdown("---")
    st.markdown("### 📊 Final Reconciliation & Verification Report")

    cleaned_invoice = invoice_df.dropna(subset=["Product Name"]).copy()
    verification_results = []
    all_matched = True

    for idx, row in cleaned_invoice.iterrows():
        exp_name = str(row["Product Name"]).strip()
        exp_code = str(row["Product Code / No"]).strip()
        exp_batch = str(row["Batch Number"]).strip()
        exp_qty = row["Quantity"]

        # Check Matches in OCR Text
        name_match = exp_name.lower() in combined_text if exp_name else False
        code_match = exp_code.lower() in combined_text if exp_code else False
        batch_match = exp_batch.lower() in combined_text if exp_batch else False

        if name_match and code_match and batch_match:
            status = "✅ PERFECT MATCH"
        else:
            status = "❌ MISMATCH / NOT FOUND"
            all_matched = False

        verification_results.append({
            "Product Name": exp_name,
            "Product Code / No": exp_code,
            "Batch Number": exp_batch,
            "Name Found?": "✅ Yes" if name_match else "❌ No",
            "Code Found?": "✅ Yes" if code_match else "❌ No",
            "Batch Found?": "✅ Yes" if batch_match else "❌ No",
            "Overall Status": status
        })

    report_df = pd.DataFrame(verification_results)

    # Display Final Status Badge
    if all_matched and len(report_df) > 0:
        st.markdown('<div class="status-pass">🎉 FINAL VERIFICATION RESULT: PASSED! ALL BATCH NOS, PRODUCT CODES & NAMES MATCHED PERFECTLY!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-fail">🚨 FINAL VERIFICATION RESULT: FAILED! BATCH NO, PRODUCT CODE, OR PRODUCT NAME MISMATCH DETECTED!</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.dataframe(report_df, use_container_width=True)

st.markdown("<br><hr><div style='text-align: center; color: #34d399; font-weight: 700;'>⚡ Designed & Developed by Dharmendra Kumar (Mishra)</div>", unsafe_allow_html=True)
