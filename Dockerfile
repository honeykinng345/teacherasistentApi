# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y \
    libnss3 \
    libatk-bridge2.0-0 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libxkbcommon0 \
    libgtk-3-0 \
    libgbm-dev \
    libpango-1.0-0 \
    libxshmfence-dev \
    libegl1 \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libx11-xcb1 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install --with-deps



# Command to run the application
CMD ["python", "app.py"]
