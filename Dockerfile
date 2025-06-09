FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (optional: only if your requirements need them)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy app files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Choreo expects the app to run on port 8080 by default
ENV PORT 8080

# Expose port (not strictly required by choreo, but good practice)
EXPOSE 8080

# Start the Python bot
CMD ["python", "-m", "bot"]
