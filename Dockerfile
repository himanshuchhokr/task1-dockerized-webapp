# Base image: a lightweight official Python image
FROM python:3.12-slim

# Don't buffer stdout — logs show up immediately (helpful when debugging containers)
ENV PYTHONUNBUFFERED=1

# Working directory inside the container
WORKDIR /app

# Copy only requirements first — Docker caches this layer, so re-builds
# after just changing app code won't reinstall dependencies every time.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application code
COPY . .

# Document which port the app listens on (informational; doesn't publish it)
EXPOSE 5000

# Run with Gunicorn (production-grade WSGI server) instead of Flask's dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
