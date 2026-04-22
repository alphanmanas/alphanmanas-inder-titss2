import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Türkiye İnşaat Tedarik Sınıflandırma Sistemi",
    page_icon="🏗️",
    layout="wide"
)

# -----------------------------
# DATA (20 GRUP)
# -----------------------------
DATA = {
    "01 – Genel & Şantiye": {
        "Geçici Yapılar": ["Konteyner Ofis", "Geçici Depo", "Geçici Barınma"],
        "İskele": ["Cephe İskele", "Mobil İskele", "Kalıp İskele"],
    },
    "02 – Zemin & Temel": {
        "Kazı": ["Genel Kazı", "Kaya Kazı"],
        "Dolgu": ["Stabilize", "Kırmataş"],
    },
    "03 – Beton": {
        "Hazır Beton": ["C25", "C30", "C35"],
        "Prekast": ["Panel", "Kiriş"],
    },
    "04 – Duvar": {"Tuğla": ["Dolu", "Delikli"], "Gazbeton": ["Blok"]},
    "05 – Metal & Çelik": {"Demir": ["B420C"], "Profil": ["IPE"]},
    "06 – Ahşap": {"MDF": ["Ham", "Lamine"]},
    "07 – İzolasyon": {"Membran": ["PVC", "Bitüm"]},
    "08 – Kapı & Pencere": {"PVC": ["Pencere"], "Alüminyum": ["Doğrama"]},
    "09 – Kaplama": {"Seramik": ["Zemin"], "Boya": ["İç Cephe"]},
    "10 – Sabit Donatılar": {"Mutfak": ["Dolap"]},
    "11 – Sistemler": {"Asansör": ["Yolcu"]},
    "12 – Mobilya": {"Ofis": ["Masa"]},
    "13 – Endüstriyel": {"Ekipman": ["Makine"]},
    "14 – Cephe": {"Cam": ["Temperli"]},
    "15 – Mekanik": {"VRF": ["Sistem"]},
    "16 – Tesisat": {"Boru": ["PPRC"]},
    "17 – Elektrik": {"Kablo": ["NYY"]},
    "18 – Dijital": {"CCTV": ["Kamera"]},
    "19 – Peyzaj": {"Sulama": ["Sistem"]},
    "20 – Enerji": {"Güneş": ["Panel"]}
}

# -----------------------------
# SESSION
# -----------------------------
if "group" not in st.session_state:
    st.session_state.group = None
if "sub" not in st.session_state:
    st.session_state.sub = None

# -----------------------------
# STYLE
# -----------------------------
st.markdown("""
<style>
body {background: #f5f6f8;}
.main-title {font-size:34px; font-weight:800; color:#111;}
.sub-title {color:#6b7280;}
.card {
    background:white;
    padding:20px;
    border-radius:16px;
    box-shadow:0 8px 20px rgba(0,0,0,0.05);
    text-align:center;
}
.big-btn button {
    height:110px !important;
    font-weight:700;
    border-radius:16px;
    background: linear-gradient(135deg,#991b1b,#1f2937);
    color:white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER (LOGO FIXED)
# -----------------------------
col1, col2 = st.columns([1.2, 4])

with col1:
    st.image("INDER-Logo-RGB.png", width=380)

with col2:
    st.markdown('<div class="main-title">Türkiye İnşaat Tedarik Sınıflandırma Sistemi</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">MasterFormat tabanlı premium dashboard</div>', unsafe_allow_html=True)

# -----------------------------
# METRICS
# -----------------------------
m1, m2, m3 = st.columns(3)

m1.markdown(f'<div class="card"><b>Grup</b><br>{len(DATA)}</div>', unsafe_allow_html=True)
m2.markdown(f'<div class="card"><b>SUB</b><br>{sum(len(v) for v in DATA.values())}</div>', unsafe_allow_html=True)
m3.markdown(f'<div class="card"><b>VAR</b><br>{sum(len(x) for v in DATA.values() for x in v.values())}</div>', unsafe_allow_html=True)

# -----------------------------
# GROUPS
# -----------------------------
st.subheader("Gruplar")

groups = list(DATA.keys())

for i in range(0, len(groups), 4):
    cols = st.columns(4)
    for j, g in enumerate(groups[i:i+4]):
        with cols[j]:
            if st.button(g, key=g):
                st.session_state.group = g
                st.session_state.sub = None

# -----------------------------
# SUB
# -----------------------------
if st.session_state.group:
    st.subheader(st.session_state.group)

    for sub in DATA[st.session_state.group]:
        if st.button(sub):
            st.session_state.sub = sub

# -----------------------------
# VAR
# -----------------------------
if st.session_state.group and st.session_state.sub:
    st.subheader(st.session_state.sub)

    for item in DATA[st.session_state.group][st.session_state.sub]:
        st.markdown(f"• {item}")
