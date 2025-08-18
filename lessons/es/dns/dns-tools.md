---
lang: "es"
title: "Herramientas DNS"
meta_title: "Herramientas DNS - DNS"
meta_description: "Aprende los comandos nslookup y dig para consultas DNS y resolución de problemas en Linux. Comprende cómo usar estas herramientas DNS esenciales con nuestra guía para principiantes."
meta_keywords: "nslookup, comando dig, herramientas DNS, DNS de Linux, resolución de problemas de DNS, tutorial de Linux, Linux para principiantes"
---

## Lesson Content

### nslookup

La herramienta "name server lookup" se utiliza para consultar servidores de nombres y encontrar información sobre registros de recursos. Busquemos dónde está el servidor de nombres para google.com:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### dig

Dig (domain information groper) es una herramienta potente para obtener información sobre los servidores de nombres DNS. Es más flexible que nslookup y excelente para solucionar problemas de DNS.

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

Lee la página man de dig.

## Quiz Question

¿Qué herramienta se utiliza para obtener información detallada sobre los servidores de nombres DNS?

## Quiz Answer

dig
