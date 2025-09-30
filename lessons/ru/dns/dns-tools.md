---
index: 6
lang: "ru"
title: "Инструменты DNS"
meta_title: "Инструменты DNS - DNS"
meta_description: "Изучите команды nslookup и dig для DNS-запросов и устранения неполадок в Linux. Узнайте, как использовать эти важные инструменты DNS с нашим руководством для начинающих."
meta_keywords: "nslookup, команда dig, инструменты DNS, Linux DNS, устранение неполадок DNS, учебник Linux, Linux для начинающих"
---

## Lesson Content

### nslookup

Инструмент "name server lookup" используется для запроса серверов имен с целью получения информации о записях ресурсов. Давайте найдем, где находится сервер имен для google.com:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### dig

Dig (domain information groper) — мощный инструмент для получения информации о DNS-серверах имен. Он более гибок, чем nslookup, и отлично подходит для устранения неполадок DNS.

```bash
pete@icebox:~$ dig www.google.com

; <<>> DiG 9.9.5-3-Ubuntu <<>> www.google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42376
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0005 , udp: 512
;; QUESTION SECTION:
;www.google.com.                        IN      A

;; ANSWER SECTION:
www.google.com.         5       IN      A       74.125.239.147
www.google.com.         5       IN      A       74.125.239.144
www.google.com.         5       IN      A       74.125.239.146
www.google.com.         5       IN      A       74.125.239.145
www.google.com.         5       IN      A       74.125.239.148

;; Query time: 27 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Feb 07 10:14:00 PST 2016
;; MSG SIZE  rcvd: 123
```

## Exercise

Практика ведет к совершенству! Вот практическая лаборатория для закрепления вашего понимания настроек сетевого интерфейса:

1. **[Изучение настроек сетевого интерфейса с помощью ethtool в Linux](https://labex.io/ru/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Научитесь использовать команду `ethtool` для изучения и управления настройками сетевого интерфейса, включая просмотр и установку скорости и дуплекса интерфейса, а также анализ режимов связи для устранения неполадок на физическом уровне сети.

Эта лаборатория поможет вам применить концепции в реальных сценариях и обрести уверенность в управлении сетевыми интерфейсами.

## Quiz Question

Какой инструмент используется для получения подробной информации о DNS-серверах имен?

## Quiz Answer

dig
