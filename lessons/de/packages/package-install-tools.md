---
lesson_id: "package-install-tools"
course_id: "packages"
lang: "de"
order_index: 5
title: "rpm und dpkg"
description: "Erfahre, wie `dpkg` und `rpm` ihre nativen Paketdatenbanken und lokalen Archive prüfen und verändern."
meta_title: "rpm und dpkg – Pakete"
meta_description: "Lerne, Pakete mit den Befehlen rpm und dpkg zu installieren, zu entfernen und aufzulisten. Verstehe die direkte Paketverwaltung für .deb- und .rpm-Dateien. Beginne deine Linux-Reise!"
meta_keywords: "rpm, dpkg, Linux-Paketverwaltung, .deb, .rpm, Linux-Tutorial, Leitfaden für Einsteiger, Pakete installieren"
---

`dpkg` ist das einfache Paketwerkzeug auf Systemen der Debian-Familie, während `rpm` auf Systemen der RPM-Familie eine ähnliche Aufgabe erfüllt. Sie entpacken native Archive, führen Lebenszyklusaktionen von Paketen aus und aktualisieren Datenbanken installierter Pakete. Paketquellenbewusste Werkzeuge wie APT und DNF bauen auf diesen einfacheren Mechanismen auf.

## Ein Archiv vor der Installation prüfen

Ein Paketarchiv entspricht nicht einer einzelnen ausführbaren Datei. Es kann viele Nutzdateien, Metadaten, Konfigurationsbehandlung und privilegierte Lebenszyklusskripte enthalten. Prüfe Herkunft, Signatur oder authentifizierten Downloadweg, Metadaten und Inhalt vor der Installation.

```bash
Debian: $ dpkg-deb --info ./some-package.deb
Debian: $ dpkg-deb --contents ./some-package.deb
RPM:    $ rpm -qip ./some-package.rpm
RPM:    $ rpm -qlp ./some-package.rpm
```

Das `p` in den gezeigten RPM-Abfrageformen bedeutet „eine Paketdatei abfragen“ statt die installierte Datenbank. Die Abfrageausgabe hilft beim Prüfen eines Pakets, kann aber nicht beweisen, dass seine Skripte oder Programme sicher sind.

:::single-choice{#package-install-tools-native-format} Welches einfache Werkzeug verwaltet Debian-`.deb`-Pakete und ihre installierte Datenbank?

::option[`rpm`]{#package-install-tools-rpm-debian explanation="RPM verwaltet auf Systemen der RPM-Familie sein eigenes natives Format und seine Datenbank."}
::option[`tar`]{#package-install-tools-tar-debian explanation="Tar kann Archive lesen, implementiert aber nicht den Lebenszyklus installierter Debian-Pakete."}
::option[`dpkg`]{#package-install-tools-dpkg-debian .correct explanation="Systeme der Debian-Familie verwenden `dpkg` für einfache Operationen auf `.deb`-Archiven und der Paketdatenbank."}
:::

## Ein lokales Archiv installieren

Die direkte einfache Installation verwendet:

```bash
Debian: $ sudo dpkg -i ./some-package.deb
RPM:    $ sudo rpm -U ./some-package.rpm
```

`dpkg -i` kann das angeforderte Archiv entpacken und konfigurieren, ruft aber keine fehlenden Abhängigkeiten aus Paketquellen ab. Auch ein direktes `rpm` stellt nicht den gewöhnlichen Arbeitsablauf eines Paketquellen-Solvers bereit. Für ein lokales Archiv ist ein übergeordneter Befehl gewöhnlich vorzuziehen, da er Abhängigkeiten aus konfigurierten Quellen auflösen kann:

```bash
Debian: $ sudo apt install ./some-package.deb
RPM:    $ sudo dnf install ./some-package.rpm
```

Prüfe die Transaktion vor der Bestätigung. Ein vorangestelltes `./` unterscheidet in APT einen lokalen Debian-Archivpfad von einem Paketnamen aus einer Paketquelle.

:::single-choice{#package-install-tools-local-dependencies} Welcher gezeigte Befehl kann eine lokale `.deb`-Datei installieren und dabei verfügbare Abhängigkeiten aus Paketquellen auflösen?

::option[`dpkg -l ./some-package.deb`]{#package-install-tools-dpkg-list-file explanation="`dpkg -l` listet Auswahlen installierter Pakete auf und ist nicht der Arbeitsablauf zur lokalen Installation mit Abhängigkeitsauflösung."}
::option[`rpm -qa ./some-package.deb`]{#package-install-tools-rpm-query-deb explanation="Die RPM-Abfragesyntax installiert kein Debian-Archiv."}
::option[`apt install ./some-package.deb`]{#package-install-tools-apt-local .correct explanation="APT erkennt den ausdrücklichen lokalen Pfad und kann deklarierte Abhängigkeiten mithilfe konfigurierter Paketquellen erfüllen."}
:::

## Ein installiertes Paket entfernen

Die Entfernung richtet sich nach dem Namen eines installierten Pakets und nicht nach dem zuvor verwendeten Archivdateinamen:

```bash
Debian: $ sudo dpkg --remove package-name
RPM:    $ sudo rpm --erase package-name
```

Unter Debian behält `--remove` gewöhnlich als conffiles klassifizierte Konfigurationsdateien bei; `--purge` fordert vorbehaltlich von Paketskripten und nicht verwalteten Daten auch deren Entfernung an. Keiner der Befehle garantiert die Löschung benutzererstellter Daten. Das übergeordnete `apt remove` oder `dnf remove` ist im Allgemeinen besser, da es verwandte Pakete bewerten und eine vollständige Transaktion darstellen kann.

:::single-choice{#package-install-tools-remove-operand} Welchen Operanden erwartet `dpkg --remove` für ein installiertes Paket?

::option[Die URL des Paketquellenindex.]{#package-install-tools-remove-url explanation="Der Ort einer Paketquelle ist nicht die Paketidentität, die der einfachen Entfernung übergeben wird."}
::option[Den Namen des installierten Pakets.]{#package-install-tools-remove-name .correct explanation="Die Entfernung richtet sich an den Paketeintrag, beispielsweise `example`, und benötigt nicht dessen früheren `.deb`-Pfad."}
::option[Die PID eines vom Paket gestarteten Prozesses.]{#package-install-tools-remove-pid explanation="Prozess-IDs haben nichts mit dem Schlüssel in der Datenbank installierter Pakete zu tun."}
:::

## Installierten Zustand abfragen

Liste installierte oder bekannte Paketeinträge auf mit:

```bash
Debian: $ dpkg-query -l
RPM:    $ rpm -qa
```

Bevorzuge für gezielte Prüfungen einen bestimmten Paketnamen und ein maschinenlesbares Format, wenn die Zuverlässigkeit eines Skripts wichtig ist. Paketdatenbanken beschreiben den verwalteten Zustand; lokale Administratoren oder Anwendungen können Dateien anschließend weiterhin ändern. Verwende daher Prüffunktionen, wenn du installierte Dateien mit den erfassten Metadaten vergleichen musst.

:::single-choice{#package-install-tools-rpm-list-installed} Welcher Befehl fragt alle in der RPM-Datenbank als installiert erfassten Pakete ab?

::option[`rpm -qa`]{#package-install-tools-rpm-query-all .correct explanation="`-q` wählt den Abfragemodus aus und `-a` erweitert ihn auf alle installierten Paketeinträge."}
::option[`rpm -e`]{#package-install-tools-rpm-erase explanation="`-e` fordert die Paketentfernung an und keine schreibgeschützte Auflistung."}
::option[`dpkg-deb --contents`]{#package-install-tools-deb-contents explanation="Dies prüft den Nutzinhalt einer Debian-Archivdatei und nicht die installierte RPM-Datenbank."}
:::

Nutze [Pakete mit RPM verwalten](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868), um Archivabfragen und Integritätsprüfungen auf einem isolierten System zu üben.

## Zusammenfassung

Du kannst nun einfache Paketoperationen von Paketquellentransaktionen unterscheiden.

1. Prüfe Metadaten und Inhalte lokaler Archive vor der Installation.
2. Verwende `dpkg` für `.deb` und `rpm` für `.rpm` bei einfachen Operationen.
3. Bevorzuge APT oder DNF, wenn Abhängigkeiten aufgelöst werden müssen.
4. Entferne anhand des installierten Paketnamens und überprüfe den verwalteten Zustand getrennt.
