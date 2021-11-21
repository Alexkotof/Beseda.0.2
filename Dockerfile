FROM python:3.9

RUN mkdir -p /usr/chat
WORKDIR /usr/chat

COPY . /usr/chat
RUN pip  install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV TZ Europe/Moscow

#CMD ["python", "app.py"]
ENTRYPOINT ["python", "app.py"]