import streamlit as st
import pandas as pd
import time
from PIL import Image
import json
import re

# 1. Page Configuration
st.set_page_config(
    page_title="DHARMENDRA KUMAR MISHRA - AI Stock Auditor",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Fixed Dynamic Neon Cyberpunk Emerald Styling
st.markdown("""
<style>
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

    [data-testid="stFileUploader"] section button {
        background-color: #065f46 !important;
        color: #ffffff !important;
        border: 1px solid #34d399 !important;
        border-radius: 10px !important;
        font-weight: 800 !important;
        padding: 8px 16px !important;
        box-shadow: 0 0 10px rgba(52, 211, 153, 0.3) !important;
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
    gemini_api_key = st.text_input("Google Gemini API Key", type="password", help="Enter API Key for live real OCR reading.")
    st.info("💡 **Strict Document Matching Mode:** Reads full product list without skipping items.")

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
    st.caption("🔍 Visual AI Deep OCR Stock Matching, Missing Item Details & Quantity Auditor")

st.divider()

# 5. Dual Photo Upload Studio
st.markdown("<h3 class='section-title'>📸 Dual Photo Input Studio</h3>", unsafe_allow_html=True)
col_img1, col_img2 = st.columns(2)

with col_img1:
    st.markdown('<div class="image-preview-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #a7f3d0;'>📑 1. Upload Stock List Image</h4>", unsafe_allow_html=True)
    list_image_file = st.file_uploader(
        "Upload Stock List Photo (With Product Name, Batch No & Expected Pcs)",
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
        "Upload Physical Stock Photo (Showing Visible Pieces & Product Packages)",
        type=["png", "jpg", "jpeg"],
        key="stock_uploader"
    )
    if stock_image_file:
        img_stock = Image.open(stock_image_file)
        st.image(img_stock, caption="Uploaded Physical Stock Photo", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Ultra-Accurate Gemini Vision AI Processing Engine
def process_images_with_vision_ai(api_key, list_img, stock_img):
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        
        strict_audit_prompt = """
        You are an Expert Optical Character Recognition (OCR) and Physical Inventory Verification Specialist.
        Analyze Image 1 (Stock List/Invoice Document) and Image 2 (Physical Goods Photo).

        STRICT INSTRUCTIONS:
        1. READ EVERY SINGLE ITEM listed in Image 1 from top to bottom. Do not omit, skip, or merge any product rows. Count every listed item accurately.
        2. For EACH item in Image 1, extract:
           - "Product Name": Exact full product title/description as written on the document.
           - "Batch No": Extract the Batch / Lot Number if visible. If not specified, write "N/A".
           - "Expected (Pcs)": Exact numerical quantity/pcs listed on Image 1.
        3. Now check Image 2 (Physical Goods Photo):
           - "Found (Pcs)": Count how many actual pieces/boxes for this exact product are visually visible in Image 2.
        4. Calculate Discrepancy:
           - "Missing Quantity": Subtract Found from Expected. Format as "X Pcs Short" or "0 Pcs" or "All X Pcs Missing".
           - "Audit Status":
             * "✅ Fully Present" (if Found == Expected)
             * "⚠️ Partial Shortage" (if Found > 0 and Found < Expected)
             * "❌ Completely Missing" (if Found == 0)

        OUTPUT REQUIREMENT:
        Return ONLY valid JSON format. An array of objects matching the exact keys:
        [
          {
            "Product Name": "Exact Name From List",
            "Batch No": "Batch Number or N/A",
            "Expected (Pcs)": 10,
            "Found (Pcs)": 8,
            "Missing Quantity": "2 Pcs Short",
            "Audit Status": "⚠️ Partial Shortage"
          }
        ]
        Do not add any text, intro, or markdown code block formatting like ```json.
        """
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[strict_audit_prompt, list_img, stock_img]
        )
        
        raw_text = response.text.strip()
        clean_json = re.sub(r'^```json\s*|^```\s*|\s*```$', '', raw_text, flags=re.MULTILINE).strip()
        data = json.loads(clean_json)
        return pd.DataFrame(data), None
    except Exception as e:
        return None, str(e)

# 7. Verification Execution Trigger
start_audit = st.button("🚀 Start AI Deep OCR & Missing Stock Verification", type="primary")

if start_audit:
    if not list_image_file or not stock_image_file:
        st.warning("⚠️ Kripya dono photos (Stock List Image aur Physical Stock Photo) upload karein verification start karne ke liye!")
    elif not gemini_api_key:
        st.error("⚠️ Please enter your Google Gemini API Key in the sidebar to perform real-time OCR reading!")
    else:
        st.markdown("---")
        st.markdown("<h3 class='section-title'>🧠 Real-Time Document Reading & Physical Stock OCR in Progress...</h3>", unsafe_allow_html=True)
        
        progress_bar = st.progress(0)
        status_box = st.empty()
        
        steps = [
            "Reading every single line and product name from the stock document...",
            "Extracting exact Batch Numbers and expected quantities (Pcs)...",
            "Cross-matching physical count from goods photo...",
            "Calculating exact missing items & building table..."
        ]
        
        for idx, step in enumerate(steps):
            status_box.info(f"⚡ {step}")
            progress_bar.progress((idx + 1) * 25)
            time.sleep(0.3)

        img_l = Image.open(list_image_file)
        img_s = Image.open(stock_image_file)
        
        res_df, err_msg = process_images_with_vision_ai(gemini_api_key, img_l, img_s)
            
        if err_msg:
            st.error(f"⚠️ OCR Reading Error: {err_msg}. Kripya Gemini API Key aur Image Quality check karein.")
        elif res_df is not None and not res_df.empty:
            status_box.success(f"✅ Real-Time OCR Completed! Successfully read {len(res_df)} listed products.")

            total_items = len(res_df)
            fully_present = len(res_df[res_df['Audit Status'].str.contains('Fully', case=False, na=False)])
            partial_shortage = len(res_df[res_df['Audit Status'].str.contains('Partial', case=False, na=False)])
            completely_missing = len(res_df[res_df['Audit Status'].str.contains('Missing', case=False, na=False)])

            st.markdown("<h3 class='section-title'>📊 Visual Audit Summary Dashboard</h3>", unsafe_allow_html=True)
            c1, c2, c3, c4 = st.columns(4)
            
            with c1:
                st.markdown(f'<div class="metric-card"><div class="metric-title">Total Listed Products</div><div class="metric-value">{total_items}</div></div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f'<div class="metric-card"><div class="metric-title">Fully Matched</div><div class="metric-value" style="color:#34d399;">{fully_present}</div></div>', unsafe_allow_html=True)
            with c3:
                st.markdown(f'<div class="metric-card"><div class="metric-title">Partial Shortage</div><div class="metric-value" style="color:#fbbf24;">{partial_shortage}</div></div>', unsafe_allow_html=True)
            with c4:
                st.markdown(f'<div class="metric-card"><div class="metric-title">Completely Missing</div><div class="metric-value" style="color:#f87171;">{completely_missing}</div></div>', unsafe_allow_html=True)

            st.markdown("---")

            st.markdown("<h3 class='section-title'>📑 Accurate Product Name, Batch No & Missing Stock Report</h3>", unsafe_allow_html=True)
            
            def highlight_status(val):
                if 'Missing' in str(val) or '❌' in str(val):
                    return 'background-color: rgba(239, 68, 68, 0.45); color: #fca5a5; font-weight: bold;'
                elif 'Partial' in str(val) or '⚠️' in str(val):
                    return 'background-color: rgba(245, 158, 11, 0.45); color: #fde047; font-weight: bold;'
                return 'background-color: rgba(16, 185, 129, 0.35); color: #6ee7b7; font-weight: bold;'

            styled_df = res_df.style.map(highlight_status, subset=['Audit Status'])
            st.dataframe(styled_df, use_container_width=True, height=420)

# 8. Footer Signature
st.markdown("""
<br><hr style="border-top: 1px solid rgba(52, 211, 153, 0.3);"><br>
<div style="text-align: center; color: #34d399; font-size: 16px; font-weight: 800; letter-spacing: 1.5px; text-shadow: 0 0 10px rgba(52, 211, 153, 0.5);">
    ⚡ ARCHITECT & DESIGNER: <span style="color: #67e8f9; text-transform: uppercase;">RAJVEER</span>
</div>
""", unsafe_allow_html=True)
