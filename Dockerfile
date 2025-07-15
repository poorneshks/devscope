# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
