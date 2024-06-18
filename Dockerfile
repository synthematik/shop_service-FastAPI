FROM python:3.12

RUN mkdir /shop_store

WORKDIR /shop_store

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "src.main:app", "--bind=0.0.0.0:8000"]