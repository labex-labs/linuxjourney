---
index: 3
lang: "ru"
title: "dhclient"
meta_title: "dhclient - Конфигурация сети"
meta_description: "Узнайте о dhclient, как он получает IP-адреса с помощью DHCP и управляет сетевыми арендами. Разберитесь с файлами dhclient.conf и dhclient.leases. Руководство для начинающих по Linux."
meta_keywords: "dhclient, DHCP, сеть Linux, IP-адрес, настройка сети, учебник Linux, руководство для начинающих"
---

## Lesson Content

Мы уже обсуждали DHCP, и чаще всего вам никогда не потребуется статически устанавливать свои IP-адреса, маски подсети и т.д. Вместо этого вы будете использовать DHCP! `dhclient` запускается при загрузке и получает список сетевых интерфейсов из файла `dhclient.conf`. Для каждого перечисленного интерфейса он пытается настроить интерфейс с использованием протокола DHCP.

В файле `dhclient.leases` `dhclient` отслеживает список арендованных адресов при перезагрузках системы. После чтения `dhclient.conf` файл `dhclient.leases` считывается, чтобы сообщить ему, какие аренды уже назначены.

### Чтобы получить новый IP

```bash
sudo dhclient
```

## Exercise

No exercises for this lesson.

## Quiz Question

Что пытается назначить IP-адреса с помощью протокола DHCP?

## Quiz Answer

dhclient
