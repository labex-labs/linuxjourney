---
title: "rpm und dpkg"
description: "Lernen Sie, Pakete mit den Befehlen rpm und dpkg zu installieren, zu entfernen und aufzulisten. Verstehen Sie die direkte Paketverwaltung für .deb- und .rpm-Dateien. Beginnen Sie Ihre Linux-Reise!"
keywords: "rpm, dpkg, Linux-Paketverwaltung, .deb, .rpm, Linux-Tutorial, Anfängerleitfaden, Pakete installieren"
---

## Lesson Content

Obwohl der Großteil dieses Kurses über Paketverwaltungssysteme (die Batmans der Paketverwaltung) handelt, dürfen wir die Robins nicht vergessen. Obwohl sehr nützlich und zuverlässig, kommen sie nicht mit dem süßen Batmobil und dem Dienstgürtel.

So wie `.exe` eine einzelne ausführbare Datei ist, so sind es auch `.deb` und `.rpm`. Normalerweise würden Sie diese nicht sehen, wenn Sie Paket-Repositories verwenden, aber wenn Sie Pakete direkt herunterladen, erhalten Sie diese höchstwahrscheinlich in diesen gängigen Formaten. Offensichtlich sind sie exklusiv für ihre Distributionen: `.deb` für Debian-basierte und `.rpm` für Red Hat-basierte.

Um diese direkten Pakete zu installieren, können Sie die Paketverwaltungsbefehle verwenden: `rpm` und `dpkg`. Diese Tools werden verwendet, um Paketdateien zu installieren; sie installieren jedoch nicht die Paketabhängigkeiten. Wenn Ihr Paket also 10 Abhängigkeiten hätte, müssten Sie diese Pakete separat installieren und dann deren Abhängigkeiten, und so weiter und so fort. Wie Sie sehen können, war das einer der Gründe, die die vollwertigen Verwaltungssysteme hervorbrachten, die wir später besprechen werden.

Denken Sie daran, dass es unzählige Male vorkommen wird, dass Sie ein Paket mit einem dieser Tools installieren, abfragen oder überprüfen müssen. Merken Sie sich diese Befehle.

### Install a package

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

Das `i` steht für install. Sie können auch das längere Format `--install` verwenden.

### Remove a package

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r` for remove
RPM: `e` for erase

### List installed packages

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l` for list
RPM: `q` for query and `a` for all

## Exercise

Suchen Sie ein Programm, das Sie auf Ihrem System installieren möchten, wie Google Chrome, und installieren Sie es mit einem dieser Befehle.

## Quiz Question

Was ist das Paketverwaltungstool für `.deb`-Dateien?

## Quiz Answer

dpkg
