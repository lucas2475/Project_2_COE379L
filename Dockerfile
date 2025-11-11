# Use official Python runtime as base image
FROM python:3.11

# Set working directory in container
WORKDIR /app

# Install system dependencies

# For x86
RUN apt-get update && apt-get install -y \
    # libgl1-mesa-glx \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# For mac
# RUN apt-get update && apt-get install -y \
# libgl1 \
# libglib2.0-0 \
# && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app_flask.py .
COPY best_model.keras .

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app_flask.py
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "app_flask.py"]