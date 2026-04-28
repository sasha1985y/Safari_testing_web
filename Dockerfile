FROM mcr.microsoft.com/playwright:v1.40.0-focal

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    xvfb \
    tigervnc-standalone-server \
    fluxbox \
    xterm \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    playwright install webkit && \
    playwright install-deps webkit

# Создайте VNC конфиг С паролем
RUN mkdir -p ~/.vnc && \
    echo "#!/bin/bash" > ~/.vnc/xstartup && \
    echo "fluxbox &" >> ~/.vnc/xstartup && \
    chmod +x ~/.vnc/xstartup

# Установите пароль VNC (пароль: playwright)
RUN echo "playwright" | vncpasswd -f > ~/.vnc/passwd && \
    chmod 600 ~/.vnc/passwd

WORKDIR /app

# Запустите VNC с паролем
CMD ["bash", "-c", "\
    echo '🚀 Запуск VNC сервера...' && \
    vncserver -kill :1 2>/dev/null || true && \
    sleep 1 && \
    vncserver -geometry 1920x1080 -depth 24 -localhost no :1 && \
    echo '✅ VNC запущен на localhost:5901' && \
    echo '🔐 Пароль: playwright' && \
    tail -f /dev/null \
"]