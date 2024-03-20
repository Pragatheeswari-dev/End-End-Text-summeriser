# Description: Dockerfile for the application to run in a container environment 
# Author: Pragatheeswari Velraj
# Created: 2024-03-20
# The Dockerfile is used to build the image for the application to run in a container environment.

FROM python:3.8-slim-buster 
# Base image for the application


# Install awscli to download the model from s3 bucket
RUN apt update -y && apt install awscli -y 
# Set the working directory in the container
WORKDIR /app 

# Copy the application files to the container image
COPY . /app 

# Install the required packages for the application
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate
RUN pip install transformers[torch] accelerate

# Command to run the application in the container environment
CMD ["python3", "app.py"] 