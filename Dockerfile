FROM python:3.9

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app_backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x wait-for-it.sh

ENTRYPOINT ["bash", "-c"]

CMD ["python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
