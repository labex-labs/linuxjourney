---
lesson_id: "package-management-systems"
course_id: "packages"
lang: "de"
order_index: 6
title: "yum und apt"
description: "Erfahre, wie die paketquellenbewussten Arbeitsabläufe von APT und DNF Pakete prüfen, installieren, entfernen und aktualisieren."
meta_title: "yum und apt – Pakete"
meta_description: "Erkunde die wichtigsten Unterschiede im Vergleich yum und apt. Dieser Leitfaden behandelt die Verwendung von yum und apt zum Installieren, Entfernen und Aktualisieren von Paketen auf RPM- und Debian-basierten Linux-Systemen."
meta_keywords: "yum oder apt, yum apt, Linux-Paketverwaltung, apt, yum, Debian, Red Hat, Pakete installieren, Pakete aktualisieren, Linux-Befehle"
---

Paketquellenbewusste Paketverwaltungen rufen Metadaten ab, lösen Abhängigkeiten, überprüfen authentifizierte Inhalte und koordinieren Transaktionen. Systeme der Debian-Familie verwenden gewöhnlich APT. Aktuelle Fedora- und Red-Hat-Enterprise-Linux-Versionen verwenden DNF; unter aktuellem RHEL bleibt der Befehl `yum` als Kompatibilitätsalias für DNF bestehen, während ältere Systeme die ursprüngliche YUM-Implementierung verwendeten.

Folge immer der Dokumentation für die installierte Distribution und Veröffentlichung, statt anzunehmen, dass eine Befehlsgruppe überall gilt.

## Metadaten aktualisieren und prüfen

APT trennt die Aktualisierung der Metadaten von Paketupgrades:

```bash
Debian family: $ sudo apt update
```

Suche und prüfe vor der Installation:

```bash
Debian family: $ apt search package-name
Debian family: $ apt show package-name
RPM family:    $ dnf search package-name
RPM family:    $ dnf info package-name
```

Die Konfiguration der Paketquellen bestimmt, was diese Befehle finden können. Lies Quellennamen, Architekturen, Versionen und Signaturfehler sorgfältig.

:::single-choice{#package-management-systems-apt-show} Welcher Befehl zeigt APT-Paketdetails für `package-name` an?

::option[`apt remove package-name`]{#package-management-systems-apt-remove-command explanation="Der Unterbefehl `remove` schlägt die Deinstallation des Pakets vor."}
::option[`dnf search package-name`]{#package-management-systems-dnf-search-command explanation="Dies durchsucht Paketquellen der RPM-Familie und ist nicht der APT-Detailbefehl."}
::option[`apt show package-name`]{#package-management-systems-apt-show-command .correct explanation="Der Unterbefehl `show` stellt Metadaten für das benannte Binärpaket dar."}
:::

## Pakete installieren

Installiere anhand des Paketnamens aus einer Paketquelle mit:

```bash
Debian family: $ sudo apt install package-name
RPM family:    $ sudo dnf install package-name
```

Die Verwaltung schlägt Abhängigkeiten und mögliche Konflikte oder Ersetzungen vor. Bestätige nicht automatisch, bevor du Paketherkunft, Version, Architektur, Downloadgröße, Datenträgeränderung, Entfernungen und neu installierte Abhängigkeiten geprüft hast.

:::single-choice{#package-management-systems-dnf-install} Welcher aktuelle Befehl installiert `package-name` aus konfigurierten Paketquellen der RPM-Familie?

::option[`rpm -qa package-name`]{#package-management-systems-rpm-query-command explanation="Dies ist eine Abfrage der installierten RPM-Datenbank und keine Installationsanfrage an eine Paketquelle."}
::option[`dnf install package-name`]{#package-management-systems-dnf-install-command .correct explanation="DNF ist die aktuelle paketquellenbewusste Verwaltung unter Fedora und neueren RHEL-Veröffentlichungen."}
::option[`apt update package-name`]{#package-management-systems-apt-update-package explanation="APT update aktualisiert Indizes und installiert kein benanntes Paket der RPM-Familie."}
:::

## Pakete entfernen

Fordere eine Entfernung an mit:

```bash
Debian family: $ sudo apt remove package-name
RPM family:    $ sudo dnf remove package-name
```

Eine Entfernung kann abhängige Pakete beeinflussen oder nun ungenutzte Abhängigkeiten und Konfiguration zurücklassen. Prüfe die vorgeschlagene Transaktion, unterscheide auf Systemen der Debian-Familie die Semantik von remove und purge und bewahre Anwendungsdaten gemäß ihrem eigenen Sicherungs- und Aufbewahrungsverfahren. Die Paketentfernung verspricht nicht, benutzererstellte Daten zu löschen.

:::single-choice{#package-management-systems-remove-review} Warum solltest du eine Entfernungstransaktion vor der Bestätigung prüfen?

::option[Eine Entfernung formatiert immer das Dateisystem, das das Paket enthält.]{#package-management-systems-removal-format explanation="Paketverwaltungen entfernen verwaltete Dateien und Zustände; sie formatieren gewöhnlich kein Dateisystem."}
::option[Paketverwaltungen können keine vorgeschlagene Änderungsmenge anzeigen.]{#package-management-systems-no-proposal explanation="Interaktive Verwaltungen zeigen gewöhnlich die geplante Transaktion gerade deshalb an, damit sie geprüft werden kann."}
::option[Andere Pakete können vom ausgewählten Paket abhängen und ebenfalls betroffen sein.]{#package-management-systems-dependent-removal .correct explanation="Abhängigkeitsbeschränkungen können eine Anfrage über den ursprünglich eingegebenen Paketnamen hinaus erweitern."}
:::

## Aktualisierungen anwenden

Aktualisiere auf einem APT-System die Metadaten und prüfe anschließend Upgrades als getrennte erfolgreiche Schritte:

```bash
$ sudo apt update
$ apt list --upgradable
$ sudo apt upgrade
```

Prüfe und installiere auf einem DNF-System verfügbare Aktualisierungen mit dem lokal dokumentierten Arbeitsablauf:

```bash
$ dnf check-update
$ sudo dnf upgrade
```

Ein Aktualisierungsbefehl kann zentrale Bibliotheken, Dienste, Kernel und Abhängigkeiten ändern. Verwende Sicherungen, Wartungsrichtlinien, Veröffentlichungshinweise und eine dem System angemessene Planung von Dienstneustarts oder Neustarts. Prüfe die Semantik des Befehlsstatus: Einige Vorgänge zur Aktualisierungsprüfung verwenden beispielsweise einen von null verschiedenen Status, um verfügbare Aktualisierungen statt einen Ausführungsfehler zu melden.

:::single-choice{#package-management-systems-apt-update-upgrade} In welcher Beziehung stehen `apt update` und `apt upgrade`?

::option[`update` entfernt Pakete; `upgrade` stellt ihre Konfigurationsdateien wieder her.]{#package-management-systems-apt-remove-restore explanation="Keiner der Befehle besitzt diese Entfernen-und-Wiederherstellen-Beziehung."}
::option[`update` aktualisiert Metadaten; `upgrade` wendet einen genehmigten Paketupgradeplan an.]{#package-management-systems-apt-two-steps .correct explanation="APT trennt die Katalogaktualisierung von der Installation neuerer Paketversionen."}
::option[Sie sind identische Namen für denselben Vorgang.]{#package-management-systems-apt-identical explanation="Sie führen getrennte Phasen aus, die unabhängig geprüft werden sollten."}
:::

## Zwischen `dnf` und `yum` wählen

Verwende `dnf` in der aktuellen Fedora- und RHEL-Dokumentation. Ein Befehl `yum` auf einem neueren RHEL-System kann das DNF-Kompatibilitätsverhalten aufrufen, doch Skripte sollten die Implementierung nicht allein aus dem Namen der ausführbaren Datei ableiten. Prüfe auf älteren Hosts die installierte Version und unterstützte Syntax, bevor du Anweisungen überträgst.

:::single-choice{#package-management-systems-yum-current-rhel} Wofür steht `yum` auf einem aktuellen RHEL-System gewöhnlich?

::option[Für einen von DNF bereitgestellten Kompatibilitätsbefehl.]{#package-management-systems-yum-dnf-alias .correct explanation="Neuere RHEL-Veröffentlichungen verwenden DNF und behalten den Befehlsnamen yum aus Kompatibilitätsgründen bei."}
::option[Für das einfache Debian-Werkzeug für `.deb`-Archive.]{#package-management-systems-yum-dpkg explanation="Debian-Systeme verwenden Werkzeuge wie APT und dpkg statt YUM für die native Paketverwaltung."}
::option[Für einen Komprimierer ausschließlich für Paketquellenmetadaten.]{#package-management-systems-yum-compressor explanation="YUM und DNF sind Paketverwaltungsschnittstellen und keine eigenständigen Komprimierungsformate."}
:::

Übe APT in [Pakete installieren und entfernen](https://labex.io/labs/linux-installing-and-removing-packages-385380) und Konzepte der DNF-/YUM-Familie in [Pakete mit YUM abfragen und aktualisieren](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869).

## Zusammenfassung

Du kannst nun verbreitete Paketquellenoperationen auswählen und prüfen.

1. Verwende APT auf Systemen der Debian-Familie und DNF auf aktuellen Systemen der RPM-Familie.
2. Prüfe Metadaten und vorgeschlagene Abhängigkeitsänderungen vor der Installation.
3. Behandle eine Entfernung als abhängigkeitsbewusste Transaktion und nicht als Löschen einer einzelnen Datei.
4. Trenne die Aktualisierung der Metadaten von der Anwendung von Upgrades, wenn das Werkzeug dies tut.
5. Prüfe, ob `yum` das ältere YUM oder ein DNF-Kompatibilitätsbefehl ist.
