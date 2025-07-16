# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (for PyMySQL and date handling)
RUN apt-get update && apt-get install -y gcc libmariadb-dev && rm -rf /var/lib/apt/lists/*

# Copy project files into the container
COPY /app .
COPY /requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5004

# Run the app
CMD ["python", "run.py"]
