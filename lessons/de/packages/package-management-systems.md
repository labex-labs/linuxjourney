---
index: 6
lang: "de"
title: "yum und apt"
meta_title: "yum und apt - Pakete"
meta_description: "Erkunden Sie die Hauptunterschiede in der yum vs apt Debatte. Dieser Leitfaden behandelt die Verwendung von yum und apt zur Installation, Entfernung und Aktualisierung von Paketen auf RPM- und Debian-basierten Linux-Systemen."
meta_keywords: "yum vs apt, yum apt, Linux Paketverwaltung, apt, yum, Debian, Red Hat, Pakete installieren, Pakete aktualisieren, Linux Befehle"
---

## Lesson Content

Paketmanager sind unverzichtbare Werkzeuge in Linux, die die Installation, Aktualisierung und Entfernung von Software vereinfachen. Sie kümmern sich automatisch um Abhängigkeiten und stellen sicher, dass alle erforderlichen Bibliotheken und Komponenten korrekt installiert werden. Zwei der bekanntesten Paketverwaltungssysteme sind **yum** und **apt**.

### Yum vs Apt

Der Hauptunterschied zwischen diesen beiden Systemen liegt in den Linux-Distributionen, die sie bedienen. Der `yum` (Yellowdog Updater, Modified) Paketmanager wird von RPM-basierten Distributionen wie Red Hat, CentOS und Fedora verwendet. Im Gegensatz dazu ist `apt` (Advanced Package Tool) der Standard für Debian-basierte Distributionen, einschließlich Ubuntu. Obwohl sowohl `yum` als auch `apt` die gleichen Ziele verfolgen, unterscheidet sich ihre Befehlssyntax.

### Pakete installieren und entfernen

Um ein neues Softwarepaket aus einem Repository zu installieren, verwenden Sie den Befehl `install`.

```bash
Debian: $ apt install paket_name
RPM: $ yum install paket_name
```

Um ein Paket zu entfernen, sind die Befehle ebenfalls unkompliziert. `apt` verwendet `remove`, während `yum` `erase` verwendet.

```bash
Debian: $ apt remove paket_name
RPM: $ yum erase paket_name
```

### Pakete aktualisieren und überprüfen

Es ist eine bewährte Methode, Ihren lokalen Paketindex zu aktualisieren, bevor Sie Software installieren oder upgraden. Dies stellt sicher, dass Sie die neuesten verfügbaren Versionen erhalten.

Für Debian-Systeme ist dies ein zweistufiger Prozess: `apt update` aktualisiert die Paketliste, und `apt upgrade` installiert die neuen Versionen. Für RPM-Systeme erledigt `yum update` beide Aktionen mit einem einzigen Befehl.

```bash
Debian: $ apt update; apt upgrade
RPM: $ yum update
```

Wenn Sie mehr Details zu einem bestimmten Paket benötigen, können Sie die folgenden Befehle verwenden, um Informationen wie Version, Größe und Beschreibung anzuzeigen.

```bash
Debian: $ apt show paket_name
RPM: $ yum info paket_name
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis der Linux-Paketverwaltung zu festigen:

1.  **[Pakete mit YUM unter Linux abfragen und aktualisieren](https://labex.io/de/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - Üben Sie die Verwaltung von Softwarepaketen auf RHEL-basierten Linux-Systemen mit YUM, einschließlich der Überprüfung, Aktualisierung und Erkundung von Repositories.
2.  **[Softwareinstallation unter Linux](https://labex.io/de/labs/linux-software-installation-on-linux-18005)** - Lernen Sie verschiedene Methoden zur Installation und Verwaltung von Software auf Ubuntu-Systemen kennen, einschließlich der Verwendung von apt, dpkg und der Handhabung von .deb-Dateien.
3.  **[Pakete installieren und entfernen](https://labex.io/de/labs/linux-installing-and-removing-packages-385380)** - Üben Sie das Aktualisieren des Systems, das Installieren und Entfernen von Paketen sowie die Optimierung der Softwarekonfiguration auf einem Debian-basierten System mit `apt`.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Selbstvertrauen in die Linux-Paketverwaltung aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um Paketinformationen auf einem Debian-System anzuzeigen? Bitte antworten Sie auf Englisch und achten Sie auf die Groß- und Kleinschreibung.

## Quiz Answer

apt show
