import streamlit as st

st.set_page_config(
    page_title="Türkiye İnşaat Tedarik Sınıflandırma Sistemi",
    layout="wide"
)

# ---------------------
# CUSTOM CSS (UI)
# ---------------------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-weight: 600;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    cursor: pointer;
    transition: 0.2s;
}
.card:hover {
    transform: scale(1.05);
    background: #e8f0fe;
}
.title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------------
# LOGO
# ---------------------
st.image("inder_logo.png", width=200)

st.markdown('<div class="title">Türkiye İnşaat Tedarik Sınıflandırma Sistemi (MasterFormat)</div>', unsafe_allow_html=True)

# ---------------------
# DATA (20 GROUP SAMPLE)
# ---------------------
DATA = {
    "01 - Genel": {"Alt": ["Kalem1", "Kalem2"]},
    "02 - Zemin": {"Alt": ["Kazı", "Dolgu"]},
    "03 - Beton": {"Alt": ["C25", "C30"]},
    "04 - Duvar": {"Alt": ["Tuğla", "Gazbeton"]},
    "05 - Çelik": {"Alt": ["Demir", "Profil"]},
    "06 - Ahşap": {"Alt": ["Kaplama", "Kiriş"]},
    "07 - İzolasyon": {"Alt": ["Su", "Isı"]},
    "08 - Kaplama": {"Alt": ["Seramik", "Granit"]},
    "09 - Tavan": {"Alt": ["Asma", "Alçı"]},
    "10 - Kapı": {"Alt": ["Çelik", "Ahşap"]},
    "11 - Pencere": {"Alt": ["PVC", "Alüminyum"]},
    "12 - Boya": {"Alt": ["İç", "Dış"]},
    "13 - Mekanik": {"Alt": ["HVAC", "Tesisat"]},
    "14 - Elektrik": {"Alt": ["Kablo", "Pano"]},
    "15 - Yangın": {"Alt": ["Sprinkler", "Alarm"]},
    "16 - Asansör": {"Alt": ["Yolcu", "Yük"]},
    "17 - Çevre": {"Alt": ["Peyzaj", "Altyapı"]},
    "18 - Yol": {"Alt": ["Asfalt", "Beton"]},
    "19 - Çatı": {"Alt": ["Membran", "Kiremit"]},
    "20 - Özel": {"Alt": ["Akıllı Sistem", "IoT"]}
}

# ---------------------
# SESSION
# ---------------------
if "group" not in st.session_state:
    st.session_state.group = None

if "sub" not in st.session_state:
    st.session_state.sub = None

# ---------------------
# GROUP GRID
# ---------------------
st.write("## Ana Gruplar")

cols = st.columns(4)

for i, g in enumerate(DATA.keys()):
    with cols[i % 4]:
        if st.button(g):
            st.session_state.group = g
            st.session_state.sub = None

# ---------------------
# SUB
# ---------------------
if st.session_state.group:
    st.write(f"### {st.session_state.group}")

    for sub in DATA[st.session_state.group]:
        if st.button(sub):
            st.session_state.sub = sub

# ---------------------
# ITEMS
# ---------------------
if st.session_state.group and st.session_state.sub:
    st.write(f"### {st.session_state.sub}")

    for item in DATA[st.session_state.group][st.session_state.sub]:
        st.write("•", item)
