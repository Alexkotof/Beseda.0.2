# beseda
1) Скачать директорию https://github.com/Alexkotof/Beseda.0.2.git
2) Перейти в скачаную директорию и из нее создать docker образ : docker build -t beseda .
3) Запустить контейнер : docker run --rm --name chat -p 5000:5000 -e TZ=Europe/Moscow beseda

Описание проекта:

Чат с использованием flask+SocketIO+docker+MongoDB.
В чате есть функции регистрации, входа и выбора "беседы", в которой хотите поговорить.
