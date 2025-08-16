---
title: "Инструменты DNS"
description: "Изучите команды nslookup и dig для DNS-запросов и устранения неполадок в Linux. Узнайте, как использовать эти основные инструменты DNS с нашим руководством для начинающих."
keywords: "nslookup, dig command, DNS tools, Linux DNS, DNS troubleshooting, Linux tutorial, beginner Linux"
---

## Lesson Content

### nslookup

Инструмент "name server lookup" используется для запроса серверов имен с целью получения информации о ресурсных записях. Давайте найдем, где находится сервер имен для google.com:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### dig

Dig (domain information groper) — это мощный инструмент для получения информации о DNS name servers. Он более гибок, чем nslookup, и отлично подходит для устранения неполадок DNS.

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

Read up on the manpage for dig.

## Quiz Question

Какой инструмент используется для получения подробной информации о DNS name servers?

## Quiz Answer

dig
