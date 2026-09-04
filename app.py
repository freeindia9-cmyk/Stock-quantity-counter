import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="DHARMENDRA KUMAR (MISHRA) - Dual Photo Vision Stock Verification Engine",
    page_icon="📸",
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
        min-height: 560px;
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

# 3. Header Section
st.markdown("""
<div class="header-box">
    <h1 class="floating-header">DHARMENDRA KUMAR (MISHRA)</h1>
    <span class="designer-badge">✨ ARCHITECT & DESIGNER: RAJVEER</span>
    <p style="color: #a7f3d0; margin-top: 10px; font-weight: 600;">👁️ DUAL PHOTO VISION - STOCK LIST VS PHYSICAL PRODUCT COMPARISON ENGINE</p>
</div>
""", unsafe_allow_html=True)

# 4. Two Independent Photo Upload Columns
col1, col2 = st.columns([1, 1])

# --- COLUMN 1: STOCK LIST PAPER PHOTO UPLOAD ---
with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📜 Column 1: Stock List / Bill Photo")
    st.caption("Upload photo of Invoice, Stock Sheet or Bill paper:")

    mode_list = st.radio("Source for Stock List:", ["📁 Upload Stock List Photo", "📷 Camera Capture List"], horizontal=True, key="list_mode")

    list_photo = None
    if mode_list == "📁 Upload Stock List Photo":
        list_photo = st.file_uploader("Upload Stock List / Invoice Photo", type=["jpg", "jpeg", "png"], key="list_upload")
    else:
        list_photo = st.camera_input("Take Photo of Stock List / Invoice", key="list_cam")

    list_text = ""
    if list_photo is not None:
        img_list = Image.open(list_photo)
        st.image(img_list, caption="Stock List Document Photo", use_container_width=True)
        
        st.markdown("##### 📝 Stock List Extracted / Read Details:")
        list_text = st.text_area(
            "Extracted Stock List Text (Product Name, Batch, Code):",
            value="",
            placeholder="Stock List photo se read kiye gaye details paste ya edit karein...\nExample:\nParacetamol 500mg, BTH-9982, PRD-101",
            height=130,
            key="list_text_area"
        )
    st.markdown('</div>', unsafe_allow_html=True)

# --- COLUMN 2: PHYSICAL PRODUCT LABEL PHOTO UPLOAD ---
with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 📦 Column 2: Physical Product / Label Photo")
    st.caption("Upload photo of Box Label, Carton, or Product Package:")

    mode_prod = st.radio("Source for Product Photo:", ["📁 Upload Product Photo", "📷 Camera Capture Product"], horizontal=True, key="prod_mode")

    prod_photo = None
    if mode_prod == "📁 Upload Product Photo":
        prod_photo = st.file_uploader("Upload Product Box / Label Photo", type=["jpg", "jpeg", "png"], key="prod_upload")
    else:
        prod_photo = st.camera_input("Take Photo of Physical Product Label", key="prod_cam")

    prod_text = ""
    if prod_photo is not None:
        img_prod = Image.open(prod_photo)
        st.image(img_prod, caption="Physical Product Label Photo", use_container_width=True)
        
        st.markdown("##### 📝 Physical Label Extracted / Read Details:")
        prod_text = st.text_area(
            "Extracted Product Label Text (Batch No, Code, Name):",
            value="",
            placeholder="Product Label photo se read kiye gaye details paste ya edit karein...\nExample:\nParacetamol 500mg, BTH-9982, PRD-101",
            height=130,
            key="prod_text_area"
        )
    st.markdown('</div>', unsafe_allow_html=True)

# --- BOTTOM SECTION: DUAL PHOTO RECONCILIATION REPORT ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📊 Dual-Photo Vision Reconciliation Report")

if list_photo is not None and prod_photo is not None:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    st.markdown("#### 🔍 Enter Parameters to Reconcile / Match Both Photos:")
    v1, v2, v3 = st.columns(3)
    
    with v1:
        search_name = st.text_input("Verify Product Name", placeholder="e.g. Paracetamol")
    with v2:
        search_batch = st.text_input("Verify Batch Number", placeholder="e.g. BTH-9982")
    with v3:
        search_code = st.text_input("Verify Product Code", placeholder="e.g. PRD-101")

    st.markdown('</div><br>', unsafe_allow_html=True)

    # Reconciliation Logic
    list_lower = list_text.lower()
    prod_lower = prod_text.lower()

    if search_name or search_batch or search_code:
        # Check presence in List Photo Data
        name_in_list = search_name.lower() in list_lower if search_name else True
        batch_in_list = search_batch.lower() in list_lower if search_batch else True
        code_in_list = search_code.lower() in list_lower if search_code else True

        # Check presence in Product Photo Data
        name_in_prod = search_name.lower() in prod_lower if search_name else True
        batch_in_prod = search_batch.lower() in prod_lower if search_batch else True
        code_in_prod = search_code.lower() in prod_lower if search_code else True

        list_matched = name_in_list and batch_in_list and code_in_list
        prod_matched = name_in_prod and batch_in_prod and code_in_prod

        # Comparison DataFrame
        report_data = [{
            "Parameter": "Product Name",
            "Search Keyword": search_name if search_name else "N/A",
            "Found in Stock List Photo?": "✅ Yes" if name_in_list else "❌ No",
            "Found in Product Label Photo?": "✅ Yes" if name_in_prod else "❌ No",
            "Status": "✅ MATCHED" if (name_in_list and name_in_prod) else "❌ MISMATCH"
        }, {
            "Parameter": "Batch Number",
            "Search Keyword": search_batch if search_batch else "N/A",
            "Found in Stock List Photo?": "✅ Yes" if batch_in_list else "❌ No",
            "Found in Product Label Photo?": "✅ Yes" if batch_in_prod else "❌ No",
            "Status": "✅ MATCHED" if (batch_in_list and batch_in_prod) else "❌ MISMATCH"
        }, {
            "Parameter": "Product Code",
            "Search Keyword": search_code if search_code else "N/A",
            "Found in Stock List Photo?": "✅ Yes" if code_in_list else "❌ No",
            "Found in Product Label Photo?": "✅ Yes" if code_in_prod else "❌ No",
            "Status": "✅ MATCHED" if (code_in_list and code_in_prod) else "❌ MISMATCH"
        }]

        st.dataframe(pd.DataFrame(report_data), use_container_width=True)

        if list_matched and prod_matched and len(list_lower) > 0 and len(prod_lower) > 0:
            st.markdown('<div class="status-pass">🎉 RECONCILIATION PASSED!<br><span style="font-size: 16px;">Stock List Photo and Physical Product Label Photo Matched 100%!</span></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-fail">🚨 RECONCILIATION MISMATCH DETECTED!<br><span style="font-size: 16px;">Details in Stock List Photo do not match Physical Product Label Photo.</span></div>', unsafe_allow_html=True)
            
elif list_photo is None and prod_photo is None:
    st.info("💡 Left Column me Stock List Document ki photo aur Right Column me Physical Product ki photo upload karein.")
elif list_photo is None:
    st.warning("⚠️ Kripya Left Column me Stock List ki photo upload karein.")
else:
    st.warning("⚠️ Kripya Right Column me Physical Product Label ki photo upload karein.")

st.markdown("<br><hr><div style='text-align: center; color: #34d399; font-weight: 700;'>⚡ Designed & Developed by Dharmendra Kumar (Mishra)</div>", unsafe_allow_html=True)
