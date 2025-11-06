import streamlit as st
from openai import OpenAI
import random
from datetime import datetime

# === KONFIGURASI CLIENT ===
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# === DATA HEWAN LENGKAP ===
hewan_dan_kode = {
    0: "Tapir", 1: "Ikan Bandeng", 2: "Bekicot", 3: "Angsa", 4: "Merak", 5: "Singa", 6: "Kelinci", 7: "Babi", 8: "Macan",
    9: "Kerbau", 10: "Kelabang", 11: "Anjing", 12: "Kuda", 13: "Gajah", 14: "Onta", 15: "Tikus", 16: "Tawon", 17: "Bangau",
    18: "Kucing", 19: "Kupu-Kupu", 20: "Lalat", 21: "Walet", 22: "Capung", 23: "Kera", 24: "Katak", 25: "Rajawali", 26: "Naga",
    27: "Kura-Kura", 28: "Ayam", 29: "Belut", 30: "Ikan Mas", 31: "Udang", 32: "Ular", 33: "Laba-Laba", 34: "Rusa",
    35: "Kambing", 36: "Musang", 37: "Ikan Gabus", 38: "Cendrawasih", 39: "Kalajengking", 40: "Gelatik", 41: "Kepiting",
    42: "Buaya", 43: "Ikan Suro", 44: "Badak", 45: "Banteng", 46: "Orang Utan", 47: "Zebra", 48: "Landak", 49: "Kelelawar",
    50: "Beruang", 51: "Kerang", 52: "Ikan Paus", 53: "Ikan Duri", 54: "Ikan Lele", 55: "Kangguru", 56: "Ikan Duyung",
    57: "Ulat Sutera", 58: "Cumi-Cumi", 59: "Kakak Tua", 60: "Cecak", 61: "Kecoak", 62: "Walang Kadung", 63: "Kumbang",
    64: "Kuda Laut", 65: "Ikan Hiu", 66: "Jerapah", 67: "Burung Onta", 68: "Burung Hantu", 69: "Mimi", 70: "Keledai",
    71: "Macan Tutul", 72: "Ikan Terbang", 73: "Semut", 74: "Pinguin", 75: "Bebek", 76: "Nyamuk", 77: "Penyu",
    78: "Ikan Gergaji", 79: "Orong-Orong", 80: "Bajing", 81: "Kancil", 82: "Kuda Nil", 83: "Ikan Layur", 84: "Kalkun",
    85: "Jangkrik", 86: "Ikan Sampan", 87: "Betet", 88: "Domba", 89: "Ikan Bendera", 90: "Trenggiling", 91: "Srigala",
    92: "Ikan Tenggiri", 93: "Babi Hutan", 94: "Ikan Kakap", 95: "Perkutut", 96: "Ikan Nus", 97: "Tokek", 98: "Tongkol",
    99: "Burung Jalak"
}

# === FUNGSI PEMBUATAN DESKRIPSI TAFSIR ===
def generate_tafsir(hewan):
    tafsir_templates = [
        f"Dalam mimpi, kemunculan {hewan.lower()} sering diartikan sebagai simbol keseimbangan antara dunia nyata dan spiritual, mengingatkanmu akan ketenangan batin.",
        f"Sosok {hewan.lower()} dalam mimpi melambangkan perjalanan jiwa yang menuntunmu menuju kebijaksanaan dan keteguhan hati.",
        f"Mimpi melihat {hewan.lower()} menjadi pertanda adanya pesan dari alam semesta untuk tetap rendah hati dan bersyukur atas perubahan yang datang.",
        f"{hewan} muncul dalam mimpi membawa makna tentang keberanian menghadapi tantangan dan menemukan harmoni dalam kehidupan.",
        f"Ketika {hewan.lower()} hadir dalam mimpimu, itu sering menandakan datangnya keberuntungan tersembunyi yang dibungkus dalam ujian kecil kehidupan.",
        f"Mimpi tentang {hewan.lower()} menggambarkan ikatan batin antara manusia dan alam, sebuah panggilan untuk lebih selaras dengan energi semesta."
    ]
    return random.choice(tafsir_templates)

# === FUNGSI PEMBUATAN PROMPT GAMBAR ===
def build_image_prompt(hewan, tanggal):
    karakter_manusia = random.choice([
        "seorang pertapa bijak duduk bersila di tepi hutan Bali",
        "wanita muda penari Bali sedang menatap makhluk dengan tenang",
        "anak kecil memegang lentera sambil tersenyum kepada makhluk mistik",
        "lelaki tua berpakaian tradisional Bali sedang bermeditasi di bawah pohon beringin",
        "seorang nelayan membawa obor di malam hari menatap makhluk di tepi pantai"
    ])

    prompt = (
        f"Desain poster klasik vintage bergaya Bali dengan latar kertas sepia dan ornamen floral di atas dan bawah. "
        f"Judul besar: 'SYAIR MIMPI KOKO BALI'. Subjudul: 'Mimpi & Tafsir – {tanggal}'. "
        f"Ilustrasi utama di tengah menampilkan {karakter_manusia} yang berinteraksi dengan {hewan.lower()} "
        f"dalam suasana mistis dan spiritual khas budaya Bali. "
        f"Gunakan bingkai dekoratif klasik dan komposisi simetris di tengah poster. "
        f"Tambahkan tekstur kertas tua dan pencahayaan hangat alami. "
        f"Di bagian bawah, buat tiga kolom sejajar bertuliskan 'Kode Alam', 'Angka Pelarian', dan 'Fokus'. "
        f"Gaya ilustrasi: ukiran tradisional Bali dengan nuansa mistik dan lembut."
    )
    return prompt

# === FUNGSI PEMBUATAN PROMPT VIDEO ===
def build_animation_prompt(hewan, scene_summary):
    return (
        f"Gerakkan hanya {hewan.lower()} dan elemen utamanya dengan gerakan lembut alami — seperti napas, aura cahaya, atau energi yang berdenyut pelan. "
        f"Biarkan latar belakang, manusia, dan ornamen floral tetap diam. "
        f"Pertahankan tone sepia klasik, suasana spiritual Bali, dan tidak mengubah komposisi gambar. "
        f"Durasi video sekitar 7 detik."
    )

# === FUNGSI PEMBUATAN POSTER ===
def generate_poster(selected_hewan=None):
    kode, hewan = random.choice(list(hewan_dan_kode.items())) if not selected_hewan else (selected_hewan, hewan_dan_kode[selected_hewan])
    tanggal = datetime.now().strftime("%d %B %Y")

    tafsir = generate_tafsir(hewan)

    # angka pelarian unik & berurutan
    def generate_unique_angka():
        angka = random.sample(range(0, 10), 4)
        angka.sort()
        return ''.join(map(str, angka))

    angka_pelarian1 = generate_unique_angka()
    angka_pelarian2 = generate_unique_angka()
    fokus = random.sample(range(10, 99), 2)
    kode_str = f"{kode:02d}"  # tampil 2 digit

    prompt = build_image_prompt(hewan, tanggal)

    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1536"
        )
        image_url = response.data[0].url
        animation_prompt = build_animation_prompt(hewan, tafsir)
        return image_url, hewan, kode_str, tafsir, angka_pelarian1, angka_pelarian2, fokus, animation_prompt

    except Exception as e:
        st.error(f"Gagal membuat poster. Error: {e}")
        return None, None, None, None, None, None, None, None

# === STREAMLIT UI ===
st.set_page_config(page_title="Syair Mimpi Koko Bali", page_icon="🌺", layout="centered")

st.title("🌺 SYAIR MIMPI KOKO BALI")
st.markdown("Panel otomatis untuk membuat poster mimpi bergaya klasik Bali dengan ilustrasi mistik yang bercerita.")

hewan_options = [f"{kode:02d} - {nama}" for kode, nama in hewan_dan_kode.items()]
selected_option = st.selectbox("Pilih Hewan atau Acak:", ["Acak"] + hewan_options)

if st.button("✨ Generate Syair Hari Ini"):
    with st.spinner("Menyiapkan karya mistik Bali..."):
        selected_hewan = None if selected_option == "Acak" else int(selected_option.split(" - ")[0])
        image_url, hewan, kode, tafsir, a1, a2, fokus, anim_prompt = generate_poster(selected_hewan)

        if image_url:
            st.image(image_url, caption=f"SYAIR {hewan.upper()} – Kode Alam {kode}")
            st.markdown(f"**Tafsir:** {tafsir}")
            st.markdown(f"**Kode Alam:** {kode}  **Angka Pelarian:** {a1} • {a2}  **Fokus:** {fokus[0]} • {fokus[1]}")
            st.divider()
            st.subheader("🎞️ Prompt Animasi Otomatis")
            st.text_area("Gunakan prompt ini di Pika Labs:", anim_prompt, height=160)
        else:
            st.warning("⚠️ Gagal menghasilkan gambar, silakan coba lagi.")
