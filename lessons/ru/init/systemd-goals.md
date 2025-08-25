---
index: 6
lang: "ru"
title: "Цели Systemd"
meta_title: "Цели Systemd - Init"
meta_description: "Изучите основы юнитов systemd и основные команды systemctl. Узнайте, как управлять службами, просматривать статусы и включать юниты в Linux. Начните свой путь!"
meta_keywords: "systemd, systemctl, службы Linux, файлы юнитов, для начинающих, учебник, руководство, команды Linux"
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

Это простая цель службы. В начале файла мы видим раздел для `[Unit]`. Это позволяет нам дать файлу unit описание, а также контролировать порядок активации юнита. Следующая часть — это раздел `[Service]`; здесь мы можем запускать, останавливать или перезагружать службу. А раздел `[Install]` используется для зависимостей. Это лишь верхушка айсберга для написания файлов systemd, поэтому я призываю вас прочитать об этом, если вы хотите узнать больше.

Теперь давайте рассмотрим некоторые команды, которые вы можете использовать с юнитами systemd:

### Список юнитов

```bash
systemctl list-units
```

### Просмотр статуса юнита

```bash
systemctl status networking.service
```

### Запуск службы

```bash
sudo systemctl start networking.service
```

### Остановка службы

```bash
sudo systemctl stop networking.service
```

### Перезапуск службы

```bash
sudo systemctl restart networking.service
```

### Включение юнита

```bash
sudo systemctl enable networking.service
```

### Отключение юнита

```bash
sudo systemctl disable networking.service
```

Опять же, вы еще не видели, насколько глубоко systemd проникает, поэтому прочитайте об этом, если хотите узнать больше.

## Exercise

Практика ведет к совершенству! Вот несколько практических заданий для закрепления вашего понимания управления процессами, которые часто контролируются службами systemd:

1. **[Управление и мониторинг процессов Linux](https://labex.io/ru/labs/comptia-manage-and-monitor-linux-processes-590864)** - Практикуйтесь во взаимодействии с процессами переднего и фонового плана, их проверке с помощью `ps`, мониторинге ресурсов с помощью `top`, настройке приоритета с помощью `renice` и их завершении с помощью `kill`. Эта лаборатория даст вам практический опыт работы с эффектами управления юнитами systemd во время выполнения.

Эти лаборатории помогут вам применить концепции в реальных сценариях и обрести уверенность в управлении процессами в Linux.

## Quiz Question

Какая команда используется для запуска службы с именем peanut.service?

## Quiz Answer

sudo systemctl start peanut.service
