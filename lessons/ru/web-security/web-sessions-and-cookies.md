---
lesson_id: "web-sessions-and-cookies"
course_id: "web-security"
lang: "ru"
order_index: 5
title: "Сеансы и cookie"
description: "Узнайте, как cookie связывает запросы браузера с веб-сеансом."
meta_title: "Сеансы и cookie — Веб-безопасность"
meta_description: "Узнайте, как cookie связывает запросы браузера с веб-сеансом."
meta_keywords: "сеансы, cookie, веб-безопасность, кибербезопасность, Linux Journey"
---

После успешного входа браузер обычно отправляет следующие запросы. **Сеанс** позволяет приложению связать их с учётной записью, которая уже вошла. Один распространённый способ — хранить в cookie браузера короткий идентификатор.

## Как передаётся cookie

Примеры сокращены. В ответе передаётся cookie с именем `session` и вымышленным токеном для наглядности.

```http
Set-Cookie: session=sample-token; Secure; HttpOnly; SameSite=Lax
```

Затем браузер может включить этот cookie в очередной запрос, который соответствует правилам его отправки.

```http
Cookie: session=sample-token
```

Сервер по токену находит ранее созданный сеанс.

:::single-choice{#web-sessions-and-cookies-direction} Какой заголовок передаёт значение cookie обратно в подходящем запросе?

::option[Set-Cookie.]{#web-sessions-and-cookies-direction-a explanation="Сервер отправляет этот заголовок в ответе, чтобы установить cookie."}
::option[Content-Type.]{#web-sessions-and-cookies-direction-c explanation="Этот заголовок описывает формат тела сообщения."}
::option[Cookie.]{#web-sessions-and-cookies-direction-b .correct explanation="Браузер добавляет этот заголовок в запрос, когда выполнены правила отправки."}
:::

## Как читать атрибуты

`Secure` ограничивает обычную передачу cookie соединениями HTTPS. `HttpOnly` закрывает скриптам страницы доступ к cookie через обычный интерфейс работы с cookie. `SameSite` управляет тем, когда браузер передаёт его в запросах, начатых с другого сайта. Каждый атрибут отвечает за свою часть поведения браузера.

:::single-choice{#web-sessions-and-cookies-secure-attribute} Какой атрибут ограничивает передачу этого cookie соединениями HTTPS?

::option[HttpOnly.]{#web-sessions-and-cookies-secure-attribute-b explanation="Он ограничивает доступ скриптов страницы к cookie."}
::option[Secure.]{#web-sessions-and-cookies-secure-attribute-a .correct explanation="Этот атрибут относится к защищённому соединению, по которому передаётся cookie."}
::option[Имя session.]{#web-sessions-and-cookies-secure-attribute-c explanation="Имя cookie — это метка, которую выбирает приложение."}
:::

## Как завершить сеанс

Когда пользователь выходит, сервис может завершить сеанс на сервере и попросить браузер удалить сохранённый cookie. Завершение на сервере важно, потому что у браузера ещё некоторое время может оставаться прежнее значение. Обращайтесь с настоящим токеном сеанса так же, как с данными для входа, и исключайте его из снимков экрана и общих журналов.

:::single-choice{#web-sessions-and-cookies-after-sign-out} Что должно произойти, если на сервер снова поступит токен завершённого сеанса?

::option[Сервер должен обработать запрос как не прошедший аутентификацию.]{#web-sessions-and-cookies-after-sign-out-c .correct explanation="Связанный с этим значением сеанс на сервере больше не действует."}
::option[Сервер должен автоматически восстановить прежний сеанс.]{#web-sessions-and-cookies-after-sign-out-a explanation="Прежний сеанс завершён."}
::option[Сервер должен принять токен, потому что у cookie есть имя.]{#web-sessions-and-cookies-after-sign-out-b explanation="Имя cookie не делает его значение действительным."}
:::

## Итоги

Теперь вы можете проследить передачу cookie сеанса между браузером и сервисом.

1. Определить, какой заголовок устанавливает cookie, а какой отправляет его обратно.
2. Объяснить назначение распространённых атрибутов cookie.
3. Описать, как сервер завершает сеанс и перестаёт принимать его токен.
