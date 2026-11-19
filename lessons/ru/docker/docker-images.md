---
lesson_id: "docker-images"
course_id: "docker"
lang: "ru"
order_index: 2
title: "Образы"
description: "Научитесь читать ссылку на образ и проверять, есть ли этот образ в локальном хранилище."
meta_title: "Образы - Docker"
meta_description: "Разберитесь в именах и тегах образов Docker, узнайте, откуда загружаются образы, и научитесь отличать их список от списка контейнеров."
meta_keywords: "образы Docker, теги образов, реестр образов, docker pull, docker image ls"
---

Образ Docker содержит программу, её файлы и настройки по умолчанию. Из этого пакета Docker создаёт контейнер. В этом уроке вы научитесь читать имена образов и узнавать, какие из них уже есть у Docker.

## Как читать имя и тег образа

В ссылке `nginx:alpine` часть `nginx` — это имя образа, а `alpine` — **тег**, по которому выбирают конкретную версию или вариант. Здесь тег указывает на вариант на базе Alpine Linux. Имя и тег разделяет двоеточие. Ссылки `nginx:alpine` и `nginx:latest` различаются, хотя имя образа у них одно.

:::single-choice{#docker-images-read-reference} Какая часть ссылки `busybox:1.36` является тегом?

::option[`busybox`]{#docker-images-reference-name explanation="BusyBox — это имя перед двоеточием."}
::option[`busybox:1.36`]{#docker-images-reference-whole explanation="Полная ссылка содержит и имя образа, и тег."}
::option[`1.36`]{#docker-images-reference-tag .correct explanation="Тег находится после двоеточия. По нему Docker выбирает образ."}
:::

## Выбор тега

Если опустить тег и написать, например, `nginx`, Docker использует `latest`. Это условленное имя тега. Тот, кто публикует образ, сам задаёт, на какой образ указывает тег, и может изменить его позже. Ссылка `nginx:alpine` явно указывает нужный вариант. Образ под этим тегом тоже может обновляться.

:::single-choice{#docker-images-default-tag} Коллега указал `nginx` без тега и считает, что Docker выбрал самый новый выпуск. Что на самом деле было выбрано?

::option[Образ, на который указывает тег latest.]{#docker-images-default-latest .correct explanation="При отсутствии тега используется latest. На какой образ он указывает, решает тот, кто публикует образ."}
::option[Самый недавно опубликованный образ Nginx.]{#docker-images-default-newest explanation="Docker использует тег с именем latest. Образы не сортируются по времени публикации."}
::option[Самый маленький доступный образ Nginx.]{#docker-images-default-smallest explanation="Размер образа не определяет тег по умолчанию. Указывайте нужный вариант по имени."}
:::

## Загрузка образа

**Реестр** хранит образы и выдаёт их по запросу. Для ссылок вроде `nginx:alpine` Docker по умолчанию обращается к Docker Hub. Чтобы скачать образ в среду Docker, к которой вы подключены, выполните `docker pull`. Эту операцию также называют **загрузкой образа из реестра**.

```bash
$ docker pull nginx:alpine
```

Если команда выполнилась успешно, образ будет доступен в этой среде. Запуск контейнера — отдельное действие. В примерах терминала `$` обозначает приглашение командной строки.

:::single-choice{#docker-images-pull-result} Загрузка образа завершилась успешно. Что сделал Docker?

::option[Запустил контейнер, который отвечает на веб-запросы.]{#docker-images-pull-started explanation="Контейнер запускается отдельной командой. Загрузка лишь делает образ доступным."}
::option[Сделал образ доступным для использования в этой среде.]{#docker-images-pull-available .correct explanation="Загруженный образ теперь можно использовать как основу для контейнера."}
::option[Отправил копию образа в реестр.]{#docker-images-pull-uploaded explanation="Pull переносит образ из реестра в локальное хранилище Docker."}
:::

## Проверка локальных образов

Команда `docker image ls` показывает уже доступные образы. В примере оставлены только столбцы с именем и тегом. В выводе Docker столбец с именем называется `REPOSITORY`.

```text
$ docker image ls
REPOSITORY   TAG
nginx        alpine
busybox      1.36
```

В первой строке указан `nginx:alpine`. Из этой таблицы можно узнать, какие образы есть в системе. Состояние созданных из них контейнеров проверяется по другому списку.

![Терминал LabEx с выводом docker pull и столбцами REPOSITORY и TAG из docker image ls](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-images/pull-and-list.png)

В снимке список отфильтрован до двух ссылок, использованных в уроке.

:::single-choice{#docker-images-local-list} Какая ссылка есть в этом выводе?

::option[`busybox:latest`]{#docker-images-local-busybox-latest explanation="В строке busybox указан тег 1.36. Строки busybox с тегом latest здесь нет."}
::option[`busybox:1.36`]{#docker-images-local-busybox .correct explanation="Объедините busybox из столбца REPOSITORY и 1.36 из столбца TAG."}
::option[`nginx:1.36`]{#docker-images-local-nginx-mixed explanation="Имя и тег нужно брать из одной строки. Здесь 1.36 относится к busybox."}
:::

## Итоги

Теперь вы можете прочитать ссылку на образ и проверить, есть ли он в локальном списке.

1. Определить имя и тег в ссылке на образ.
2. Объяснить, что произойдёт, если не указать тег.
3. Загрузить образ из реестра с помощью `docker pull`.
4. Прочитать столбцы с именем и тегом в выводе `docker image ls`.
