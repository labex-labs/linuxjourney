---
lang: "ru"
title: "Цели Systemd"
description: "Изучите основы юнитов systemd и основные команды systemctl. Узнайте, как управлять службами, просматривать статусы и включать юниты в Linux. Начните свой путь!"
keywords: "systemd, systemctl, службы Linux, файлы юнитов, для начинающих, учебник, руководство, команды Linux"
---

## Lesson Content

Мы не будем вдаваться в детали написания файлов systemd unit. Однако мы кратко рассмотрим файл unit и то, как вручную управлять юнитами.

Вот базовый файл service unit: foobar.service

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

Это простой service target. В начале файла мы видим секцию для `[Unit]`. Это позволяет нам дать файлу unit описание, а также контролировать порядок активации юнита. Следующая часть — секция `[Service]`; здесь мы можем запустить, остановить или перезагрузить службу. А секция `[Install]` используется для зависимостей. Это лишь верхушка айсберга для написания файлов systemd, поэтому я настоятельно рекомендую вам изучить эту тему, если вы хотите узнать больше.

Теперь давайте рассмотрим некоторые команды, которые вы можете использовать с юнитами systemd:

### List units

```bash
systemctl list-units
```

### View status of unit

```bash
systemctl status networking.service
```

### Start a service

```bash
sudo systemctl start networking.service
```

### Stop a service

```bash
sudo systemctl stop networking.service
```

### Restart a service

```bash
sudo systemctl restart networking.service
```

### Enable a unit

```bash
sudo systemctl enable networking.service
```

### Disable a unit

```bash
sudo systemctl disable networking.service
```

Опять же, вы еще не видели, насколько глубоко systemd проникает, поэтому изучите его, если хотите узнать больше.

## Exercise

Просмотрите статусы юнитов и запустите/остановите несколько служб. Что вы наблюдаете?

## Quiz Question

Какая команда используется для запуска службы с именем peanut.service?

## Quiz Answer

sudo systemctl start peanut.service
