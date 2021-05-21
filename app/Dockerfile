FROM tiangolo/uvicorn-gunicorn-fastapi:latest
WORKDIR /
RUN ls -a
ADD . ./app
RUN ls -a
RUN ls -a ../
RUN ls -a /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt
WORKDIR /app