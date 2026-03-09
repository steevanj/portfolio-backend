# Use official Python image
FROM python:3.11

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure Python output is sent straight to terminal
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Wait for MySQL, run migrations, collect static, start Gunicorn
CMD ["sh", "-c", "sleep 15 && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000 --workers 3"]