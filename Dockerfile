FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install system dependencies needed for OpenCV and rembg
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Hugging Face Spaces uses port 7860
EXPOSE 7860

# Update this to use wsgi.py with the correct port
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "wsgi:app"]
