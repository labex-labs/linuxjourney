---
index: 8
lang: "de"
title: "Swap"
meta_title: "Swap – Das Dateisystem"
meta_description: "Erfahren Sie mehr über den Linux-Swap-Speicher, seine Funktionsweise sowie die Erstellung und Verwaltung von Swap-Partitionen. Optimieren Sie die Speichernutzung Ihres Systems mit dieser Anleitung!"
meta_keywords: "Linux Swap, mkswap, swapon, swapoff, /etc/fstab, virtueller Speicher, Linux Anfänger, Linux Tutorial"
---

## Lesson Content

In unserem vorherigen Beispiel habe ich Ihnen gezeigt, wie Sie Ihre Partitionstabelle anzeigen können. Lassen Sie uns dieses Beispiel noch einmal aufgreifen, genauer gesagt diese Zeile:

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

Was ist diese Swap-Partition? Nun, Swap verwenden wir, um unserem System virtuellen Speicher zuzuweisen. Wenn Ihr Arbeitsspeicher knapp wird, verwendet das System diese Partition, um Speicherbereiche von inaktiven Prozessen auf die Festplatte zu "swappen", damit Sie nicht durch Speichermangel ausgebremst werden.

### Verwendung einer Partition für den Swap-Bereich

Angenommen, wir möchten, dass unsere Partition `/dev/sdb2` für den Swap-Bereich verwendet wird.

1. Stellen Sie zunächst sicher, dass sich nichts auf der Partition befindet.
2. Führen Sie aus: `mkswap /dev/sdb2`, um Swap-Bereiche zu initialisieren.
3. Führen Sie aus: `swapon /dev/sdb2`. Dies aktiviert das Swap-Gerät.
4. Wenn die Swap-Partition beim Booten bestehen bleiben soll, müssen Sie einen Eintrag in die Datei `/etc/fstab` aufnehmen. `sw` ist der Dateisystemtyp, den Sie verwenden werden.
5. Zum Entfernen von Swap: `swapoff /dev/sdb2`.

Im Allgemeinen sollten Sie etwa die doppelte Menge an Swap-Speicher zuweisen, als Sie Arbeitsspeicher haben. Moderne Systeme sind heute jedoch in der Regel leistungsfähig genug und verfügen ohnehin über ausreichend RAM.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Swap-Speicher und der Verwaltung des virtuellen Speichers zu festigen:

1. **[Erstellen und Aktivieren einer Swap-Datei in Linux](https://labex.io/de/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Üben Sie das Erstellen und Aktivieren einer Swap-Datei, eine entscheidende Fähigkeit für die Verwaltung des virtuellen Speichers Ihres Systems.

Dieses Labor hilft Ihnen, die Konzepte von Swap-Partitionen in realen Szenarien anzuwenden und Selbstvertrauen im Umgang mit Systemressourcen aufzubauen.

## Quiz Question

Was ist der Befehl, um den Swap-Bereich auf einem Gerät zu aktivieren?

## Quiz Answer

swapon
