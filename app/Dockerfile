FROM tiangolo/uvicorn-gunicorn-fastapi:latest
WORKDIR /
COPY . /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt
WORKDIR /app