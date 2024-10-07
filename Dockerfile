FROM python:3.12-bullseye
EXPOSE 8000
WORKDIR /KafkaDjango
COPY ./requirements.txt .
RUN apt update && apt-get install -y gcc
RUN apt-get update && apt install -y librdkafka-dev && \
    apt install -y python3-dev && \
    apt install -y libssl-dev
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
