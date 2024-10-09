FROM python:3.12-bullseye

ENV PYTHONBUFFERD=1
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

WORKDIR /KafkaDjango

COPY . /KafkaDjango/

RUN apt update && apt-get install -y gcc
RUN apt-get update && apt install -y librdkafka-dev && \
    apt install -y python3-dev && \
    apt install -y libssl-dev

RUN pip3 install -r requirements.txt --no-cache-dir

RUN chmod +x docker-entrypoint.sh

CMD ["/KafkaDjango/docker-entrypoint.sh"]
