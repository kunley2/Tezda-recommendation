FROM python:3.10.9 
# Image from dockerhub
# Expose the port 5000 in which our application runs
RUN apt update
RUN pip install --upgrade pip

ENV PORT=8000
EXPOSE 8000 
# Upgrade pip
WORKDIR /app 
# Make /app as a working directory in the container
COPY . .
RUN pip install -r requirements.txt 
CMD ["python", "main.py"]
# CMD gunicorn --worker-class g