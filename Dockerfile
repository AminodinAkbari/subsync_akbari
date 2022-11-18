FROM python:3.10.5-slim

WORKDIR /subsync_akbari

COPY ./requirements.txt /subsync_akbari/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /subsync_akbari/requirements.txt

COPY . /subsync_akbari

CMD ["uvicorn", "main.main:app","--root-path /subsync_akbari/" , "--proxy-headers", "--host", "0.0.0.0", "--port", "8004"]

