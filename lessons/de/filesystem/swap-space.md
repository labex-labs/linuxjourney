---
index: 8
lang: "de"
title: "Swap"
meta_title: "Swap - Das Dateisystem"
meta_description: "Erfahren Sie mehr über den Linux-Swap-Bereich, wie er funktioniert und wie Sie Swap-Partitionen erstellen und verwalten. Optimieren Sie die Speichernutzung Ihres Systems mit diesem Leitfaden!"
meta_keywords: "Linux Swap, mkswap, swapon, swapoff, /etc/fstab, virtueller Speicher, Linux Anfänger, Linux Tutorial"
---

## Lesson Content

In unserem vorherigen Beispiel habe ich Ihnen gezeigt, wie Sie Ihre Partitionstabelle anzeigen können. Lassen Sie uns dieses Beispiel noch einmal aufgreifen, genauer gesagt diese Zeile:

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

Was ist diese Swap-Partition? Nun, Swap ist das, was wir verwenden, um unserem System virtuellen Speicher zuzuweisen. Wenn Sie wenig Speicher haben, verwendet das System diese Partition, um Teile des Speichers von inaktiven Prozessen auf die Festplatte "auszulagern", damit Sie nicht wegen Speichermangels ausgebremst werden.

### Eine Partition für den Swap-Bereich verwenden

Nehmen wir an, wir wollten unsere Partition `/dev/sdb2` für den Swap-Bereich verwenden.

1. Stellen Sie zunächst sicher, dass sich nichts auf der Partition befindet.
2. Führen Sie aus: `mkswap /dev/sdb2`, um Swap-Bereiche zu initialisieren.
3. Führen Sie aus: `swapon /dev/sdb2`. Dies aktiviert das Swap-Gerät.
4. Wenn Sie möchten, dass die Swap-Partition beim Booten bestehen bleibt, müssen Sie einen Eintrag in die Datei `/etc/fstab` hinzufügen. `sw` ist der Dateisystemtyp, den Sie verwenden werden.
5. Um Swap zu entfernen: `swapoff /dev/sdb2`.

Im Allgemeinen sollten Sie etwa doppelt so viel Swap-Speicherplatz zuweisen, wie Sie Arbeitsspeicher haben. Moderne Systeme sind heute jedoch in der Regel leistungsstark genug und verfügen ohnehin über ausreichend RAM.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Linux-Swap-Bereichs und der Verwaltung des virtuellen Speichers zu vertiefen:

1. **[Swap-Datei in Linux erstellen und aktivieren](https://labex.io/de/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** – Üben Sie das Erstellen und Aktivieren einer Swap-Datei, eine entscheidende Fähigkeit für die Verwaltung des virtuellen Speichers Ihres Systems.

Dieses Lab hilft Ihnen, die Konzepte von Swap-Partitionen in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Systemressourcen aufzubauen.

## Quiz Question

Wie lautet der Befehl zum Aktivieren des Swap-Bereichs auf einem Gerät?

## Quiz Answer

swapon
