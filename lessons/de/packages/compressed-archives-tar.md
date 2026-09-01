---
lesson_id: "compressed-archives-tar"
course_id: "packages"
lang: "de"
order_index: 3
title: "tar und gzip"
description: "Erfahre, wie du Dateien mit `tar` archivierst, Datenströme mit `gzip` komprimierst und Archive vor einer sicheren Extraktion prüfst."
meta_title: "tar und gzip – Pakete"
meta_description: "Ein umfassender Leitfaden zur Verwendung von tar und gzip unter Linux. Lerne tar-Komprimierung, das Erstellen und Extrahieren von Archiven und den Unterschied zwischen gzip und tar kennen. Beherrsche Befehle zum Komprimieren von tar.gz-Dateien und verwalte deine Softwarepakete wirkungsvoll."
meta_keywords: "tar und gzip, tar-Komprimierung, gzip tar, tar.gz komprimieren, gzip und tar, Linux-Archivierung, Dateikomprimierung, tar-Befehl, gzip-Befehl, Linux-Tutorial"
---

Archivierung und Komprimierung lösen unterschiedliche Probleme. Ein Archiv fasst einen Verzeichnisbaum und dessen Metadaten in einem Datenstrom zusammen. Komprimierung codiert einen Datenstrom, um seine Größe zu verringern. Eine `.tar.gz`-Datei ist konventionsgemäß ein tar-Archiv, dessen Datenstrom mit gzip komprimiert wurde.

## Einen Datenstrom mit `gzip` komprimieren

Standardmäßig komprimiert `gzip` eine Datei und ersetzt den ursprünglichen Namen durch eine `.gz`-Datei:

```bash
$ gzip report.txt
```

Nach der erfolgreichen Erstellung von `report.txt.gz` wird `report.txt` dabei gewöhnlich entfernt. Dekomprimiere die Datei mit:

```bash
$ gunzip report.txt.gz
```

Verwende, sofern unterstützt, `gzip -k report.txt`, um die Eingabedatei zu behalten, oder nutze Standarddatenströme, wenn du ausdrückliche Kontrolle benötigst. Eine Dateinamenerweiterung ist eine Konvention und kein Beweis für das tatsächliche Format; Werkzeuge wie `file` können den Inhalt prüfen.

:::single-choice{#tar-gzip-gzip-role} Was ist in dieser Lektion die Hauptaufgabe von `gzip`?

::option[Einen Verzeichnisbaum mit Dateimetadaten zu einem Archiv zusammenzufassen.]{#tar-gzip-directory-archive explanation="Tar übernimmt diese Archivierungsaufgabe, bevor die gzip-Komprimierung angewendet wird."}
::option[Einen einzelnen Eingabedatenstrom zu komprimieren.]{#tar-gzip-compress-stream .correct explanation="Gzip wandelt einen Bytestrom um und codiert nicht selbst eine Verzeichnishierarchie."}
::option[Abhängigkeitsmetadaten in einer Paketdatenbank zu installieren.]{#tar-gzip-package-install explanation="Komprimierung ist von der Installation nativer Pakete und der Abhängigkeitsverfolgung getrennt."}
:::

## Ein tar-Archiv erstellen

Erstelle ein unkomprimiertes Archiv mit:

```bash
$ tar -cvf project.tar file1 file2 directory1
```

- `-c` erstellt ein neues Archiv.
- `-v` listet Mitglieder während der Verarbeitung auf und ist optional.
- `-f project.tar` benennt die Archivdatei; da `-f` ein Argument verbraucht, solltest du den Dateinamen direkt daneben angeben.

Pfade werden als Namen von Archivmitgliedern gespeichert. Erstelle Archive aus einem bewusst gewählten Arbeitsverzeichnis und vermeide, unbeabsichtigt Geheimnisse, Zwischenspeicher, Sockets oder weit gefasste absolute Pfade aufzunehmen.

:::single-choice{#tar-gzip-create-option} Welche Option von `tar` erstellt ein neues Archiv?

::option[`-x`]{#tar-gzip-option-extract explanation="Die Operation `-x` extrahiert Archivmitglieder."}
::option[`-c`]{#tar-gzip-option-create .correct explanation="Die Erstellungsoperation schreibt aus den benannten Eingaben ein neues Archiv."}
::option[`-t`]{#tar-gzip-option-list explanation="Die Operation `-t` listet Archivmitglieder auf, ohne sie zu extrahieren."}
:::

## Ein gzip-komprimiertes tar-Archiv erstellen

GNU tar und viele andere Implementierungen können gzip mit `-z` aufrufen:

```bash
$ tar -czvf project.tar.gz file1 file2 directory1
```

Das Ergebnis ist ein einzelner gzip-komprimierter tar-Datenstrom. Komprimierung verschlüsselt das Archiv nicht und verbirgt seinen Inhalt nicht vor jemandem, der es lesen und dekomprimieren kann. Wenn Vertraulichkeit erforderlich ist, verwende einen geeigneten Arbeitsablauf mit authentifizierter Verschlüsselung und verwalte Schlüssel getrennt.

:::single-choice{#tar-gzip-z-option} Was fordert `-z` im gezeigten `tar`-Befehl an?

::option[Das Archiv mit einem Zero-Knowledge-Schlüssel zu verschlüsseln.]{#tar-gzip-z-encrypt explanation="Weder tar noch gzip bietet über diese Option eine Verschlüsselung."}
::option[Jedes Mitglied mit einer Länge von null zu verwerfen.]{#tar-gzip-z-zero explanation="Die Option wählt gzip aus und filtert Archivmitglieder nicht nach ihrer Größe."}
::option[Den Archivdatenstrom mit gzip zu verarbeiten.]{#tar-gzip-z-gzip .correct explanation="Die Option `z` verbindet den Archivierungsvorgang von tar mit der Komprimierung oder Dekomprimierung durch gzip."}
:::

## Vor dem Extrahieren auflisten

Behandle ein Archiv von einer anderen Partei als nicht vertrauenswürdige Eingabe. Liste zuerst seine Mitgliedsnamen auf:

```bash
$ tar -tzf download.tar.gz
```

Achte auf unerwartete absolute Pfade, `..`-Traversierungskomponenten, überraschende symbolische oder harte Links, Gerätedateien und Namen, die wichtige Dateien überschreiben würden. Moderne tar-Implementierungen wenden Schutzmaßnahmen an, doch Verhalten und Optionen unterscheiden sich, und die Extraktion erzeugt weiterhin vom Angreifer ausgewählte Namen und Inhalte.

Extrahiere in ein neu erstelltes, unprivilegiertes Staging-Verzeichnis:

```bash
$ mkdir extraction-stage
$ tar -xzf download.tar.gz -C extraction-stage
```

Extrahiere ein ungeprüftes Archiv nicht als root. Prüfe, was erstellt wurde, bevor du ausgewählte Dateien an ihre endgültigen Orte verschiebst.

:::single-choice{#tar-gzip-list-before-extract} Welche Operation listet Archivmitglieder auf, ohne sie zu extrahieren?

::option[`tar -czf download.tar.gz .`]{#tar-gzip-create-download explanation="Dies erstellt oder ersetzt aus dem aktuellen Verzeichnis ein Archiv."}
::option[`tar -xzf download.tar.gz`]{#tar-gzip-extract-download explanation="Die Operation `-x` schreibt Mitglieder in das Zielverzeichnis."}
::option[`tar -tzf download.tar.gz`]{#tar-gzip-list-members .correct explanation="Die Operation `-t` liest und zeigt die Mitgliedertabelle an, während `-z` gzip verarbeitet."}
:::

## Andere Komprimierungsformate

Tar-Implementierungen können mit Komprimierern wie bzip2 und xz arbeiten, die in GNU tar gewöhnlich mit `-j` beziehungsweise `-J` ausgewählt werden. Formatunterstützung und automatische Erkennung unterscheiden sich. Lies daher `tar --help` oder das lokale Handbuch. ZIP ist ein getrenntes Archivformat, das mit Werkzeugen wie `zip` und `unzip` bedient wird.

:::single-choice{#tar-gzip-archive-confidentiality} Macht die gzip-Komprimierung ein tar-Archiv vertraulich?

::option[Nein; jeder mit Lesezugriff kann es gewöhnlich dekomprimieren.]{#tar-gzip-not-encryption .correct explanation="Komprimierung verändert Darstellung und Größe, bietet aber weder Zugriffskontrolle noch kryptografische Geheimhaltung."}
::option[Ja; gzip leitet einen Verschlüsselungsschlüssel aus dem Dateinamen ab.]{#tar-gzip-filename-key explanation="Gzip implementiert keinen solchen Verschlüsselungsmechanismus."}
::option[Ja; tar verschlüsselt jedes Mitglied, bevor gzip es verarbeitet.]{#tar-gzip-tar-encrypt explanation="Tar archiviert Mitglieder, verschlüsselt ihre Inhalte aber nicht automatisch."}
:::

Übe mit entbehrlichen Dateien in [Dateipaketierung und -komprimierung](https://labex.io/labs/linux-file-packaging-and-compression-385413) und wende anschließend Prüfung und Staging in [Eine Sicherung mit tar erstellen und wiederherstellen](https://labex.io/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843) an.

## Zusammenfassung

Du kannst tar-Archivierung nun sicher mit gzip-Komprimierung verbinden.

1. Unterscheide ein tar-Archiv von der gzip-Komprimierung.
2. Erstelle Archive mit `-c` und gzip-Datenströme mit `-z`.
3. Liste Mitglieder mit `-t` auf, bevor du sie mit `-x` extrahierst.
4. Extrahiere nicht vertrauenswürdige Inhalte in ein unprivilegiertes Staging-Verzeichnis.
5. Behandle Komprimierung getrennt von Verschlüsselung.
