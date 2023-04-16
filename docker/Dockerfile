# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set the environment variables for the PostgreSQL instance
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=testdb

# Copy the initialization script to the container
COPY init.sql /docker-entrypoint-initdb.d/

# Set the working directory to /app
WORKDIR /app

# Expose port 5432 for PostgreSQL connections
EXPOSE 5432

# Install Azure CLI and configure ACR authentication
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -sL https://aka.ms/InstallAzureCLIDeb | bash && \
    az login --service-principal -u $SERVICE_PRINCIPAL_ID -p $SERVICE_PRINCIPAL_SECRET --tenant $TENANT_ID && \
    az acr login --name $ACR_NAME

# Set the entrypoint command to start PostgreSQL
CMD ["postgres"]
