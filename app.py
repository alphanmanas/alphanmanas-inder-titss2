import streamlit as st

st.set_page_config(
    page_title="Türkiye İnşaat Tedarik Sistemi",
    layout="wide"
)

# -----------------------------
# DATA
# -----------------------------
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
    }
}

# -----------------------------
# SESSION
# -----------------------------
if "selected_group" not in st.session_state:
    st.session_state.selected_group = None

if "selected_sub" not in st.session_state:
    st.session_state.selected_sub = None

# -----------------------------
# HELPERS
# -----------------------------
total_groups = len(DATA)
total_subs = sum(len(v) for v in DATA.values())
total_vars = sum(len(items) for subs in DATA.values() for items in subs.values())

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
.main {
    background: #f6f8fb;
}
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 1500px;
}
.hero {
    background: linear-gradient(135deg, #0f172a, #1d4ed8);
    border-radius: 24px;
    padding: 28px 30px;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    margin-bottom: 18px;
}
.hero h1 {
    margin: 0;
    font-size: 2.2rem;
    font-weight: 800;
}
.hero p {
    margin-top: 8px;
    margin-bottom: 0;
    color: #dbeafe;
    font-size: 1rem;
}
.metric-box {
    background: white;
    padding: 18px 12px;
    border-radius: 18px;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);
    text-align: center;
    border: 1px solid #eef2f7;
}
.metric-title {
    font-size: 0.9rem;
    color: #64748b;
    margin-bottom: 6px;
}
.metric-value {
    font-size: 1.8rem;
    font-weight: 800;
    color: #0f172a;
}
.panel {
    background: white;
    border-radius: 22px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
    border: 1px solid #eef2f7;
}
.panel-title {
    font-size: 1.2rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 12px;
}
div.stButton > button {
    width: 100%;
    border-radius: 16px;
    border: none;
    padding: 0.9rem 0.8rem;
    font-weight: 700;
    min-height: 78px;
    background: linear-gradient(135deg, #dc2626, #2563eb);
    color: white;
    box-shadow: 0 8px 18px rgba(37, 99, 235, 0.18);
}
div.stButton > button:hover {
    color: white;
    filter: brightness(1.03);
}
.subbutton div.stButton > button {
    min-height: 64px !important;
    background: linear-gradient(135deg, #0f766e, #1d4ed8) !important;
}
.item-card {
    background: #f8fafc;
    border-left: 6px solid #2563eb;
    padding: 14px 16px;
    border-radius: 12px;
    margin-bottom: 10px;
    font-weight: 600;
    color: #0f172a;
}
.path {
    color: #64748b;
    font-size: 0.95rem;
    margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>Türkiye İnşaat Tedarik Sınıflandırma Sistemi</h1>
    <p>MasterFormat tabanlı ulusal sınıflandırma kurgusu • Demo Dashboard</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# METRICS
# -----------------------------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Ana Grup</div>
        <div class="metric-value">{total_groups}</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">SUB Sayısı</div>
        <div class="metric-value">{total_subs}</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">VAR Sayısı</div>
        <div class="metric-value">{total_vars}</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    selected_code = st.session_state.selected_group.split(" – ")[0] if st.session_state.selected_group else "-"
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Seçilen Grup</div>
        <div class="metric-value">{selected_code}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown('<div class="panel"><div class="panel-title">20 Ana Grup</div></div>', unsafe_allow_html=True)

# -----------------------------
# GROUP GRID
# -----------------------------
group_names = list(DATA.keys())
for row_start in range(0, len(group_names), 4):
    cols = st.columns(4)
    row_items = group_names[row_start:row_start+4]
    for i, group_name in enumerate(row_items):
        with cols[i]:
            if st.button(group_name, key=f"group_{group_name}"):
                st.session_state.selected_group = group_name
                st.session_state.selected_sub = None

st.write("")

# -----------------------------
# SUB PANEL
# -----------------------------
if st.session_state.selected_group:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="path">Ana Grup &gt; {st.session_state.selected_group}</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="panel-title">SUB Gruplar</div>', unsafe_allow_html=True)

    sub_names = list(DATA[st.session_state.selected_group].keys())
    sub_cols = st.columns(min(3, len(sub_names)) if len(sub_names) > 0 else 1)

    for idx, sub_name in enumerate(sub_names):
        with sub_cols[idx % len(sub_cols)]:
            st.markdown('<div class="subbutton">', unsafe_allow_html=True)
            if st.button(sub_name, key=f"sub_{sub_name}"):
                st.session_state.selected_sub = sub_name
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# ITEMS PANEL
# -----------------------------
if st.session_state.selected_group and st.session_state.selected_sub:
    st.write("")
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="path">Ana Grup &gt; {st.session_state.selected_group} &gt; {st.session_state.selected_sub}</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="panel-title">VAR / Kalem Listesi</div>', unsafe_allow_html=True)

    for item in DATA[st.session_state.selected_group][st.session_state.selected_sub]:
        st.markdown(f'<div class="item-card">{item}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
