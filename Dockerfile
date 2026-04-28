FROM mcr.microsoft.com/playwright:v1.40.0-focal

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    xvfb \
    x11-utils \
    fluxbox \
    libxkbcommon-x11-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    playwright install webkit && \
    playwright install-deps webkit

WORKDIR /app

# Запустите Xvfb и bash
ENTRYPOINT ["bash", "-c"]
CMD ["Xvfb :99 -screen 0 1920x1080x24 & export DISPLAY=:99 && /bin/bash"]