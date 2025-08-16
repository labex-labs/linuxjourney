---
lang: "ru"
title: "yum и apt"
description: "Изучите yum и apt для управления пакетами Linux. Устанавливайте, удаляйте и обновляйте программное обеспечение в системах Debian/RPM с помощью этого руководства для начинающих. Начните сегодня!"
keywords: "yum, apt, управление пакетами Linux, apt руководство, yum руководство, команды Linux, руководство для начинающих, установка пакетов"
---

## Lesson Content

Ах, Бэтмены управления пакетами! Эти системы поставляются со всеми необходимыми функциями для упрощения установки, удаления и изменения пакетов, включая установку зависимостей пакетов. Две из самых популярных систем управления — это **yum** и **apt**. Yum является эксклюзивным для семейства Red Hat, а apt — для семейства Debian.

### Install a package from a repository

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Remove a package

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Updating packages for a repository

Всегда рекомендуется обновлять репозитории пакетов, чтобы они были актуальными, прежде чем устанавливать и обновлять пакет.

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### Get information about an installed package

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

Выполните каждую из этих команд для работы с пакетами и посмотрите полученный вывод.

## Quiz Question

Какая команда используется для отображения информации о пакете в системе Debian?

## Quiz Answer

apt show
