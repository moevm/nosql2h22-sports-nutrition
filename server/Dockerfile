FROM python:3.8-slim-buster

ENV PYTHONPATH "${PYTHONPATH}:/"

COPY . ./server
RUN apt-get update \
    && pip install --no-cache-dir -r ./server/requirements.txt

ENTRYPOINT ["python3", "./server/main.py"]