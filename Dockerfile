# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files and run migrations at container startup
# Best practice: use an entrypoint script for this
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000"]
