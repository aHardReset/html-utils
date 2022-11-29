FROM tiangolo/uvicorn-gunicorn:python3.9-slim

LABEL maintainer = "Aaron Garibay <aaron.contreras@unosquare.com>"

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./html_utils /app
