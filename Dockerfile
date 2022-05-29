FROM python:3.10-slim

ENV TZ=Europe/Lisbon
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /etc/api

COPY ./requirements.txt /etc/api/requirements.txt

RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /etc/api/requirements.txt

COPY ./content /etc/api

CMD ["sh", "entrypoint.sh"]
