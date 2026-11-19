---
lesson_id: "compose-files"
course_id: "docker-compose"
lang: "ru"
order_index: 1
title: "Файлы Compose"
description: "Научитесь находить в файле Compose сервисы, образы, команды и порты."
meta_title: "Файлы Compose - Docker Compose"
meta_description: "Научитесь находить в файле Compose сервисы, образы, команды и порты."
meta_keywords: "файлы Compose, сервисы, Docker Compose, DevOps, Linux Journey"
---

Один раз запустить веб-сервер и вспомогательную программу можно отдельными командами. **Файл Compose** собирает настройки в одном месте, чтобы вы могли снова запустить те же сервисы. Для курса нужна среда Docker с подключаемым модулем Compose, который предоставляет команду `docker compose`.

## Описываем два сервиса

Создайте учебный каталог `journey-compose` и сохраните в нём пример под именем `compose.yaml`. **Сервис** описывает, как Compose должен запускать контейнер. В этом файле описаны веб-сервер и небольшой контейнер с инструментами, который останется запущенным для следующих проверок.

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8080:80"
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
```

Для отступов используйте пробелы. Ключи с отступом под `web` относятся к этому сервису. Дефис под `ports` начинает элемент списка. Квадратные скобки в `command` тоже обозначают список. В данном случае там указаны имя программы и её аргумент.

:::single-choice{#compose-files-service-images} Какой сервис использует образ BusyBox?

::option[Сервис web.]{#compose-files-service-images-a explanation="В строке с образом у web указано nginx."}
::option[Сервис toolbox.]{#compose-files-service-images-c .correct explanation="В поле image у toolbox указано busybox:1.36."}
::option[Оба сервиса.]{#compose-files-service-images-b explanation="У каждого сервиса своё поле с образом."}
:::

## Читаем настройки веб-сервиса

Веб-сервис публикует порт 80 контейнера на порту 8080 хоста. После запуска сервиса запрос к `http://127.0.0.1:8080` с компьютера, на котором работает Docker, может достичь Nginx. У контейнера с инструментами опубликованных портов нет. Команда `sleep` оставляет его запущенным на время упражнения, на 3600 секунд.

:::single-choice{#compose-files-mapping-owner} Какая настройка определяет, как браузер на хосте Docker подключается к Nginx?

::option[Настройка ports в разделе web.]{#compose-files-mapping-owner-a .correct explanation="Эта запись связывает адрес и порт хоста с веб-контейнером."}
::option[Тег образа в разделе toolbox.]{#compose-files-mapping-owner-b explanation="Он выбирает образ для контейнера с инструментами."}
::option[Аргумент команды sleep в разделе toolbox.]{#compose-files-mapping-owner-c explanation="Аргумент определяет, как долго выполняется программа."}
:::

## Проверяем, как Compose прочитал настройки

Выполните команду в каталоге с файлом. Введите только то, что стоит после приглашения `$`. Compose читает `compose.yaml` и выводит конфигурацию так, как он её понял. Найдите записи `web` и `toolbox`. Кратко записанные настройки могут выводиться в более подробном виде.

```bash
$ docker compose config
```

:::single-choice{#compose-files-config-scope} Команда без ошибок показала два сервиса. Что удалось проверить?

::option[Оба контейнера запустились.]{#compose-files-config-scope-a explanation="Команда читает и выводит настройки."}
::option[Браузер получил успешный ответ.]{#compose-files-config-scope-c explanation="Запрос можно проверить после запуска сервера."}
::option[Compose может прочитать определения обоих сервисов.]{#compose-files-config-scope-b .correct explanation="Прочитанную конфигурацию можно проверить до запуска сервисов."}
:::

## Итоги

Теперь вы можете читать простой файл Compose.

1. Находите имена сервисов и ссылки на образы в разделе services.
2. Соотносите настройки сервиса с контейнером, который они описывают.
3. Проверяйте прочитанные настройки командой docker compose config.
