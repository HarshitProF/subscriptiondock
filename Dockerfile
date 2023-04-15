# Use the official Python image as the base image
FROM python:3.11.1

# Set the working directory in the container
WORKDIR /bot

# Copy the application files into the working directory
COPY . /bot

EXPOSE 4000 

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["python", "-m", "bot"]