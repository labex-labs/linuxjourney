---
lesson_id: "web-http-requests-responses"
course_id: "web-security"
lang: "ru"
order_index: 1
title: "Запросы и ответы HTTP"
description: "Научитесь читать метод, путь, статус и тип содержимого в обмене HTTP."
meta_title: "Запросы и ответы HTTP — Веб-безопасность"
meta_description: "Научитесь читать метод, путь, статус и тип содержимого в обмене HTTP."
meta_keywords: "запросы и ответы HTTP, веб-безопасность, кибербезопасность, Linux Journey"
---

Браузер или другой клиент обращается к веб-серверу с **запросом HTTP**. Сервер возвращает **ответ HTTP**. По этим двум сообщениям можно узнать, что запросил клиент и что вернул сервер.

## Как читать запрос

Перед вами короткий запрос HTTP/1.1. `GET` — метод, обозначающий действие, которое запрашивает клиент. `/health` — путь. Заголовок `Host` указывает, к какому сайту обращается клиент.

```http
GET /health HTTP/1.1
Host: site.example
```

**Заголовок** — именованное значение со сведениями о сообщении. Метод и путь указаны в первой строке запроса.

:::single-choice{#web-http-requests-responses-request-path} Что клиент просит получить с сервера?

::option[Файл с именем HTTP/1.1.]{#web-http-requests-responses-request-path-b explanation="В этом поле указана версия протокола."}
::option[Ресурс по пути /health.]{#web-http-requests-responses-request-path-a .correct explanation="Путь указан после GET в первой строке."}
::option[Ресурс по пути /site.example.]{#web-http-requests-responses-request-path-c explanation="Заголовок Host обозначает сайт. Путь указан отдельно."}
:::

## Как читать ответ

В пустой папке для упражнений создайте страницу и запустите HTTP-сервер Python на адресе обратной петли. Перенаправление вывода запишет страницу. Оставьте сервер запущенным в этом терминале, пока запрос не завершится. Затем остановите его сочетанием Ctrl+C.

```bash
$ mkdir web-demo
$ printf '%s\n' ready > web-demo/health.txt
$ python3 -m http.server 8094 --bind 127.0.0.1 --directory web-demo
```

Во втором терминале на той же машине выполните `curl -i`. Параметр выводит заголовки ответа перед содержимым.

```bash
$ curl -i http://127.0.0.1:8094/health.txt
```

В начале ответа указан **код статуса**. Код `200` означает, что запрос выполнен успешно. Пустая строка отделяет заголовки от тела ответа. `Content-Type` подсказывает клиенту, как читать тело, например как обычный текст.

:::single-choice{#web-http-requests-responses-response-parts} Что помогает клиенту решить, как показать содержимое?

::option[Заголовок ответа Content-Type.]{#web-http-requests-responses-response-parts-b .correct explanation="В нём указан тип тела ответа."}
::option[Имя хоста в исходном запросе.]{#web-http-requests-responses-response-parts-a explanation="Оно обозначает сайт, к которому обратился клиент."}
::option[Только путь.]{#web-http-requests-responses-response-parts-c explanation="Путь указывает ресурс, но не определяет формат ответа."}
:::

![Сохранённый ответ HTTP из LabEx со статусом 200, текстовым типом содержимого и телом ready](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-http-requests-responses/http-response.png)

## Как сравнивать результаты

Ответ `404` означает, что сервер не нашёл запрошенный ресурс или не сообщает о его наличии. По одному пути сервер может вернуть 200, а по другому — 404. При сравнении результатов учитывайте точные метод и путь.

:::single-choice{#web-http-requests-responses-health-scope} Запрос к /health получил 200. Что можно сказать о /welcome?

::option[Путь /welcome тоже вернул 200.]{#web-http-requests-responses-health-scope-a explanation="В примере проверялся другой путь."}
::option[До хоста не удалось достучаться.]{#web-http-requests-responses-health-scope-b explanation="На запрос проверки состояния пришёл ответ."}
::option[Результат станет известен после запроса к /welcome.]{#web-http-requests-responses-health-scope-c .correct explanation="Два пути могут давать разные результаты."}
:::

Чтобы попрактиковаться в проверке заголовков ответа и доступности сервера, пройдите урок [Как проверить подключение к серверу с помощью curl в Linux](https://labex.io/tutorials/linux-how-to-test-server-connectivity-with-curl-in-linux-415082).

## Итоги

Теперь вы можете читать основные части простого обмена HTTP.

1. Найти метод, путь и хост в запросе.
2. Прочитать статус и тип содержимого в ответе.
3. Описать результат именно того запроса, который был выполнен.
