import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Türkiye İnşaat Tedarik Sınıflandırma Sistemi",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# DATA
# =========================================================
DATA = {
    "01 – Genel & Şantiye": {
        "Geçici Yapılar": ["Konteyner Ofis", "Geçici Depo", "Geçici Barınma Ünitesi"],
        "İskele": ["Cephe İskelesi", "Mobil İskele", "Kalıp İskelesi"],
        "Şantiye Ekipmanları": ["Jeneratör", "Kompresör", "Aydınlatma Kulesi"],
    },
    "02 – Zemin & Temel": {
        "Kazı": ["Genel Kazı", "Kaya Kazısı", "Makinalı Kazı"],
        "Dolgu": ["Kırmataş Dolgu", "Stabilize Dolgu", "Sıkıştırılmış Dolgu"],
        "Zemin İyileştirme": ["Jet Grout", "Fore Kazık", "Enjeksiyon"],
    },
    "03 – Beton": {
        "Hazır Beton": ["C25", "C30", "C35", "C40"],
        "Prekast": ["Prekast Kiriş", "Prekast Döşeme", "Prekast Panel"],
        "Katkı Kimyasalları": ["Akışkanlaştırıcı", "Priz Geciktirici", "Su Yalıtım Katkısı"],
    },
    "04 – Duvar & Masonry": {
        "Tuğla": ["Dolu Tuğla", "Delikli Tuğla", "Asmolen"],
        "Gazbeton": ["Blok", "Panel", "Lento"],
        "Taş": ["Doğal Taş Kaplama", "Kesme Taş", "Dekoratif Taş"],
    },
    "05 – Metal & Çelik": {
        "İnşaat Demiri": ["B420C", "Nervürlü Demir", "Hasır Çelik"],
        "Profil Çelik": ["IPE", "HEA", "Kutu Profil"],
        "Ankraj": ["Kimyasal Ankraj", "Mekanik Ankraj", "Ağır Yük Ankrajı"],
    },
    "06 – Ahşap & Kompozit": {
        "Ahşap Yapı": ["Lamine Ahşap", "Masif Ahşap", "Çatı Kirişi"],
        "MDF": ["Ham MDF", "Lamine MDF", "Neme Dayanıklı MDF"],
        "CLT": ["CLT Panel", "CLT Döşeme", "CLT Duvar"],
    },
    "07 – İzolasyon & Su Yalıtımı": {
        "Membran": ["PVC Membran", "Bitümlü Membran", "EPDM Membran"],
        "Poliüretan": ["Sprey Köpük", "Likit Membran", "Dolgu Köpüğü"],
        "Bitüm": ["Bitümlü Örtü", "Soğuk Uygulama", "Sıcak Uygulama"],
    },
    "08 – Kapı & Pencere": {
        "Alüminyum": ["Alüminyum Doğrama", "Sürme Sistem", "Isı Yalıtımlı Doğrama"],
        "PVC": ["PVC Pencere", "PVC Kapı", "Sürme PVC"],
        "Çelik Kapı": ["Daire Kapısı", "Yangın Kapısı", "Villa Kapısı"],
    },
    "09 – İç Kaplama (Finishes)": {
        "Boya": ["İç Cephe Boyası", "Dış Cephe Boyası", "Epoksi Boya"],
        "Seramik": ["Duvar Seramiği", "Zemin Seramiği", "Porselen"],
        "Parke": ["Laminat Parke", "Lamine Parke", "Masif Parke"],
    },
    "10 – Sabit Donatılar": {
        "Dolap": ["Gömme Dolap", "Vestiyer", "Arşiv Dolabı"],
        "Mutfak": ["Mutfak Dolabı", "Tezgâh", "Ankastre Modül"],
        "Banyo": ["Lavabo Ünitesi", "Duş Sistemi", "Gömme Rezervuar"],
    },
    "11 – Özel Sistemler": {
        "Asansör": ["Yolcu Asansörü", "Yük Asansörü", "Panoramik Asansör"],
        "Yürüyen Merdiven": ["İç Mekân", "Dış Mekân", "AVM Tipi"],
    },
    "12 – Mobilya": {
        "Ofis": ["Masa", "Toplantı Masası", "Dosya Dolabı"],
        "Sabit Mobilya": ["Resepsiyon Bankosu", "Sabit Tezgâh", "Özel Üretim Raf"],
    },
    "13 – Endüstriyel Sistemler": {
        "Fabrika Ekipmanları": ["Konveyör", "Endüstriyel Raf", "Makine Kaidesi"],
    },
    "14 – Dış Cephe": {
        "Giydirme Cephe": ["Stick Sistem", "Panel Sistem", "Spider Sistem"],
        "Cam Sistemleri": ["Low-E Cam", "Temperli Cam", "Lamine Cam"],
    },
    "15 – Mekanik (HVAC)": {
        "Chiller": ["Hava Soğutmalı", "Su Soğutmalı", "Scroll Chiller"],
        "VRF": ["Heat Pump", "Heat Recovery", "Mini VRF"],
        "Klima": ["Split Klima", "Kaset Tipi", "Salon Tipi"],
    },
    "16 – Tesisat": {
        "Boru": ["PPRC", "Çelik Boru", "PE Boru"],
        "Armatür": ["Batarya", "Vana", "Mix Armatür"],
        "Yangın": ["Sprinkler", "Yangın Dolabı", "Pompa"],
    },
    "17 – Elektrik": {
        "Kablo": ["NYY", "TTR", "Data Kablosu"],
        "Trafo": ["Kuru Tip", "Yağlı Tip", "Dağıtım Trafosu"],
        "Pano": ["Ana Dağıtım Panosu", "Kat Panosu", "Kompanzasyon Panosu"],
    },
    "18 – Zayıf Akım & Dijital": {
        "CCTV": ["IP Kamera", "NVR", "PTZ Kamera"],
        "Fiber": ["Fiber Kablo", "Patch Panel", "ODF"],
        "IoT": ["Sensör", "Gateway", "Akıllı Sayaç"],
    },
    "19 – Peyzaj & Altyapı": {
        "Bordür": ["Beton Bordür", "Granit Bordür", "Dekoratif Bordür"],
        "Sulama": ["Damla Sulama", "Sprink Sulama", "Kontrol Ünitesi"],
        "Kanalizasyon": ["Koruge Boru", "Muayene Bacası", "Rögar Kapağı"],
    },
    "20 – Enerji & Yeni Nesil": {
        "Güneş": ["PV Panel", "İnverter", "Taşıyıcı Konstrüksiyon"],
        "Batarya (MCAP dahil)": ["LFP Batarya", "MCAP Modül", "Enerji Depolama Kabini"],
        "Şarj Altyapısı": ["AC Şarj Ünitesi", "DC Hızlı Şarj", "Yük Yönetim Sistemi"],
    },
}

# =========================================================
# SESSION
# =========================================================
if "selected_group" not in st.session_state:
    st.session_state.selected_group = None

if "selected_sub" not in st.session_state:
    st.session_state.selected_sub = None

if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# =========================================================
# HELPERS
# =========================================================
def total_sub_count():
    return sum(len(subs) for subs in DATA.values())

def total_var_count():
    return sum(len(vars_) for subs in DATA.values() for vars_ in subs.values())

def filter_data(query: str):
    if not query:
        return DATA

    q = query.lower().strip()
    filtered = {}

    for group, subs in DATA.items():
        group_match = q in group.lower()
        matched_subs = {}

        for sub, vars_list in subs.items():
            sub_match = q in sub.lower()
            matched_vars = [v for v in vars_list if q in v.lower()]

            if sub_match:
                matched_subs[sub] = vars_list
            elif matched_vars:
                matched_subs[sub] = matched_vars

        if group_match:
            filtered[group] = subs
        elif matched_subs:
            filtered[group] = matched_subs

    return filtered

# =========================================================
# STYLE
# =========================================================
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: Inter, Arial, sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #f5f6f8 0%, #eef1f5 100%);
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #1f2937 100%);
    border-right: 1px solid rgba(255,255,255,0.05);
}

section[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

.block-container {
    max-width: 1540px;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

.hero-shell {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    border: 1px solid #e5e7eb;
    border-radius: 28px;
    box-shadow: 0 20px 45px rgba(15, 23, 42, 0.08);
    padding: 26px 28px;
    margin-bottom: 18px;
}

.hero-title {
    color: #111827;
    font-size: 2.25rem;
    font-weight: 800;
    line-height: 1.08;
    margin-bottom: 0.35rem;
}

.hero-subtitle {
    color: #6b7280;
    font-size: 1rem;
}

.logo-box {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 24px;
    padding: 18px;
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.06);
    min-height: 170px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.metric-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 20px 16px;
    text-align: center;
    box-shadow: 0 12px 28px rgba(15, 23, 42, 0.05);
}

.metric-label {
    color: #6b7280;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 8px;
}

.metric-value {
    color: #111827;
    font-size: 1.95rem;
    font-weight: 800;
}

.panel {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 24px;
    padding: 24px;
    margin-top: 18px;
    box-shadow: 0 14px 34px rgba(15, 23, 42, 0.06);
}

.panel-title {
    color: #111827;
    font-size: 1.28rem;
    font-weight: 800;
    margin-bottom: 12px;
}

.pathline {
    color: #6b7280;
    font-size: 0.94rem;
    margin-bottom: 10px;
}

.var-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    border-left: 6px solid #991b1b;
    border-radius: 14px;
    padding: 15px 16px;
    margin-bottom: 10px;
    font-weight: 700;
    color: #1f2937;
    box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
}

.sidebar-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 14px;
    margin-bottom: 14px;
}

.sidebar-title {
    font-size: 0.9rem;
    font-weight: 700;
    margin-bottom: 6px;
    color: #e5e7eb !important;
}

.sidebar-value {
    font-size: 1rem;
    font-weight: 600;
    color: #ffffff !important;
}

.search-note {
    color: #6b7280;
    font-size: 0.9rem;
    margin-top: 6px;
}

.stTextInput > div > div > input {
    border-radius: 14px;
    min-height: 46px;
}

.stButton > button {
    width: 100%;
    min-height: 112px;
    border-radius: 20px;
    border: none;
    font-weight: 800;
    font-size: 1.02rem;
    color: white;
    background: linear-gradient(135deg, #991b1b 0%, #1f2937 100%);
    box-shadow: 0 14px 28px rgba(31, 41, 55, 0.14);
    transition: all 0.18s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    color: white;
    opacity: 0.97;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR / USER PANEL
# =========================================================
with st.sidebar:
    st.markdown("## Kullanıcı Paneli")
    st.markdown(
        """
        <div class="sidebar-card">
            <div class="sidebar-title">Kullanıcı</div>
            <div class="sidebar-value">İNDER Demo Kullanıcısı</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class="sidebar-card">
            <div class="sidebar-title">Tarih</div>
            <div class="sidebar-value">{datetime.now().strftime("%d.%m.%Y")}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class="sidebar-card">
            <div class="sidebar-title">Ana Grup</div>
            <div class="sidebar-value">{len(DATA)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class="sidebar-card">
            <div class="sidebar-title">SUB Sayısı</div>
            <div class="sidebar-value">{total_sub_count()}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class="sidebar-card">
            <div class="sidebar-title">VAR Sayısı</div>
            <div class="sidebar-value">{total_var_count()}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    selected_label = st.session_state.selected_group if st.session_state.selected_group else "Seçilmedi"
    st.markdown(
        f"""
        <div class="sidebar-card">
            <div class="sidebar-title">Aktif Grup</div>
            <div class="sidebar-value">{selected_label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# HERO
# =========================================================
hero_left, hero_right = st.columns([1.35, 4.65])

with hero_left:
    st.markdown('<div class="logo-box">', unsafe_allow_html=True)
    try:
        st.image("inder_logo.png", width=340)
    except:
        st.info("Logo dosyası için repo içine inder_logo.png yükleyin.")
    st.markdown('</div>', unsafe_allow_html=True)

with hero_right:
    st.markdown(
        """
        <div class="hero-shell">
            <div class="hero-title">Türkiye İnşaat Tedarik Sınıflandırma Sistemi</div>
            <div class="hero-subtitle">MasterFormat tabanlı ulusal tedarik sınıflandırma altyapısı • Kurumsal premium demo dashboard</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# METRICS
# =========================================================
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Ana Grup</div><div class="metric-value">{len(DATA)}</div></div>',
        unsafe_allow_html=True
    )

with m2:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">SUB Sayısı</div><div class="metric-value">{total_sub_count()}</div></div>',
        unsafe_allow_html=True
    )

with m3:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">VAR Sayısı</div><div class="metric-value">{total_var_count()}</div></div>',
        unsafe_allow_html=True
    )

selected_code = "-"
if st.session_state.selected_group:
    selected_code = st.session_state.selected_group.split(" – ")[0]

with m4:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Seçilen Grup</div><div class="metric-value">{selected_code}</div></div>',
        unsafe_allow_html=True
    )

# =========================================================
# SEARCH
# =========================================================
st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown('<div class="panel-title">Arama</div>', unsafe_allow_html=True)

search_query = st.text_input(
    "Ara",
    value=st.session_state.search_query,
    placeholder="Grup, SUB veya VAR ara",
    label_visibility="collapsed"
)
st.session_state.search_query = search_query

st.markdown(
    '<div class="search-note">Grup, alt grup veya ürün seviyesinde arama yapabilirsiniz.</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

filtered_data = filter_data(st.session_state.search_query)

# =========================================================
# GROUPS
# =========================================================
st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown('<div class="panel-title">20 Grup</div>', unsafe_allow_html=True)

groups = list(filtered_data.keys())

if not groups:
    st.warning("Arama kriterine uygun grup bulunamadı.")
else:
    for i in range(0, len(groups), 4):
        cols = st.columns(4)
        row = groups[i:i+4]
        for j, group in enumerate(row):
            with cols[j]:
                if st.button(group, key=f"group_{i}_{j}"):
                    st.session_state.selected_group = group
                    st.session_state.selected_sub = None

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# SUBS
# =========================================================
if st.session_state.selected_group and st.session_state.selected_group in DATA:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="pathline">Grup > {st.session_state.selected_group}</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="panel-title">SUB Gruplar</div>', unsafe_allow_html=True)

    subs = list(DATA[st.session_state.selected_group].keys())

    for i in range(0, len(subs), 3):
        cols = st.columns(3)
        row = subs[i:i+3]
        for j, sub in enumerate(row):
            with cols[j]:
                if st.button(sub, key=f"sub_{i}_{j}"):
                    st.session_state.selected_sub = sub

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# VARS
# =========================================================
if (
    st.session_state.selected_group
    and st.session_state.selected_sub
    and st.session_state.selected_group in DATA
    and st.session_state.selected_sub in DATA[st.session_state.selected_group]
):
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="pathline">Grup > {st.session_state.selected_group} > SUB > {st.session_state.selected_sub}</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="panel-title">VAR Listesi</div>', unsafe_allow_html=True)

    for item in DATA[st.session_state.selected_group][st.session_state.selected_sub]:
        st.markdown(f'<div class="var-card">{item}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
