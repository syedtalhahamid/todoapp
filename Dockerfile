
# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 5000

# Run flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run", "--port=5000"]
