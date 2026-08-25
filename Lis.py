import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AN Project", page_icon="🤖", layout="centered")

# Judul Utama
st.markdown("<h1 style='text-align: center;'>🤖 AN Project</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Official Links & AI Service</p>", unsafe_allow_html=True)

# Section Link Bio
st.subheader("🔗 Links")
st.link_button("🎵 TikTok Main (@anproject032)", "https://tiktok.com/@anproject032", use_container_width=True)
st.link_button("🎵 TikTok Backup (@project.an_)", "https://tiktok.com/@project.an_", use_container_width=True)
st.link_button("🌐 Link AI Lama", "https://short-url.cc/1CuUK", use_container_width=True)

st.divider()

# Section AI Asisten
st.subheader("💬 AI Asisten")
api_key = st.text_input("Masukkan Gemini API Key:", type="password")
prompt = st.text_area("Tanyakan sesuatu ke AI:")

if st.button("Kirim ke AI", use_container_width=True):
    if not api_key:
        st.warning("Masukkan API Key terlebih dahulu!")
    elif not prompt:
        st.warning("Tuliskan pertanyaanmu!")
    else:
        try:
            with st.spinner("Sedang memproses..."):
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                st.markdown("### Jawaban:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")            font-size: 1.1rem;
            transition: transform 0.2s ease;
        }

        .link-card:hover .arrow {
            color: #ffffff;
            transform: translateX(4px);
        }

        footer {
            margin-top: 36px;
            font-size: 0.8rem;
            color: #64748b;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Profile Avatar -->
        <div class="profile-img">🤖</div>
        
        <!-- Header Info -->
        <h1>AN Project</h1>
        <p class="bio">Official Links & AI Assistant Service</p>

        <!-- Links List -->
        <div class="links-container">
            
            <!-- Link AI -->
            <a href="https://short-url.cc/1CuUK" target="_blank" class="link-card">
                <div class="link-info">
                    <div class="icon-box ai-bg">🤖</div>
                    <span>AI Assistant</span>
                </div>
                <span class="arrow">➔</span>
            </a>

            <!-- Link TikTok 1 -->
            <a href="https://tiktok.com/@anproject032" target="_blank" class="link-card">
                <div class="link-info">
                    <div class="icon-box tiktok-bg">🎵</div>
                    <span>TikTok Main (@anproject032)</span>
                </div>
                <span class="arrow">➔</span>
            </a>

            <!-- Link TikTok 2 -->
            <a href="https://tiktok.com/@project.an_" target="_blank" class="link-card">
                <div class="link-info">
                    <div class="icon-box tiktok-bg">🎵</div>
                    <span>TikTok Backup (@project.an_)</span>
                </div>
                <span class="arrow">➔</span>
            </a>

        </div>

        <footer>
            © AN Project • Powered by Termux
        </footer>
    </div>

</body>
</html>
EOF
