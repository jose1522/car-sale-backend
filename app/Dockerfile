FROM tiangolo/uvicorn-gunicorn-fastapi:latest
COPY ./app /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r ./app/requirements.txt
WORKDIR /app