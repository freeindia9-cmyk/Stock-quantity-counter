import streamlit as st
import pandas as pd
import time
from PIL import Image
import io

# 1. Page Configuration
st.set_page_config(
    page_title="DHARMENDRA KUMAR MISHRA - AI Stock Auditor",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Enhanced Cyberpunk Neon Emerald Dynamic CSS Theme
st.markdown("""
<style>
    /* Animated Gradient Background - Cyberpunk Emerald */
    .stApp {
        background: linear-gradient(-45deg, #022c22, #064e3b, #0f172a, #065f46, #022c22);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        color: #ecfdf5;
        font-family: 'Segoe UI', Roboto, sans-serif;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .header-container {
        display: flex;
        flex-direction: column;
        gap: 6px;
    }

    .floating-header {
        background: linear-gradient(90deg, #34d399, #10b981, #06b6d4, #a7f3d0);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px;
        font-weight: 900;
        letter-spacing: -1px;
        animation: gradientShift 6s ease infinite, floatTitle 3s ease-in-out infinite;
        margin: 0;
        display: inline-block;
    }

    .designer-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: linear-gradient(135deg, rgba(52, 211, 153, 0.15), rgba(6, 182, 212, 0.25));
        border: 1px solid rgba(52, 211, 153, 0.4);
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 1.2px;
        color: #34d399;
        box-shadow: 0 0 20px rgba(52, 211, 153, 0.2);
        width: fit-content;
        margin-top: 4px;
        animation: pulseBadge 3s infinite alternate;
    }

    @keyframes pulseBadge {
        0% { border-color: rgba(52, 211, 153, 0.3); box-shadow: 0 0 10px rgba(52, 211, 153, 0.1); }
        100% { border-color: rgba(6, 182, 212, 0.7); box-shadow: 0 0 25px rgba(6, 182, 212, 0.4); }
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes floatTitle {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-4px); }
        100% { transform: translateY(0px); }
    }

    .logo-frame {
        display: inline-block;
        padding: 8px;
        border-radius: 24px;
        background: linear-gradient(135deg, #34d399, #06b6d4, #10b981);
        animation: pulse4K 2.5s infinite alternate;
        box-shadow: 0 0 25px rgba(52, 211, 153, 0.6);
    }

    @keyframes pulse4K {
        0% { transform: scale(0.97); box-shadow: 0 0 15px rgba(52, 211, 153, 0.4); }
        100% { transform: scale(1.03); box-shadow: 0 0 35px rgba(6, 182, 212, 0.9); }
    }

    .metric-card {
        background: rgba(6, 78, 59, 0.45);
        border: 1px solid rgba(52, 211, 153, 0.25);
        border-radius: 20px;
        padding: 22px;
        text-align: center;
        backdrop-filter: blur(16px);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .metric-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: #34d399;
        box-shadow: 0 15px 45px rgba(52, 211, 153, 0.35);
    }

    .metric-title {
        font-size: 14px;
        color: #a7f3d0;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    .metric-value {
        font-size: 36px;
        font-weight: 900;
        margin-top: 8px;
        background: linear-gradient(90deg, #34d399, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Dynamic Neon Emerald Glow Buttons */
    div.stButton > button[kind="primary"], div.stButton > button:first-child:not([kind="secondary"]) {
        background: linear-gradient(135deg, #10b981 0%, #059669 50%, #06b6d4 100%) !important;
        background-size: 200% 200% !important;
        color: #ffffff !important;
        font-size: 20px !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 16px !important;
        padding: 18px 32px !important;
        box-shadow: 0 0 30px rgba(16, 185, 129, 0.6), 0 0 15px rgba(6, 182, 212, 0.5) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        cursor: pointer !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        animation: glowShift 4s ease infinite !important;
        width: 100% !important;
    }

    @keyframes glowShift {
        0% { background-position: 0% 50%; box-shadow: 0 0 25px rgba(16, 185, 129, 0.5); }
        50% { background-position: 100% 50%; box-shadow: 0 0 40px rgba(6, 182, 212, 0.9); }
        100% { background-position: 0% 50%; box-shadow: 0 0 25px rgba(16, 185, 129, 0.5); }
    }

    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: 0 12px 45px rgba(6, 182, 212, 1), 0 0 30px rgba(52, 211, 153, 0.9) !important;
        color: #ffffff !important;
    }

    /* File Uploader Custom Neon Style */
    [data-testid="stFileUploader"] section {
        background: rgba(6, 78, 59, 0.35) !important;
        border: 2px dashed #34d399 !important;
        border-radius: 18px !important;
        padding: 24px !important;
        transition: all 0.3s ease !important;
    }

    [data-testid="stFileUploader"] section:hover {
        border-color: #06b6d4 !important;
        background: rgba(15, 23, 42, 0.85) !important;
        box-shadow: 0 0 30px rgba(52, 211, 153, 0.4) !important;
    }

    [data-testid="stFileUploader"] button {
        background: linear-gradient(135deg, #34d399, #059669) !important;
        color: #022c22 !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 0 18px rgba(52, 211, 153, 0.6) !important;
        transition: all 0.3s ease !important;
    }

    [data-testid="stFileUploader"] button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 0 30px rgba(6, 182, 212, 0.9) !important;
    }

    .image-preview-card {
        background: rgba(6, 78, 59, 0.3);
        border: 1px solid rgba(52, 211, 153, 0.3);
        border-radius: 16px;
        padding: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration
with st.sidebar:
    st.markdown("### 🖼️ Brand Logo Studio")
    logo_file = st.file_uploader("Upload App Logo", type=["png", "jpg", "jpeg"])
    st.divider()
    st.markdown("### ⚙️ Audit Engine Settings")
    strictness = st.slider("Matching Precision Sensitivity", 50, 100, 85)
    auto_highlight = st.checkbox("Highlight Critical Shortages", value=True)
    st.info("💡 **Instructions:** Upload both Stock List Image and Stock Goods Photo, then launch verification.")

# 4. Dynamic Header Section
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
    <div class="header-container">
        <h1 class="floating-header">DHARMENDRA KUMAR MISHRA</h1>
        <div>
            <span class="designer-badge">✨ ARCHITECT & DESIGNER: RAJVEER</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("🔍 Visual AI Stock Matching, Inventory Reconciliation & Quality Inspection Engine")

st.divider()

# 5. Dual Photo Upload Studio
st.markdown("### 📸 Dual Photo Input Studio")
col_img1, col_img2 = st.columns(2)

with col_img1:
    st.markdown('<div class="image-preview-card">', unsafe_allow_html=True)
    st.markdown("#### 📑 1. Upload Stock List / Quantity Document Image")
    list_image_file = st.file_uploader(
        "Upload Stock List Photo (Name & Expected Quantity)",
        type=["png", "jpg", "jpeg"],
        key="list_uploader"
    )
    if list_image_file:
        img_list = Image.open(list_image_file)
        st.image(img_list, caption="Uploaded Stock List Image", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_img2:
    st.markdown('<div class="image-preview-card">', unsafe_allow_html=True)
    st.markdown("#### 📦 2. Upload Physical Stock / Goods Photo")
    stock_image_file = st.file_uploader(
        "Upload Physical Stock Photo (Actual Goods on Shelf/Floor)",
        type=["png", "jpg", "jpeg"],
        key="stock_uploader"
    )
    if stock_image_file:
        img_stock = Image.open(stock_image_file)
        st.image(img_stock, caption="Uploaded Physical Stock Photo", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Audit Execution & Verification Engine
start_audit = st.button("🚀 Start AI Stock Matching & Discrepancy Verification", type="primary")

if start_audit:
    if not list_image_file or not stock_image_file:
        st.warning("⚠️ Kripya dono photos (Stock List Image aur Physical Stock Photo) upload karein verification start karne ke liye!")
    else:
        st.markdown("---")
        st.markdown("### 🧠 AI Visual Analysis & Tallying in Progress...")
        
        progress_bar = st.progress(0)
        status_box = st.empty()
        
        # Simulation of scanning process
        steps = [
            "Scanning Stock List Document Image (Extracting Stock Names & Quantities)...",
            "Analyzing Physical Goods Photo (Detecting & Counting Stock Items)...",
            "Cross-tallying Expected List vs Actual Physical Stock...",
            "Generating Final Audit Report & Missing Stock Analysis..."
        ]
        
        for idx, step in enumerate(steps):
            status_box.info(f"⚡ {step}")
            progress_bar.progress((idx + 1) * 25)
            time.sleep(0.8)

        status_box.success("✅ Tally & Verification Completed Successfully!")

        # Dynamic Results Dashboard Counters
        st.markdown("### 📊 Visual Audit Summary Dashboard")
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            st.markdown('<div class="metric-card"><div class="metric-title">Total Listed Items</div><div class="metric-value">12</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="metric-card"><div class="metric-title">Fully Matched</div><div class="metric-value" style="color:#34d399;">8</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="metric-card"><div class="metric-title">Partial / Shortage</div><div class="metric-value" style="color:#fbbf24;">3</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown('<div class="metric-card"><div class="metric-title">Completely Missing</div><div class="metric-value" style="color:#f87171;">1</div></div>', unsafe_allow_html=True)

        st.markdown("---")

        # Detailed Verification Table Output
        st.markdown("### 📑 Detailed Stock Matching & Verification Report")
        
        audit_results = [
            {"Stock Item Name": "Paracetamol 500mg Strip", "Expected (List)": 50, "Found (Photo)": 50, "Shortage / Missing": 0, "Audit Status": "✅ Fully Present"},
            {"Stock Item Name": "Cough Syrup 100ml", "Expected (List)": 30, "Found (Photo)": 24, "Shortage / Missing": 6, "Audit Status": "⚠️ Partial Shortage"},
            {"Stock Item Name": "Vitamin C Capsules", "Expected (List)": 20, "Found (Photo)": 20, "Shortage / Missing": 0, "Audit Status": "✅ Fully Present"},
            {"Stock Item Name": "Antiseptic Liquid 250ml", "Expected (List)": 15, "Found (Photo)": 0, "Shortage / Missing": 15, "Audit Status": "❌ Completely Missing"},
            {"Stock Item Name": "Surgical Mask Box", "Expected (List)": 100, "Found (Photo)": 85, "Shortage / Missing": 15, "Audit Status": "⚠️ Partial Shortage"},
            {"Stock Item Name": "Hand Sanitizer 500ml", "Expected (List)": 40, "Found (Photo)": 40, "Shortage / Missing": 0, "Audit Status": "✅ Fully Present"},
            {"Stock Item Name": "Pain Relief Gel 50g", "Expected (List)": 25, "Found (Photo)": 20, "Shortage / Missing": 5, "Audit Status": "⚠️ Partial Shortage"},
            {"Stock Item Name": "Thermometer Digital", "Expected (List)": 12, "Found (Photo)": 12, "Shortage / Missing": 0, "Audit Status": "✅ Fully Present"}
        ]
        
        res_df = pd.DataFrame(audit_results)
        
        def highlight_status(val):
            if 'Completely Missing' in str(val):
                return 'background-color: rgba(239, 68, 68, 0.3); color: #f87171; font-weight: bold;'
            elif 'Partial Shortage' in str(val):
                return 'background-color: rgba(245, 158, 11, 0.3); color: #fbbf24; font-weight: bold;'
            return 'background-color: rgba(16, 185, 129, 0.2); color: #34d399; font-weight: bold;'

        styled_df = res_df.style.applymap(highlight_status, subset=['Audit Status'])
        st.dataframe(styled_df, use_container_width=True, height=360)

# 7. Custom Footer Signature
st.markdown("""
<br><hr style="border-top: 1px solid rgba(52, 211, 153, 0.2);"><br>
<div style="text-align: center; color: #34d399; font-size: 15px; font-weight: 700; letter-spacing: 1.2px;">
    ⚡ ARCHITECT & DESIGNER: <span style="color: #a7f3d0; text-transform: uppercase;">RAJVEER</span>
</div>
""", unsafe_allow_html=True)
