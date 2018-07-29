# Use an official Python runtime as a parent image
FROM python:3.6.6

# Copy the current directory contents into the container
ADD . /hnparse

# Set the working directory
WORKDIR /hnparse

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#specify what to run within the container
CMD python ./hackernews
