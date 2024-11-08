# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Command to run the FastAPI application on port 8003
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
