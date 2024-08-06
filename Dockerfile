FROM python:3.8-slim-buster

# Update and install dependencies
RUN apt update && apt upgrade -y
RUN apt install git -y

# Copy requirements and install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install -U pip && pip3 install -U -r /requirements.txt

# Copy the start script to the container
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Set the working directory
WORKDIR /Ultra-Forward-Bot

# Set the start script as the default command
CMD ["/bin/bash", "/start.sh"]