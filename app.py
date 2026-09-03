import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="DHARMENDRA KUMAR (MISHRA) - Batch & Product Verification Engine",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom Styling
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

# 3. Header Section
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.markdown('<div style="font-size: 50px;">🔍</div>', unsafe_allow_html=True)

with col_title:
    st.markdown('<h1 class="floating-header">DHARMENDRA KUMAR (MISHRA)</h1>', unsafe_allow_html=True)
    st.markdown('<span class="designer-badge">✨ ARCHITECT & DESIGNER: RAJVEER</span>', unsafe_allow_html=True)
    st.caption("🏷️ Automatic Batch No., Product Code & Name Verification Engine")

st.divider()

# 4. Step 1: Invoice Data Entry
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
st.markdown("### 📸 Step 2: Upload Product / Label Image")

uploaded_file = st.file_uploader("Upload Image showing Product Name, Batch No. & Product Code", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    c1, c2 = st.columns([1, 1])

    with c1:
        st.markdown("#### 🖼️ Uploaded Label Image")
        st.image(image, use_container_width=True)

    with c2:
        st.markdown("#### 📝 Extracted Image Information")
        manual_text_input = st.text_area(
            "Image OCR Read Data (Paste or edit extracted text if needed):",
            value="",
            placeholder="Image me likha hua Batch No, Product Name, Code yahan read hoke aayega...",
            height=200
        )

    st.markdown("---")
    st.markdown("### 📊 Final Reconciliation & Verification Report")

    cleaned_invoice = invoice_df.dropna(subset=["Product Name"]).copy()
    verification_results = []
    all_matched = True
    
    combined_text = manual_text_input.lower()

    for idx, row in cleaned_invoice.iterrows():
        exp_name = str(row["Product Name"]).strip()
        exp_code = str(row["Product Code / No"]).strip()
        exp_batch = str(row["Batch Number"]).strip()

        # Strict Verification Check
        name_match = exp_name.lower() in combined_text if (exp_name and combined_text) else False
        code_match = exp_code.lower() in combined_text if (exp_code and combined_text) else False
        batch_match = exp_batch.lower() in combined_text if (exp_batch and combined_text) else False

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

    # Status Alert Display
    if all_matched and len(report_df) > 0 and len(combined_text) > 0:
        st.markdown('<div class="status-pass">🎉 FINAL VERIFICATION RESULT: PASSED! ALL BATCH NOS, PRODUCT CODES & NAMES MATCHED PERFECTLY!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-fail">🚨 FINAL VERIFICATION RESULT: FAILED! BATCH NO, PRODUCT CODE, OR PRODUCT NAME MISMATCH DETECTED!</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.dataframe(report_df, use_container_width=True)

st.markdown("<br><hr><div style='text-align: center; color: #34d399; font-weight: 700;'>⚡ Designed & Developed by Dharmendra Kumar (Mishra)</div>", unsafe_allow_html=True)
