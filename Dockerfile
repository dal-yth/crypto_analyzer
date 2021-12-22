FROM python:3.10-alpine

ENV FLASK_APP main.py
ENV FLASK_ENV production

RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY app app
COPY main.py config.py ./

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]