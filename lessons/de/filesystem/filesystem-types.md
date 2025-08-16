---
title: "Dateisystemtypen"
description: "Erfahren Sie mehr über Linux-Dateisystemtypen wie ext4, Btrfs und XFS. Verstehen Sie Journaling und VFS für konsistente Daten. Entdecken Sie gängige Linux-Dateisysteme in diesem Leitfaden für Anfänger."
keywords: "Linux-Dateisystemtypen, ext4, Btrfs, XFS, Journaling, VFS, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Es gibt viele verschiedene Dateisystemimplementierungen. Einige sind schneller als andere, einige unterstützen größere Speicherkapazitäten, und andere funktionieren nur auf kleineren Speicherkapazitäten. Verschiedene Dateisysteme organisieren ihre Daten auf unterschiedliche Weisen, und wir werden detailliert darauf eingehen, welche Arten von Dateisystemen es gibt. Da so viele verschiedene Implementierungen verfügbar sind, benötigen Anwendungen eine Möglichkeit, mit den verschiedenen Operationen umzugehen. Daher gibt es eine Abstraktionsschicht namens Virtual File System (VFS). Es ist eine Schicht zwischen Anwendungen und den verschiedenen Dateisystemtypen, sodass Ihre Anwendungen unabhängig vom Dateisystem damit arbeiten können.

Sie können viele Dateisysteme auf Ihren Festplatten haben, je nachdem, wie sie partitioniert sind, und wir werden dies in einer kommenden Lektion behandeln.

### Journaling

Journaling ist bei den meisten Dateisystemtypen standardmäßig aktiviert, aber falls nicht, sollten Sie wissen, was es bewirkt. Nehmen wir an, Sie kopieren eine große Datei und plötzlich fällt der Strom aus. Nun, wenn Sie sich auf einem nicht-journaling-fähigen Dateisystem befinden, würde die Datei beschädigt und Ihr Dateisystem wäre inkonsistent. Wenn Sie dann neu starten, würde Ihr System eine Dateisystemprüfung durchführen, um sicherzustellen, dass alles in Ordnung ist. Die Reparaturen könnten jedoch eine Weile dauern, je nachdem, wie groß Ihr Dateisystem war.

Wenn Sie sich auf einem journaling-fähigen System befänden, würde Ihre Maschine, noch bevor sie mit dem Kopieren der Datei beginnt, in einer Protokolldatei (Journal) festhalten, was Sie tun werden. Wenn Sie die Datei tatsächlich kopieren und der Vorgang abgeschlossen ist, markiert das Journal diese Aufgabe als erledigt. Das Dateisystem ist dadurch immer in einem konsistenten Zustand, sodass es genau weiß, wo Sie aufgehört haben, wenn Ihre Maschine plötzlich heruntergefahren wurde. Dies verkürzt auch die Startzeit, da nicht das gesamte Dateisystem überprüft wird, sondern nur Ihr Journal.

### Common Desktop Filesystem Types

- ext4 – Dies ist die aktuellste Version der nativen Linux-Dateisysteme. Es ist kompatibel mit den älteren ext2- und ext3-Versionen. Es unterstützt Festplattenvolumen bis zu 1 Exabyte und Dateigrößen bis zu 16 Terabyte und vieles mehr. Es ist die Standardwahl für Linux-Dateisysteme.
- Btrfs – „Better or Butter FS“ ist ein neues Dateisystem für Linux, das Snapshots, inkrementelle Backups, Leistungssteigerung und vieles mehr bietet. Es ist weit verbreitet, aber noch nicht ganz stabil und kompatibel.
- XFS – Hochleistungs-Journaling-Dateisystem, ideal für ein System mit großen Dateien wie einem Medienserver.
- NTFS and FAT – Windows-Dateisysteme
- HFS+ – Macintosh-Dateisystem

Überprüfen Sie, welche Dateisysteme auf Ihrer Maschine vorhanden sind:

```plaintext
pete@icebox:~$ df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
/dev/sda1      ext4       6461592 2402708   3707604  40% /
udev           devtmpfs    501356       4    501352   1% /dev
tmpfs          tmpfs       102544    1068    101476   2% /run
/dev/sda6      xfs       13752320  460112  13292208   4% /home
```

Der Befehl **df** meldet die Festplattenspeichernutzung des Dateisystems und andere Details zu Ihrer Festplatte; wir werden später mehr über dieses Tool sprechen.

## Exercise

Recherchieren Sie online ein wenig über die anderen Dateisystemtypen: ReiserFS, ZFS, JFS und andere, die Sie finden können.

## Quiz Question

Was ist der gängige Linux-Dateisystemtyp?

## Quiz Answer

ext4
