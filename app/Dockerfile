FROM tiangolo/uvicorn-gunicorn-fastapi:latest
RUN ls -a
WORKDIR /
COPY . /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN ls -a
RUN ls -a ../
RUN ls -a ./app
RUN pip install -r /app/requirements.txt
WORKDIR /app