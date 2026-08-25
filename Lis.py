import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AN Project", page_icon="🤖", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>🤖 AN Project</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Official Links & AI Service</p>", unsafe_allow_html=True)

# Section Links
st.subheader("🔗 Links")
st.link_button("🎵 TikTok Main (@anproject032)", "https://tiktok.com/@anproject032", use_container_width=True)
st.link_button("🎵 TikTok Backup (@project.an_)", "https://tiktok.com/@project.an_", use_container_width=True)
st.link_button("🌐 Link AI Lama", "https://short-url.cc/1CuUK", use_container_width=True)

st.divider()

# Section AI Asisten
st.subheader("💬 AI Asisten")
prompt = st.text_area("Tanyakan sesuatu ke AI:")

if st.button("Kirim ke AI", use_container_width=True):
    if not prompt:
        st.warning("Tuliskan pertanyaanmu!")
    else:
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
            with st.spinner("Sedang memproses..."):
                genai.configure(api_key=api_key)
                # Menggunakan model terbaru gemini-2.5-flash
                model = genai.GenerativeModel('gemini-2.5-flash')
                response = model.generate_content(prompt)
                st.markdown("### Jawaban:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
