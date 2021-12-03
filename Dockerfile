FROM python:3.10-alpine

RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY app/ .

CMD ["flask", "run", "--host", "0.0.0.0"]