---
index: 6
lang: "de"
title: "yum und apt"
meta_title: "yum und apt - Pakete"
meta_description: "Lernen Sie yum und apt für die Linux-Paketverwaltung. Installieren, entfernen und aktualisieren Sie Software auf Debian-/RPM-Systemen mit diesem Tutorial für Anfänger. Starten Sie noch heute!"
meta_keywords: "yum, apt, Linux-Paketverwaltung, apt-Tutorial, yum-Tutorial, Linux-Befehle, Anfängerleitfaden, Paketinstallation"
---

## Lesson Content

Ah, die Batmans der Paketverwaltung! Diese Systeme bieten alle Funktionen, um die Installation, Entfernung und Änderung von Paketen zu erleichtern, einschließlich der Installation von Paketabhängigkeiten. Zwei der beliebtesten Verwaltungssysteme sind **yum** und **apt**. Yum ist exklusiv für die Red Hat-Familie, und apt ist exklusiv für die Debian-Familie.

### Installieren Sie ein Paket aus einem Repository

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Ein Paket entfernen

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

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Paketverwaltung zu vertiefen:

1. **[Pakete mit YUM in Linux abfragen und aktualisieren](https://labex.io/de/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Üben Sie die Verwaltung von Softwarepaketen auf RHEL-basierten Linux-Systemen mit YUM, einschließlich der Überprüfung, Aktualisierung und Erkundung von Repositories.
2. **[Softwareinstallation unter Linux](https://labex.io/de/labs/linux-software-installation-on-linux-18005)** - Lernen Sie verschiedene Methoden zur Installation und Verwaltung von Software auf Ubuntu-Systemen, einschließlich der Verwendung von apt, dpkg und der Handhabung von .deb-Dateien.
3. **[Pakete installieren und entfernen](https://labex.io/de/labs/linux-installing-and-removing-packages-385380)** - Üben Sie das Aktualisieren des Systems, das Installieren und Entfernen von Paketen und das Optimieren der Softwarekonfiguration auf einem Debian-basierten System mit `apt`.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Linux-Paketverwaltung aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um Paketinformationen auf einem Debian-System anzuzeigen?

## Quiz Answer

apt show
