FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Expose the port
EXPOSE 8000

# Command to run your FastAPI app
CMD ["uvicorn", "aap.routr.main:app", "--host", "0.0.0.0", "--port", "8000"]
