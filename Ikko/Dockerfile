# Use the official Python image as the base image
FROM python:3.12.3

# Install system dependencies
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -ms /bin/bash appuser

# Set the working directory
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Create and activate the virtual environment, then install dependencies
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Change ownership of the app directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Set environment variable for the virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Command to run the bot or Django server
CMD ["sh", "-c", ". venv/bin/activate && python manage.py collectstatic && python manage.py runserver 0.0.0.0:8001"]