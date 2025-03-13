# Use the official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Django runs on
EXPOSE 8000

# Command to start Django
CMD ["gunicorn", "sendify.wsgi:application", "--bind", "0.0.0.0:8000"]
