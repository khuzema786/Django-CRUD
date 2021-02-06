# Import Python Image
FROM python:3.8.6

# Setting PYTHONUNBUFFERED to a non empty value ensures 
# that the python output is sent straight to terminal 
# (e.g. your container log) without being first buffered 
# and that you can see the output of your application (e.g. django logs) 
# in real time.
# This also ensures that no partial output is held in a buffer somewhere 
# and never written in case the python application crashes.
ENV PYTHONUNBUFFERED 1

# Create a new direcctory & set it to current directory
RUN mkdir /code
WORKDIR /code

# Add requirements.txt to /code/ & run
ADD requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Add all files to /code/
ADD . /code/