---
index: 6
lang: "de"
title: "Protokolldateien verwalten"
meta_title: "Protokolldateien verwalten - Protokollierung"
meta_description: "Erfahren Sie, wie Sie Linux-Protokolldateien effizient mit logrotate verwalten. Entdecken Sie Protokollrotation, Komprimierung und Konfiguration, um Speicherplatz zu sparen. Beginnen Sie noch heute mit dem Lernen!"
meta_keywords: "logrotate, Linux-Protokolle, Protokollverwaltung, Protokollrotation, Linux-Tutorial, Anfänger, Leitfaden, Speicherplatz"
---

## Lesson Content

Protokolldateien erzeugen viele Daten und speichern diese Daten auf Ihren Festplatten. Dies bringt jedoch viele Probleme mit sich. Meistens möchten wir nur neuere Protokolle sehen können. Wir möchten auch unseren Speicherplatz effizient verwalten. Wie machen wir das alles? Die Antwort ist mit `logrotate`.

Das Dienstprogramm `logrotate` übernimmt die Protokollverwaltung für uns. Es verfügt über eine Konfigurationsdatei, mit der wir festlegen können, wie viele und welche Protokolle aufbewahrt werden sollen, wie unsere Protokolle zur Platzersparnis komprimiert werden sollen und vieles mehr. Das Tool `logrotate` wird normalerweise einmal täglich über Cron ausgeführt, und die Konfigurationsdateien finden Sie unter `/etc/logrotate.d`.

Es gibt andere Protokollrotations-Tools, die Sie zur Verwaltung Ihrer Protokolle verwenden können, aber `logrotate` ist das gebräuchlichste.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Protokolldateiverwaltung und verwandter Systemadministrationsaufgaben zu vertiefen:

1. **[Anzeigen von Protokoll- und Konfigurationsdateien in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** – Üben Sie grundlegende Linux-Befehlszeilenkenntnisse zum effizienten Anzeigen und Navigieren von Textdateien, einschließlich Systemprotokollen und Konfigurationsdateien, die von Tools wie `logrotate` verwaltet werden.
2. **[Schnelle Bedrohungserkennung](https://labex.io/de/labs/linux-rapid-threat-detection-387930)** – Erlernen Sie grundlegende Linux-Befehlszeilenkenntnisse für die Cybersicherheitsanalyse. Verwenden Sie die Befehle `tail` und `head`, um schnell aktuelle Protokolleinträge zu extrahieren und zu analysieren, und simulieren Sie so eine schnelle Bedrohungserkennung in einer hochriskanten technischen Umgebung.
3. **[Erstellen und Wiederherstellen einer Sicherung mit tar in Linux](https://labex.io/de/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** – Sammeln Sie praktische Erfahrungen mit Systemadministrationsaufgaben, indem Sie Verzeichnisse sichern, was oft Teil von Protokollrotationsstrategien zur Archivierung alter Protokolle ist.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit Protokolldateien in Linux aufzubauen.

## Quiz Question

Welches Dienstprogramm wird zur Verwaltung von Protokollen verwendet?

## Quiz Answer

logrotate
