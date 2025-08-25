---
index: 6
lang: "de"
title: "DNS-Tools"
meta_title: "DNS-Tools - DNS"
meta_description: "Lernen Sie die Befehle nslookup und dig für DNS-Abfragen und Fehlerbehebung unter Linux. Verstehen Sie, wie Sie diese wichtigen DNS-Tools mit unserem anfängerfreundlichen Leitfaden verwenden."
meta_keywords: "nslookup, dig Befehl, DNS-Tools, Linux DNS, DNS-Fehlerbehebung, Linux-Tutorial, Linux für Anfänger"
---

## Lesson Content

### nslookup

Das Tool "name server lookup" wird verwendet, um Namensserver abzufragen und Informationen über Ressourcendatensätze zu finden. Lassen Sie uns herausfinden, wo sich der Namensserver für google.com befindet:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### dig

Dig (domain information groper) ist ein leistungsstarkes Tool, um Informationen über DNS-Namensserver zu erhalten. Es ist flexibler als nslookup und hervorragend zur Fehlerbehebung bei DNS-Problemen geeignet.

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

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis der Netzwerkschnittstelleneinstellungen zu vertiefen:

1. **[Netzwerkschnittstelleneinstellungen mit ethtool in Linux untersuchen](https://labex.io/de/labs/linux-examine-network-interface-settings-with-ethtool-in-linux-592759)** – Lernen Sie, den Befehl `ethtool` zu verwenden, um Netzwerkschnittstelleneinstellungen zu untersuchen und zu verwalten, einschließlich des Anzeigens und Festlegens von Schnittstellengeschwindigkeit und Duplex sowie der Analyse von Verbindungsmodi zur Fehlerbehebung bei Problemen auf der physikalischen Netzwerkschicht.

Dieses Labor wird Ihnen helfen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit Netzwerkschnittstellen aufzubauen.

## Quiz Question

Welches Tool wird verwendet, um detaillierte Informationen über DNS-Namensserver zu erhalten?

## Quiz Answer

dig
