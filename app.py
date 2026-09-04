import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="DHARMENDRA KUMAR (MISHRA) - Dual Column Superior Stock Scanner",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Cyberpunk Emerald Glassmorphism UI CSS
st.markdown("""
<style>
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
        background: rgba(15, 23, 42, 0.65);
        border: 1px solid rgba(52, 211, 153, 0.35);
        border-radius: 18px;
        padding: 22px;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        min-height: 520px;
    }

    /* Uploader Customization */
    [data-testid="stFileUploader"] section {
        background: rgba(6, 78, 59, 0.25) !important;
        border: 2px dashed #34d399 !important;
        border-radius: 16px !important;
        padding: 20px !important;
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

# 3. Header
st.markdown("""
<div class="header-box">
    <h1 class="floating-header">DHARMENDRA KUMAR (MISHRA)</h1>
    <span class="designer-badge">✨ ARCHITECT & DESIGNER: RAJVEER</span>
    <p style="color: #a7f3d0; margin-top: 10px; font-weight: 600;">👁️ DUAL-COLUMN SUPERIOR VISION & STOCK RECONCILIATION ENGINE</p>
</div>
""", unsafe_allow_html=True)

# 4. Two Independent Columns Layout
col_left, col_right = st.columns([1, 1])

# --- LEFT COLUMN: STOCK LIST ---
with col_left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📋 Column 1: Expected Stock List / Bill")
    st.caption("Enter your expected Stock Details (Product Name, Code, Batch No, Quantity):")

    default_stock_list = pd.DataFrame([
        {
            "Product Name": "Paracetamol 500mg",
            "Product Code": "PRD-101",
            "Batch Number": "BTH-9982",
            "Quantity": 1
        },
        {
            "Product Name": "Abbott Syrup",
            "Product Code": "ABT-550",
            "Batch Number": "BTH-1240",
            "Quantity": 1
        }
    ])

    stock_df = st.data_editor(
        default_stock_list,
        num_rows="dynamic",
        use_container_width=True,
        key="stock_list_editor"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# --- RIGHT COLUMN: STOCK PHOTO UPLOAD & SCAN ---
with col_right:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📸 Column 2: Upload Stock / Label Photo")
    
    input_mode = st.radio("Select Source:", ["📁 File Upload", "📷 Live Camera"], horizontal=True)

    uploaded_photo = None
    if input_mode == "📁 File Upload":
        uploaded_photo = st.file_uploader("Upload Image showing Product Name, Batch No. & Code", type=["jpg", "jpeg", "png"])
    else:
        uploaded_photo = st.camera_input("Take Live Photo")

    extracted_ocr_text = ""

    if uploaded_photo is not None:
        img = Image.open(uploaded_photo)
        st.image(img, caption="Uploaded Stock Photo", use_container_width=True)
        
        st.markdown("##### 📝 Extracted / Read Text from Photo:")
        extracted_ocr_text = st.text_area(
            "Photo Read Data (Batch No, Product Code, Name):",
            value="",
            placeholder="Type or paste the read details from photo label...",
            height=130
        )
    st.markdown('</div>', unsafe_allow_html=True)

# --- BOTTOM SECTION: RECONCILIATION & MATCHING REPORT ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📊 Superior Verification & Reconciliation Report")

if uploaded_photo is not None:
    cleaned_stock = stock_df.dropna(subset=["Product Name"]).copy()
    verification_data = []
    overall_pass = True
    read_text_lower = extracted_ocr_text.lower()

    for idx, row in cleaned_stock.iterrows():
        p_name = str(row["Product Name"]).strip()
        p_code = str(row["Product Code"]).strip()
        p_batch = str(row["Batch Number"]).strip()
        p_qty = row["Quantity"]

        # 1-to-1 Match check with Photo text
        name_found = p_name.lower() in read_text_lower if (p_name and read_text_lower) else False
        code_found = p_code.lower() in read_text_lower if (p_code and read_text_lower) else False
        batch_found = p_batch.lower() in read_text_lower if (p_batch and read_text_lower) else False

        if name_found and code_found and batch_found:
            status = "✅ MATCHED PERFECTLY"
        else:
            status = "❌ MISMATCH / NOT FOUND"
            overall_pass = False

        verification_data.append({
            "Product Name": p_name,
            "Product Code": p_code,
            "Batch Number": p_batch,
            "Expected Qty": p_qty,
            "Name Found?": "✅ Yes" if name_found else "❌ No",
            "Code Found?": "✅ Yes" if code_found else "❌ No",
            "Batch Found?": "✅ Yes" if batch_found else "❌ No",
            "Status": status
        })

    report_df = pd.DataFrame(verification_data)

    if overall_pass and len(report_df) > 0 and len(read_text_lower) > 0:
        st.markdown('<div class="status-pass">🎉 RECONCILIATION PASSED!<br><span style="font-size: 16px;">Stock List Data matched 100% with Uploaded Stock Photo!</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-fail">🚨 RECONCILIATION MISMATCH DETECTED!<br><span style="font-size: 16px;">One or more items, batch numbers, or product codes do not match the photo data.</span></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.dataframe(report_df, use_container_width=True)

else:
    st.info("💡 Right Column me photo upload ya capture karein reconciliation report dekhne ke liye.")

st.markdown("<br><hr><div style='text-align: center; color: #34d399; font-weight: 700;'>⚡ Designed & Developed by Dharmendra Kumar (Mishra)</div>", unsafe_allow_html=True)
