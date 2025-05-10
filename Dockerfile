# Using a stable, reproducible base image
FROM python:3.13.2-alpine3.21

# Creates a non-root user and set ownership
RUN adduser -D myuser

# Set the environment PATH
ENV PATH=$PATH:/home/myuser/.local/bin

# Set the non-root user to run the application
USER myuser

# Set the working directory
WORKDIR /app

# Copy the requirements file to the Docker image
COPY fastapi_app/requirements.txt ./

# Install project dependencies
RUN pip install --no-cache-dir --upgrade pip==25.1.1 && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the Docker image
COPY fastapi_app/server_api.py ./

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "server_api.py"]

