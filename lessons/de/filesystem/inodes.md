---
lesson_id: "inodes"
course_id: "filesystem"
lang: "de"
order_index: 11
title: "Inodes"
description: "Lerne, wie Inode-Nummern Verzeichnisnamen mit Metadaten und Daten von Dateisystemobjekten verbinden."
meta_title: "Inodes – Das Dateisystem"
meta_description: "Lerne Linux-Inodes, Verzeichniseinträge, Metadaten, Hardlinks, offene Referenzen und Inode-Kapazität mit ls -li, stat und df -i kennen."
meta_keywords: "Linux Inode, Inode Linux, Inode Nummer, Dateisystem, df -i, ls -li, stat, Hardlink"
---

In Inode-basierten Unix-Dateisystemen ordnet ein Verzeichnis jeden Eintragsnamen einer Inode-Nummer zu. Der Inode stellt das Dateisystemobjekt dar und zeichnet Metadaten auf, die zum Auffinden und Interpretieren seiner Daten nötig sind. Der Pfadname ist daher nicht als primäre Identität des Objekts selbst gespeichert.

## Mit einem Inode gespeicherte Metadaten

Zu den häufig mit einem Inode verbundenen Metadaten gehören:

- Objekttyp und Berechtigungsmodus
- Benutzer- und Gruppeneigentümerschaft
- logische Größe und Buchhaltung zugewiesener Blöcke
- Anzahl der Hardlinks
- Zeitstempel für Zugriff, Änderung und Statusänderung
- Verweise auf Dateidaten oder dateisystemspezifische Extent-Strukturen

Der Inode speichert normalerweise nicht den Namen des Verzeichniseintrags. Ein Dateisystem kann außerdem erweiterte Attribute, Zugriffskontrolllisten, Geburtszeit, Inline-Daten oder weitere Informationen in formatspezifischen Strukturen speichern.

`ctime` ist der Zeitpunkt der Inode-Statusänderung und nicht zwangsläufig die Erstellungszeit der Datei. Ein getrennter Geburts- oder Erstellungszeitstempel ist optional und möglicherweise nicht verfügbar.

:::single-choice{#inodes-name-location} Wo ist die Pfadnamenkomponente einer gewöhnlichen Datei normalerweise mit ihrer Inode-Nummer verknüpft?

::option[Im Prozess-Scheduler.]{#inodes-scheduler-name explanation="Der Zustand der CPU-Ablaufplanung implementiert keine Pfadauflösung des Dateisystems."}
::option[In einem Verzeichniseintrag.]{#inodes-directory-entry .correct explanation="Ein Verzeichnis ordnet innerhalb dieses Dateisystems einen Namen einer Inode-Nummer zu."}
::option[In der Partitionstabelle des Datenträgers.]{#inodes-partition-name explanation="Eine Partitionstabelle ordnet Speicherbereiche und keine einzelnen Dateinamen zu."}
:::

## Inode-Nummern und Dateisystemumfang

Zeige Inode-Nummern an:

```bash
$ ls -li
```

Das erste Feld ist die Inode-Nummer. Untersuche ein Objekt ausführlicher:

```bash
$ stat path
```

Eine Inode-Nummer ist nur innerhalb eines Dateisystems zu einem bestimmten Zeitpunkt eindeutig. Dieselbe Nummer kann in einem anderen Dateisystem vorkommen und nach der Freigabe eines Inodes erneut verwendet werden. Identifiziere ein Objekt zuverlässig durch Dateisystemidentität und Inode-Nummer gemeinsam, nicht allein anhand der Inode-Nummer.

:::single-choice{#inodes-number-scope} In welchem Umfang ist eine Inode-Nummer eine Objektkennung?

::option[Für immer auf jedem Linux-System der Welt.]{#inodes-global-forever explanation="Inodes werden lokal in einem Dateisystem zugewiesen und ihre Kennungen können wiederverwendet werden."}
::option[In einem Dateisystem zu einem bestimmten Zeitpunkt.]{#inodes-one-filesystem .correct explanation="Andere Dateisysteme können dieselbe Nummer verwenden; freigegebene Inode-Nummern können später erneut vergeben werden."}
::option[Nur im Shellprozess, der die Datei erstellt hat.]{#inodes-shell-scope explanation="Das Dateisystem und nicht eine einzelne Shell verwaltet die Inode-Identität."}
:::

## Hardlinks und offene Referenzen

Mehrere Verzeichniseinträge können auf denselben Inode verweisen; dies sind Hardlinks. Das Erstellen eines weiteren Hardlinks erhöht die Linkanzahl des Objekts. Wird ein Name entfernt, sinkt die Anzahl, ohne die Daten zu löschen, solange ein anderer Link vorhanden ist.

Auch nach dem Entfernen des letzten Verzeichniseintrags bleibt eine geöffnete Datei zugewiesen, bis die letzte Prozessreferenz geschlossen wird. Ihre Linkanzahl kann null sein, während ein Dateideskriptor weiterhin darauf zugreift. Das erklärt, warum das Löschen eines großen geöffneten Protokolls die von `df` gemeldete Belegung nicht sofort verringern muss.

:::single-choice{#inodes-unlinked-open-file} Wann werden die Ressourcen einer nicht mehr verlinkten Datei normalerweise freigegeben?

::option[Sofort nach dem Entfernen eines beliebigen Hardlink-Namens.]{#inodes-one-link-removed explanation="Andere Hardlinks oder offene Referenzen können das Objekt am Leben halten."}
::option[Erst nach der Neuformatierung des gesamten Dateisystems.]{#inodes-reformat-only explanation="Gewöhnliche Unlink- und Close-Operationen geben nicht mehr verwendete Inodes und Blöcke frei."}
::option[Nachdem ihre Linkanzahl null ist und die letzte offene Referenz geschlossen wurde.]{#inodes-zero-links-no-opens .correct explanation="Verzeichnisnamen und Dateideskriptoren von Prozessen sind voneinander unabhängige Referenzen auf den Inode."}
:::

## Inode-Kapazität

In Dateisystemen mit einem endlichen oder gemeldeten Inode-Pool können Millionen kleiner Dateien die Metadatenkapazität erschöpfen, bevor die Datenblöcke voll sind. Untersuche die Inode-Buchhaltung eingehängter Dateisysteme:

```bash
$ df -i
```

Sind keine freien Inodes vorhanden, kann das Erstellen einer weiteren Datei fehlschlagen, obwohl `df -h` freie Blöcke meldet. Zuweisungsstrategien unterscheiden sich: Manche Dateisysteme reservieren Inode-Strukturen bei ihrer Erstellung, andere verwalten Metadaten dynamisch und können Inode-Kapazität anders melden.

:::single-choice{#inodes-df-i-purpose} Was meldet `df -i`, wenn das Dateisystem eine Inode-Buchhaltung bereitstellt?

::option[Den Inhalt jeder Datei in Inode-Reihenfolge.]{#inodes-df-i-content explanation="Df meldet zusammengefasste Dateisystemstatistiken und liest keine Dateiinhalte."}
::option[Verbrauchte und verfügbare Inode-Kapazität.]{#inodes-df-i-capacity .correct explanation="Die Inode-Ansicht hilft, die Erschöpfung von Metadatenobjekten unabhängig von Datenblöcken zu diagnostizieren."}
::option[Die Firmware-Version des Datenträgers.]{#inodes-df-i-firmware explanation="Das Firmware-Inventar steht in keinem Zusammenhang mit der Inode-Nutzung."}
:::

## Dateisystemspezifische Datenzuordnung

Gehe nicht davon aus, dass jeder Inode genau zwölf direkte sowie drei indirekte Zeiger besitzt. Das beschreibt einige klassische Dateisystemstrukturen sinnvoll, doch modernes ext4 kann Extents verwenden, während XFS, Btrfs und andere Dateisysteme andere Strukturen einsetzen. Inline-Daten und komprimierte oder Copy-on-Write-Extents verändern die Beziehung zusätzlich.

Verwende dateisystemspezifische Diagnosewerkzeuge nur in schreibgeschützten oder dokumentierten Modi, wenn die interne Zuordnung wichtig ist. Für die gewöhnliche Administration bieten `stat`, `find -inum`, `df -i` und linkbewusste Werkzeuge sicherere Abstraktionen.

:::single-choice{#inodes-layout-portability} Warum solltest du nicht für jeden Inode eine feste Zeigerstruktur voraussetzen?

::option[Inodes verweisen in keiner Weise auf Dateidaten.]{#inodes-no-data-reference explanation="Das Dateisystem muss das Objekt mit seinem Inhalt verknüpfen, auch wenn der Mechanismus variiert."}
::option[Dateisystemimplementierungen verwenden unterschiedliche Extent-, Baum- und Inline-Datenstrukturen.]{#inodes-format-specific-layout .correct explanation="Die Zuordnung vom Inode zum Inhalt auf dem Datenträger gehört zum Format des jeweiligen Dateisystems."}
::option[Jede Inode-Struktur wird getrennt vom Dateieigentümer ausgewählt.]{#inodes-owner-layout explanation="Dateisystemimplementierung und -format bestimmen die Metadatenstruktur."}
:::

Nutze das Lab [Dateien und Verzeichnisse unter Linux verwalten](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835), um Inode-Nummern und Linkanzahlen an entbehrlichen Dateien zu vergleichen.

## Zusammenfassung

Du kannst Pfadnamen, Inodes, Links und Dateisystemkapazität nun miteinander in Beziehung setzen.

1. Behandle Verzeichniseinträge als Zuordnungen von Namen zu Inode-Nummern.
2. Lies Metadaten und Zeitstempel, ohne ctime mit der Erstellung zu verwechseln.
3. Begrenze Inode-Nummern auf ein Dateisystem und einen Zeitpunkt.
4. Berücksichtige sowohl Hardlinks als auch offene Dateideskriptoren.
5. Verwende dateisystemspezifische Modelle statt einer universellen Zeigerstruktur.
