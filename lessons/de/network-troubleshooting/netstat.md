---
index: 4
lang: "de"
title: "netstat"
meta_title: "netstat - Fehlerbehebung"
meta_description: "Lernen Sie den netstat-Befehl für die Linux-Netzwerkanalyse. Verstehen Sie Netzwerkverbindungen, Ports und Sockets mit dieser anfängerfreundlichen Anleitung."
meta_keywords: "netstat, netstat-Befehl, Linux-Netzwerk, Netzwerkverbindungen, Linux-Tutorial, Anfänger, Anleitung"
---

## Lesson Content

### Bekannte Ports

Wir haben die Datenübertragung über Ports auf unserer Maschine besprochen; schauen wir uns einige bekannte Ports an.

Eine Liste bekannter Ports erhalten Sie, indem Sie die Datei **/etc/services** einsehen:

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

Die erste Spalte ist der Name des Dienstes, dann die Portnummer und das von ihm verwendete Transportschichtprotokoll.

### netstat

Ein äußerst nützliches Werkzeug, um detaillierte Informationen über Ihr Netzwerk zu erhalten, ist **netstat**. Netstat zeigt verschiedene netzwerkbezogene Informationen an, wie z.B. Netzwerkverbindungen, Routing-Tabellen, Informationen über Netzwerkschnittstellen und vieles mehr; es ist das Schweizer Taschenmesser der Netzwerk-Tools. Wir werden uns hauptsächlich auf eine Funktion von netstat konzentrieren, nämlich den Status von Netzwerkverbindungen. Bevor wir uns ein Beispiel ansehen, sprechen wir zunächst über Sockets und Ports. Ein Socket ist eine Schnittstelle, die es Programmen ermöglicht, Daten zu senden und zu empfangen, während ein Port verwendet wird, um zu identifizieren, welche Anwendung Daten senden oder empfangen soll. Die Socket-Adresse ist die Kombination aus IP-Adresse und Port. Jede Verbindung zwischen einem Host und einem Ziel erfordert einen eindeutigen Socket. Zum Beispiel ist HTTP ein Dienst, der auf Port 80 läuft; wir können jedoch viele HTTP-Verbindungen haben, und um jede Verbindung aufrechtzuerhalten, wird pro Verbindung ein Socket erstellt.

```bash
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 icebox:domain           *:*                     LISTEN
tcp        0      0 localhost:ipp           *:*                     LISTEN
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT
tcp6       0      0 ip6-localhost:ipp       [::]:*                     LISTEN
tcp6       1      0 ip6-localhost:35094     ip6-localhost:ipp       CLOSE_WAIT
tcp6       0      0 ip6-localhost:ipp       ip6-localhost:35094     FIN_WAIT2
```

Der Befehl `netstat -a` zeigt die lauschenden und nicht-lauschenden Sockets für Netzwerkverbindungen an; das Flag `-t` zeigt nur TCP-Verbindungen an.

Die Spalten sind von links nach rechts wie folgt:

- **Proto**: Verwendetes Protokoll, TCP oder UDP.
- **Recv-Q**: Daten, die zum Empfang in der Warteschlange stehen.
- **Send-Q**: Daten, die zum Senden in der Warteschlange stehen.
- **Local Address**: Lokal verbundener Host.
- **Foreign Address**: Remote verbundener Host.
- **State**: Der Zustand des Sockets.

Eine Liste der Socket-Zustände finden Sie in der Manpage, hier sind jedoch einige:

- **LISTENING**: Der Socket wartet auf eingehende Verbindungen. Denken Sie daran, wenn wir eine TCP-Verbindung herstellen, muss unser Ziel auf uns warten, bevor wir uns verbinden können.
- **SYN_SENT**: Der Socket versucht aktiv, eine Verbindung herzustellen.
- **ESTABLISHED**: Der Socket hat eine etablierte Verbindung.
- **CLOSE_WAIT**: Der Remote-Host wurde heruntergefahren, und wir warten darauf, dass der Socket geschlossen wird.
- **TIME_WAIT**: Der Socket wartet nach dem Schließen, um noch im Netzwerk befindliche Pakete zu verarbeiten.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis der Netzwerkschnittstelleneinstellungen zu vertiefen:

1. **[Netzwerkschnittstelleneinstellungen mit ethtool in Linux untersuchen](https://labex.io/de/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** – Lernen Sie, den Befehl `ethtool` zu verwenden, um Netzwerkschnittstelleneinstellungen zu untersuchen und zu verwalten, einschließlich des Anzeigens und Festlegens von Schnittstellengeschwindigkeit und Duplex sowie der Analyse von Link-Modi zur Fehlerbehebung bei Problemen auf der physikalischen Schicht des Netzwerks.

Dieses Labor wird Ihnen helfen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit Netzwerkschnittstellen aufzubauen.

## Quiz Question

Welcher Port wird für HTTPS verwendet?

## Quiz Answer

443
