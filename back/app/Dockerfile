FROM python:3.12

WORKDIR /app

COPY ./req.txt .

RUN pip install --no-cache-dir --upgrade -r req.txt

COPY . .

CMD ["python", "main.py"]