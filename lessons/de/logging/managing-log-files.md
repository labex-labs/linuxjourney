---
title: "Verwalten von Protokolldateien"
description: "Erfahren Sie, wie Sie Linux-Protokolldateien effizient mit logrotate verwalten. Entdecken Sie Protokollrotation, Komprimierung und Konfiguration, um Speicherplatz zu sparen. Beginnen Sie noch heute mit dem Lernen!"
keywords: "logrotate, Linux-Protokolle, Protokollverwaltung, Protokollrotation, Linux-Tutorial, Anfänger, Leitfaden, Speicherplatz"
---

## Lesson Content

Protokolldateien erzeugen viele Daten und speichern diese auf Ihren Festplatten. Dies bringt jedoch viele Probleme mit sich. Meistens möchten wir nur neuere Protokolle sehen können. Wir möchten auch unseren Speicherplatz effizient verwalten. Wie machen wir das alles? Die Antwort ist mit `logrotate`.

Das Dienstprogramm `logrotate` übernimmt die Protokollverwaltung für uns. Es verfügt über eine Konfigurationsdatei, die es uns ermöglicht, festzulegen, wie viele und welche Protokolle aufbewahrt werden sollen, wie unsere Protokolle zur Platzersparnis komprimiert werden sollen und vieles mehr. Das `logrotate`-Tool wird normalerweise einmal täglich über cron ausgeführt, und die Konfigurationsdateien finden Sie unter `/etc/logrotate.d`.

Es gibt andere Tools zur Protokollrotation, die Sie zur Verwaltung Ihrer Protokolle verwenden können, aber `logrotate` ist das gebräuchlichste.

## Exercise

Schauen Sie sich Ihre `logrotate`-Konfigurationsdatei an und sehen Sie, wie sie einige Ihrer Protokolle verwaltet.

## Quiz Question

Welches Dienstprogramm wird zur Verwaltung von Protokollen verwendet?

## Quiz Answer

logrotate
