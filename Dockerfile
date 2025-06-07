FROM python:3.11

RUN adduser --disabled-password --gecos '' --uid 10001 botuser

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

USER 10001

CMD ["python", "-m", "bot"]
