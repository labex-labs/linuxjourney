---
lesson_id: "package-repositories"
course_id: "packages"
lang: "de"
order_index: 2
title: "Paketquellen"
description: "Erfahre, wie Paketquellen signierte Paketindizes veröffentlichen und wie APT konfigurierte Quellen der Debian-Familie findet."
meta_title: "Paketquellen – Pakete"
meta_description: "Erkunde Linux-Paketquellen und ihre Rolle in der Paketverwaltung. Erfahre, wie dein System Quellen wie die Datei /etc/apt/sources.list verwendet, um Linux-Pakete zu finden und zu installieren."
meta_keywords: "Linux-Paketquellen, APT-Quellenliste, /etc/apt/sources.list, Linux-Pakete, Linux für Einsteiger, Linux-Tutorial, Paketverwaltung"
---

Eine Paketquelle veröffentlicht Pakete zusammen mit Indizes und Veröffentlichungsmetadaten. Eine Paketverwaltung lädt diese Indizes herunter, wählt Versionen aus, die mit der konfigurierten Distribution und Architektur kompatibel sind, überprüft die Authentifizierung der Paketquelle und ruft die benötigten Paketdateien ab.

## Metadaten der Paketquelle und lokale Kataloge

Eine Paketquelle ist mehr als ein Verzeichnis mit Archiven. Ihre Metadaten beschreiben verfügbare Paketnamen, Versionen, Architekturen, Prüfsummen, Abhängigkeiten und Bereiche der Paketquelle. Der Client speichert einen lokalen Katalog zwischen, damit er Pakete durchsuchen und auflösen kann, ohne zuerst jedes Archiv herunterzuladen.

Aktualisiere die konfigurierten Metadaten auf einem System der Debian-Familie mit:

```bash
$ sudo apt update
```

Dies aktualisiert die lokalen Paketindizes; es installiert nicht von selbst alle verfügbaren Upgrades. Prüfe die gemeldeten Quellen und Authentifizierungsfehler, statt fehlgeschlagene Einträge zu ignorieren.

:::single-choice{#package-repositories-apt-update} Was aktualisiert `apt update` in erster Linie?

::option[Jede installierte Paketbinärdatei ohne Bestätigung.]{#package-repositories-all-binaries explanation="Die Installation von Upgrades ist ein getrennter Vorgang von der Aktualisierung der Metadaten."}
::option[Die Passwörter von Benutzern, die Pakete installieren dürfen.]{#package-repositories-user-passwords explanation="Die Aktualisierung von Paketquellenindizes ändert keine lokalen Authentifizierungsdaten."}
::option[Die lokalen Indizes, die verfügbare Pakete aus konfigurierten Quellen beschreiben.]{#package-repositories-local-indexes .correct explanation="APT lädt aktuelle Metadaten der Paketquellen herunter, damit spätere Suchen und die Abhängigkeitsauflösung einen aktuellen Katalog verwenden."}
:::

## Konfiguration von APT-Quellen

APT liest konfigurierte Quellen aus beiden folgenden Orten:

- `/etc/apt/sources.list`
- auf `.list` oder `.sources` endenden Dateien unter `/etc/apt/sources.list.d/`

Die Erweiterung `.list` verwendet das traditionelle einzeilige Format. Die Erweiterung `.sources` verwendet Abschnitte im deb822-Stil, die die aktuelle APT-Dokumentation für neue Konfigurationen empfiehlt. Eine Distribution kann ihre Standardquellen an beiden Orten ablegen. Daher enthält `/etc/apt/sources.list` nicht garantiert die vollständige oder primäre Konfiguration.

Eine Quelle im deb822-Stil kann so aussehen:

```text
Types: deb
URIs: https://deb.example.invalid/repository
Suites: stable
Components: main
Signed-By: /etc/apt/keyrings/example.gpg
```

Dies veranschaulicht lediglich die Syntax; die reservierte Domain `.invalid` ist keine nutzbare Paketquelle.

:::single-choice{#package-repositories-apt-locations} Wo kann APT aktive Definitionen von Paketquellen lesen?

::option[Ausschließlich aus `/etc/apt/sources.list`.]{#package-repositories-only-main-list explanation="APT liest außerdem unterstützte Quelldateien aus `/etc/apt/sources.list.d/`."}
::option[Ausschließlich aus Dateien in den Home-Verzeichnissen der Benutzer.]{#package-repositories-only-home explanation="Die systemweite Konfiguration von APT-Quellen befindet sich gewöhnlich unter `/etc/apt`."}
::option[Aus `/etc/apt/sources.list` und unterstützten Dateien in `/etc/apt/sources.list.d/`.]{#package-repositories-both-locations .correct explanation="APT kombiniert die Hauptdatei mit Definitionen in `.list`- und `.sources`-Dateien im Quellenlistenverzeichnis."}
:::

## Authentifizierung von Paketquellen

APT überprüft signierte Veröffentlichungsmetadaten einer Paketquelle und vergleicht anschließend heruntergeladene Paketdateien mit den authentifizierten Prüfsummen in diesen Metadaten. `Signed-By` kann eine Quelle auf einen bestimmten Schlüsselbund begrenzen, statt für diese Paketquelle jedem global konfigurierten Schlüssel zu vertrauen.

Eine gültige Signatur bestätigt, dass die Metadaten vom Inhaber eines akzeptierten Signaturschlüssels stammen und nicht unbemerkt verändert wurden. Sie beweist nicht, dass die Software des Herausgebers fehlerfrei, nicht bösartig oder für das System geeignet ist. Bestätige den Fingerabdruck des Schlüssels und die Quellenanweisungen über einen unabhängigen vertrauenswürdigen Kanal.

:::single-choice{#package-repositories-signed-by} Welchen Sicherheitszweck erfüllt `Signed-By` in einer APT-Quellendefinition?

::option[Jedes installierte Paket zu verschlüsseln, damit root es nicht lesen kann.]{#package-repositories-package-encryption explanation="Die Signierung von Paketquellen ermöglicht Herkunfts- und Integritätsprüfungen, nicht die Geheimhaltung vor dem lokalen Administrator."}
::option[Diese Quelle auf ausgewählte Signaturschlüssel zu begrenzen.]{#package-repositories-key-scope .correct explanation="Das Feld bindet die Prüfung der Paketquelle an ausgewähltes Schlüsselbundmaterial statt an eine uneingeschränkte globale Schlüsselmenge."}
::option[Zu garantieren, dass die Paketquelle keine anfällige Software enthält.]{#package-repositories-no-vulnerabilities explanation="Kryptografische Authentizität bewertet weder Softwarequalität noch Sicherheitsfehler."}
:::

## Drittanbieterquellen bewusst hinzufügen

Eine Paketquelle kann Pakete und Lebenszyklusskripte mit Systemrechten installieren. Ihr Hinzufügen erweitert daher die Vertrauensgrenze der Software des Systems. Vorher solltest du:

1. Die Paketquelle der Distribution bevorzugen, wenn sie die Anforderung erfüllt.
2. Herausgeber, unterstützte Veröffentlichung, Architektur und Fingerabdruck des Signaturschlüssels bestätigen.
3. Eine eigene Quelldatei und einen begrenzten Schlüsselbund verwenden.
4. Paketnamen und Änderungen an Abhängigkeiten vor der Installation prüfen.
5. Dokumentieren, wie du die Quelle deaktivierst und ihre Pakete migrierst oder entfernst.

Kopiere keine veralteten Anweisungen, die Signaturprüfungen deaktivieren oder ein ungeprüftes entferntes Skript in eine privilegierte Shell leiten.

:::single-choice{#package-repositories-third-party-risk} Warum erweitert das Hinzufügen einer Drittanbieterquelle die Vertrauensgrenze des Systems?

::option[Ihre authentifizierten Pakete und Skripte können mit Systemrechten installiert werden.]{#package-repositories-privileged-install .correct explanation="Das Vertrauen in die Signaturquelle kann Code und Lebenszyklusaktionen autorisieren, die das Betriebssystem beeinflussen."}
::option[Sie veranlasst den Linux-Kernel, keine Dateiberechtigungen mehr durchzusetzen.]{#package-repositories-disable-permissions explanation="Die Konfiguration von Paketquellen deaktiviert nicht die gewöhnlichen Zugriffskontrollmechanismen des Kernels."}
::option[Sie wandelt alle nativen Pakete in Quellarchive um.]{#package-repositories-convert-source explanation="Das Hinzufügen einer Paketquelle ändert die verfügbaren Paketquellen und nicht das grundlegende Format bestehender Pakete."}
:::

Übe die paketquellenbasierte Installation in [Softwareinstallation unter Linux](https://labex.io/labs/linux-software-installation-on-linux-18005) oder vergleiche einen Arbeitsablauf der Red-Hat-Familie in [Pakete mit YUM abfragen und aktualisieren](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869). Die genaue APT-Syntax findest du im lokalen Handbuch `sources.list(5)`.

## Zusammenfassung

Du kannst nun erklären, wie eine konfigurierte Paketquelle zu vertrauenswürdigen Paketmetadaten wird.

1. Unterscheide Paketquellenindizes von Paketarchiven.
2. Verwende `apt update`, um den lokalen Katalog zu aktualisieren.
3. Finde APT-Quellendefinitionen im einzeiligen und deb822-Stil.
4. Begrenze Signaturschlüssel und prüfe Vertrauen in Drittanbieter bewusst.
