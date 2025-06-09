FROM python:3.11-slim

# Create a non-root user with UID in the allowed range (10001+ for Choreo)
RUN adduser --disabled-password --gecos '' --uid 10001 botuser

# Install system dependencies (customize based on your actual bot needs)
RUN apt-get update && apt-get install -y ffmpeg libsndfile1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Switch to the non-root user (required by Choreo)
USER 10001

# Expose default Choreo port (optional, useful if you run a web server)
EXPOSE 8080

# Start the bot (adjust if your entry point is different)
CMD ["python", "-m", "bot"]
