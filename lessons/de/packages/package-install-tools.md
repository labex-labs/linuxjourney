---
index: 5
lang: "de"
title: "rpm und dpkg"
meta_title: "rpm und dpkg - Pakete"
meta_description: "Lernen Sie, Pakete mit den Befehlen rpm und dpkg zu installieren, zu entfernen und aufzulisten. Verstehen Sie die direkte Paketverwaltung für .deb- und .rpm-Dateien. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "rpm, dpkg, Linux-Paketverwaltung, .deb, .rpm, Linux-Tutorial, Anfängerleitfaden, Pakete installieren"
---

## Lesson Content

Obwohl es in diesem Kurs hauptsächlich um Paketverwaltungssysteme geht (die Batmans der Paketverwaltung), dürfen wir die Robins nicht vergessen. Obwohl sehr nützlich und zuverlässig, kommen sie nicht mit dem süßen Batmobil und dem Utility Belt.

So wie `.exe` eine einzelne ausführbare Datei ist, so sind es auch `.deb` und `.rpm`. Normalerweise würden Sie diese nicht sehen, wenn Sie Paket-Repositories verwenden, aber wenn Sie Pakete direkt herunterladen, erhalten Sie diese höchstwahrscheinlich in diesen gängigen Formaten. Offensichtlich sind sie exklusiv für ihre Distributionen: `.deb` für Debian-basierte und `.rpm` für Red Hat-basierte.

Um diese direkten Pakete zu installieren, können Sie die Paketverwaltungsbefehle verwenden: `rpm` und `dpkg`. Diese Tools werden verwendet, um Paketdateien zu installieren; sie installieren jedoch nicht die Paketabhängigkeiten. Wenn Ihr Paket also 10 Abhängigkeiten hätte, müssten Sie diese Pakete separat installieren und dann deren Abhängigkeiten, und so weiter und so fort. Wie Sie sehen können, war dies einer der Gründe, die die vollwertigen Verwaltungssysteme hervorbrachten, die wir später besprechen werden.

Denken Sie daran, dass es unzählige Male vorkommen wird, dass Sie ein Paket mit einem dieser Tools installieren, abfragen oder überprüfen müssen. Merken Sie sich diese Befehle.

### Ein Paket installieren

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

Das `i` steht für Installieren. Sie können auch das längere Format `--install` verwenden.

### Ein Paket entfernen

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r` für remove
RPM: `e` für erase

### Installierte Pakete auflisten

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l` für list
RPM: `q` für query und `a` für all

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis der direkten Paketverwaltung zu vertiefen:

1. **[Pakete mit RPM unter Linux verwalten](https://labex.io/de/labs/rhel-managing-packages-with-rpm-in-linux-590868)** – Sammeln Sie praktische Erfahrungen beim Abfragen von Paketinformationen, Überprüfen der Integrität, Auflisten von Abhängigkeiten, Simulieren der Entfernung und Untersuchen von RPM-Paketinhalten mit `rpm` und verwandten Tools.

Dieses Labor wird Ihnen helfen, die Konzepte der Verwaltung einzelner Paketdateien in einem realen Szenario anzuwenden und Vertrauen in diese wichtigen Linux-Tools aufzubauen.

## Quiz Question

Was ist das Paketverwaltungstool für `.deb`-Dateien?

## Quiz Answer

dpkg
