---
index: 4
lang: "de"
title: "netstat"
meta_title: "netstat - Fehlerbehebung"
meta_description: "Meistern Sie den Linux-netstat-Befehl zur Analyse von Netzwerkverbindungen, Ports und Sockets. Dieser Leitfaden behandelt gängige Zustände wie SYN_SENT und netstat close_wait zur effektiven Fehlerbehebung."
meta_keywords: "linux netstat, netstat, netstat Befehl, syn_sent netstat, netstat close_wait, Netzwerkverbindungen, Linux-Netzwerk, Netzwerkanalyse, Linux-Tutorial"
---

## Lesson Content

### Bekannte Ports

Wir haben besprochen, wie Daten über Ports auf unserem Rechner übertragen werden. Werfen wir einen Blick auf einige gängige, bekannte Ports. Eine Liste dieser Ports finden Sie in der Datei **/etc/services**:

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..usw..
```

Die erste Spalte zeigt den Dienstnamen, gefolgt von seiner zugewiesenen Portnummer und dem verwendeten Protokoll der Transportschicht.

### Einführung in linux netstat

Ein äußerst nützliches Werkzeug zur Erfassung detaillierter Netzwerkinformationen ist **netstat**. Der Befehl `linux netstat` zeigt eine breite Palette netzwerkbezogener Daten an, einschließlich aktiver Netzwerkverbindungen, Routing-Tabellen und Schnittstellenstatistiken. Er wird oft als das Schweizer Taschenmesser der Netzwerkwerkzeuge bezeichnet.

In dieser Lektion konzentrieren wir uns darauf, `netstat` zur Überprüfung des Status von Netzwerkverbindungen zu verwenden. Bevor wir uns ein Beispiel ansehen, klären wir den Unterschied zwischen Sockets und Ports. Ein **Port** ist eine numerische Kennung, die verwendet wird, um Daten an eine bestimmte Anwendung weiterzuleiten. Ein **Socket** ist ein Endpunkt für die Kommunikation, der es Programmen ermöglicht, Daten zu senden und zu empfangen. Die Socket-Adresse ist die eindeutige Kombination aus einer IP-Adresse und einer Portnummer. Jede Verbindung zwischen einem Host und einem Ziel erfordert einen eindeutigen Socket. Zum Beispiel läuft der HTTP-Dienst zwar auf Port 80, aber es können gleichzeitig mehrere HTTP-Verbindungen bestehen, und für jede davon wird ein eindeutiger Socket erstellt.

Untersuchen wir die Ausgabe von `netstat -at`:

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

Der Befehl `netstat -a` zeigt alle lauschenden und nicht lauschenden Sockets an, während das Flag `-t` die Ausgabe filtert, um nur TCP-Verbindungen anzuzeigen.

Die Spalten sind wie folgt:

- **Proto**: Das verwendete Protokoll (z. B. TCP oder UDP).
- **Recv-Q**: Die Warteschlange der Daten, die empfangen werden sollen.
- **Send-Q**: Die Warteschlange der Daten, die gesendet werden sollen.
- **Local Address**: Die Adresse des lokalen Hosts.
- **Foreign Address**: Die Adresse des Remote-Hosts.
- **State**: Der aktuelle Zustand des Sockets.

### Verständnis der Verbindungszustände

Die Spalte **State** (Zustand) liefert wichtige Informationen über den Status einer Verbindung. Hier sind einige gängige Zustände, denen Sie begegnen werden:

- **LISTENING**: Der Socket wartet auf eingehende Verbindungen. Damit eine TCP-Verbindung hergestellt werden kann, muss das Ziel lauschen.
- **SYN_SENT**: Bei der Verwendung von `netstat` zeigt ein Zustand `SYN_SENT` an, dass der Socket aktiv versucht, eine Verbindung herzustellen.
- **ESTABLISHED**: Der Socket hat eine vollständig hergestellte Verbindung.
- **CLOSE_WAIT**: Der Zustand `netstat close_wait` bedeutet, dass der Remote-Host heruntergefahren wurde und das lokale System darauf wartet, dass die Anwendung den Socket schließt.
- **TIME_WAIT**: Der Socket wartet nach dem Schließen, um alle Pakete zu verarbeiten, die sich möglicherweise noch im Netzwerk befinden.

You can see a full list of socket states in the `netstat` man page.

Sie können eine vollständige Liste der Socket-Zustände in der `netstat`-Manpage einsehen.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis der Netzwerkschnittstelleneinstellungen zu festigen:

1. **[Netzwerkschnittstelleneinstellungen mit ethtool unter Linux untersuchen](https://labex.io/de/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Lernen Sie, den Befehl `ethtool` zu verwenden, um Netzwerkschnittstelleneinstellungen zu untersuchen und zu verwalten, einschließlich der Anzeige und Einstellung von Schnittstellengeschwindigkeit und Duplex sowie der Analyse von Link-Modi zur Fehlerbehebung bei Netzwerkproblemen der physischen Schicht.

Dieses Labor hilft Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Netzwerkschnittstellen aufzubauen.

## Quiz Question

Welcher Port wird für HTTPS verwendet?

## Quiz Answer

443
