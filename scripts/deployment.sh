#!/bin/bash

set -e  # Exit on error

# Check if pyfiglet is installed
if ! command -v figlet &> /dev/null; then
    echo "Installing pyfiglet..."
    pip install pyfiglet
fi

# Function to print section headers
print_header() {
    echo
    figlet "$1"
    echo
}

# Check if required directories exist
if [ ! -d "./nginx" ] || [ ! -d "./docker" ] || [ ! -d "./scripts" ]; then
    echo "Error: Required directories not found. Please run this script from the project root."
    exit 1
fi

# Download packages
print_header "PACKAGES DOWNLOAD"
if [ ! -x "./scripts/cr_pull.sh" ]; then
    chmod +x ./scripts/cr_pull.sh
fi
./scripts/cr_pull.sh

# Setup HTTPS
print_header "HTTP/HTTPS"
docker-compose -f docker/docker-compose.staging.yml up -d swag
docker-compose -f docker/docker-compose.staging.yml down

# Copy nginx files
print_header "NGINX"
if [ ! -d "/home/withnoedge/swag" ]; then
    echo "Creating swag directory..."
    mkdir -p /home/withnoedge/swag
fi
cp -Rf ./nginx/* /home/withnoedge/swag/

# Start services
print_header "SERVER READY"
docker-compose -f docker/docker-compose.staging.yml up -d
