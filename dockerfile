FROM python:3.9-alpine3.15

ENV PYTHONBUFFERED=1

WORKDIR /Dashboard

COPY . .

RUN pip install -r requirements.txt

CMD python dashboard

EXPOSE 8050
