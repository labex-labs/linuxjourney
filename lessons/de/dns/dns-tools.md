---
index: 6
lang: "de"
title: "DNS-Tools"
meta_title: "DNS-Tools - DNS"
meta_description: "Entdecken Sie wesentliche Linux DNS-Tools wie nslookup und den leistungsstarken dig-Befehl. Dieses anfängerfreundliche Linux-Tutorial behandelt DNS-Abfragen und DNS-Fehlerbehebungstechniken."
meta_keywords: "nslookup, dig-Befehl, DNS-Tools, Linux DNS, DNS-Fehlerbehebung, Namenserver-Abfrage, Linux-Tutorial, Anfänger Linux"
---

## Lesson Content

Unter Linux stehen mehrere Befehlszeilen-Dienstprogramme für die Netzwerkanalyse zur Verfügung. Wenn es um Probleme mit dem Domain Name System (DNS) geht, stechen zwei primäre **DNS-Tools** hervor: `nslookup` und `dig`. Zu wissen, wie man sie benutzt, ist entscheidend für jede **DNS-Fehlerbehebung** auf einem **Linux DNS**-Server oder -Client.

### Verwendung von nslookup für grundlegende DNS-Abfragen

Das Tool `nslookup` (Name Server Lookup) ist ein klassisches Dienstprogramm zum Abfragen von DNS-Servern, um Informationen zur Zuordnung von Domainnamen oder IP-Adressen zu erhalten. Obwohl es manchmal zugunsten von `dig` als veraltet gilt, bleibt es ein schnelles und einfaches Werkzeug für einfache Nachschlagevorgänge.

Um die IP-Adresse für eine Domain wie `www.google.com` zu finden, können Sie Folgendes ausführen:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

In dieser Ausgabe zeigen `Server` und `Address` den DNS-Server an, der die Abfrage beantwortet hat. Die `Non-authoritative answer` bedeutet, dass der Server ein zwischengespeichertes Ergebnis geliefert hat, anstatt direkt die autoritative Quelle abzufragen. `Name` und `Address` zeigen die aufgelöste IP-Adresse für die Domain an.

### Erweiterte DNS-Fehlerbehebung mit dig

Der Befehl `dig` (Domain Information Groper) ist ein leistungsstarkes und flexibles Werkzeug zur Abfrage von DNS-Namenservern. Er liefert detailliertere Informationen als `nslookup` und ist daher die bevorzugte Wahl für ernsthafte **DNS-Fehlerbehebung**.

Hier ist ein Beispiel für die Verwendung des **dig-Befehls**:

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

Die Ausgabe von `dig` ist in Abschnitte unterteilt:

- **QUESTION SECTION**: Zeigt die gesendete Abfrage. Hier haben wir nach einem `A` (Address)-Eintrag für `www.google.com` gefragt.
- **ANSWER SECTION**: Zeigt die vom DNS-Server erhaltene Antwort. In diesem Fall sind mehrere IP-Adressen mit der Domain von Google verknüpft.
- **Statistics**: Der letzte Abschnitt enthält Metadaten zur Abfrage, wie die Abfragezeit und den antwortenden Server.

Aufgrund seiner detaillierten Ausgabe und Flexibilität ist `dig` ein unverzichtbares Werkzeug für jeden, der Netzwerkdienste unter Linux verwaltet oder Fehler behebt.

## Exercise

Um mehr Erfahrung mit Linux-Netzwerkdienstprogrammen zu sammeln, sollten Sie das folgende praktische Labor ausprobieren:

1. **[Netzwerkschnittstelleneinstellungen mit ethtool unter Linux überprüfen](https://labex.io/de/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Lernen Sie, den Befehl `ethtool` zu verwenden, um Netzwerkschnittstelleneinstellungen zu überprüfen und zu verwalten, einschließlich der Anzeige und Einstellung von Schnittstellengeschwindigkeit und Duplex sowie der Analyse von Link-Modi zur Fehlerbehebung bei Problemen auf der physischen Schicht des Netzwerks.

Dieses Labor hilft Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Netzwerkschnittstellen aufzubauen.

## Quiz Question

Welches Tool wird verwendet, um detaillierte Informationen über DNS-Namenserver abzurufen? Bitte antworten Sie nur mit Kleinbuchstaben in englischer Sprache.

## Quiz Answer

dig
