# Backend Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . /app

# Set environment to development for Flask to auto-reload on code changes
ENV FLASK_ENV=development

# Expose port 5000 (or any port your Flask app uses)
EXPOSE 5000

# Use watchmedo for auto-reload on code changes, or directly rely on Flask's built-in reloader
CMD ["flask", "run", "--host=0.0.0.0"]
