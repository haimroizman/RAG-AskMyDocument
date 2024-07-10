From python:3.12
# prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# ensures that the python output is sent straight to terminal without buffering it first(for logging purposes)
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install dependencies to the app directory without caching
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Expose the port FastAPI is running on
EXPOSE 8000

# Run the FastAPI application -> the reload is for development purposes, I know that in production it should be disabled!!!!
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]