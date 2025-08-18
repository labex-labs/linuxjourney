---
lang: "de"
title: "swap"
meta_description: "Erfahren Sie mehr über den Linux-Swap-Speicher, wie er funktioniert und wie Sie Swap-Partitionen erstellen und verwalten. Optimieren Sie die Speichernutzung Ihres Systems mit diesem Leitfaden!"
meta_keywords: "Linux swap, mkswap, swapon, swapoff, /etc/fstab, virtueller Speicher, Linux Anfänger, Linux Tutorial"
---

## Lesson Content

In unserem vorherigen Beispiel habe ich Ihnen gezeigt, wie Sie Ihre Partitionstabelle anzeigen können. Lassen Sie uns dieses Beispiel noch einmal aufgreifen, genauer gesagt diese Zeile:

```
Number  Start   End     Size    Type      File system     Flags
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
```

Was ist diese swap-Partition? Nun, swap ist das, was wir verwenden, um unserem System virtuellen Speicher zuzuweisen. Wenn der Speicher knapp wird, verwendet das System diese Partition, um Speicherteile von inaktiven Prozessen auf die Festplatte zu "swappen", damit Sie nicht durch Speichermangel ausgebremst werden.

### Eine Partition für den swap-Bereich verwenden

Nehmen wir an, wir wollten unsere Partition `/dev/sdb2` für den swap-Bereich verwenden.

1. Stellen Sie zunächst sicher, dass sich nichts auf der Partition befindet.
2. Führen Sie aus: `mkswap /dev/sdb2`, um swap-Bereiche zu initialisieren.
3. Führen Sie aus: `swapon /dev/sdb2`. Dies aktiviert das swap-Gerät.
4. Wenn die swap-Partition beim Booten bestehen bleiben soll, müssen Sie einen Eintrag in die Datei `/etc/fstab` hinzufügen. `sw` ist der Dateisystemtyp, den Sie verwenden werden.
5. Um swap zu entfernen: `swapoff /dev/sdb2`.

Im Allgemeinen sollten Sie etwa doppelt so viel swap-Speicher zuweisen, wie Sie Arbeitsspeicher haben. Moderne Systeme sind heute jedoch in der Regel leistungsstark genug und verfügen ohnehin über ausreichend RAM.

## Exercise

Partitionieren Sie den freien Speicherplatz auf dem USB-Laufwerk für den swap-Bereich.

## Quiz Question

Wie lautet der Befehl, um swap-Speicher auf einem Gerät zu aktivieren?

## Quiz Answer

swapon
