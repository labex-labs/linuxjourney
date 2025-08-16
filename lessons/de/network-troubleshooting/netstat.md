---
lang: "de"
title: "netstat"
description: "Lernen Sie den netstat-Befehl für die Linux-Netzwerkanalyse. Verstehen Sie Netzwerkverbindungen, Ports und Sockets mit dieser anfängerfreundlichen Anleitung."
keywords: "netstat, netstat-Befehl, Linux-Netzwerk, Netzwerkverbindungen, Linux-Tutorial, Anfänger, Anleitung"
---

## Lesson Content

### Bekannte Ports

Wir haben die Datenübertragung über Ports auf unserer Maschine besprochen; schauen wir uns einige bekannte Ports an.

Eine Liste der bekannten Ports erhalten Sie in der Datei **/etc/services**:

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

Die erste Spalte ist der Name des Dienstes, dann die Portnummer und das von ihm verwendete Transportprotokoll.

### netstat

Ein äußerst nützliches Werkzeug, um detaillierte Informationen über Ihr Netzwerk zu erhalten, ist **netstat**. Netstat zeigt verschiedene netzwerkbezogene Informationen an, wie z.B. Netzwerkverbindungen, Routing-Tabellen, Informationen über Netzwerkschnittstellen und mehr; es ist das Schweizer Taschenmesser der Netzwerk-Tools. Wir werden uns hauptsächlich auf eine Funktion von netstat konzentrieren, nämlich den Status von Netzwerkverbindungen. Bevor wir uns ein Beispiel ansehen, sprechen wir zuerst über Sockets und Ports. Ein Socket ist eine Schnittstelle, die es Programmen ermöglicht, Daten zu senden und zu empfangen, während ein Port verwendet wird, um zu identifizieren, welche Anwendung Daten senden oder empfangen soll. Die Socket-Adresse ist die Kombination aus IP-Adresse und Port. Jede Verbindung zwischen einem Host und einem Ziel erfordert einen eindeutigen Socket. Zum Beispiel ist HTTP ein Dienst, der auf Port 80 läuft; wir können jedoch viele HTTP-Verbindungen haben, und um jede Verbindung aufrechtzuerhalten, wird pro Verbindung ein Socket erstellt.

```bash
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 icebox:domain           *:*                     LISTEN
tcp        0      0 localhost:ipp           *:*                     LISTEN
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN
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
- **State**: Der Status des Sockets.

Eine Liste der Socket-Zustände finden Sie in der Manpage, hier sind jedoch einige:

- **LISTENING**: Der Socket lauscht auf eingehende Verbindungen. Denken Sie daran, wenn wir eine TCP-Verbindung herstellen, muss unser Ziel auf uns lauschen, bevor wir uns verbinden können.
- **SYN_SENT**: Der Socket versucht aktiv, eine Verbindung herzustellen.
- **ESTABLISHED**: Der Socket hat eine etablierte Verbindung.
- **CLOSE_WAIT**: Der Remote-Host wurde heruntergefahren, und wir warten darauf, dass der Socket geschlossen wird.
- **TIME_WAIT**: Der Socket wartet nach dem Schließen, um noch im Netzwerk befindliche Pakete zu verarbeiten.

## Exercise

Schauen Sie sich die Manpage für `netstat` an und lernen Sie alle Funktionen kennen, die es bietet.

## Quiz Question

Welcher Port wird für HTTPS verwendet?

## Quiz Answer

443
