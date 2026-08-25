cat << 'EOF' > index.html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AN Project - Links & AI</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #09090b 100%);
            color: #ffffff;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            width: 100%;
            max-width: 420px;
            text-align: center;
        }

        .profile-img {
            width: 96px;
            height: 96px;
            border-radius: 50%;
            background: linear-gradient(135deg, #6366f1, #a855f7);
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 42px;
            margin: 0 auto 16px auto;
            box-shadow: 0 10px 25px rgba(168, 85, 247, 0.4);
            border: 3px solid rgba(255, 255, 255, 0.2);
        }

        h1 {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 6px;
            letter-spacing: -0.5px;
        }

        p.bio {
            color: #94a3b8;
            font-size: 0.9rem;
            margin-bottom: 28px;
        }

        .links-container {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .link-card {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 20px;
            background: rgba(255, 255, 255, 0.06);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 16px;
            color: #ffffff;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        .link-card:hover, .link-card:active {
            transform: translateY(-3px) scale(1.02);
            background: rgba(255, 255, 255, 0.12);
            border-color: rgba(168, 85, 247, 0.5);
            box-shadow: 0 8px 25px rgba(168, 85, 247, 0.25);
        }

        .link-info {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .icon-box {
            width: 38px;
            height: 38px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }

        .ai-bg { background: rgba(99, 102, 241, 0.2); color: #818cf8; }
        .tiktok-bg { background: rgba(244, 63, 94, 0.2); color: #fb7185; }

        .arrow {
            color: #64748b;
            font-size: 1.1rem;
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
