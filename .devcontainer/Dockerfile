# Use Ubuntu 14.04 LTS as base image
FROM ubuntu:14.04

# Install Python 3.4
RUN apt-get update && apt-get install -y python3.4 python3-pip

# Set Python 3.4 as the default Python version
RUN ln -s /usr/bin/python3.4 /usr/bin/python

# Upgrade pip
RUN python -m pip install --upgrade pip