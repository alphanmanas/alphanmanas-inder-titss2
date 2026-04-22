import streamlit as st

st.set_page_config(
    page_title="UİTS Dashboard",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# DATA
# -------------------------------------------------
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

# -------------------------------------------------
# SESSION
# -------------------------------------------------
if "selected_group" not in st.session_state:
    st.session_state.selected_group = None
if "selected_sub" not in st.session_state:
    st.session_state.selected_sub = None

# -------------------------------------------------
# HELPERS
# -------------------------------------------------
def total_subs(data):
    return sum(len(v) for v in data.values())

def total_vars(data):
    return sum(len(items) for subs in data.values() for items in subs.values())

def flatten_search(data, query):
    query = query.lower().strip()
    if not query:
        return data
    filtered = {}
    for group, subs in data.items():
        gmatch = query in group.lower()
        new_subs = {}
        for sub, vars_ in subs.items():
            smatch = query in sub.lower()
            matched_vars = [v for v in vars_ if query in v.lower()]
            if smatch:
                new_subs[sub] = vars_
            elif matched_vars:
                new_subs[sub] = matched_vars
        if gmatch:
            filtered[group] = subs
        elif new_subs:
            filtered[group] = new_subs
    return filtered

# -------------------------------------------------
# CSS
# -------------------------------------------------
st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at top left, rgba(37,99,235,0.12), transparent 28%),
        radial-gradient(circle at top right, rgba(220,38,38,0.10), transparent 24%),
        #f6f8fc;
}

.block-container {
    max-width: 1500px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

.hero-wrap {
    background: linear-gradient(135deg, #0b1220 0%, #13203b 52%, #1d4ed8 100%);
    border-radius: 28px;
    padding: 30px 32px;
    color: white;
    box-shadow: 0 20px 40px rgba(15, 23, 42, 0.18);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 18px;
}

.hero-kicker {
    font-size: 0.95rem;
    color: #cbd5e1;
    margin-bottom: 8px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    font-weight: 700;
}

.hero-title {
    font-size: 2.35rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 10px;
}

.hero-sub {
    color: #dbeafe;
    font-size: 1rem;
    max-width: 860px;
}

.metric-card {
    background: rgba(255,255,255,0.82);
    backdrop-filter: blur(10px);
    border-radius: 22px;
    padding: 18px 18px;
    box-shadow: 0 10px 25px rgba(15,23,42,0.08);
    border: 1px solid rgba(255,255,255,0.7);
    min-height: 110px;
}

.metric-label {
    color: #64748b;
    font-size: 0.9rem;
    margin-bottom: 8px;
    font-weight: 600;
}

.metric-value {
    color: #0f172a;
    font-size: 2rem;
    font-weight: 800;
    line-height: 1;
}

.metric-foot {
    color: #94a3b8;
    font-size: 0.8rem;
    margin-top: 10px;
}

.panel {
    background: rgba(255,255,255,0.84);
    backdrop-filter: blur(10px);
    border-radius: 24px;
    padding: 20px;
    box-shadow: 0 14px 30px rgba(15,23,42,0.08);
    border: 1px solid rgba(255,255,255,0.65);
}

.panel-title {
    color: #0f172a;
    font-size: 1.15rem;
    font-weight: 800;
    margin-bottom: 10px;
}

.panel-path {
    color: #64748b;
    font-size: 0.92rem;
    margin-bottom: 8px;
}

.sidebar-card {
    background: linear-gradient(135deg, #ffffff, #f8fafc);
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 16px;
    margin-bottom: 14px;
}

.sidebar-title {
    font-size: 0.95rem;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 10px;
}

div.stButton > button {
    width: 100%;
    border-radius: 18px;
    border: none !important;
    min-height: 84px;
    font-weight: 800;
    font-size: 0.98rem;
    color: white !important;
    background: linear-gradient(135deg, #dc2626 0%, #2563eb 100%) !important;
    box-shadow: 0 10px 20px rgba(37,99,235,0.18);
    transition: all 0.18s ease;
}

div.stButton > button:hover {
    transform: translateY(-1px);
    filter: brightness(1.03);
}

.sub-btn div.stButton > button {
    min-height: 68px !important;
    background: linear-gradient(135deg, #0f766e 0%, #1d4ed8 100%) !important;
    font-size: 0.95rem !important;
}

.item-card {
    background: linear-gradient(135deg, #ffffff, #f8fafc);
    border: 1px solid #e2e8f0;
    border-left: 6px solid #2563eb;
    padding: 15px 16px;
    border-radius: 14px;
    margin-bottom: 10px;
    box-shadow: 0 6px 16px rgba(15,23,42,0.05);
    font-weight: 700;
    color: #0f172a;
}

.search-note {
    color: #64748b;
    font-size: 0.86rem;
    margin-top: 4px;
}

hr {
    margin-top: 0.6rem;
    margin-bottom: 0.8rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">Kontrol Paneli</div>', unsafe_allow_html=True)
    search = st.text_input("Arama", placeholder="Grup, SUB veya VAR ara")
    st.markdown('<div class="search-note">Sunum için hızlı filtreleme alanı</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">Aktif Seçim</div>', unsafe_allow_html=True)
    st.write("Grup:", st.session_state.selected_group if st.session_state.selected_group else "-")
    st.write("SUB:", st.session_state.selected_sub if st.session_state.selected_sub else "-")
    if st.button("Seçimi Temizle"):
        st.session_state.selected_group = None
        st.session_state.selected_sub = None
    st.markdown('</div>', unsafe_allow_html=True)

filtered_data = flatten_search(DATA, search)

# -------------------------------------------------
# HERO
# -------------------------------------------------
st.markdown("""
<div class="hero-wrap">
    <div class="hero-kicker">UİTS Dashboard</div>
    <div class="hero-title">Türkiye İnşaat Tedarik Sınıflandırma Sistemi</div>
    <div class="hero-sub">
        MasterFormat tabanlı ulusal sınıflandırma kurgusunun görsel demo sürümü.
        Ana grup → SUB → VAR akışı üzerinden sunum ve karar destek kullanımı için tasarlanmıştır.
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# METRICS
# -------------------------------------------------
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Ana Grup</div>
        <div class="metric-value">{len(DATA)}</div>
        <div class="metric-foot">Toplam sınıflandırma katmanı</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">SUB Sayısı</div>
        <div class="metric-value">{total_subs(DATA)}</div>
        <div class="metric-foot">Alt kırılım seti</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">VAR Sayısı</div>
        <div class="metric-value">{total_vars(DATA)}</div>
        <div class="metric-foot">Gösterilen örnek kalemler</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    selected_code = st.session_state.selected_group.split(" – ")[0] if st.session_state.selected_group else "-"
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Seçilen Grup</div>
        <div class="metric-value">{selected_code}</div>
        <div class="metric-foot">Aktif demo odağı</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# -------------------------------------------------
# GROUPS PANEL
# -------------------------------------------------
st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown('<div class="panel-title">20 Ana Grup</div>', unsafe_allow_html=True)

group_names = list(filtered_data.keys())
for row_start in range(0, len(group_names), 4):
    cols = st.columns(4)
    for i, group_name in enumerate(group_names[row_start:row_start+4]):
        with cols[i]:
            if st.button(group_name, key=f"group_{group_name}"):
                st.session_state.selected_group = group_name
                st.session_state.selected_sub = None

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# SUB PANEL
# -------------------------------------------------
if st.session_state.selected_group and st.session_state.selected_group in filtered_data:
    st.write("")
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="panel-path">Ana Grup → {st.session_state.selected_group}</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="panel-title">SUB Gruplar</div>', unsafe_allow_html=True)

    sub_names = list(filtered_data[st.session_state.selected_group].keys())
    sub_cols = st.columns(min(3, max(1, len(sub_names))))

    for idx, sub_name in enumerate(sub_names):
        with sub_cols[idx % len(sub_cols)]:
            st.markdown('<div class="sub-btn">', unsafe_allow_html=True)
            if st.button(sub_name, key=f"sub_{st.session_state.selected_group}_{sub_name}"):
                st.session_state.selected_sub = sub_name
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# ITEMS PANEL
# -------------------------------------------------
if (
    st.session_state.selected_group
    and st.session_state.selected_sub
    and st.session_state.selected_group in filtered_data
    and st.session_state.selected_sub in filtered_data[st.session_state.selected_group]
):
    st.write("")
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown(
        f'<div class="panel-path">Ana Grup → {st.session_state.selected_group} → {st.session_state.selected_sub}</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="panel-title">VAR / Kalem Listesi</div>', unsafe_allow_html=True)

    for item in filtered_data[st.session_state.selected_group][st.session_state.selected_sub]:
        st.markdown(f'<div class="item-card">{item}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
