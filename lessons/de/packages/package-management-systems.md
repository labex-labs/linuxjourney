---
lang: "de"
title: "yum und apt"
description: "Lernen Sie yum und apt für die Linux-Paketverwaltung. Installieren, entfernen und aktualisieren Sie Software auf Debian-/RPM-Systemen mit diesem Tutorial für Anfänger. Starten Sie noch heute!"
keywords: "yum, apt, Linux-Paketverwaltung, apt-Tutorial, yum-Tutorial, Linux-Befehle, Anfängerleitfaden, Paketinstallation"
---

## Lesson Content

Ah, die Batmans der Paketverwaltung! Diese Systeme bieten alle notwendigen Funktionen, um die Installation, Entfernung und Änderung von Paketen zu vereinfachen, einschließlich der Installation von Paketabhängigkeiten. Zwei der beliebtesten Verwaltungssysteme sind **yum** und **apt**. Yum ist exklusiv für die Red Hat-Familie, und apt ist exklusiv für die Debian-Familie.

### Installieren Sie ein Paket aus einem Repository

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Entfernen Sie ein Paket

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Aktualisieren von Paketen für ein Repository

Es ist immer bewährte Praxis, Ihre Paket-Repositories zu aktualisieren, damit sie auf dem neuesten Stand sind, bevor Sie ein Paket installieren und aktualisieren.

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### Informationen zu einem installierten Paket abrufen

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

Führen Sie jeden dieser Paketbefehle aus und sehen Sie sich die Ausgabe an, die Sie erhalten.

## Quiz Question

Welcher Befehl wird verwendet, um Paketinformationen auf einem Debian-System anzuzeigen?

## Quiz Answer

apt show
