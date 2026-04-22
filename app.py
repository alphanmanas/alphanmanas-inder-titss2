import streamlit as st

st.set_page_config(
    page_title="UİTS – Ulusal İnşaat Tedarik Sistemi",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# BRAND / STYLE
# =========================================================
BRAND_BLACK = "#231F20"
BRAND_GOLD = "#9A8457"
BG = "#F7F6F3"
CARD_BG = "#FFFFFF"
BORDER = "#E7E3DB"
TEXT_MUTED = "#6B7280"

st.markdown(f"""
<style>
    .main {{
        background-color: {BG};
    }}

    .block-container {{
        max-width: 1650px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }}

    .brand-header {{
        background: linear-gradient(180deg, #ffffff 0%, #fcfbf8 100%);
        border: 1px solid {BORDER};
        border-radius: 24px;
        padding: 26px 30px 24px 30px;
        margin-bottom: 18px;
        box-shadow: 0 8px 26px rgba(35, 31, 32, 0.05);
    }}

    .brand-title {{
        font-family: Georgia, "Times New Roman", serif;
        color: {BRAND_BLACK};
        font-size: 40px;
        line-height: 1.05;
        font-weight: 700;
        letter-spacing: 0.01em;
        margin: 0;
    }}

    .brand-subtitle {{
        color: {TEXT_MUTED};
        font-size: 14px;
        margin-top: 8px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
    }}

    .brand-tagline {{
        color: {BRAND_GOLD};
        font-size: 14px;
        margin-top: 10px;
        font-family: Georgia, "Times New Roman", serif;
        letter-spacing: 0.05em;
    }}

    .hero-kpi {{
        background: {CARD_BG};
        padding: 20px 22px;
        border-radius: 18px;
        border: 1px solid {BORDER};
        box-shadow: 0 4px 14px rgba(35, 31, 32, 0.05);
        min-height: 128px;
    }}

    .hero-kpi-label {{
        font-size: 13px;
        color: #475569;
        margin-bottom: 10px;
        font-weight: 600;
    }}

    .hero-kpi-value {{
        font-size: 32px;
        color: {BRAND_BLACK};
        font-weight: 800;
        line-height: 1.1;
        font-family: Georgia, "Times New Roman", serif;
    }}

    .hero-kpi-note {{
        font-size: 11px;
        color: {TEXT_MUTED};
        margin-top: 8px;
    }}

    .section-card {{
        background: {CARD_BG};
        padding: 18px 18px 16px 18px;
        border-radius: 18px;
        border: 1px solid {BORDER};
        box-shadow: 0 4px 14px rgba(35, 31, 32, 0.04);
        margin-bottom: 16px;
    }}

    .section-title {{
        font-size: 18px;
        font-weight: 700;
        color: {BRAND_BLACK};
        margin-bottom: 10px;
    }}

    .metric-box {{
        padding: 18px;
        border-radius: 18px;
        color: white;
        min-height: 128px;
        margin-bottom: 10px;
        box-shadow: 0 8px 18px rgba(35, 31, 32, 0.08);
    }}

    .metric-label {{
        font-size: 13px;
        opacity: 0.94;
        margin-bottom: 10px;
        font-weight: 600;
    }}

    .metric-value {{
        font-size: 30px;
        font-weight: 800;
        line-height: 1.15;
        font-family: Georgia, "Times New Roman", serif;
    }}

    .metric-note {{
        font-size: 12px;
        opacity: 0.9;
        margin-top: 10px;
    }}

    .gold-box {{
        background: linear-gradient(135deg, #8C7447, #B59B69);
    }}

    .black-box {{
        background: linear-gradient(135deg, #1F1B1C, #3A3234);
    }}

    .green-box {{
        background: linear-gradient(135deg, #0F766E, #14B8A6);
    }}

    .red-box {{
        background: linear-gradient(135deg, #991B1B, #DC2626);
    }}

    .slate-box {{
        background: linear-gradient(135deg, #334155, #475569);
    }}

    .purple-box {{
        background: linear-gradient(135deg, #6D28D9, #8B5CF6);
    }}

    .path-line {{
        font-size: 13px;
        color: {TEXT_MUTED};
        margin-bottom: 8px;
    }}

    .var-card {{
        background: #FCFBF8;
        border: 1px solid {BORDER};
        border-left: 5px solid {BRAND_GOLD};
        border-radius: 14px;
        padding: 14px 16px;
        margin-bottom: 10px;
        color: #334155;
        font-size: 14px;
        font-weight: 700;
    }}

    div.stButton > button {{
        width: 100%;
        min-height: 108px;
        border-radius: 18px;
        border: 1px solid {BORDER} !important;
        background: linear-gradient(180deg, #ffffff 0%, #fbfaf7 100%) !important;
        color: {BRAND_BLACK} !important;
        font-weight: 800 !important;
        font-size: 16px !important;
        box-shadow: 0 8px 18px rgba(35, 31, 32, 0.05);
    }}

    div.stButton > button:hover {{
        border: 1px solid {BRAND_GOLD} !important;
        color: {BRAND_GOLD} !important;
    }}

    .sub-btn div.stButton > button {{
        min-height: 84px !important;
        font-size: 15px !important;
    }}

    .stTextInput label {{
        font-weight: 600 !important;
    }}
</style>
""", unsafe_allow_html=True)

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
# HELPERS
# =========================================================
def total_subs(data):
    return sum(len(v) for v in data.values())

def total_vars(data):
    return sum(len(items) for subs in data.values() for items in subs.values())

def search_filter(data, query):
    q = query.lower().strip()
    if not q:
        return data
    out = {}
    for group, subs in data.items():
        gmatch = q in group.lower()
        new_subs = {}
        for sub, vars_ in subs.items():
            smatch = q in sub.lower()
            matched_vars = [v for v in vars_ if q in v.lower()]
            if smatch:
                new_subs[sub] = vars_
            elif matched_vars:
                new_subs[sub] = matched_vars
        if gmatch:
            out[group] = subs
        elif new_subs:
            out[group] = new_subs
    return out

# =========================================================
# STATE
# =========================================================
if "selected_group" not in st.session_state:
    st.session_state.selected_group = None
if "selected_sub" not in st.session_state:
    st.session_state.selected_sub = None

# =========================================================
# HEADER
# =========================================================
st.markdown(f"""
<div class="brand-header">
    <div class="brand-title">Türkiye İnşaat Tedarik Sınıflandırma Sistemi</div>
    <div class="brand-subtitle">UİTS • Ulusal İnşaat Tedarik Sistemi • MasterFormat Tabanlı Demo Dashboard</div>
    <div class="brand-tagline">Malzeme sınıflandırma ve tedarik veri altyapısı</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("Kontrol Paneli")
search = st.sidebar.text_input("Arama", placeholder="Grup, SUB veya VAR ara")
if st.sidebar.button("Seçimi Temizle"):
    st.session_state.selected_group = None
    st.session_state.selected_sub = None

filtered_data = search_filter(DATA, search)

# =========================================================
# HERO KPI
# =========================================================
h1, h2, h3, h4 = st.columns(4)

with h1:
    st.markdown(f"""
    <div class="hero-kpi">
        <div class="hero-kpi-label">Ana Grup</div>
        <div class="hero-kpi-value">{len(DATA)}</div>
        <div class="hero-kpi-note">Ulusal sınıflandırma omurgası</div>
    </div>
    """, unsafe_allow_html=True)

with h2:
    st.markdown(f"""
    <div class="hero-kpi">
        <div class="hero-kpi-label">SUB Sayısı</div>
        <div class="hero-kpi-value">{total_subs(DATA)}</div>
        <div class="hero-kpi-note">Alt kırılım katmanı</div>
    </div>
    """, unsafe_allow_html=True)

with h3:
    st.markdown(f"""
    <div class="hero-kpi">
        <div class="hero-kpi-label">VAR Sayısı</div>
        <div class="hero-kpi-value">{total_vars(DATA)}</div>
        <div class="hero-kpi-note">Gösterilen örnek kalemler</div>
    </div>
    """, unsafe_allow_html=True)

with h4:
    selected_code = st.session_state.selected_group.split(" – ")[0] if st.session_state.selected_group else "-"
    st.markdown(f"""
    <div class="hero-kpi">
        <div class="hero-kpi-label">Seçilen Grup</div>
        <div class="hero-kpi-value">{selected_code}</div>
        <div class="hero-kpi-note">Aktif sunum odağı</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================================================
# MAIN GROUPS
# =========================================================
st.markdown('<div class="section-card"><div class="section-title">20 Ana Grup</div>', unsafe_allow_html=True)

group_names = list(filtered_data.keys())
for row_start in range(0, len(group_names), 4):
    cols = st.columns(4)
    for i, group_name in enumerate(group_names[row_start:row_start+4]):
        with cols[i]:
            if st.button(group_name, key=f"group_{group_name}"):
                st.session_state.selected_group = group_name
                st.session_state.selected_sub = None

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# SUB GROUPS
# =========================================================
if st.session_state.selected_group and st.session_state.selected_group in filtered_data:
    st.markdown('<div class="section-card"><div class="section-title">SUB Gruplar</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="path-line">Ana Grup → {st.session_state.selected_group}</div>',
        unsafe_allow_html=True
    )

    sub_names = list(filtered_data[st.session_state.selected_group].keys())
    sub_cols = st.columns(min(3, max(1, len(sub_names))))

    for idx, sub_name in enumerate(sub_names):
        with sub_cols[idx % len(sub_cols)]:
            st.markdown('<div class="sub-btn">', unsafe_allow_html=True)
            if st.button(sub_name, key=f"sub_{st.session_state.selected_group}_{sub_name}"):
                st.session_state.selected_sub = sub_name
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# VAR LIST
# =========================================================
if (
    st.session_state.selected_group
    and st.session_state.selected_sub
    and st.session_state.selected_group in filtered_data
    and st.session_state.selected_sub in filtered_data[st.session_state.selected_group]
):
    st.markdown('<div class="section-card"><div class="section-title">VAR / Kalem Listesi</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="path-line">Ana Grup → {st.session_state.selected_group} → {st.session_state.selected_sub}</div>',
        unsafe_allow_html=True
    )

    for item in filtered_data[st.session_state.selected_group][st.session_state.selected_sub]:
        st.markdown(f'<div class="var-card">{item}</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
