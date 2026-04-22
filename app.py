import streamlit as st
import base64

st.set_page_config(layout="wide")

# ---------------- COLORS ----------------
BG = "#f6f4ef"
CARD_BG = "#ffffff"
BORDER = "#e7e2d9"
BRAND_BLACK = "#1f1f1f"
BRAND_GOLD = "#b89b5e"
TEXT_MUTED = "#6b7280"

# ---------------- LOGO ----------------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo = get_base64("INDER-Logo-RGB.png")

# ---------------- CSS ----------------
st.markdown(f"""
<style>

.main {{
    background-color: {BG};
}}

.block-container {{
    max-width: 1650px;
}}

.brand-header {{
    background: {CARD_BG};
    border-radius: 22px;
    padding: 25px;
    border: 1px solid {BORDER};
    margin-bottom: 20px;
}}

.brand-title {{
    font-size: 38px;
    font-weight: 800;
    color: {BRAND_BLACK};
}}

.brand-sub {{
    color: {TEXT_MUTED};
    font-size: 14px;
}}

.kpi {{
    background: {CARD_BG};
    padding: 22px;
    border-radius: 18px;
    border: 1px solid {BORDER};
    min-height: 130px;
}}

.kpi-title {{
    font-size: 14px;
    color: {TEXT_MUTED};
}}

.kpi-value {{
    font-size: 32px;
    font-weight: 800;
    color: {BRAND_BLACK};
}}

.section {{
    background: {CARD_BG};
    padding: 20px;
    border-radius: 18px;
    border: 1px solid {BORDER};
    margin-top: 20px;
}}

.group-card {{
    padding: 20px;
    border-radius: 18px;
    color: white;
    font-weight: 600;
    margin-bottom: 15px;
    cursor: pointer;
    text-align:center;
    font-size:18px;
}}

.g1 {{ background: linear-gradient(135deg,#2c3e50,#4ca1af); }}
.g2 {{ background: linear-gradient(135deg,#c0392b,#8e44ad); }}
.g3 {{ background: linear-gradient(135deg,#16a085,#27ae60); }}
.g4 {{ background: linear-gradient(135deg,#d35400,#f39c12); }}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(f"""
<div class="brand-header">
    <div style="display:flex;align-items:center;gap:20px;">
        <img src="data:image/png;base64,{logo}" style="height:80px;">
        <div>
            <div class="brand-title">Türkiye İnşaat Tedarik Sınıflandırma Sistemi</div>
            <div class="brand-sub">MasterFormat Tabanlı • İNDER Projesi</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- KPI ----------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown('<div class="kpi"><div class="kpi-title">Toplam Grup</div><div class="kpi-value">20</div></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="kpi"><div class="kpi-title">Alt Grup</div><div class="kpi-value">150+</div></div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="kpi"><div class="kpi-title">Ürün Kalemi</div><div class="kpi-value">500+</div></div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="kpi"><div class="kpi-title">Sistem Durumu</div><div class="kpi-value">Aktif</div></div>', unsafe_allow_html=True)

# ---------------- GROUPS ----------------
st.markdown('<div class="section"><b>MasterFormat Grupları</b></div>', unsafe_allow_html=True)

cols = st.columns(4)

groups = [
("01 Genel Şartlar","g1"),
("02 Mevcut Koşullar","g2"),
("03 Beton","g3"),
("04 Duvar","g4"),
("05 Metaller","g1"),
("06 Ahşap","g2"),
("07 Isı Yalıtım","g3"),
("08 Kapı Pencere","g4")
]

for i,(g,cls) in enumerate(groups):
    with cols[i%4]:
        st.markdown(f'<div class="group-card {cls}">{g}</div>', unsafe_allow_html=True)
