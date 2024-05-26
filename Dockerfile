# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Update package lists and install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    awscli \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py file to the working directory
COPY app.py .

# Expose the port that the app will be running on
EXPOSE 8501

# Set the entrypoint command to run the app.py file
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]
