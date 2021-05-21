FROM tiangolo/uvicorn-gunicorn-fastapi:latest
COPY . /app
WORKDIR /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt