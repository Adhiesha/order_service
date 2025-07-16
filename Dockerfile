# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (for PyMySQL)
RUN apt-get update && apt-get install -y gcc libmariadb-dev && rm -rf /var/lib/apt/lists/*

# Copy everything into /app in container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set environment variables
ENV PYTHONPATH=/app

# Expose Flask port
EXPOSE 5004

# Run the app
CMD ["python", "app/run.py"]
