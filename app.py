import streamlit as st
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="STOCKS QUANTITY COUNTER - DHARMENDRA KUMAR (MISHRA)",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Original Cyberpunk Neon Emerald Dynamic CSS Theme
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
        text-transform: uppercase;
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

    div.stButton > button[kind="primary"], div.stButton > button:first-child:not([kind="secondary"]) {
        background: linear-gradient(135deg, #10b981 0%, #059669 50%, #06b6d4 100%) !important;
        background-size: 200% 200% !important;
        color: #ffffff !important;
        font-size: 16px !important;
        font-weight: 800 !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 12px 24px !important;
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.5) !important;
        transition: all 0.4s ease !important;
        text-transform: uppercase !important;
    }

    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 10px 30px rgba(6, 182, 212, 0.8) !important;
    }

    [data-testid="stFileUploader"] section {
        background: rgba(6, 78, 59, 0.4) !important;
        border: 2px dashed #34d399 !important;
        border-radius: 14px !important;
        padding: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Dynamic Header Section
col_logo, col_title = st.columns([1, 5])

with col_logo:
    st.markdown('<div class="logo-frame" style="font-size: 50px; padding: 10px 20px;">📦</div>', unsafe_allow_html=True)

with col_title:
    st.markdown("""
    <div class="header-container">
        <h1 class="floating-header">STOCKS QUANTITY COUNTER</h1>
        <div>
            <span class="designer-badge">✨ ARCHITECT & DESIGNER: DHARMENDRA KUMAR (MISHRA)</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("📋 Easy Stock Entry, Image Attachment, Quantity Counting & Missing Items Track Engine")

st.divider()

# Session State Initialization for Items
if 'stock_items' not in st.session_state:
    st.session_state['stock_items'] = []

# 4. Add New Stock Entry Section
st.markdown("### ➕ नया स्टॉक आइटम दर्ज करें (Add New Stock Entry)")

with st.form("stock_entry_form", clear_on_submit=True):
    col1, col2, col3 = st.columns([3, 2, 2])
    
    with col1:
        item_name = st.text_input("📦 सामान का नाम (Stock / Item Name)", placeholder="उदा: Laptop, Cable, Chair...")
    with col2:
        item_qty = st.number_input("🔢 मात्रा (Quantity)", min_value=0, value=1, step=1)
    with col3:
        status = st.selectbox("📌 स्थिति (Status)", ["उपलब्ध (Available)", "मिसिंग / कम है (Missing)", "खराब / डैमेज (Damaged)"])

    col_img, col_notes = st.columns([3, 4])
    with col_img:
        stock_photo = st.file_uploader("📷 स्टॉक फोटो अपलोड करें (Upload Image)", type=["png", "jpg", "jpeg"])
    with col_notes:
        notes = st.text_input("📝 टिप्पणी / विवरण (Notes)", placeholder="उदा: Rack No. 3 में रखा है / 2 पीस कम हैं")

    submit_btn = st.form_submit_button("➕ स्टॉक लिस्ट में जोड़ें (Add Stock Item)")

    if submit_btn:
        if item_name.strip() == "":
            st.warning("⚠️ कृपया सामान का नाम दर्ज करें!")
        else:
            st.session_state['stock_items'].append({
                "ID": len(st.session_state['stock_items']) + 1,
                "Item Name": item_name.strip(),
                "Quantity": item_qty,
                "Status": status,
                "Photo": stock_photo,
                "Notes": notes.strip() if notes else "N/A"
            })
            st.success(f"✅ '{item_name}' सफलतापूर्वक जोड़ दिया गया!")

st.markdown("---")

# 5. Dashboard Summary Metrics
total_items = len(st.session_state['stock_items'])
total_quantity = sum([item['Quantity'] for item in st.session_state['stock_items']])
missing_count = sum([1 for item in st.session_state['stock_items'] if "मिसिंग" in item['Status']])
damaged_count = sum([1 for item in st.session_state['stock_items'] if "डैमेज" in item['Status']])

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f'<div class="metric-card"><div class="metric-title">कुल आइटम (Unique Items)</div><div class="metric-value">{total_items}</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="metric-card"><div class="metric-title">कुल स्टॉक मात्रा (Total Qty)</div><div class="metric-value" style="color:#34d399;">{total_quantity}</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="metric-card"><div class="metric-title">मिसिंग सामान (Missing)</div><div class="metric-value" style="color:#f87171;">{missing_count}</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown(f'<div class="metric-card"><div class="metric-title">डैमेज आइटम (Damaged)</div><div class="metric-value" style="color:#fbbf24;">{damaged_count}</div></div>', unsafe_allow_html=True)

st.markdown("---")

# 6. Display Stock List & Image Table
st.markdown("### 📄 स्टॉक एवं क्वांटिटी लिस्ट (Stock Counter List)")

if len(st.session_state['stock_items']) == 0:
    st.info("ℹ️ अभी तक कोई स्टॉक ऐड नहीं किया गया है। ऊपर दिए गए फ़ॉर्म से सामान की डिटेल भरें।")
else:
    # Table Header
    h1, h2, h3, h4, h5, h6 = st.columns([1, 3, 2, 2, 2, 3])
    h1.markdown("**क्रमांक**")
    h2.markdown("**सामान का नाम (Stock)**")
    h3.markdown("**मात्रा (Qty)**")
    h4.markdown("**स्थिति (Status)**")
    h5.markdown("**फोटो (Photo)**")
    h6.markdown("**टिप्पणी (Notes)**")
    st.markdown("<hr style='margin:4px 0; border-color:rgba(52, 211, 153, 0.3);'>", unsafe_allow_html=True)

    # Loop Items
    for idx, item in enumerate(st.session_state['stock_items']):
        col1, col2, col3, col4, col5, col6 = st.columns([1, 3, 2, 2, 2, 3])
        
        col1.write(f"#{idx + 1}")
        col2.markdown(f"**{item['Item Name']}**")
        col3.write(f"{item['Quantity']} Pcs")
        
        # Color coding for Status
        if "मिसिंग" in item['Status']:
            col4.markdown(f"<span style='color:#f87171; font-weight:bold;'>❌ {item['Status']}</span>", unsafe_allow_html=True)
        elif "डैमेज" in item['Status']:
            col4.markdown(f"<span style='color:#fbbf24; font-weight:bold;'>⚠️ {item['Status']}</span>", unsafe_allow_html=True)
        else:
            col4.markdown(f"<span style='color:#34d399; font-weight:bold;'>✅ {item['Status']}</span>", unsafe_allow_html=True)

        if item['Photo'] is not None:
            col5.image(item['Photo'], width=80)
        else:
            col5.caption("कोई फोटो नहीं")

        col6.write(item['Notes'])
        st.markdown("<hr style='margin:4px 0; border-color:rgba(255,255,255,0.05);'>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🗑️ पूरी लिस्ट रीसेट करें (Clear All Items)"):
        st.session_state['stock_items'] = []
        st.experimental_rerun()

# 7. Footer
st.markdown("""
<br><hr style="border-top: 1px solid rgba(52, 211, 153, 0.2);"><br>
<div style="text-align: center; color: #34d399; font-size: 14px; font-weight: 700; letter-spacing: 1px;">
    ⚡ Designed & Developed by <span style="color: #a7f3d0;">Dharmendra Kumar (Mishra)</span>
</div>
""", unsafe_allow_html=True)
  
