---
index: 1
lang: "de"
title: "Systemprotokollierung"
meta_title: "Systemprotokollierung - Protokollierung"
meta_description: "Erfahren Sie mehr über die Linux-Systemprotokollierung, Syslog und wie Sie Protokolldateien in /var/log anzeigen können. Verstehen Sie rsyslogd und überwachen Sie Systemereignisse mit diesem Leitfaden für Anfänger."
meta_keywords: "Linux-Protokollierung, Syslog, rsyslogd, var log, Systemprotokolle, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Die Dienste, der Kernel, die Daemons usw. auf Ihrem System tun ständig etwas. Diese Daten werden tatsächlich auf Ihrem System in Form von Protokollen gespeichert. Dies ermöglicht uns, ein menschenlesbares Journal der Ereignisse zu haben, die auf unserem System stattfinden. Diese Daten werden normalerweise im Verzeichnis `/var` gespeichert; das Verzeichnis `/var` ist der Ort, an dem wir unsere variablen Daten, wie z.B. Protokolle, aufbewahren!

Wie werden diese Nachrichten überhaupt auf Ihrem System empfangen? Es gibt einen Dienst namens Syslog, der diese Informationen an den Systemlogger sendet.

Syslog enthält tatsächlich viele Komponenten. Eine der wichtigen ist ein Daemon namens `syslogd` (neuere Linux-Distributionen verwenden `rsyslogd`), der auf das Eintreten von Ereignismeldungen wartet und die gewünschten filtert. Je nachdem, was er mit dieser Nachricht tun soll, sendet er sie an eine Datei, Ihre Konsole oder tut nichts damit.

Man könnte meinen, dass dieser Systemlogger der zentrale Ort zur Verwaltung von Protokollen ist, aber leider ist das nicht der Fall. Sie werden viele Anwendungen sehen, die ihre eigenen Protokollierungsregeln schreiben und verschiedene Protokolldateien generieren. Im Allgemeinen sollte das Format der Protokolle jedoch einen Zeitstempel und die Ereignisdetails enthalten.

Hier ist ein Beispiel für eine Zeile aus Syslog:

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Hier sehen wir, dass am 27. Januar um 07:41:32 unser Cron-Dienst den Job `cron.weekly` ausgeführt hat. Sie können alle Ereignismeldungen, die Syslog sammelt, in der Datei `/var/log/syslog` einsehen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Protokollen und Dateianzeigen zu vertiefen:

1. **[Protokoll- und Konfigurationsdateien in Linux anzeigen](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** – Erlernen Sie grundlegende Linux-Befehlszeilenkenntnisse zum effizienten Anzeigen und Navigieren in Textdateien, einschließlich Systemprotokollen und Konfigurationsdateien. Üben Sie die Verwendung von Befehlen wie `cat`, `more` und `less`, um wichtige Informationen aus verschiedenen Dateitypen zu extrahieren.
2. **[Linux tail Befehl: Dateiende anzeigen](https://labex.io/de/labs/linux-linux-tail-command-file-end-display-214303)** – Erlernen Sie den Linux-Befehl `tail` zum Anzeigen und Überwachen des Endes von Textdateien. Dies ist besonders nützlich für die Echtzeit-Protokollanalyse.
3. **[Text mit grep in Linux suchen](https://labex.io/de/labs/comptia-search-text-with-grep-in-linux-590841)** – In diesem Lab lernen Sie, Text in Dateien auf einem Linux-System mit dem Befehl `grep` zu suchen. Dies ist von unschätzbarem Wert, um bestimmte Einträge in großen Protokolldateien zu finden.

Diese Labs helfen Ihnen, die Konzepte der Protokolldateiverwaltung und -analyse in realen Szenarien anzuwenden und Vertrauen in die Linux-Systemüberwachung aufzubauen.

## Quiz Question

Welcher Daemon verwaltet Protokolle auf neueren Linux-Systemen?

## Quiz Answer

rsyslogd
