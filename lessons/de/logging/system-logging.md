---
lang: "de"
title: "Systemprotokollierung"
meta_description: "Erfahren Sie mehr über die Linux-Systemprotokollierung, syslog und wie Sie Protokolldateien in /var/log anzeigen können. Verstehen Sie rsyslogd und überwachen Sie Systemereignisse mit diesem Leitfaden für Anfänger."
meta_keywords: "Linux-Protokollierung, syslog, rsyslogd, var log, Systemprotokolle, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Die Dienste, der Kernel, Daemons usw. auf Ihrem System tun ständig etwas. Diese Daten werden tatsächlich in Form von Protokollen auf Ihrem System gespeichert. Dies ermöglicht uns, ein menschenlesbares Journal der Ereignisse zu haben, die auf unserem System stattfinden. Diese Daten werden normalerweise im Verzeichnis `/var` gespeichert; das Verzeichnis `/var` ist der Ort, an dem wir unsere variablen Daten, wie z. B. Protokolle, aufbewahren!

Wie werden diese Nachrichten überhaupt auf Ihrem System empfangen? Es gibt einen Dienst namens syslog, der diese Informationen an den Systemlogger sendet.

Syslog enthält tatsächlich viele Komponenten. Eine der wichtigen ist ein laufender Daemon namens `syslogd` (neuere Linux-Distributionen verwenden `rsyslogd`), der auf das Auftreten von Ereignismeldungen wartet und die gewünschten filtert. Je nachdem, was er mit dieser Nachricht tun soll, sendet er sie an eine Datei, Ihre Konsole oder tut nichts damit.

Man könnte meinen, dass dieser Systemlogger der zentrale Ort zur Verwaltung von Protokollen ist, aber leider ist das nicht der Fall. Sie werden viele Anwendungen sehen, die ihre eigenen Protokollierungsregeln schreiben und verschiedene Protokolldateien generieren. Im Allgemeinen sollte das Format der Protokolle jedoch einen Zeitstempel und die Ereignisdetails enthalten.

Hier ist ein Beispiel für eine Zeile aus syslog:

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Hier können wir sehen, dass am 27. Januar um 07:41:32 unser cron-Dienst den Job `cron.weekly` ausgeführt hat. Sie können alle Ereignismeldungen, die syslog sammelt, in der Datei `/var/log/syslog` einsehen.

## Exercise

Sehen Sie sich Ihre Datei `/var/log/syslog` an und prüfen Sie, was sonst noch auf Ihrem Computer passiert.

## Quiz Question

Was ist der Daemon, der Protokolle auf neueren Linux-Systemen verwaltet?

## Quiz Answer

rsyslogd
