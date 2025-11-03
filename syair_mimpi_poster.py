import streamlit as st
from openai import OpenAI
import base64
import random
from datetime import datetime
import time
import os

# ======================================
# 🔑 KONFIGURASI API
# ======================================
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.set_page_config(page_title="Syair Mimpi Koko Bali", page_icon="🌺", layout="centered")
st.title("🌺 SYAIR MIMPI KOKO BALI")
st.caption("Panel otomatis untuk membuat poster mimpi bergaya klasik Bali dengan tafsir orisinal dan visual mistis.")


# ======================================
# 📜 DATA 00–99 HEWAN
# ======================================
HEWAN_KODE = {
    0: "Tapir", 1: "Ikan Bandeng", 2: "Bekicot", 3: "Angsa", 4: "Merak", 5: "Singa", 6: "Kelinci", 7: "Babi",
    8: "Macan", 9: "Kerbau", 10: "Kelabang", 11: "Anjing", 12: "Kuda", 13: "Gajah", 14: "Onta", 15: "Tikus",
    16: "Tawon", 17: "Bangau", 18: "Kucing", 19: "Kupu Kupu", 20: "Lalat", 21: "Walet", 22: "Capung", 23: "Kera",
    24: "Katak", 25: "Rajawali", 26: "Naga", 27: "Kura Kura", 28: "Ayam", 29: "Belut", 30: "Ikan Mas", 31: "Udang",
    32: "Ular", 33: "Laba Laba", 34: "Rusa", 35: "Kambing", 36: "Musang", 37: "Ikan Gabus", 38: "Cendrawasih", 39: "Kalajengking",
    40: "Gelatik", 41: "Kepiting", 42: "Buaya", 43: "Ikan Suro", 44: "Badak", 45: "Banteng", 46: "Orang Utan", 47: "Zebra",
    48: "Landak", 49: "Kelelawar", 50: "Beruang", 51: "Kerang", 52: "Ikan Paus", 53: "Ikan Duri", 54: "Ikan Lele", 55: "Kangguru",
    56: "Ikan Duyung", 57: "Ulat Sutera", 58: "Cumi Cumi", 59: "Kakak Tua", 60: "Cecak", 61: "Kecoak", 62: "Walang Kadung", 63: "Kumbang",
    64: "Kuda Laut", 65: "Ikan Hiu", 66: "Jerapah", 67: "Burung Onta", 68: "Burung Hantu", 69: "Mimi", 70: "Keledai", 71: "Macan Tutul",
    72: "Ikan Terbang", 73: "Semut", 74: "Pinguin", 75: "Bebek", 76: "Nyamuk", 77: "Penyu", 78: "Ikan Gergaji", 79: "Orong Orong",
    80: "Bajing", 81: "Kancil", 82: "Kuda Nil", 83: "Ikan Layur", 84: "Kalkun", 85: "Jangkrik", 86: "Ikan Sampan", 87: "Betet",
    88: "Domba", 89: "Ikan Bendera", 90: "Trenggiling", 91: "Srigala", 92: "Ikan Tenggiri", 93: "Babi Hutan", 94: "Ikan Kakap",
    95: "Perkutut", 96: "Ikan Nus", 97: "Tokek", 98: "Tongkol", 99: "Burung Jalak"
}


# ======================================
# 💬 PEMBANGKIT TAFSIR ORISINAL
# ======================================
def generate_unique_tafsir(hewan):
    gaya_tafsir = [
        f"Saat {hewan.lower()} hadir dalam mimpimu, ada pesan halus dari semesta tentang arah hidup dan keseimbangan batinmu.",
        f"Kemunculan {hewan.lower()} dalam mimpi sering dianggap sebagai panggilan untuk lebih mendengarkan intuisi dan perasaan terdalam.",
        f"Mimpi tentang {hewan.lower()} membawa getaran spiritual — tanda bahwa perubahan besar akan datang dalam diam.",
        f"Jika {hewan.lower()} hadir di alam tidurmu, mungkin itu simbol kekuatan, perlindungan, dan doa yang sedang dijawab oleh alam.",
        f"Mimpi melihat {hewan.lower()} bisa jadi isyarat agar kamu lebih sabar, karena keberuntungan sedang menyiapkan jalannya perlahan.",
        f"{hewan} dalam mimpi mencerminkan perjalanan spiritualmu — antara ketenangan, keberanian, dan bisikan halus dari dunia tak kasat mata.",
        f"Alam bawah sadar menghadirkan {hewan.lower()} sebagai pengingat untuk menghargai tanda-tanda kecil dalam hidupmu yang sering terabaikan.",
        f"{hewan} muncul bukan kebetulan, tetapi pesan tentang keseimbangan antara akal dan nurani, antara dunia nyata dan mimpi."
    ]
    return random.choice(gaya_tafsir)


# ======================================
# 🖼️ PEMBUAT POSTER
# ======================================
def generate_poster(selected_hewan=None):
    if selected_hewan == "Acak" or selected_hewan is None:
        kode = random.choice(list(HEWAN_KODE.keys()))
        hewan = HEWAN_KODE[kode]
    else:
        # Ambil angka dari teks dropdown misal "07 – Babi"
        kode = int(selected_hewan.split("–")[0].strip())
        hewan = selected_hewan.split("–")[1].strip()

    kode_str = f"{kode:02d}"  # format jadi dua digit (01, 02, ...)
    tafsir = generate_unique_tafsir(hewan)
    tanggal = datetime.now().strftime("%d %B %Y")

    angka_pelarian = [str(random.randint(1000, 9999)), str(random.randint(1000, 9999))]
    fokus = [str(random.randint(10, 99)), str(random.randint(10, 99))]

    tema_visual = random.choice([
        f"adegan magis di malam hari di mana seekor {hewan.lower()} muncul di antara cahaya bulan, dikelilingi ornamen Bali mistis",
        f"ilustrasi simbolik dengan {hewan.lower()} berada di tengah pusaran energi spiritual dan bunga kamboja, gaya vintage klasik Bali",
        f"adegan mistik rakyat Bali menggambarkan {hewan.lower()} sebagai penjaga mimpi di langit berornamen tradisional",
        f"lukisan klasik Bali dengan {hewan.lower()} muncul di antara asap dupa dan sinar cahaya ilahi, menggambarkan tafsir mimpi kuno"
    ])

    prompt = f"""
    Buat desain poster bergaya klasik vintage Bali dengan latar kertas sepia dan ornamen floral di bagian atas dan bawah.
    Judul besar: 'SYAIR MIMPI KOKO BALI'.
    Subjudul: 'Mimpi & Tafsir – {tanggal}'.
    Ilustrasi utama menggambarkan {tema_visual}.
    Tambahkan teks tafsir: '{tafsir}'
    Di bagian bawah buat tiga kolom sejajar:
    1. 'Kode Alam' dengan ikon {hewan} dan angka {kode_str}.
    2. 'Angka Pelarian' berisi {angka_pelarian[0]} dan {angka_pelarian[1]}.
    3. 'Fokus' dengan angka {fokus[0]} dan {fokus[1]} di dalam lingkaran.
    Gunakan tipografi klasik warna coklat tua dan nuansa spiritual Bali kuno.
    """

    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1536",
            quality="high"
        )

        image_base64 = response.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        filename = f"syair_{kode_str}_{hewan.lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        with open(filename, "wb") as f:
            f.write(image_bytes)

        return filename, hewan, kode_str, angka_pelarian, fokus, tafsir

    except Exception as e:
        return None, None, None, None, None, str(e)


# ======================================
# 📋 STREAMLIT UI
# ======================================
if "history" not in st.session_state:
    st.session_state.history = []

# Buat dropdown dengan angka + nama
hewan_list = ["Acak"] + [f"{k:02d} – {v}" for k, v in HEWAN_KODE.items()]
selected_hewan = st.selectbox("Pilih Hewan untuk Tafsir:", hewan_list)

if st.button("✨ Generate Syair Hari Ini"):
    with st.spinner("🪄 Sedang merangkai mimpi dan menciptakan visual mistis..."):
        time.sleep(1)
        filename, hewan, kode, angka_pelarian, fokus, tafsir = generate_poster(selected_hewan)

    if filename:
        st.image(filename, caption=f"🪶 SYAIR {hewan.upper()} – Kode Alam {kode}")
        st.markdown(f"**Kode Alam:** {kode} ({hewan})")
        st.markdown(f"**Angka Pelarian:** {angka_pelarian[0]} – {angka_pelarian[1]}")
        st.markdown(f"**Fokus:** {fokus[0]} & {fokus[1]}")
        st.markdown(f"**Tafsir:** {tafsir}")

        with open(filename, "rb") as img_file:
            st.download_button(
                label="💾 Download Poster",
                data=img_file,
                file_name=filename,
                mime="image/png"
            )

        st.session_state.history.append({
            "filename": filename,
            "hewan": hewan,
            "kode": kode,
            "tafsir": tafsir
        })
        st.success("✅ Poster berhasil dibuat dan disimpan!")
    else:
        st.warning(f"Gagal membuat poster. Error: {tafsir}")


# ======================================
# 🗂️ RIWAYAT SYAIR
# ======================================
if st.session_state.history:
    st.subheader("🗂️ Riwayat Syair yang Pernah Dibuat")
    cols = st.columns(3)
    for i, item in enumerate(reversed(st.session_state.history[-9:])):
        with cols[i % 3]:
            st.image(item["filename"], use_container_width=True)
            st.caption(f"{item['kode']} – {item['hewan']}")
