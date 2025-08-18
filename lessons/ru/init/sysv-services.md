---
lang: "ru"
title: "Служба System V"
meta_title: "Служба System V - Init"
meta_description: "Научитесь управлять службами System V с помощью инструментов командной строки. Узнайте, как перечислять, запускать, останавливать и перезапускать службы с помощью этого удобного для новичков руководства по Linux."
meta_keywords: "Службы System V, службы Linux, команда service, SysV init, руководство по Linux, Linux для начинающих, управление службами, руководство по Linux"
---

## Lesson Content

Существует множество инструментов командной строки, которые можно использовать для управления службами Sys V.

### List services

```bash
service --status-all
```

### Start a service

```bash
sudo service networking start
```

### Stop a service

```bash
sudo service networking stop
```

### Restart a service

```bash
sudo service networking restart
```

Эти команды не являются специфичными для систем инициализации Sys V; вы также можете использовать их для управления службами Upstart. Поскольку Linux пытается отойти от более традиционных скриптов инициализации Sys V, все еще существуют механизмы, помогающие этому переходу.

## Exercise

Управляйте несколькими службами и изменяйте их состояния. Что вы наблюдаете?

## Quiz Question

Какая команда используется для остановки службы с именем `peanut` в Sys V?

## Quiz Answer

sudo service peanut stop
