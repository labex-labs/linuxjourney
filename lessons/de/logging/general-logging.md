---
index: 3
lang: "de"
title: "Allgemeine Protokollierung"
meta_title: "Allgemeine Protokollierung - Protokollierung"
meta_description: "Erfahren Sie mehr über Linux-Protokolldateien wie /var/log/messages und syslog. Verstehen Sie ihre Unterschiede für eine effektive Systemfehlerbehebung. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "Linux-Protokolle, syslog, var/log/messages, Linux-Fehlerbehebung, Linux-Anfänger, Linux-Anleitung, Systemprotokolle"
---

## Lesson Content

Es gibt viele Protokolldateien, die Sie auf Ihrem System einsehen können; viele wichtige finden Sie unter `/var/log`. Wir werden nicht alle durchgehen, aber wir werden ein paar der wichtigsten besprechen.

Es gibt zwei allgemeine Protokolldateien, die Sie einsehen können, um einen Überblick darüber zu erhalten, was Ihr System tut:

### `/var/log/messages`

Dieses Protokoll enthält alle nicht-kritischen und nicht-Debug-Meldungen, einschließlich Meldungen, die während des Bootvorgangs (dmesg), der Authentifizierung (auth), Cron, Daemon usw. protokolliert wurden. Es ist sehr nützlich, um einen Überblick darüber zu erhalten, wie sich Ihre Maschine verhält.

### `/var/log/syslog`

Dies protokolliert alles außer auth-Meldungen; es ist äußerst nützlich zum Debuggen von Fehlern auf Ihrer Maschine.

Diese beiden Protokolle sollten mehr als ausreichend sein, wenn Sie Probleme mit Ihrem System beheben. Wenn Sie jedoch nur eine bestimmte Protokollkomponente anzeigen möchten, gibt es auch dafür separate Protokolle.

## Exercise

Schauen Sie sich Ihre Dateien `/var/log/messages` und `/var/log/syslog` an und sehen Sie, was die Unterschiede sind.

## Quiz Question

Welche Protokolldatei protokolliert alles außer auth-Meldungen?

## Quiz Answer

syslog
